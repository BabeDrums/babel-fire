"""Focused regressions for FIRE's current-task declutter rules."""
import json
import os
import unittest

from playwright.sync_api import sync_playwright, expect

KEY = "production-projects-v1"
URL = os.environ.get("FIRE_URL", "http://127.0.0.1:8000")


def project_data(*, setup_complete=False, structure_complete=False):
    sections = (
        [{"id": "sec1", "name": "Intro", "type": "Intro", "lengthBars": 4}]
        if structure_complete
        else []
    )
    project = {
        "id": "p1",
        "type": "study",
        "schemaVersion": 5,
        "title": "Even",
        "artist": "Babel",
        "createdAt": 1,
        "notes": [],
        "map": {
            "setup": {
                "reference": setup_complete,
                "tempo": "111" if setup_complete else "",
                "meter": "4/4",
                "grid": setup_complete,
                "firstListen": setup_complete,
            },
            "sections": sections,
            "structureVerified": structure_complete,
            "tracks": [],
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


class CurrentTaskDeclutter(unittest.TestCase):
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

    def open(self, route, data=None):
        width = int(os.environ.get("FIRE_TEST_WIDTH", "390"))
        context = self.browser.new_context(
            viewport={"width": width, "height": 1000}, has_touch=True
        )
        self.addCleanup(context.close)
        state = data or project_data()
        context.add_init_script(
            """localStorage.setItem(%s,%s);
            history.replaceState({route:%s,projectId:'p1',fromRoute:'project',fromLabel:'Even'},'');"""
            % (json.dumps(KEY), json.dumps(json.dumps(state)), json.dumps(route))
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
        response = page.goto(URL)
        self.assertEqual(response.status, 200)
        self.addCleanup(lambda: self.assertEqual(errors, []))
        return page

    def test_project_home_keeps_only_current_phase_and_project_utilities(self):
        page = self.open("project")
        text = page.locator(".project-overview").inner_text()
        self.assertNotIn("Next\n", text)
        self.assertNotIn("The Skeleton", text)
        expect(page.locator('.quick-card[data-route="roadmap"]')).to_be_visible()
        expect(page.locator('.quick-card[data-route="notes"]')).to_be_visible()

    def test_new_project_omits_redundant_project_label(self):
        page = self.open("new-project")
        self.assertEqual(page.locator(".project-field-label").count(), 0)
        expect(page.locator(".create-project-action")).to_be_visible()

    def test_incomplete_map_setup_shows_one_quiet_checkpoint_prerequisite(self):
        page = self.open("map")
        rows = page.locator(".phase-checkpoints .list-row")
        self.assertEqual(rows.count(), 1)
        expect(rows.first).to_have_text("Available after Song Setup")
        self.assertEqual(page.locator('.phase-checkpoints [data-route="structure"]').count(), 0)
        self.assertEqual(page.locator('.phase-checkpoints [data-route="tracks"]').count(), 0)

    def test_structure_hides_repeated_labels_and_unavailable_next(self):
        page = self.open("structure", project_data(setup_complete=True))
        self.assertEqual(page.locator(".structure-ready-label").count(), 0)
        self.assertEqual(page.locator('.section-kicker:text-is("Structure")').count(), 0)
        self.assertEqual(page.locator('button[data-route="tracks"]').count(), 0)
        expect(page.locator('[data-action="open-add-section"]')).to_be_visible()
        expect(page.locator('[data-action="toggle-structure-verified"]')).to_be_visible()

    def test_tracks_reveals_next_only_after_a_track_is_selected(self):
        page = self.open(
            "tracks", project_data(setup_complete=True, structure_complete=True)
        )
        self.assertEqual(page.locator('[data-action="start-section-study"]').count(), 0)
        page.locator('[data-action="toggle-track-choice"][data-name="Vocal"]').click()
        expect(page.locator('[data-action="start-section-study"]')).to_be_visible()

    def test_unimplemented_roadmap_rows_are_quieter_than_current_phase_on_phone(self):
        if int(os.environ.get("FIRE_TEST_WIDTH", "390")) > 430:
            self.skipTest("phone density assertion")
        page = self.open("roadmap")
        current_height = page.locator(".road-phase.current").bounding_box()["height"]
        future_height = page.locator(".road-phase.unimplemented").first.bounding_box()["height"]
        self.assertLess(future_height, current_height)


if __name__ == "__main__":
    unittest.main()
