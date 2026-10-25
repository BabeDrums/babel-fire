"""Rhythm, navigation, and visual-grammar regressions for the isolated FIRE G7 preview shell."""
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

    def test_project_field_focus_belongs_to_outer_group(self):
        page = self.open("projects", empty_db())
        page.get_by_role("button", name="New Project").click()
        group = page.locator(".project-field-group")
        title = page.get_by_role("textbox", name="Title")
        title.focus()
        self.assertEqual(title.evaluate("el => getComputedStyle(el).boxShadow"), "none")
        self.assertGreater(
            float(group.evaluate("el => parseFloat(getComputedStyle(el).borderTopWidth)")),
            0,
        )
        self.assertNotEqual(group.evaluate("el => getComputedStyle(el).boxShadow"), "none")

    def test_new_project_uses_major_then_action_spacing(self):
        page = self.open("projects", empty_db())
        page.get_by_role("button", name="New Project").click()
        project_type = page.locator(".project-type-control").bounding_box()
        fields = page.locator(".project-field-group").bounding_box()
        actions = page.locator(".sheet-actions").bounding_box()
        major_gap = float(page.evaluate("parseFloat(getComputedStyle(document.documentElement).getPropertyValue('--sheet-major-gap'))"))
        action_gap = float(page.evaluate("parseFloat(getComputedStyle(document.documentElement).getPropertyValue('--sheet-action-gap'))"))
        self.assertAlmostEqual(fields["y"] - (project_type["y"] + project_type["height"]), major_gap, delta=1.0)
        self.assertAlmostEqual(actions["y"] - (fields["y"] + fields["height"]), action_gap, delta=1.0)

    def test_project_action_cancel_matches_action_group_width(self):
        page = self.open("projects")
        page.get_by_role("button", name="Actions for Smithereens").click()
        group = page.locator(".action-menu").bounding_box()
        cancel = page.get_by_role("button", name="Cancel")
        cancel_box = cancel.bounding_box()
        self.assertAlmostEqual(cancel_box["x"], group["x"], delta=1.0)
        self.assertAlmostEqual(cancel_box["width"], group["width"], delta=1.0)
        self.assertNotEqual(cancel.evaluate("el => getComputedStyle(el).backgroundColor"), "rgba(0, 0, 0, 0)")

    def test_toolbar_actions_are_anchored_controls_without_changing_back_semantics(self):
        projects = self.open("projects")
        add = projects.get_by_role("button", name="New Project")
        self.assertNotEqual(add.evaluate("el => getComputedStyle(el).backgroundColor"), "rgba(0, 0, 0, 0)")
        project = self.open("project")
        more = project.get_by_role("button", name="Project actions")
        back = project.get_by_role("button", name="Projects")
        self.assertNotEqual(more.evaluate("el => getComputedStyle(el).backgroundColor"), "rgba(0, 0, 0, 0)")
        self.assertEqual(back.evaluate("el => getComputedStyle(el).backgroundColor"), "rgba(0, 0, 0, 0)")
        self.assertAlmostEqual(add.bounding_box()["width"], more.bounding_box()["width"], delta=1.0)

    def test_grouped_page_rows_share_one_64px_rhythm(self):
        sections = [{"id": "s1", "name": "Intro", "lengthBars": 8}]
        data = study_db(setup=True, sections=sections, verified=True)
        pages = {
            "projects": (self.open("projects", data), ".project-card"),
            "home": (self.open("project", data), ".journey-row"),
            "setup": (self.open("setup", data), ".form-row"),
            "structure": (self.open("structure", data), ".arrangement-row"),
            "verification": (self.open("structure", data), ".structure-confirm-row"),
        }
        heights = {}
        for name, (page, selector) in pages.items():
            heights[name] = float(page.locator(selector).first.evaluate("el => parseFloat(getComputedStyle(el).minHeight)"))
        self.assertEqual(set(heights.values()), {64.0})

    def test_connected_selection_surfaces_share_cell_geometry(self):
        tracks = self.open("tracks")
        track = tracks.locator('.track-tile[data-name="Vocal"]')
        track_height = float(track.evaluate("el => parseFloat(getComputedStyle(el).minHeight)"))
        self.assertEqual(track_height, 52.0)
        self.assertEqual(track.evaluate("el => getComputedStyle(el).borderTopWidth"), "0px")
        expect(tracks.locator(".track-grid.selection-surface")).to_be_visible()

        structure = self.open("structure")
        structure.get_by_role("button", name="Add Section").click()
        intro = structure.get_by_role("button", name="Intro")
        self.assertEqual(float(intro.evaluate("el => parseFloat(getComputedStyle(el).minHeight)")), track_height)
        expect(structure.locator(".section-types.selection-surface")).to_be_visible()
        expect(structure.locator(".bars-grid.segmented-control")).to_be_visible()
        self.assertEqual(structure.locator(".bars-grid .segment-option").count(), 5)

    def test_selected_cells_use_parent_owned_geometry_without_inner_outline(self):
        page = self.open("tracks", study_db(tracks=[{"id": "t1", "name": "Vocal"}]))
        selected = page.locator('.track-tile[data-name="Vocal"]')
        surface = page.locator(".track-grid")
        self.assertEqual(selected.evaluate("el => getComputedStyle(el).boxShadow"), "none")
        self.assertEqual(selected.evaluate("el => getComputedStyle(el).borderRadius"), "0px")
        self.assertGreater(float(surface.evaluate("el => parseFloat(getComputedStyle(el).borderTopLeftRadius)")), 0)
        self.assertEqual(page.locator(".track-check").count(), 0)

        projects = self.open("projects", empty_db())
        projects.get_by_role("button", name="New Project").click()
        chosen = projects.get_by_role("button", name="Original")
        self.assertEqual(chosen.evaluate("el => getComputedStyle(el).borderRadius"), "0px")
        self.assertEqual(projects.locator(".project-type-control").evaluate("el => getComputedStyle(el).paddingTop"), "0px")

    def test_add_section_uses_major_group_spacing(self):
        page = self.open("structure")
        page.get_by_role("button", name="Add Section").click()
        types = page.locator(".section-types").bounding_box()
        bars = page.locator(".bars-grid").bounding_box()
        actions = page.locator(".sheet-actions").bounding_box()
        content_gap = float(page.evaluate("parseFloat(getComputedStyle(document.documentElement).getPropertyValue('--sheet-content-gap'))"))
        action_gap = float(page.evaluate("parseFloat(getComputedStyle(document.documentElement).getPropertyValue('--sheet-action-gap'))"))
        self.assertAlmostEqual(bars["y"] - (types["y"] + types["height"]), content_gap, delta=1.0)
        self.assertAlmostEqual(actions["y"] - (bars["y"] + bars["height"]), action_gap, delta=1.0)
        self.assertEqual(page.locator("#sectionAddedNotice").count(), 0)

    def test_tracks_and_structure_use_toolbar_plus_without_fake_other_row(self):
        structure = self.open("structure")
        structure_add = structure.get_by_role("button", name="Add Section")
        self.assertTrue(structure_add.evaluate("el => el.closest('.toolbar') !== null"))

        tracks = self.open("tracks")
        track_add = tracks.get_by_role("button", name="Add Track")
        self.assertTrue(track_add.evaluate("el => el.closest('.toolbar') !== null"))
        self.assertEqual(tracks.get_by_role("button", name="Other").count(), 0)

    def test_track_grid_balances_the_final_row_for_the_current_viewport(self):
        page = self.open("tracks")
        surface = page.locator(".track-grid").bounding_box()
        tiles = page.locator(".track-tile")
        first = tiles.first.bounding_box()
        last = tiles.last.bounding_box()
        width = page.viewport_size["width"]
        if width >= 700:
            self.assertAlmostEqual(last["width"], surface["width"] - 2, delta=3.0)
        else:
            penultimate = tiles.nth(tiles.count() - 2).bounding_box()
            combined = penultimate["width"] + last["width"] + 1
            self.assertAlmostEqual(combined, surface["width"] - 2, delta=3.0)
            self.assertAlmostEqual(first["width"], last["width"], delta=2.0)

    def test_structure_rows_do_not_fake_completion_or_project_accessories(self):
        sections = [{"id": "s1", "name": "Intro", "lengthBars": 8}]
        page = self.open("structure", study_db(sections=sections))
        row = page.locator(".arrangement-row")
        self.assertEqual(row.locator(".checkmark").count(), 0)
        self.assertEqual(row.locator(".chevron").count(), 0)
        self.assertEqual(row.locator(".more-button").count(), 0)
        self.assertEqual(row.locator(".arrangement-index").count(), 0)
        expect(page.get_by_role("button", name="Reorder section 1, Intro")).to_be_visible()
        expect(page.get_by_role("button", name="Edit section 1, Intro, 8 bars")).to_be_visible()

    def test_row_label_typography_does_not_change_with_progress_state(self):
        sections = [{"id": "s1", "name": "Intro", "lengthBars": 8}]
        page = self.open("project", study_db(setup=True, sections=sections, verified=False))
        weights = page.locator(".journey-row .row-title").evaluate_all(
            "els => els.map(el => getComputedStyle(el).fontWeight)"
        )
        self.assertEqual(len(set(weights)), 1)

        setup = self.open("setup", study_db(setup=True))
        structure = self.open("structure", study_db(sections=sections))
        setup_weight = setup.locator(".form-label").first.evaluate("el => getComputedStyle(el).fontWeight")
        structure_weight = structure.locator(".arrangement-name").first.evaluate("el => getComputedStyle(el).fontWeight")
        self.assertEqual(setup_weight, structure_weight)

    def test_structure_and_setup_share_primary_label_anchor(self):
        sections = [{"id": "s1", "name": "Intro", "lengthBars": 8}]
        setup = self.open("setup")
        structure = self.open("structure", study_db(sections=sections))
        setup_x = setup.locator(".form-label").first.bounding_box()["x"]
        structure_x = structure.locator(".arrangement-name").first.bounding_box()["x"]
        self.assertAlmostEqual(setup_x, structure_x, delta=1.0)

    def test_setup_editable_values_share_one_trailing_control_grammar(self):
        page = self.open("setup")
        values = page.locator(".value-control")
        self.assertEqual(values.count(), 2)
        heights = values.evaluate_all("els => els.map(el => getComputedStyle(el).minHeight)")
        backgrounds = values.evaluate_all("els => els.map(el => getComputedStyle(el).backgroundColor)")
        self.assertEqual(len(set(heights)), 1)
        self.assertEqual(len(set(backgrounds)), 1)
        self.assertNotEqual(backgrounds[0], "rgba(0, 0, 0, 0)")

    def test_work_screens_share_first_content_anchor(self):
        sections = [{"id": "s1", "name": "Intro", "lengthBars": 8}]
        pages = [
            self.open("setup", study_db(setup=True)),
            self.open("structure", study_db(sections=sections, verified=True)),
            self.open("tracks", study_db(tracks=[{"id": "t1", "name": "Vocal"}])),
        ]
        starts = [page.locator(".work-content").first.bounding_box()["y"] for page in pages]
        self.assertLessEqual(max(starts) - min(starts), 1.0)

    def test_concise_work_labels_are_current(self):
        home = self.open("project")
        expect(home.get_by_role("button", name="Setup")).to_be_visible()
        self.assertEqual(home.get_by_text("Song Setup", exact=True).count(), 0)

        setup = self.open("setup")
        expect(setup.locator(".title-block h1")).to_have_text("Setup")
        expect(setup.get_by_text("Listen", exact=True)).to_be_visible()
        self.assertEqual(setup.get_by_text("First Listen", exact=True).count(), 0)

        sections = [{"id": "s1", "name": "Intro", "lengthBars": 8}]
        structure = self.open("structure", study_db(sections=sections))
        expect(structure.get_by_text("Accurate", exact=True)).to_be_visible()
        self.assertEqual(structure.get_by_text("Matches the song", exact=True).count(), 0)

    def test_toolbar_to_title_gap_is_tight_and_consistent(self):
        pages = [self.open("projects"), self.open("project"), self.open("structure")]
        gaps = []
        for page in pages:
            toolbar = page.locator(".toolbar").bounding_box()
            title = page.locator(".title-block").bounding_box()
            gaps.append(round(title["y"] - (toolbar["y"] + toolbar["height"]), 1))
        self.assertLessEqual(max(gaps), 8.0)
        self.assertLessEqual(max(gaps) - min(gaps), 1.0)

    def test_work_completion_actions_share_lower_page_action_region(self):
        sections = [{"id": "s1", "name": "Intro", "lengthBars": 8}]
        setup = self.open("setup", study_db(setup=True))
        structure = self.open("structure", study_db(sections=sections, verified=True))
        tracks = self.open("tracks", study_db(tracks=[{"id": "t1", "name": "Vocal"}]))
        for page, label in ((setup, "Continue"), (structure, "Continue"), (tracks, "Done")):
            footer = page.locator(".page-action-footer")
            expect(footer.get_by_role("button", name=label)).to_be_visible()
            self.assertTrue(footer.evaluate("el => el.closest('.work-screen') !== null"))

    def test_visible_back_retraces_actual_work_path(self):
        sections = [{"id": "s1", "name": "Intro", "lengthBars": 8}]
        data = study_db(
            setup=True,
            sections=sections,
            verified=True,
            tracks=[{"id": "t1", "name": "Vocal"}],
            tracks_verified=False,
        )
        page = self.open("project", data)
        page.get_by_role("button", name="Setup").click()
        expect(page.locator(".title-block h1")).to_have_text("Setup")
        page.get_by_role("button", name="Continue").click()
        expect(page.locator(".title-block h1")).to_have_text("Structure")
        page.get_by_role("button", name="Continue").click()
        expect(page.locator(".title-block h1")).to_have_text("Tracks")

        page.locator(".icon-back").click()
        expect(page.locator(".title-block h1")).to_have_text("Structure")
        page.locator(".icon-back").click()
        expect(page.locator(".title-block h1")).to_have_text("Setup")
        page.locator(".icon-back").click()
        expect(page.locator(".title-block h1")).to_have_text("Smithereens")

    def test_direct_work_entry_backs_to_home_and_browser_back_agrees(self):
        page = self.open("project")
        page.get_by_role("button", name="Tracks").click()
        expect(page.locator(".title-block h1")).to_have_text("Tracks")
        page.locator(".icon-back").click()
        expect(page.locator(".title-block h1")).to_have_text("Smithereens")

        page.get_by_role("button", name="Structure").click()
        expect(page.locator(".title-block h1")).to_have_text("Structure")
        page.go_back()
        expect(page.locator(".title-block h1")).to_have_text("Smithereens")

    def test_done_returns_home_without_creating_back_loop(self):
        sections = [{"id": "s1", "name": "Intro", "lengthBars": 8}]
        data = study_db(
            setup=True,
            sections=sections,
            verified=True,
            tracks=[{"id": "t1", "name": "Vocal"}],
            tracks_verified=False,
        )
        page = self.open("project", data)
        page.get_by_role("button", name="Tracks").click()
        page.get_by_role("button", name="Done").click()
        expect(page.locator(".title-block h1")).to_have_text("Smithereens")
        page.locator(".icon-back").click()
        expect(page.locator(".title-block h1")).to_have_text("Projects")

    def test_context_redundant_sheet_titles_remain_removed(self):
        sections = [{"id": "s1", "name": "Intro", "lengthBars": 8}]
        structure = self.open("structure", study_db(sections=sections))
        structure.get_by_role("button", name="Add Section").click()
        self.assertEqual(structure.locator(".sheet h2").count(), 0)
        structure.get_by_role("button", name="Done").click()
        structure.get_by_role("button", name="Edit section 1, Intro, 8 bars").click()
        self.assertEqual(structure.locator(".sheet h2").count(), 0)

        projects = self.open("projects")
        projects.get_by_role("button", name="Actions for Smithereens").click()
        projects.get_by_role("button", name="Delete", exact=True).click()
        expect(projects.locator(".sheet h2")).to_have_text("Delete project?")


if __name__ == "__main__":
    unittest.main()
