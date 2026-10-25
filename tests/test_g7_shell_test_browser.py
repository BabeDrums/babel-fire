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
        self.assertEqual(add.evaluate("el => getComputedStyle(el).backgroundColor"), "rgba(0, 0, 0, 0)")
        self.assertEqual(add.evaluate("el => getComputedStyle(el).borderTopWidth"), "0px")
        self.assertEqual(add.evaluate("el => getComputedStyle(el).boxShadow"), "none")
        self.assertEqual(add.evaluate("el => getComputedStyle(el, '::before').width"), "22px")
        self.assertIn(
            "data:image/svg+xml",
            add.evaluate("el => getComputedStyle(el, '::before').webkitMaskImage"),
        )
        self.assertEqual(add.evaluate("el => getComputedStyle(el, '::after').content"), "none")

        title_box = page.locator("h1").bounding_box()
        add_box = add.bounding_box()
        self.assertIsNotNone(title_box)
        self.assertIsNotNone(add_box)
        title_center = title_box["y"] + title_box["height"] / 2
        add_center = add_box["y"] + add_box["height"] / 2
        self.assertLessEqual(abs(title_center - add_center), 2.0)

        palette = page.locator(".shell-test-glyph-palette")
        expect(palette).to_be_visible()
        swatches = palette.locator(".glyph-swatch")
        self.assertEqual(swatches.count(), 6)
        for swatch in swatches.all():
            self.assertEqual(swatch.evaluate("el => getComputedStyle(el).height"), "44px")
            self.assertIn(
                "data:image/svg+xml",
                swatch.evaluate("el => getComputedStyle(el, '::before').webkitMaskImage"),
            )

        complete = page.locator(".checkmark").first
        current = page.locator(".journey-mark.current")
        incomplete = page.locator(".completion-ring").first
        for marker in (complete, current, incomplete):
            self.assertEqual(marker.evaluate("el => getComputedStyle(el).width"), "24px")
            self.assertEqual(marker.evaluate("el => getComputedStyle(el).height"), "24px")
            self.assertEqual(marker.evaluate("el => getComputedStyle(el).borderTopWidth"), "0px")
            self.assertEqual(marker.evaluate("el => getComputedStyle(el).backgroundColor"), "rgba(0, 0, 0, 0)")

        # Complete is the canonical check without a surrounding circle, drawn in the shared 18px optical frame.
        self.assertEqual(complete.evaluate("el => getComputedStyle(el).borderRadius"), "0px")
        self.assertEqual(complete.evaluate("el => getComputedStyle(el, '::before').width"), "18px")
        self.assertEqual(complete.evaluate("el => getComputedStyle(el, '::before').height"), "18px")
        self.assertIn(
            "data:image/svg+xml",
            complete.evaluate("el => getComputedStyle(el, '::before').webkitMaskImage"),
        )

        # Current and incomplete share width/caps; only weight and contrast step down.
        self.assertEqual(current.evaluate("el => getComputedStyle(el, '::before').width"), "18px")
        self.assertEqual(current.evaluate("el => getComputedStyle(el, '::before').height"), "3px")
        self.assertEqual(current.evaluate("el => getComputedStyle(el, '::before').borderRadius"), "2px")
        self.assertEqual(current.evaluate("el => getComputedStyle(el, '::before').backgroundColor"), "rgb(217, 217, 223)")
        self.assertEqual(incomplete.evaluate("el => getComputedStyle(el, '::before').width"), "18px")
        self.assertEqual(incomplete.evaluate("el => getComputedStyle(el, '::before').height"), "2px")
        self.assertEqual(incomplete.evaluate("el => getComputedStyle(el, '::before').borderRadius"), "2px")

        current_row = page.get_by_role("button", name="Current")
        self.assertEqual(current_row.evaluate("el => getComputedStyle(el).backgroundColor"), "rgba(0, 0, 0, 0)")

        management = page.get_by_role("button", name="Example row actions")
        self.assertEqual(management.evaluate("el => getComputedStyle(el).borderLeftWidth"), "0px")
        self.assertEqual(management.evaluate("el => getComputedStyle(el).fontSize"), "0px")
        self.assertEqual(management.evaluate("el => getComputedStyle(el, '::before').width"), "20px")
        self.assertIn(
            "data:image/svg+xml",
            management.evaluate("el => getComputedStyle(el, '::before').webkitMaskImage"),
        )

        chevron = page.locator(".chevron").first
        back = page.locator(".shell-test-link")
        self.assertEqual(chevron.evaluate("el => getComputedStyle(el).fontSize"), "0px")
        self.assertEqual(chevron.evaluate("el => getComputedStyle(el, '::before').width"), "20px")
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
        self.assertEqual(reorder.evaluate("el => getComputedStyle(el, '::before').width"), "20px")
        self.assertEqual(reorder.evaluate("el => getComputedStyle(el, '::before').height"), "20px")
        self.assertIn(
            "data:image/svg+xml",
            reorder.evaluate("el => getComputedStyle(el, '::before').webkitMaskImage"),
        )

        # Supporting arrangement metadata belongs under the name; reorder alone owns the far-right lane.
        arrangement_name = page.locator(".arrangement-name").first
        arrangement_bars = page.locator(".arrangement-bars").first
        name_box = arrangement_name.bounding_box()
        bars_box = arrangement_bars.bounding_box()
        reorder_box = reorder.bounding_box()
        self.assertIsNotNone(name_box)
        self.assertIsNotNone(bars_box)
        self.assertIsNotNone(reorder_box)
        self.assertGreaterEqual(bars_box["y"], name_box["y"] + name_box["height"] - 1)
        self.assertLess(bars_box["x"] + bars_box["width"], reorder_box["x"])
        self.assertLessEqual(abs(bars_box["x"] - name_box["x"]), 1.0)

        # Every row family derives its far-right center from one canonical 44px lane.
        row_examples = [
            page.get_by_role("button", name="Complete"),
            page.locator(".arrangement-row").first,
            page.locator(".project-card").first,
        ]
        for row_example in row_examples:
            columns = row_example.evaluate("el => getComputedStyle(el).gridTemplateColumns").split()
            self.assertEqual(columns[-1], "44px")

        # State and commodity marks share both the same center and the same edge-derived centerline.
        accessory_locators = [complete, current, incomplete, chevron, reorder, management]
        centers = []
        for locator in accessory_locators:
            box = locator.bounding_box()
            self.assertIsNotNone(box)
            centers.append(box["x"] + box["width"] / 2)
        self.assertLessEqual(max(centers) - min(centers), 1.5)

        rows_group = page.locator("#rowsHeading").locator("xpath=..").locator(".group")
        group_box = rows_group.bounding_box()
        self.assertIsNotNone(group_box)
        border_right = rows_group.evaluate("el => parseFloat(getComputedStyle(el).borderRightWidth)")
        expected_center = group_box["x"] + group_box["width"] - border_right - 22
        for center in centers:
            self.assertLessEqual(abs(center - expected_center), 1.0)

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
