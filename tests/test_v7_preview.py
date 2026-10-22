"""Physical-review regressions for the isolated FIRE V7 preview shell."""
import json
import os
import unittest

from playwright.sync_api import sync_playwright, expect

SOURCE_KEY = "production-projects-v1"
PREVIEW_KEY = "production-projects-v1-v7-preview"
URL = os.environ.get("FIRE_URL", "http://127.0.0.1:8000").rstrip("/") + "/v7-preview/"


def study_db(*, setup=False, structure=False, tracks=False):
    project = {
        "id": "p1",
        "type": "study",
        "schemaVersion": 5,
        "title": "Creep",
        "artist": "Radiohead",
        "createdAt": 1,
        "notes": [],
        "map": {
            "setup": {
                "reference": setup,
                "tempo": "111" if setup else "",
                "meter": "4/4",
                "grid": setup,
                "firstListen": setup,
            },
            "sections": ([{"id": "s1", "name": "Intro", "lengthBars": 8}] if structure else []),
            "structureVerified": structure,
            "tracks": ([{"id": "t1", "name": "Vocal"}] if tracks else []),
            "timeline": {"presence": [], "events": []},
            "sectionData": {},
            "mapVerified": False,
            "teachBack": False,
            "phaseParking": "",
            "phaseTakeaway": "",
        },
        "skeleton": {
            "session": {"tracks": {}, "markers": {}},
            "draft": {"parts": {}},
            "bounce": {"exported": False, "listened": False},
        },
    }
    return {"version": 5, "currentProjectId": "p1", "projects": [project]}


def empty_db():
    return {"version": 5, "currentProjectId": None, "projects": []}


class V7Preview(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pw = sync_playwright().start()
        cls.browser = cls.pw.chromium.launch(
            executable_path=os.environ.get("CHROMIUM_PATH", "/usr/bin/chromium"),
            args=["--no-sandbox"],
        )

    @classmethod
    def tearDownClass(cls):
        cls.browser.close()
        cls.pw.stop()

    def open(self, route="project", data=None, height=844, source_data=None):
        width = int(os.environ.get("FIRE_TEST_WIDTH", "390"))
        context = self.browser.new_context(
            viewport={"width": width, "height": height}, has_touch=True
        )
        self.addCleanup(context.close)
        state = study_db() if data is None else data
        scripts = [
            "localStorage.setItem(%s,%s);"
            % (json.dumps(PREVIEW_KEY), json.dumps(json.dumps(state)))
        ]
        if source_data is not None:
            scripts.append(
                "localStorage.setItem(%s,%s);"
                % (json.dumps(SOURCE_KEY), json.dumps(json.dumps(source_data)))
            )
        context.add_init_script("".join(scripts))
        page = context.new_page()
        page.set_default_timeout(5000)
        errors = []
        page.on("pageerror", lambda error: errors.append(str(error)))
        page.on(
            "console",
            lambda message: errors.append(message.text)
            if message.type == "error" and "404 (File not found)" not in message.text
            else None,
        )
        response = page.goto(URL + f"#{route}")
        self.assertEqual(response.status, 200)
        self.addCleanup(lambda: self.assertEqual(errors, []))
        return page

    def assert_short_page_locked(self, page):
        if int(os.environ.get("FIRE_TEST_WIDTH", "390")) >= 700:
            return
        expect(page.locator("#app")).to_have_attribute("data-scrollable", "false")
        expect(page.locator("html")).to_have_attribute("data-v7-fit", "true")

    def assert_tall_page_scrolls(self, page):
        if int(os.environ.get("FIRE_TEST_WIDTH", "390")) >= 700:
            return
        expect(page.locator("#app")).to_have_attribute("data-scrollable", "true")
        expect(page.locator("html")).to_have_attribute("data-v7-fit", "false")

    def test_projects_is_one_job_open_or_create(self):
        page = self.open("projects")
        expect(page.locator("h1")).to_have_text("Projects")
        self.assertEqual(page.locator(".root-screen .topbar").count(), 0)
        self.assertEqual(page.locator(".projects-heading .sub").count(), 0)
        expect(page.get_by_role("button", name="New Project")).to_be_visible()
        expect(page.locator(".project-list.group")).to_be_visible()
        expect(page.locator(".project-row")).to_contain_text("Creep")
        self.assertEqual(page.locator(".preview-note").count(), 0)
        expect(page.locator(".build-stamp")).to_contain_text("FIRE V7 PREVIEW")
        self.assertEqual(page.locator('script[src*="new-project.js"]').count(), 0)
        self.assert_short_page_locked(page)

    def test_empty_projects_has_one_create_path_and_creation_stays_sandboxed(self):
        source = study_db(setup=True, structure=True, tracks=True)
        page = self.open("projects", empty_db(), source_data=source)
        expect(page.locator(".projects-empty")).to_have_text("No projects yet.")
        expect(page.get_by_role("button", name="New Project")).to_have_count(1)

        page.get_by_role("button", name="New Project").click()
        expect(page.locator(".sheet")).to_be_visible()
        page.get_by_role("textbox", name="Song title").fill("Still")
        page.get_by_role("textbox", name="Artist").fill("Babel")
        page.get_by_role("button", name="Create Project").click()

        expect(page.locator("h1")).to_have_text("Still")
        preview = page.evaluate("(key) => JSON.parse(localStorage.getItem(key))", PREVIEW_KEY)
        production = page.evaluate("(key) => JSON.parse(localStorage.getItem(key))", SOURCE_KEY)
        self.assertEqual(len(preview["projects"]), 1)
        self.assertEqual(preview["projects"][0]["title"], "Still")
        self.assertEqual(production, source)

    def test_short_work_pages_do_not_fake_scroll(self):
        page = self.open("structure", height=780)
        self.assert_short_page_locked(page)
        page = self.open("review-map", height=780)
        self.assert_short_page_locked(page)
        self.assertEqual(page.get_by_role("button", name="Back to Project").count(), 0)

    def test_genuinely_tall_project_home_gets_scroll_end_clearance(self):
        page = self.open("project", study_db(setup=True, structure=True, tracks=True), height=720)
        self.assert_tall_page_scrolls(page)
        if int(os.environ.get("FIRE_TEST_WIDTH", "390")) < 700:
            padding = page.locator("#app").evaluate("el => parseFloat(getComputedStyle(el).paddingBottom)")
            self.assertGreater(padding, 60)

    def test_project_home_is_continue_journey_notes_without_v6_chrome(self):
        page = self.open("project")
        expect(page.locator("h1")).to_have_text("Creep")
        expect(page.locator(".section-title").nth(0)).to_have_text("Continue")
        expect(page.locator(".section-title").nth(1)).to_have_text("Journey")
        expect(page.locator(".section-title").nth(2)).to_have_text("Notes")
        expect(page.locator(".continue-title")).to_have_text("Song Setup")
        expect(page.locator('.journey-row[aria-current="step"] .row-title')).to_have_text("Song Setup")
        self.assertEqual(page.get_by_text("Locked", exact=True).count(), 0)
        self.assertEqual(page.get_by_text("Recommended", exact=True).count(), 0)
        self.assertEqual(page.get_by_text("In progress", exact=True).count(), 0)
        self.assertEqual(page.get_by_text("Later", exact=True).count(), 0)
        self.assertEqual(page.get_by_text("Checkpoint", exact=False).count(), 0)
        self.assertEqual(page.get_by_text("Step ", exact=False).count(), 0)
        self.assertEqual(page.get_by_text("Roadmap", exact=True).count(), 0)
        self.assertEqual(page.locator(".context-nav-button,.context-nav-sheet").count(), 0)

    def test_completed_journey_work_remains_revisitable_and_current_moves_forward(self):
        page = self.open("project", study_db(setup=True))
        setup = page.locator(".journey-row", has_text="Song Setup")
        expect(setup.locator(".journey-mark")).to_have_text("✓")
        expect(setup).to_be_enabled()
        expect(page.locator('.journey-row[aria-current="step"] .row-title')).to_have_text("Structure")
        setup.click()
        expect(page.locator("h1")).to_have_text("Song Setup")

    def test_song_setup_is_focused_and_does_not_explain_status_twice(self):
        page = self.open("setup")
        expect(page.locator("h1")).to_have_text("Song Setup")
        self.assertEqual(page.locator(".journey,.journey-group").count(), 0)
        self.assertEqual(page.locator(".form-row").count(), 5)
        expect(page.locator(".back")).to_contain_text("Creep")
        self.assertEqual(page.get_by_text("Mark done", exact=True).count(), 0)
        self.assertEqual(page.get_by_role("button", name="Continue to Structure").count(), 0)

        page = self.open("setup", study_db(setup=True))
        self.assertEqual(page.get_by_text("Done", exact=True).count(), 0)
        expect(page.get_by_role("button", name="Continue to Structure")).to_be_visible()

    def test_song_setup_continuation_reacts_to_tempo_without_rerendering_input(self):
        data = study_db()
        data["projects"][0]["map"]["setup"].update(
            {"reference": True, "grid": True, "firstListen": True}
        )
        page = self.open("setup", data)
        tempo = page.get_by_role("textbox", name="Tempo")
        tempo.fill("111")
        expect(tempo).to_have_value("111")
        expect(page.get_by_role("button", name="Continue to Structure")).to_be_visible()

    def test_guidance_does_not_hard_lock_structure_or_tracks(self):
        page = self.open("structure")
        expect(page.locator("h1")).to_have_text("Structure")
        expect(page.get_by_role("button", name="Add Section")).to_be_enabled()
        page = self.open("tracks")
        expect(page.locator("h1")).to_have_text("Tracks")
        expect(page.locator('.track-tile[data-name="Vocal"]')).to_be_enabled()

    def test_structure_uses_actual_task_before_continuation(self):
        page = self.open("structure")
        self.assertEqual(page.get_by_role("button", name="Continue to Tracks").count(), 0)
        page.get_by_role("button", name="Add Section").click()
        expect(page.locator(".sheet")).to_be_visible()
        box = page.locator(".sheet").bounding_box()
        self.assertLess(box["height"], 560)
        page.locator('[data-action="quick-add-section"][data-name="Intro"]').click()
        expect(page.locator(".sheet-backdrop")).to_be_hidden()
        expect(page.locator(".arrangement-row")).to_have_count(1)
        expect(page.locator(".arrangement-row")).to_contain_text("Intro")
        expect(page.locator(".arrangement-row")).to_contain_text("8 bars")
        expect(page.locator(".group.arrangement .add-section-row")).to_be_visible()
        self.assertEqual(page.get_by_role("button", name="Continue to Tracks").count(), 0)
        page.get_by_role("button", name="Structure matches the song").click()
        expect(page.get_by_role("button", name="Continue to Tracks")).to_be_visible()

    def test_tracks_shows_continuation_only_after_the_task_has_started(self):
        page = self.open("tracks", study_db(setup=True, structure=True))
        expect(page.locator("h1")).to_have_text("Tracks")
        expect(page.locator(".sub")).to_have_text("Choose everything you hear in the song.")
        self.assertEqual(page.get_by_text("Step ", exact=False).count(), 0)
        self.assertEqual(page.get_by_role("button", name="Continue to Section Study").count(), 0)
        tile = page.locator('.track-tile[data-name="Drums"]')
        tile.click()
        expect(tile).to_have_attribute("aria-pressed", "true")
        expect(page.get_by_role("button", name="Continue to Section Study")).to_be_visible()
        expect(page.locator(".action-row.action-separated")).to_be_visible()

    def test_section_study_explains_only_real_missing_context(self):
        page = self.open("section-study")
        expect(page.locator("h1")).to_have_text("Section Study")
        expect(page.locator(".prereq-card")).to_contain_text("needs a structure and at least one track")
        self.assertEqual(page.get_by_role("button", name="Back to Project").count(), 0)
        expect(page.locator('.prereq-actions [data-route="structure"]')).to_be_visible()
        expect(page.locator('.prereq-actions [data-route="tracks"]')).to_be_visible()

    def test_review_map_stays_visible_without_pretending_editor_is_migrated(self):
        page = self.open("project", study_db(setup=True, structure=True, tracks=True))
        page.get_by_role("button", name="Review Map").click()
        expect(page.locator("h1")).to_have_text("Review Map")
        expect(page.locator(".prereq-card")).to_contain_text("still uses V6")

    def test_project_actions_keep_core_edit_reset_delete_paths(self):
        page = self.open("project", study_db(setup=True, structure=True, tracks=True))
        page.get_by_role("button", name="Project actions").click()
        expect(page.get_by_role("button", name="Edit Project")).to_be_visible()
        expect(page.get_by_role("button", name="Reset Progress")).to_be_visible()
        expect(page.get_by_role("button", name="Delete Project")).to_be_visible()


if __name__ == "__main__":
    unittest.main()
