"""Browser regressions for the final generic G7 shell-polish pass."""
import os
import re
import unittest

from playwright.sync_api import expect, sync_playwright

BASE = os.environ.get("FIRE_URL", "http://127.0.0.1:8000").rstrip("/")
URL = BASE + "/v7-preview/?reset=1"
TRANSPARENT = "rgba(0, 0, 0, 0)"


class G7FinalShellPolishBrowser(unittest.TestCase):
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

    def open(self):
        width = int(os.environ.get("FIRE_TEST_WIDTH", "390"))
        context = self.browser.new_context(viewport={"width": width, "height": 844}, has_touch=True)
        self.addCleanup(context.close)
        page = context.new_page()
        page.set_default_timeout(5000)
        errors = []
        page.on("pageerror", lambda error: errors.append(str(error)))
        page.on("console", lambda message: errors.append(message.text) if message.type == "error" else None)
        response = page.goto(URL)
        self.assertEqual(response.status, 200)
        self.addCleanup(lambda: self.assertEqual(errors, []))
        expect(page.locator(".project-list")).to_be_visible()
        return page

    def assert_pressed_surface(self, color):
        match = re.fullmatch(r"rgba\(255, 255, 255, ([0-9.]+)\)", color)
        self.assertIsNotNone(match, f"Expected translucent white pressed surface, got {color}")
        self.assertAlmostEqual(float(match.group(1)), 0.045, delta=0.003)

    def press_and_read(self, page, control, parent):
        box = control.bounding_box()
        self.assertIsNotNone(box)
        page.mouse.move(box["x"] + box["width"] / 2, box["y"] + box["height"] / 2)
        page.mouse.down()
        parent_color = parent.evaluate("el => getComputedStyle(el).backgroundColor")
        child_color = control.evaluate("el => getComputedStyle(el).backgroundColor")
        page.mouse.up()
        return parent_color, child_color

    def test_project_text_fields_restore_normal_text_assistance_and_keep_focus_progression(self):
        page = self.open()
        page.get_by_role("button", name="New Project").click()

        title = page.locator("#newProjectTitle")
        artist = page.locator("#newProjectArtist")
        expect(title).to_be_visible()
        expect(artist).to_be_visible()

        for field in (title, artist):
            self.assertEqual(field.get_attribute("autocorrect"), "on")
            self.assertEqual(field.get_attribute("spellcheck"), "true")
            self.assertNotEqual(field.get_attribute("autocomplete"), "off")
            self.assertEqual(field.get_attribute("autocapitalize"), "words")

        self.assertEqual(title.get_attribute("enterkeyhint"), "next")
        self.assertEqual(artist.get_attribute("enterkeyhint"), "done")
        title.fill("Even")
        title.press("Enter")
        expect(artist).to_be_focused()

    def test_split_action_rows_use_one_edge_to_edge_pressed_surface(self):
        page = self.open()

        # Projects: both the main target and the trailing actions target paint the parent row.
        project_row = page.locator('[data-project-card="preview-creep"]')
        more = project_row.locator(".project-card-actions")
        parent_color, child_color = self.press_and_read(page, more, project_row)
        self.assert_pressed_surface(parent_color)
        self.assertEqual(child_color, TRANSPARENT)
        page.get_by_role("button", name="Cancel").click()

        project_open = project_row.locator(".project-open")
        parent_color, child_color = self.press_and_read(page, project_open, project_row)
        self.assert_pressed_surface(parent_color)
        self.assertEqual(child_color, TRANSPARENT)
        expect(page.locator("h1")).to_have_text("Creep")

        # Structure: edit content and reorder accessory share the same parent-owned press surface.
        page.locator('.journey-row[data-route="structure"]').click()
        expect(page.locator("h1")).to_have_text("Structure")
        structure_row = page.locator(".arrangement-row").first
        edit = structure_row.locator(".section-edit-target")
        parent_color, child_color = self.press_and_read(page, edit, structure_row)
        self.assert_pressed_surface(parent_color)
        self.assertEqual(child_color, TRANSPARENT)
        expect(page.locator(".sheet")).to_be_visible()
        page.keyboard.press("Escape")
        expect(page.locator(".sheet")).to_be_hidden()

        handle = structure_row.locator(".reorder-handle")
        parent_color, child_color = self.press_and_read(page, handle, structure_row)
        self.assert_pressed_surface(parent_color)
        self.assertEqual(child_color, TRANSPARENT)


if __name__ == "__main__":
    unittest.main()
