"""Focused regressions for FIRE's state-aware composition and root scroll fitting."""
import json
import os
import unittest

from playwright.sync_api import sync_playwright, expect

KEY = "production-projects-v1"
URL = os.environ.get("FIRE_URL", "http://127.0.0.1:8000")


def project_data():
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
                "reference": True,
                "tempo": "111",
                "meter": "4/4",
                "grid": True,
                "firstListen": True,
            },
            "sections": [],
            "structureVerified": False,
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


class AdaptiveComposition(unittest.TestCase):
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

    def open(self, route="map", height=1000):
        width = int(os.environ.get("FIRE_TEST_WIDTH", "390"))
        context = self.browser.new_context(
            viewport={"width": width, "height": height}, has_touch=True
        )
        self.addCleanup(context.close)
        data = project_data()
        context.add_init_script(
            """localStorage.setItem(%s,%s);
            history.replaceState({route:%s,projectId:'p1',fromRoute:'project',fromLabel:'Even'},'');"""
            % (json.dumps(KEY), json.dumps(json.dumps(data)), json.dumps(route))
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

    def test_completed_song_setup_collapses_and_can_be_edited(self):
        page = self.open("map")
        summary = page.locator('[data-action="toggle-setup-disclosure"]')
        expect(summary).to_be_visible()
        expect(summary).to_contain_text("Ready · 111 BPM · 4/4")
        self.assertEqual(page.locator("#tempoInput").count(), 0)
        self.assertEqual(page.locator(".checkpoint-progress").count(), 0)

        summary.click()
        tempo = page.locator("#tempoInput")
        expect(tempo).to_be_visible()
        tempo.fill("112")
        tempo.blur()
        expect(page.locator('[data-action="toggle-setup-disclosure"]')).to_contain_text(
            "Ready · 112 BPM · 4/4"
        )

    def test_project_current_phase_is_the_action_without_progress_slab(self):
        page = self.open("project")
        current = page.locator('.project-current .hero-card[data-action="go"]')
        expect(current).to_be_visible()
        expect(current).to_have_attribute("data-route", "map")
        expect(current).to_contain_text("The Map")
        expect(current).to_contain_text("0 of 3 checkpoints")
        self.assertEqual(page.locator(".project-current .progress").count(), 0)
        self.assertNotIn("Continue The Map", page.locator(".project-current").inner_text())

    def test_roadmap_future_detail_is_quiet_and_root_fit_is_content_driven(self):
        page = self.open("roadmap", height=1200)
        self.assertEqual(page.locator(".road-phase.unimplemented .micro").count(), 0)
        self.assertEqual(page.locator(".road-phase.unimplemented .road-checks").count(), 0)
        expect(page.locator(".road-phase.current .road-checks")).to_be_visible()

        page.wait_for_function(
            "document.querySelector('#app').dataset.viewportFit === 'true'"
        )
        self.assertEqual(
            page.evaluate("document.documentElement.style.overflowY"), "hidden"
        )

        page.evaluate(
            """const probe=document.createElement('div');
            probe.id='fitProbe'; probe.style.height='2000px';
            document.querySelector('#app').appendChild(probe);"""
        )
        page.wait_for_function(
            "document.querySelector('#app').dataset.viewportFit === 'false'"
        )
        self.assertEqual(page.evaluate("document.documentElement.style.overflowY"), "")

        page.evaluate("document.querySelector('#fitProbe').remove()")
        page.wait_for_function(
            "document.querySelector('#app').dataset.viewportFit === 'true'"
        )


if __name__ == "__main__":
    unittest.main()
