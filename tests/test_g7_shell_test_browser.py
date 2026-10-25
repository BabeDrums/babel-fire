"""Browser smoke coverage for the real G7 Shell Test certification surface."""
import os
import re
import unittest

from playwright.sync_api import expect, sync_playwright

URL = os.environ.get("FIRE_URL", "http://127.0.0.1:8000").rstrip("/") + "/v7-preview/shell-test.html"


class G7ShellTestBrowser(unittest.TestCase):
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
        return page

    def test_shell_test_loads_exact_build_and_shared_primitives(self):
        page = self.open()
        expect(page.locator("h1")).to_have_text("Shell Test")
        build = page.locator(".build-info")
        expect(build).to_have_text(re.compile(r"G7 · [0-9a-f]{7}"))

        add = page.get_by_role("button", name="Example add action")
        self.assertEqual(add.evaluate("el => getComputedStyle(el).fontSize"), "0px")
        self.assertEqual(add.evaluate("el => getComputedStyle(el, '::before').width"), "18px")
        self.assertEqual(add.evaluate("el => getComputedStyle(el, '::before').borderRadius"), "999px")
        self.assertEqual(add.evaluate("el => getComputedStyle(el, '::after').height"), "18px")

        # The contextual action belongs to the same visual title line instead of floating above it.
        title_box = page.locator("h1").bounding_box()
        add_box = add.bounding_box()
        self.assertIsNotNone(title_box)
        self.assertIsNotNone(add_box)
        title_center = title_box["y"] + title_box["height"] / 2
        add_center = add_box["y"] + add_box["height"] / 2
        self.assertLessEqual(abs(title_center - add_center), 2.0)

        complete = page.locator(".checkmark").first
        self.assertEqual(complete.evaluate("el => getComputedStyle(el).fontSize"), "0px")
        self.assertEqual(complete.evaluate("el => getComputedStyle(el, '::before').width"), "6px")
        self.assertEqual(complete.evaluate("el => getComputedStyle(el, '::before').height"), "2px")
        self.assertEqual(complete.evaluate("el => getComputedStyle(el, '::before').borderRadius"), "999px")
        self.assertEqual(complete.evaluate("el => getComputedStyle(el, '::after').width"), "11px")
        self.assertEqual(complete.evaluate("el => getComputedStyle(el, '::after').borderRadius"), "999px")

        current = page.locator(".journey-mark.current")
        self.assertEqual(current.evaluate("el => getComputedStyle(el).borderTopWidth"), "2px")
        self.assertEqual(current.evaluate("el => getComputedStyle(el).borderTopColor"), "rgb(217, 217, 223)")
        self.assertEqual(current.evaluate("el => getComputedStyle(el, '::after').content"), '""')
        self.assertEqual(current.evaluate("el => getComputedStyle(el, '::after').position"), "absolute")
        for side in ("top", "right", "bottom", "left"):
            self.assertEqual(current.evaluate(f"el => getComputedStyle(el, '::after').{side}"), "0px")
        inner_ring_width = current.evaluate(
            "el => parseFloat(getComputedStyle(el, '::after').borderTopWidth)"
        )
        self.assertGreaterEqual(inner_ring_width, 2.5)
        self.assertEqual(current.evaluate("el => getComputedStyle(el, '::after').borderTopStyle"), "solid")
        self.assertEqual(
            current.evaluate("el => getComputedStyle(el, '::after').borderTopColor"),
            "rgba(232, 232, 237, 0.38)",
        )
        self.assertEqual(current.evaluate("el => getComputedStyle(el, '::after').backgroundColor"), "rgba(0, 0, 0, 0)")

        management = page.get_by_role("button", name="Example row actions")
        self.assertEqual(management.evaluate("el => getComputedStyle(el).borderLeftWidth"), "0px")
        self.assertEqual(management.evaluate("el => getComputedStyle(el).fontSize"), "0px")
        self.assertEqual(management.evaluate("el => getComputedStyle(el, '::before').width"), "3px")
        self.assertEqual(management.evaluate("el => getComputedStyle(el, '::before').height"), "3px")

        # Back and forward are the exact same continuous rounded chevron mask, mirrored by direction.
        chevron = page.locator(".chevron").first
        back = page.locator(".shell-test-link")
        self.assertEqual(chevron.evaluate("el => getComputedStyle(el).fontSize"), "0px")
        forward_mask = chevron.evaluate("el => getComputedStyle(el, '::before').webkitMaskImage")
        back_mask = back.evaluate("el => getComputedStyle(el, '::before').webkitMaskImage")
        self.assertEqual(forward_mask, back_mask)
        self.assertIn("data:image/svg+xml", forward_mask)
        self.assertEqual(chevron.evaluate("el => getComputedStyle(el, '::after').content"), "none")
        self.assertNotEqual(back.evaluate("el => getComputedStyle(el, '::before').transform"), "none")
        self.assertEqual(back.evaluate("el => getComputedStyle(el).width"), "44px")
        self.assertEqual(back.evaluate("el => getComputedStyle(el).height"), "44px")

        reorder = page.get_by_role("button", name="Reorder example")
        self.assertEqual(reorder.evaluate("el => getComputedStyle(el).fontSize"), "0px")
        self.assertEqual(reorder.evaluate("el => getComputedStyle(el, '::before').width"), "14px")
        self.assertEqual(reorder.evaluate("el => getComputedStyle(el, '::before').height"), "2px")
        self.assertEqual(reorder.evaluate("el => getComputedStyle(el, '::before').borderRadius"), "999px")

    def test_shell_test_temporary_ui_uses_same_adaptive_dialog_primitive(self):
        page = self.open()
        page.get_by_role("button", name="Open selection").click()
        dialog = page.get_by_role("dialog", name="Shell Test dialog")
        expect(dialog).to_be_visible()
        self.assertEqual(page.evaluate("document.body.style.overflow"), "hidden")
        actions = dialog.locator(".sheet-actions")
        self.assertEqual(actions.evaluate("el => getComputedStyle(el).borderTopWidth"), "0px")
        self.assertEqual(actions.evaluate("el => getComputedStyle(el).paddingTop"), "0px")
        self.assertNotIn("inset", dialog.evaluate("el => getComputedStyle(el).boxShadow"))
        page.keyboard.press("Escape")
        expect(dialog).to_be_hidden()
        self.assertEqual(page.evaluate("document.body.style.overflow"), "")


if __name__ == "__main__":
    unittest.main()
