"""Focused regression for the shared G7 primary row-label anchor."""
import json
import os
import unittest

from playwright.sync_api import sync_playwright

PREVIEW_KEY = "production-projects-v1-v7-preview"
URL = os.environ.get("FIRE_URL", "http://127.0.0.1:8000").rstrip("/") + "/v7-preview/"


def study_db():
    return {
        "version": 5,
        "currentProjectId": "p1",
        "projects": [{
            "id": "p1",
            "type": "study",
            "schemaVersion": 5,
            "title": "Smithereens",
            "artist": "Twenty One Pilots",
            "createdAt": 1,
            "lastActivityAt": 1,
            "notes": [],
            "map": {
                "setup": {
                    "reference": True,
                    "tempo": "111",
                    "meter": "4/4",
                    "grid": True,
                    "firstListen": True,
                },
                "sections": [{"id": "s1", "name": "Intro", "lengthBars": 8}],
                "structureVerified": False,
                "tracks": [],
                "tracksVerified": False,
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
        }],
    }


class V7SharedRowAnchor(unittest.TestCase):
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

    def test_project_home_setup_and_structure_share_primary_label_anchor(self):
        width = int(os.environ.get("FIRE_TEST_WIDTH", "390"))
        context = self.browser.new_context(viewport={"width": width, "height": 844}, has_touch=True)
        self.addCleanup(context.close)
        context.add_init_script(
            "localStorage.setItem(%s,%s);"
            % (json.dumps(PREVIEW_KEY), json.dumps(json.dumps(study_db())))
        )
        page = context.new_page()
        page.set_default_timeout(5000)

        page.goto(URL + "#project")
        home_x = page.locator(".journey-row .row-title").first.bounding_box()["x"]
        mark_x = page.locator(".journey-row .journey-mark").first.bounding_box()["x"]
        self.assertGreater(mark_x, home_x)

        page.goto(URL + "#setup")
        setup_x = page.locator(".form-label").first.bounding_box()["x"]

        page.goto(URL + "#structure")
        structure_x = page.locator(".arrangement-name").first.bounding_box()["x"]

        self.assertAlmostEqual(home_x, setup_x, delta=1.0)
        self.assertAlmostEqual(home_x, structure_x, delta=1.0)


if __name__ == "__main__":
    unittest.main()
