"""Physical-review regressions for the isolated FIRE G7 preview shell."""
import json
import os
import unittest
from pathlib import Path

from playwright.sync_api import sync_playwright, expect

SOURCE_KEY = "production-projects-v1"
PREVIEW_KEY = "production-projects-v1-v7-preview"
URL = os.environ.get("FIRE_URL", "http://127.0.0.1:8000").rstrip("/") + "/v7-preview/"


def study_project(project_id="p1", title="Creep", artist="Radiohead", *, setup=False, sections=None, verified=False, tracks=None, tracks_verified=False, activity=1, notes=None):
    return {
        "id": project_id,
        "type": "study",
        "schemaVersion": 5,
        "title": title,
        "artist": artist,
        "createdAt": 1,
        "lastActivityAt": activity,
        "notes": notes or [],
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


def study_db(*, setup=False, structure=False, tracks=False, notes=None):
    sections = [{"id": "s1", "name": "Intro", "lengthBars": 8}] if structure else []
    selected_tracks = [{"id": "t1", "name": "Vocal"}] if tracks else []
    project = study_project(
        setup=setup,
        sections=sections,
        verified=structure,
        tracks=selected_tracks,
        tracks_verified=tracks,
        notes=notes,
    )
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
            "lastActivityAt": 1,
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
            "localStorage.setItem(%s,%s);" % (json.dumps(PREVIEW_KEY), json.dumps(json.dumps(state)))
        ]
        if source_data is not None:
            scripts.append(
                "localStorage.setItem(%s,%s);" % (json.dumps(SOURCE_KEY), json.dumps(json.dumps(source_data)))
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

    def test_projects_build_trace_and_integrated_actions(self):
        page = self.open("projects")
        expect(page.locator(".title-block h1")).to_have_text("Projects")
        expect(page.get_by_role("button", name="New Project")).to_be_visible()
        expect(page.locator(".root-build-info")).to_contain_text("G7 ·")
        actions = page.get_by_role("button", name="Actions for Creep")
        expect(actions).to_be_visible()
        self.assertGreaterEqual(actions.bounding_box()["width"], 44)
        self.assertGreaterEqual(actions.bounding_box()["height"], 44)
        self.assertEqual(actions.evaluate("el => getComputedStyle(el).borderLeftStyle"), "none")

    def test_one_header_scaffold_and_title_scale_across_levels(self):
        projects = self.open("projects")
        project_page = self.open("project")
        setup = self.open("setup")
        sizes = [
            float(page.locator(".title-block h1").evaluate("el => parseFloat(getComputedStyle(el).fontSize)"))
            for page in (projects, project_page, setup)
        ]
        self.assertEqual(sizes[0], sizes[1])
        self.assertEqual(sizes[1], sizes[2])
        for page in (projects, project_page, setup):
            expect(page.locator(".toolbar")).to_be_visible()
        self.assertAlmostEqual(
            projects.locator(".title-block").bounding_box()["y"],
            project_page.locator(".title-block").bounding_box()["y"],
            delta=2,
        )

    def test_new_project_is_stable_minimal_and_uses_cover_public_label(self):
        page = self.open("projects", empty_db())
        page.get_by_role("button", name="New Project").click()
        original = page.get_by_role("button", name="Original")
        cover = page.get_by_role("button", name="Cover")
        title = page.get_by_role("textbox", name="Title")
        artist = page.get_by_role("textbox", name="Artist")
        expect(original).to_have_attribute("aria-pressed", "true")
        expect(cover).to_be_visible()
        expect(title).to_be_visible()
        expect(artist).to_be_visible()
        self.assertEqual(page.locator(".sheet h2").count(), 0)
        self.assertEqual(page.locator(".sheet .field-label").count(), 0)
        self.assertEqual(page.locator(".grabber").count(), 0)
        expect(title).to_have_attribute("placeholder", "Title")
        expect(artist).to_have_attribute("placeholder", "Artist")
        title_y = title.bounding_box()["y"]
        artist_y = artist.bounding_box()["y"]
        expect(title).to_have_attribute("autocapitalize", "words")
        expect(artist).to_have_attribute("autocapitalize", "words")
        cover.click()
        self.assertAlmostEqual(title.bounding_box()["y"], title_y, delta=1)
        self.assertAlmostEqual(artist.bounding_box()["y"], artist_y, delta=1)
        self.assertEqual(page.get_by_text("Song", exact=True).count(), 0)
        self.assertEqual(page.get_by_text("Artist (optional)", exact=True).count(), 0)

    def test_original_artist_optional_cover_artist_required(self):
        page = self.open("projects", empty_db())
        page.get_by_role("button", name="New Project").click()
        page.get_by_role("textbox", name="Title").fill("Even")
        expect(page.get_by_role("button", name="Create")).to_be_enabled()
        page.get_by_role("button", name="Cover").click()
        expect(page.get_by_role("button", name="Create")).to_be_disabled()
        page.get_by_role("textbox", name="Artist").fill("Babel")
        expect(page.get_by_role("button", name="Create")).to_be_enabled()
        page.get_by_role("button", name="Create").click()
        expect(page.locator(".screen-meta")).to_have_text("Babel · Cover")
        preview = page.evaluate("(key) => JSON.parse(localStorage.getItem(key))", PREVIEW_KEY)
        self.assertEqual(preview["projects"][0]["type"], "study")

    def test_project_actions_are_terse_and_edit_sheet_is_minimal(self):
        page = self.open("projects")
        page.get_by_role("button", name="Actions for Creep").click()
        expect(page.get_by_role("button", name="Edit", exact=True)).to_be_visible()
        expect(page.get_by_role("button", name="Reset", exact=True)).to_be_visible()
        expect(page.get_by_role("button", name="Delete", exact=True)).to_be_visible()
        self.assertEqual(page.get_by_role("button", name="Edit Details").count(), 0)
        self.assertEqual(page.get_by_role("button", name="Reset Progress").count(), 0)
        self.assertEqual(page.get_by_role("button", name="Delete Project").count(), 0)
        self.assertEqual(page.locator(".sheet h2").count(), 0)
        self.assertEqual(page.locator(".sheet").get_by_text("Creep", exact=True).count(), 0)
        self.assertEqual(page.locator(".grabber").count(), 0)
        page.get_by_role("button", name="Edit", exact=True).click()
        self.assertEqual(page.locator(".sheet h2").count(), 0)
        self.assertEqual(page.locator(".sheet .field-label").count(), 0)
        expect(page.get_by_role("textbox", name="Title")).to_have_attribute("autocapitalize", "words")
        expect(page.get_by_role("textbox", name="Artist")).to_have_attribute("autocapitalize", "words")

    def test_project_card_actions_do_not_change_active_project(self):
        old = study_project("old", "Old Song", activity=10)
        recent = study_project("recent", "Recent Song", activity=20)
        data = {"version": 5, "currentProjectId": "old", "projects": [old, recent]}
        page = self.open("projects", data)
        page.get_by_role("button", name="Actions for Recent Song").click()
        preview = page.evaluate("(key) => JSON.parse(localStorage.getItem(key))", PREVIEW_KEY)
        self.assertEqual(preview["currentProjectId"], "old")
        page.get_by_role("button", name="Edit", exact=True).click()
        expect(page.get_by_role("textbox", name="Title")).to_have_value("Recent Song")

    def test_destructive_project_actions_require_confirmation(self):
        data = study_db(setup=True, structure=True, tracks=True)
        page = self.open("projects", data)
        page.get_by_role("button", name="Actions for Creep").click()
        page.get_by_role("button", name="Reset", exact=True).click()
        expect(page.locator(".sheet h2")).to_have_text("Reset progress?")
        before = page.evaluate("(key) => JSON.parse(localStorage.getItem(key))", PREVIEW_KEY)
        self.assertTrue(before["projects"][0]["map"]["setup"]["reference"])
        page.get_by_role("button", name="Reset", exact=True).click()
        after = page.evaluate("(key) => JSON.parse(localStorage.getItem(key))", PREVIEW_KEY)
        self.assertFalse(after["projects"][0]["map"]["setup"]["reference"])

        page.get_by_role("button", name="Actions for Creep").click()
        page.get_by_role("button", name="Delete", exact=True).click()
        expect(page.locator(".sheet h2")).to_have_text("Delete project?")
        self.assertEqual(len(page.evaluate("(key) => JSON.parse(localStorage.getItem(key)).projects", PREVIEW_KEY)), 1)
        page.get_by_role("button", name="Cancel").click()
        self.assertEqual(len(page.evaluate("(key) => JSON.parse(localStorage.getItem(key)).projects", PREVIEW_KEY)), 1)

    def test_more_control_is_same_visual_component_on_card_and_project_home(self):
        projects = self.open("projects")
        card_more = projects.get_by_role("button", name="Actions for Creep")
        card_size = float(card_more.evaluate("el => parseFloat(getComputedStyle(el).fontSize)"))
        home = self.open("project")
        toolbar_more = home.get_by_role("button", name="Project actions")
        home_size = float(toolbar_more.evaluate("el => parseFloat(getComputedStyle(el).fontSize)"))
        self.assertEqual(card_size, home_size)
        self.assertGreaterEqual(toolbar_more.bounding_box()["width"], 44)

    def test_projects_sort_by_meaningful_activity_not_opening(self):
        old = study_project("old", "Old Song", activity=10)
        recent = study_project("recent", "Recent Song", activity=20)
        data = {"version": 5, "currentProjectId": "old", "projects": [old, recent]}
        page = self.open("projects", data)
        titles = page.locator(".project-copy strong").all_text_contents()
        self.assertEqual(titles[:2], ["Recent Song", "Old Song"])
        page.locator('[data-project="old"]').click()
        page.get_by_role("button", name="Projects").click()
        titles = page.locator(".project-copy strong").all_text_contents()
        self.assertEqual(titles[:2], ["Recent Song", "Old Song"])
        page.get_by_role("button", name="Actions for Old Song").click()
        page.get_by_role("button", name="Edit", exact=True).click()
        page.get_by_role("textbox", name="Title").fill("Old Song Edited")
        page.get_by_role("button", name="Save").click()
        titles = page.locator(".project-copy strong").all_text_contents()
        self.assertEqual(titles[0], "Old Song Edited")

    def test_project_home_is_one_coherent_cover_progression(self):
        page = self.open("project")
        expect(page.locator(".title-block h1")).to_have_text("Creep")
        expect(page.locator(".screen-meta")).to_have_text("Radiohead · Cover")
        self.assertEqual(page.locator(".journey-group .journey-row").count(), 3)
        current = page.locator('.journey-row[aria-current="step"]')
        expect(current).to_contain_text("Song Setup")
        self.assertEqual(page.locator(".continue-row").count(), 0)
        self.assertEqual(page.locator(".map-complete").count(), 0)
        self.assertEqual(page.get_by_text("Section Study", exact=True).count(), 0)
        self.assertEqual(page.get_by_text("Review Map", exact=True).count(), 0)
        self.assertEqual(page.get_by_text("Later", exact=True).count(), 0)

    def test_completed_project_home_uses_progression_itself_as_status(self):
        page = self.open("project", study_db(setup=True, structure=True, tracks=True))
        self.assertEqual(page.locator(".journey-row.done").count(), 3)
        self.assertEqual(page.locator(".map-complete").count(), 0)
        self.assertEqual(page.get_by_text("Song map complete.", exact=True).count(), 0)

    def test_work_pages_remove_default_helper_copy(self):
        setup = self.open("setup")
        tracks = self.open("tracks")
        self.assertEqual(setup.get_by_text("Import it into your session.", exact=True).count(), 0)
        self.assertEqual(setup.get_by_text("Align it to the bar grid.", exact=True).count(), 0)
        self.assertEqual(setup.get_by_text("Play the full song once.", exact=True).count(), 0)
        self.assertEqual(tracks.get_by_text("Choose everything you hear.", exact=True).count(), 0)

    def test_song_setup_tempo_focus_and_live_continuation(self):
        data = study_db()
        data["projects"][0]["map"]["setup"].update({"reference": True, "grid": True, "firstListen": True})
        page = self.open("setup", data)
        tempo = page.get_by_role("textbox", name="Tempo")
        expect(tempo).to_have_attribute("inputmode", "decimal")
        self.assertGreaterEqual(float(tempo.evaluate("el => parseFloat(getComputedStyle(el).fontSize)")), 16)
        tempo.focus()
        self.assertEqual(tempo.evaluate("el => getComputedStyle(el).outlineStyle"), "none")
        tempo.fill("111")
        expect(page.get_by_role("button", name="Continue")).to_be_visible()

    def test_structure_builder_chooses_type_and_bars_before_insertion(self):
        page = self.open("structure")
        page.get_by_role("button", name="Add Section").click()
        self.assertEqual(page.locator(".grabber").count(), 0)
        intro = page.get_by_role("button", name="Intro")
        intro.click()
        self.assertEqual(page.locator(".arrangement-row").count(), 0)
        page.get_by_role("button", name="12").click()
        page.get_by_role("button", name="Add", exact=True).click()
        expect(page.locator(".sheet")).to_be_visible()
        expect(page.locator("#sectionAddedNotice")).to_have_text("Added Intro · 12 bars")
        page.get_by_role("button", name="Done").click()
        expect(page.locator(".arrangement-row")).to_contain_text("Intro")
        expect(page.locator(".arrangement-row")).to_contain_text("12 bars")

    def test_structure_builder_supports_custom_length_without_edit_round_trip(self):
        page = self.open("structure")
        page.get_by_role("button", name="Add Section").click()
        page.get_by_role("button", name="Verse").click()
        page.get_by_role("button", name="Custom").last.click()
        custom = page.get_by_role("textbox", name="Custom bars")
        custom.fill("6")
        page.get_by_role("button", name="Add", exact=True).click()
        page.get_by_role("button", name="Done").click()
        expect(page.locator(".arrangement-row")).to_contain_text("6 bars")

    def test_edit_section_has_no_move_buttons_and_reorder_handle_is_direct(self):
        sections = [
            {"id": "s1", "name": "Intro", "lengthBars": 8},
            {"id": "s2", "name": "Verse", "lengthBars": 16},
        ]
        data = {"version": 5, "currentProjectId": "p1", "projects": [study_project(sections=sections)]}
        page = self.open("structure", data)
        handle = page.get_by_role("button", name="Reorder Verse")
        self.assertGreaterEqual(handle.bounding_box()["width"], 44)
        self.assertGreaterEqual(handle.bounding_box()["height"], 44)
        page.get_by_role("button", name="Edit Intro").click()
        self.assertEqual(page.get_by_role("button", name="Move Up").count(), 0)
        self.assertEqual(page.get_by_role("button", name="Move Down").count(), 0)
        expect(page.get_by_role("textbox", name="Name")).to_have_attribute("autocapitalize", "words")

    def test_structure_reorders_from_handle_keyboard_without_edit_sheet(self):
        sections = [
            {"id": "s1", "name": "Intro", "lengthBars": 8},
            {"id": "s2", "name": "Verse", "lengthBars": 16},
        ]
        data = {"version": 5, "currentProjectId": "p1", "projects": [study_project(sections=sections)]}
        page = self.open("structure", data)
        page.get_by_role("button", name="Reorder Verse").focus()
        page.keyboard.press("ArrowUp")
        names = page.locator(".arrangement-name").all_text_contents()
        self.assertEqual(names, ["Verse", "Intro"])
        self.assertEqual(page.locator(".sheet").count(), 0)

    def test_tracks_selection_requires_done_to_complete_mapping(self):
        data = study_db(setup=True, structure=True, tracks=False)
        page = self.open("tracks", data)
        page.locator('.track-tile[data-name="Vocal"]').click()
        expect(page.get_by_role("button", name="Done")).to_be_visible()
        pending = page.evaluate("(key) => JSON.parse(localStorage.getItem(key))", PREVIEW_KEY)
        self.assertFalse(pending["projects"][0]["map"]["tracksVerified"])
        page.get_by_role("button", name="Done").click()
        expect(page.locator(".journey-row.done")).to_have_count(3)
        self.assertEqual(page.locator(".map-complete").count(), 0)
        self.assertEqual(page.get_by_text("Section Study", exact=True).count(), 0)
        self.assertNotIn("section-study", page.url)
        complete = page.evaluate("(key) => JSON.parse(localStorage.getItem(key))", PREVIEW_KEY)
        self.assertTrue(complete["projects"][0]["map"]["tracksVerified"])

    def test_track_changes_invalidate_previous_confirmation(self):
        data = study_db(setup=True, structure=True, tracks=True)
        page = self.open("tracks", data)
        page.locator('.track-tile[data-name="Drums"]').click()
        changed = page.evaluate("(key) => JSON.parse(localStorage.getItem(key))", PREVIEW_KEY)
        self.assertFalse(changed["projects"][0]["map"]["tracksVerified"])
        page.get_by_role("button", name="Done").click()
        confirmed = page.evaluate("(key) => JSON.parse(localStorage.getItem(key))", PREVIEW_KEY)
        self.assertTrue(confirmed["projects"][0]["map"]["tracksVerified"])

    def test_tracks_keep_compact_grid_and_integrate_other(self):
        page = self.open("tracks")
        self.assertEqual(page.locator(".track-grid").count(), 1)
        expect(page.get_by_role("button", name="Other")).to_have_class(lambda value: "track-tile" in value and "track-other" in value)
        page.locator('.track-tile[data-name="Vocal"]').click()
        expect(page.locator('.track-tile[data-name="Vocal"] .track-check')).to_have_text("✓")

    def test_custom_track_name_uses_word_capitalization(self):
        page = self.open("tracks")
        page.get_by_role("button", name="Other").click()
        field = page.get_by_role("textbox", name="Track name")
        expect(field).to_have_attribute("autocapitalize", "words")
        field.fill("Strings")
        page.get_by_role("button", name="Add").click()
        expect(page.locator('.track-tile[data-name="Strings"]')).to_be_visible()
        state = page.evaluate("(key) => JSON.parse(localStorage.getItem(key))", PREVIEW_KEY)
        self.assertFalse(state["projects"][0]["map"]["tracksVerified"])

    def test_original_project_stays_first_class(self):
        page = self.open("project", original_db())
        expect(page.locator(".title-block h1")).to_have_text("Even")
        expect(page.locator(".screen-meta")).to_have_text("Babel · Original")
        expect(page.get_by_text("Original workflow isn't built yet.")).to_be_visible()
        expect(page.get_by_role("button", name="Project actions")).to_be_visible()

    def test_existing_notes_remain_reachable(self):
        data = study_db(notes=[{"type": "Idea", "context": "Project", "text": "Keep verse small."}])
        page = self.open("project", data)
        expect(page.get_by_role("button", name="Notes 1 saved")).to_be_visible()
        page.get_by_role("button", name="Notes 1 saved").click()
        expect(page.locator(".note-card")).to_contain_text("Keep verse small.")

    def test_preview_remains_isolated_from_v6_storage(self):
        source = study_db(setup=True, structure=True, tracks=True)
        page = self.open("projects", empty_db(), source_data=source)
        page.get_by_role("button", name="New Project").click()
        page.get_by_role("textbox", name="Title").fill("Even")
        page.get_by_role("button", name="Create").click()
        production = page.evaluate("(key) => JSON.parse(localStorage.getItem(key))", SOURCE_KEY)
        self.assertEqual(production, source)

    def test_phone_pages_use_natural_document_scrolling_and_no_visualviewport_logic(self):
        page = self.open("project", study_db(setup=True, structure=True, tracks=True), height=720)
        self.assertNotEqual(page.evaluate("getComputedStyle(document.documentElement).overflowY"), "hidden")
        self.assertNotEqual(page.evaluate("getComputedStyle(document.body).overflowY"), "hidden")
        source = Path("v7-preview/app.js").read_text()
        styles = Path("v7-preview/styles.css").read_text()
        self.assertNotIn("visualViewport", source)
        self.assertNotIn("dataset.scrollable", source)
        self.assertNotIn("data-v7-fit", styles)

    def test_superseded_g7_interactions_are_removed(self):
        source = Path("v7-preview/app.js").read_text()
        model = Path("v7-preview/model.js").read_text()
        styles = Path("v7-preview/styles.css").read_text()
        self.assertNotIn("quick-add-section", source)
        self.assertNotIn("move-section", source)
        self.assertNotIn("continue-section-study", source)
        self.assertNotIn('>Recreation<', source)
        self.assertNotIn('class="grabber"', source)
        self.assertNotIn(".grabber", styles)
        self.assertNotIn("continue-row", source)
        self.assertNotIn("map-complete", source)
        self.assertIn("Cover", model)
        self.assertIn("tracksVerified", model)


if __name__ == "__main__":
    unittest.main()
