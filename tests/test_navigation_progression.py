"""Focused regressions for FIRE's Phase → Step progression and context navigation."""
import json
import os
import unittest

from playwright.sync_api import sync_playwright, expect

KEY = "production-projects-v1"
URL = os.environ.get("FIRE_URL", "http://127.0.0.1:8000")


def study_project(*, setup=False, structure=False, tracks=False):
    sections = (
        [{"id": "s1", "name": "Intro", "lengthBars": 4}]
        if structure
        else []
    )
    track_list = [{"id": "t1", "name": "Vocal"}] if tracks else []
    p = {
        "id": "p1",
        "type": "study",
        "schemaVersion": 5,
        "title": "Even",
        "artist": "Babel",
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
            "sections": sections,
            "structureVerified": structure,
            "tracks": track_list,
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
    return {"version": 5, "currentProjectId": "p1", "projects": [p]}


class NavigationProgression(unittest.TestCase):
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

    def open(self, route="map", data=None):
        width = int(os.environ.get("FIRE_TEST_WIDTH", "390"))
        context = self.browser.new_context(
            viewport={"width": width, "height": 1000}, has_touch=True
        )
        self.addCleanup(context.close)
        state = data or study_project()
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

    def test_map_phase_home_uses_steps_not_manual_checkpoint_controls(self):
        page = self.open("map")
        expect(page.locator(".step-head .section-kicker")).to_have_text("Steps")
        self.assertEqual(page.locator(".step-row").count(), 3)
        self.assertEqual(page.locator(".step-row .round-check").count(), 0)
        self.assertEqual(page.locator(".checkpoint-head,.checkpoint-count,.phase-checkpoints").count(), 0)
        expect(page.locator('.step-row[data-route="structure"] .step-state')).to_have_text("Locked")
        expect(page.locator('.step-row[data-route="tracks"] .step-state')).to_have_text("Locked")
        expect(page.locator('.step-row[data-route="section-study"] .step-state')).to_have_text("Locked")

    def test_step_state_moves_from_locked_to_current_to_done(self):
        page = self.open("map", study_project(setup=True))
        expect(page.locator('.step-row[data-route="structure"] .step-state')).to_have_text("Current")
        expect(page.locator('.step-row[data-route="tracks"] .step-state')).to_have_text("Locked")

        page = self.open("map", study_project(setup=True, structure=True))
        expect(page.locator('.step-row[data-route="structure"] .step-state')).to_have_text("Done")
        expect(page.locator('.step-row[data-route="tracks"] .step-state')).to_have_text("Current")

    def test_context_title_opens_project_local_navigation(self):
        page = self.open("structure", study_project(setup=True))
        context = page.locator('.context-nav-button')
        expect(context).to_contain_text("The Map")
        self.assertGreaterEqual(context.bounding_box()["height"], 44)
        context.click()
        expect(page.locator('.context-nav-sheet')).to_be_visible()
        for route in ["project", "roadmap", "notes", "map", "structure"]:
            expect(page.locator(f'.context-nav-row[data-route="{route}"]')).to_be_visible()
        expect(page.locator('.context-nav-row[data-route="tracks"]')).to_be_disabled()
        page.locator('.context-nav-row[data-route="project"]').click()
        expect(page.locator("h1")).to_have_text("Even")

    def test_new_project_back_label_resolves_to_projects(self):
        page = self.open("new-project")
        expect(page.locator('[data-action="history-back"]')).to_contain_text("Projects")

    def test_working_step_position_is_explicit(self):
        page = self.open("structure", study_project(setup=True))
        expect(page.locator('.workflow-position')).to_have_text("Step 1 of 3")
        page = self.open("tracks", study_project(setup=True, structure=True))
        expect(page.locator('.workflow-position')).to_have_text("Step 2 of 3")


if __name__ == "__main__":
    unittest.main()
