"""Physical-review regressions for the isolated FIRE G7 preview shell."""
import json
import os
import unittest
from pathlib import Path

from playwright.sync_api import sync_playwright, expect

SOURCE_KEY = "production-projects-v1"
PREVIEW_KEY = "production-projects-v1-v7-preview"
URL = os.environ.get("FIRE_URL", "http://127.0.0.1:8000").rstrip("/") + "/v7-preview/"


def study_db(*, setup=False, structure=False, tracks=False, notes=None):
    project = {
        "id": "p1",
        "type": "study",
        "schemaVersion": 5,
        "title": "Creep",
        "artist": "Radiohead",
        "createdAt": 1,
        "notes": notes or [],
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


def original_db():
    return {
        "version": 5,
        "currentProjectId": "o1",
        "projects": [{
            "id": "o1",
            "type": "original",
            "schemaVersion": 5,
            "title": "Even",
            "artist": "Babel",
            "createdAt": 1,
            "notes": [],
        }],
    }


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
        context = self.browser.new_context(viewport={"width": width, "height": height}, has_touch=True)
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

    def test_projects_keeps_build_trace_out_of_content_hierarchy(self):
        page = self.open("projects")
        expect(page.locator("h1")).to_have_text("Projects")
        expect(page.get_by_role("button", name="New Project")).to_be_visible()
        expect(page.locator(".root-build-info")).to_contain_text("G7 ·")
        self.assertEqual(page.locator(".projects-heading .build-info").count(), 0)
        self.assertEqual(page.locator(".sheet-meta").count(), 0)
        self.assertEqual(page.locator(".root-build-info").evaluate("el => getComputedStyle(el).position"), "fixed")

    def test_project_card_has_open_and_secondary_actions_without_entering_project(self):
        page = self.open("projects")
        expect(page.locator(".project-open")).to_contain_text("Creep")
        actions = page.get_by_role("button", name="Actions for Creep")
        expect(actions).to_be_visible()
        actions.click()
        expect(page.locator(".sheet")).to_be_visible()
        expect(page.get_by_role("button", name="Edit")).to_be_visible()
        page.get_by_role("button", name="Edit").click()
        title = page.get_by_role("textbox", name="Project title")
        title.fill("Creep Edit")
        page.get_by_role("button", name="Save").click()
        expect(page.locator(".project-open")).to_contain_text("Creep Edit")
        self.assertEqual(page.locator(".project-identity").count(), 0)

    def test_new_project_explicitly_supports_original_and_recreation(self):
        source = study_db(setup=True, structure=True, tracks=True)
        page = self.open("projects", empty_db(), source_data=source)
        page.get_by_role("button", name="New Project").click()
        expect(page.get_by_role("button", name="Original")).to_be_visible()
        expect(page.get_by_role("button", name="Recreation")).to_be_visible()
        self.assertEqual(page.locator("#newProjectTitle").count(), 0)

        page.get_by_role("button", name="Original").click()
        page.get_by_role("textbox", name="Project title").fill("Even")
        create = page.get_by_role("button", name="Create")
        expect(create).to_be_enabled()
        create.click()
        expect(page.locator(".project-identity h1")).to_have_text("Even")
        expect(page.locator(".project-identity .sub")).to_have_text("Original")
        preview = page.evaluate("(key) => JSON.parse(localStorage.getItem(key))", PREVIEW_KEY)
        production = page.evaluate("(key) => JSON.parse(localStorage.getItem(key))", SOURCE_KEY)
        self.assertEqual(preview["projects"][0]["type"], "original")
        self.assertEqual(production, source)

        page = self.open("projects", empty_db())
        page.get_by_role("button", name="New Project").click()
        page.get_by_role("button", name="Recreation").click()
        page.get_by_role("textbox", name="Song title").fill("Smithereens")
        expect(page.get_by_role("button", name="Create")).to_be_disabled()
        page.get_by_role("textbox", name="Artist").fill("Twenty One Pilots")
        expect(page.get_by_role("button", name="Create")).to_be_enabled()

    def test_project_home_removes_redundant_continue_and_journey_headers(self):
        page = self.open("project")
        expect(page.locator(".project-identity h1")).to_have_text("Creep")
        expect(page.locator(".continue-title")).to_have_text("Song Setup")
        self.assertEqual(page.locator(".journey-row", has_text="Song Setup").count(), 0)
        self.assertEqual(page.locator(".section-title").count(), 0)
        self.assertEqual(page.get_by_text("Continue", exact=True).count(), 0)
        self.assertEqual(page.get_by_text("Journey", exact=True).count(), 0)
        expect(page.locator(".future-label")).to_have_text("Later")
        expect(page.locator(".future-phase-list span")).to_have_count(6)

    def test_work_pages_share_one_title_scale_and_remove_redundant_copy(self):
        setup = self.open("setup")
        structure = self.open("structure")
        tracks = self.open("tracks")
        setup_size = float(setup.locator(".work-header h1").evaluate("el => parseFloat(getComputedStyle(el).fontSize)"))
        structure_size = float(structure.locator(".work-header h1").evaluate("el => parseFloat(getComputedStyle(el).fontSize)"))
        tracks_size = float(tracks.locator(".work-header h1").evaluate("el => parseFloat(getComputedStyle(el).fontSize)"))
        self.assertEqual(setup_size, structure_size)
        self.assertEqual(structure_size, tracks_size)
        self.assertEqual(setup.locator(".work-header .sub").count(), 0)
        self.assertEqual(structure.locator(".work-header .sub").count(), 0)
        expect(tracks.locator(".work-header .sub")).to_have_text("Choose everything you hear.")
        self.assertEqual(setup.get_by_text("Prepare the reference before studying it.", exact=True).count(), 0)
        self.assertEqual(structure.get_by_text("Build the song one section at a time.", exact=True).count(), 0)
        self.assertEqual(structure.get_by_text("Add the first section you hear.", exact=True).count(), 0)

    def test_nested_work_uses_icon_back_navigation_not_repeated_project_title(self):
        page = self.open("setup")
        back = page.locator(".icon-back")
        expect(back).to_be_visible()
        expect(back).to_have_attribute("aria-label", "Creep")
        self.assertEqual(back.get_by_text("Creep", exact=True).count(), 0)

    def test_interaction_grammar_is_predictable(self):
        page = self.open("setup")
        page.locator(".reference-row").click()
        self.assertEqual(page.locator(".sheet").count(), 0)

        page = self.open("tracks")
        page.locator('.track-tile[data-name="Vocal"]').click()
        self.assertEqual(page.locator(".sheet").count(), 0)
        page.get_by_role("button", name="Other").click()
        expect(page.locator(".sheet")).to_be_visible()
        expect(page.locator(".sheet h2")).to_have_text("Add Track")

        page = self.open("structure")
        page.get_by_role("button", name="Add Section").click()
        expect(page.locator(".sheet h2")).to_have_text("Add Section")

    def test_structure_uses_one_arrangement_surface_from_empty_state_forward(self):
        page = self.open("structure")
        expect(page.locator(".group.arrangement")).to_be_visible()
        expect(page.get_by_role("button", name="Add Section")).to_be_visible()
        self.assertEqual(page.locator(".structure-empty").count(), 0)
        page.get_by_role("button", name="Add Section").click()
        page.locator('[data-action="quick-add-section"][data-name="Intro"]').click()
        expect(page.locator(".arrangement-row")).to_contain_text("Intro")
        expect(page.locator(".structure-confirm-row")).to_contain_text("Matches the song")
        self.assertEqual(page.get_by_role("button", name="Continue").count(), 0)
        page.locator(".structure-confirm-row").click()
        expect(page.get_by_role("button", name="Continue")).to_be_visible()

    def test_tracks_keeps_direct_choices_and_compact_creation_path(self):
        page = self.open("tracks")
        vocal = page.locator('.track-tile[data-name="Vocal"]')
        vocal.click()
        expect(vocal).to_have_attribute("aria-pressed", "true")
        expect(page.get_by_role("button", name="Continue")).to_be_visible()
        other = page.get_by_role("button", name="Other")
        expect(other).to_be_visible()
        other.click()
        field = page.get_by_role("textbox", name="Track name")
        field.fill("Strings")
        page.get_by_role("button", name="Add").click()
        expect(page.locator('.track-tile[data-name="Strings"]')).to_be_visible()

    def test_existing_notes_remain_reachable_without_a_notes_header(self):
        data = study_db(notes=[{"type": "Idea", "context": "Project", "text": "Keep verse small."}])
        page = self.open("project", data)
        expect(page.get_by_role("button", name="Notes 1 saved")).to_be_visible()
        self.assertEqual(page.get_by_text("Notes", exact=True).count(), 1)
        page.get_by_role("button", name="Notes 1 saved").click()
        expect(page.locator(".note-card")).to_contain_text("Keep verse small.")

    def test_original_project_is_first_class_even_before_its_core_spine_is_built(self):
        page = self.open("project", original_db())
        expect(page.locator(".project-identity h1")).to_have_text("Even")
        expect(page.locator(".project-identity .sub")).to_have_text("Babel · Original")
        expect(page.get_by_text("Original workflow comes with the FIRE Core spine.")).to_be_visible()
        expect(page.get_by_role("button", name="Project actions")).to_be_visible()

    def test_placeholders_stay_truthful_and_quiet(self):
        complete = study_db(setup=True, structure=True, tracks=True)
        page = self.open("section-study", complete)
        expect(page.get_by_text("Section Study isn't built yet.")).to_be_visible()
        self.assertEqual(page.locator(".work-header .sub").count(), 0)
        page = self.open("review-map", complete)
        expect(page.get_by_text("Review Map isn't built yet.")).to_be_visible()
        self.assertEqual(page.locator(".work-header .sub").count(), 0)

    def test_song_setup_continuation_reacts_to_tempo_without_rerendering_input(self):
        data = study_db()
        data["projects"][0]["map"]["setup"].update({"reference": True, "grid": True, "firstListen": True})
        page = self.open("setup", data)
        tempo = page.get_by_role("textbox", name="Tempo")
        tempo.fill("111")
        expect(tempo).to_have_value("111")
        expect(page.get_by_role("button", name="Continue")).to_be_visible()
        width = page.get_by_role("button", name="Continue").bounding_box()["width"]
        self.assertLess(width, page.viewport_size["width"] - 40)

    def test_phone_pages_use_natural_document_scrolling(self):
        page = self.open("project", study_db(setup=True, structure=True, tracks=True), height=720)
        self.assertNotEqual(page.evaluate("getComputedStyle(document.documentElement).overflowY"), "hidden")
        self.assertNotEqual(page.evaluate("getComputedStyle(document.body).overflowY"), "hidden")
        source = Path("v7-preview/app.js").read_text()
        styles = Path("v7-preview/styles.css").read_text()
        self.assertNotIn("visualViewport", source)
        self.assertNotIn("dataset.scrollable", source)
        self.assertNotIn("data-v7-fit", styles)

    def test_preview_remains_isolated_from_v6_storage(self):
        source = study_db(setup=True, structure=True, tracks=True)
        page = self.open("projects", empty_db(), source_data=source)
        page.get_by_role("button", name="New Project").click()
        page.get_by_role("button", name="Original").click()
        page.get_by_role("textbox", name="Project title").fill("Still")
        page.get_by_role("button", name="Create").click()
        production = page.evaluate("(key) => JSON.parse(localStorage.getItem(key))", SOURCE_KEY)
        self.assertEqual(production, source)


if __name__ == "__main__":
    unittest.main()
