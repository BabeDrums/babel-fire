"""Browser regressions for the final generic G7 shell-polish pass."""
import os
import unittest
from pathlib import Path

from playwright.sync_api import expect, sync_playwright

BASE = os.environ.get("FIRE_URL", "http://127.0.0.1:8000").rstrip("/")
URL = BASE + "/v7-preview/?reset=1"


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

    def test_split_action_rows_share_parent_pressed_contract_and_keep_semantics(self):
        # Chromium touch emulation does not reliably expose transient :active state. Certify the
        # shipped selector ownership statically, then certify the child actions independently in
        # the real browser. Physical iPhone/iPad review remains authoritative for touch appearance.
        css = Path("v7-preview/frame-primitives.css").read_text(encoding="utf-8")
        for selector in (
            ".project-card:has(.project-open:active)",
            ".project-card:has(.project-card-actions:active)",
            ".arrangement-row:has(.section-edit-target:active)",
            ".arrangement-row:has(.reorder-handle:active)",
        ):
            self.assertIn(selector, css)
        self.assertIn("background: rgba(255,255,255,.045);", css)
        self.assertIn(
            ".project-open:active,\n.project-card-actions:active,\n.section-edit-target:active,\n.reorder-handle:active {\n  background: transparent;\n}",
            css,
        )

        page = self.open()

        # Project trailing action still opens management without navigating the row.
        more = page.locator('[data-project-card="preview-creep"] .project-card-actions')
        more.click()
        expect(page.locator(".sheet")).to_be_visible()
        expect(page.locator("h1")).to_have_text("Projects")
        page.get_by_role("button", name="Cancel").click()
        expect(page.locator(".sheet")).to_be_hidden()

        # Main project target still navigates independently.
        page.locator('[data-project-card="preview-creep"] .project-open').click()
        expect(page.locator("h1")).to_have_text("Creep")

        # Structure edit target still opens the editor while the reorder accessory remains distinct.
        page.locator('.journey-row[data-route="structure"]').click()
        expect(page.locator("h1")).to_have_text("Structure")
        edit = page.locator(".arrangement-row:first-child .section-edit-target")
        handle = page.locator(".arrangement-row:first-child .reorder-handle")
        expect(edit).to_be_visible()
        expect(handle).to_be_visible()
        edit.click()
        expect(page.locator(".sheet")).to_be_visible()
        page.keyboard.press("Escape")
        expect(page.locator(".sheet")).to_be_hidden()


if __name__ == "__main__":
    unittest.main()
