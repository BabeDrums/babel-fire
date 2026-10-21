"""Physical-review prototype regressions for the isolated FIRE V7 preview shell."""
import json
import os
import unittest

from playwright.sync_api import sync_playwright, expect

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

    def open(self, route="project", data=None):
        width = int(os.environ.get("FIRE_TEST_WIDTH", "390"))
        context = self.browser.new_context(
            viewport={"width": width, "height": 1000}, has_touch=True
        )
        self.addCleanup(context.close)
        state = data or study_db()
        context.add_init_script(
            "localStorage.setItem(%s,%s);"
            % (json.dumps(PREVIEW_KEY), json.dumps(json.dumps(state)))
        )
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

    def test_project_home_is_continue_plus_journey_without_custom_navigator(self):
        page = self.open("project")
        expect(page.locator("h1")).to_have_text("Creep")
        expect(page.locator(".section-title").nth(0)).to_contain_text("Continue")
        expect(page.locator(".section-title").nth(1)).to_contain_text("Journey")
        expect(page.locator(".continue-title")).to_have_text("Song Setup")
        self.assertEqual(page.locator(".context-nav-button,.context-nav-sheet").count(), 0)
        self.assertEqual(page.get_by_text("Checkpoint", exact=False).count(), 0)
        self.assertEqual(page.get_by_text("Step ", exact=False).count(), 0)
        self.assertEqual(page.get_by_text("Roadmap", exact=True).count(), 0)

    def test_song_setup_is_a_dedicated_work_page(self):
        page = self.open("project")
        page.locator(".continue-card").click()
        expect(page.locator("h1")).to_have_text("Song Setup")
        self.assertEqual(page.locator(".journey,.phase-block").count(), 0)
        self.assertEqual(page.locator(".form-row").count(), 5)
        expect(page.locator(".back")).to_contain_text("Creep")

    def test_guidance_does_not_hard_lock_structure_or_tracks(self):
        page = self.open("structure")
        expect(page.locator("h1")).to_have_text("Structure")
        expect(page.locator(".add-row")).to_be_enabled()
        page = self.open("tracks")
        expect(page.locator("h1")).to_have_text("Tracks")
        expect(page.locator('.track-tile[data-name="Vocal"]')).to_be_enabled()

    def test_section_study_explains_missing_context_instead_of_dead_lock(self):
        page = self.open("section-study")
        expect(page.locator("h1")).to_have_text("Section Study")
        expect(page.locator(".prereq-card")).to_contain_text("Nothing is locked")
        expect(page.locator('.prereq-actions [data-route="structure"]')).to_be_visible()
        expect(page.locator('.prereq-actions [data-route="tracks"]')).to_be_visible()

    def test_add_section_is_compact_and_immediate(self):
        page = self.open("structure")
        page.locator(".add-row").click()
        expect(page.locator(".sheet")).to_be_visible()
        box = page.locator(".sheet").bounding_box()
        self.assertLess(box["height"], 600)
        page.locator('[data-action="quick-add-section"][data-name="Intro"]').click()
        expect(page.locator(".sheet-backdrop")).to_be_hidden()
        expect(page.locator(".arrangement-row")).to_have_count(1)
        expect(page.locator(".arrangement-row")).to_contain_text("Intro")
        expect(page.locator(".arrangement-row")).to_contain_text("8 bars")

    def test_tracks_is_focused_and_continuation_is_direct(self):
        page = self.open("tracks", study_db(setup=True, structure=True))
        expect(page.locator("h1")).to_have_text("Tracks")
        self.assertEqual(page.get_by_text("Step ", exact=False).count(), 0)
        tile = page.locator('.track-tile[data-name="Drums"]')
        tile.click()
        expect(tile).to_have_attribute("aria-pressed", "true")
        expect(page.locator('[data-action="continue-section-study"]')).to_be_enabled()


if __name__ == "__main__":
    unittest.main()
