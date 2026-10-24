"""Visual-grammar regressions for the isolated FIRE G7 preview shell."""
import json
import os
import unittest

from playwright.sync_api import sync_playwright, expect

PREVIEW_KEY = "production-projects-v1-v7-preview"
URL = os.environ.get("FIRE_URL", "http://127.0.0.1:8000").rstrip("/") + "/v7-preview/"


def study_project(*, setup=False, sections=None, verified=False, tracks=None, tracks_verified=False):
    return {
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
                "reference": setup,
                "tempo": "111" if setup else "",
                "meter": "4/4",
                "grid": setup,
                "firstListen": setup,
            },
            "sections": sections or [],
            "structureVerified": verified,
            "tracks": tracks or [],
            "tracksVerified": tracks_verified,
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


def study_db(*, setup=False, sections=None, verified=False, tracks=None, tracks_verified=False):
    return {
        "version": 5,
        "currentProjectId": "p1",
        "projects": [study_project(
            setup=setup,
            sections=sections,
            verified=verified,
            tracks=tracks,
            tracks_verified=tracks_verified,
        )],
    }


def empty_db():
    return {"version": 5, "currentProjectId": None, "projects": []}


class V7VisualGrammar(unittest.TestCase):
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
        context = self.browser.new_context(viewport={"width": width, "height": 844}, has_touch=True)
        self.addCleanup(context.close)
        state = study_db() if data is None else data
        context.add_init_script(
            "localStorage.setItem(%s,%s);" % (json.dumps(PREVIEW_KEY), json.dumps(json.dumps(state)))
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

    def test_project_form_groups_fields_and_cancel_has_button_shape(self):
        page = self.open("projects", empty_db())
        page.get_by_role("button", name="New Project").click()
        expect(page.locator(".project-field-group")).to_be_visible()
        self.assertEqual(page.locator(".project-field-group .project-field-row").count(), 2)
        self.assertEqual(page.locator(".project-field-group").get_by_role("textbox").count(), 2)
        cancel = page.get_by_role("button", name="Cancel")
        self.assertEqual(cancel.evaluate("el => getComputedStyle(el).borderTopStyle"), "solid")
        self.assertGreater(float(cancel.evaluate("el => parseFloat(getComputedStyle(el).borderTopWidth)")), 0)

    def test_structure_add_moves_to_toolbar_and_verification_is_separate_surface(self):
        sections = [{"id": "s1", "name": "Intro", "lengthBars": 8}]
        page = self.open("structure", study_db(sections=sections))
        add = page.get_by_role("button", name="Add Section")
        expect(add).to_be_visible()
        self.assertEqual(add.evaluate("el => el.closest('.toolbar') !== null"), True)
        self.assertEqual(page.locator(".arrangement").get_by_text("Add Section", exact=True).count(), 0)
        expect(page.locator(".structure-verification")).to_be_visible()
        self.assertEqual(page.locator(".structure-verification").evaluate("el => getComputedStyle(el).backgroundColor"), page.locator(".arrangement").evaluate("el => getComputedStyle(el).backgroundColor"))

    def test_projects_and_structure_share_row_rhythm_without_fake_accessories(self):
        projects = self.open("projects")
        project_height = projects.locator(".project-card").first.evaluate("el => getComputedStyle(el).minHeight")
        sections = [{"id": "s1", "name": "Intro", "lengthBars": 8}]
        structure = self.open("structure", study_db(sections=sections))
        section_height = structure.locator(".arrangement-row").first.evaluate("el => getComputedStyle(el).minHeight")
        self.assertEqual(project_height, section_height)
        self.assertEqual(structure.locator(".arrangement-row .more-button").count(), 0)
        expect(structure.get_by_role("button", name="Reorder Intro")).to_be_visible()

    def test_choice_tile_family_is_shared_between_tracks_section_types_and_bars(self):
        tracks = self.open("tracks")
        track = tracks.locator('.track-tile[data-name="Vocal"]')
        track_radius = track.evaluate("el => getComputedStyle(el).borderRadius")
        track_height = track.evaluate("el => getComputedStyle(el).minHeight")

        structure = self.open("structure")
        structure.get_by_role("button", name="Add Section").click()
        intro = structure.get_by_role("button", name="Intro")
        bar = structure.get_by_role("button", name="8", exact=True)
        self.assertIn("choice-tile", intro.get_attribute("class"))
        self.assertIn("choice-tile", bar.get_attribute("class"))
        self.assertEqual(intro.evaluate("el => getComputedStyle(el).borderRadius"), track_radius)
        self.assertEqual(intro.evaluate("el => getComputedStyle(el).minHeight"), track_height)
        intro.click()
        tracks.locator('.track-tile[data-name="Vocal"]').click()
        self.assertEqual(
            intro.evaluate("el => getComputedStyle(el).backgroundColor"),
            tracks.locator('.track-tile[data-name="Vocal"]').evaluate("el => getComputedStyle(el).backgroundColor"),
        )

    def test_context_redundant_sheet_titles_are_removed_but_warning_titles_remain(self):
        sections = [{"id": "s1", "name": "Intro", "lengthBars": 8}]
        structure = self.open("structure", study_db(sections=sections))
        structure.get_by_role("button", name="Add Section").click()
        self.assertEqual(structure.locator(".sheet h2").count(), 0)
        structure.get_by_role("button", name="Done").click()
        structure.get_by_role("button", name="Edit Intro").click()
        self.assertEqual(structure.locator(".sheet h2").count(), 0)

        projects = self.open("projects")
        projects.get_by_role("button", name="Actions for Smithereens").click()
        projects.get_by_role("button", name="Delete", exact=True).click()
        expect(projects.locator(".sheet h2")).to_have_text("Delete project?")

    def test_work_completion_actions_share_page_action_footer(self):
        setup = self.open("setup", study_db(setup=True))
        expect(setup.locator(".page-action-footer").get_by_role("button", name="Continue")).to_be_visible()

        sections = [{"id": "s1", "name": "Intro", "lengthBars": 8}]
        structure = self.open("structure", study_db(sections=sections, verified=True))
        expect(structure.locator(".page-action-footer").get_by_role("button", name="Continue")).to_be_visible()

        tracks_data = study_db(tracks=[{"id": "t1", "name": "Vocal"}])
        tracks = self.open("tracks", tracks_data)
        expect(tracks.locator(".page-action-footer").get_by_role("button", name="Done")).to_be_visible()


if __name__ == "__main__":
    unittest.main()
