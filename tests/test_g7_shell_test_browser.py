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

        optical_y = lambda locator: locator.evaluate(
            "el => new DOMMatrixReadOnly(getComputedStyle(el, '::before').transform).m42"
        )

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
        self.assertAlmostEqual(optical_y(add), 1.0, delta=0.05)

        title_box = page.locator("h1").bounding_box()
        add_box = add.bounding_box()
        self.assertIsNotNone(title_box)
        self.assertIsNotNone(add_box)
        title_center = title_box["y"] + title_box["height"] / 2
        add_center = add_box["y"] + add_box["height"] / 2
        self.assertLessEqual(abs(title_center - add_center), 2.0)

        comparison = page.locator(".symbol-comparison-stage")
        expect(comparison).to_be_visible()
        variants = comparison.locator(".symbol-variant")
        self.assertEqual(variants.count(), 3)
        buttons = comparison.locator(".symbol-button")
        symbols = comparison.locator(".normalized-symbol")
        self.assertEqual(buttons.count(), 18)
        self.assertEqual(symbols.count(), 18)

        for button in buttons.all():
            self.assertEqual(button.evaluate("el => getComputedStyle(el).width"), "44px")
            self.assertEqual(button.evaluate("el => getComputedStyle(el).height"), "44px")

        for symbol in symbols.all():
            self.assertEqual(symbol.get_attribute("data-normalized"), "true")
            self.assertEqual(symbol.evaluate("el => getComputedStyle(el).width"), "20px")
            self.assertEqual(symbol.evaluate("el => getComputedStyle(el).height"), "20px")
            center = symbol.evaluate(
                """el => {
                    const art = el.querySelector('.symbol-art');
                    const b = art.getBBox();
                    const m = art.transform.baseVal.consolidate()?.matrix;
                    return {
                        x: b.x + b.width / 2 + (m?.e || 0),
                        y: b.y + b.height / 2 + (m?.f || 0)
                    };
                }"""
            )
            self.assertAlmostEqual(center["x"], 12.0, delta=0.01)
            self.assertAlmostEqual(center["y"], 12.0, delta=0.01)

        current = comparison.locator('[data-symbol-variant="symbol-button-current"] .symbol-button').first
        circle = comparison.locator('[data-symbol-variant="symbol-button-circle"] .symbol-button').first
        glass = comparison.locator('[data-symbol-variant="symbol-button-glass"] .symbol-button').first
        self.assertEqual(current.evaluate("el => getComputedStyle(el).borderRadius"), "12px")
        self.assertEqual(circle.evaluate("el => getComputedStyle(el).borderRadius"), "50%")
        self.assertEqual(glass.evaluate("el => getComputedStyle(el).borderRadius"), "50%")
        self.assertNotEqual(glass.evaluate("el => getComputedStyle(el).backdropFilter"), "none")
        self.assertNotEqual(glass.evaluate("el => getComputedStyle(el).boxShadow"), "none")

        complete = page.locator(".checkmark").first
        current_state = page.locator(".journey-mark.current")
        incomplete = page.locator(".completion-ring").first
        for marker in (complete, current_state, incomplete):
            self.assertEqual(marker.evaluate("el => getComputedStyle(el).width"), "24px")
            self.assertEqual(marker.evaluate("el => getComputedStyle(el).height"), "24px")
            self.assertEqual(marker.evaluate("el => getComputedStyle(el).borderTopWidth"), "0px")
            self.assertEqual(marker.evaluate("el => getComputedStyle(el).backgroundColor"), "rgba(0, 0, 0, 0)")
            self.assertAlmostEqual(optical_y(marker), 1.0, delta=0.05)

        # Complete is the canonical check without a surrounding circle, drawn in the shared 18px optical frame.
        self.assertEqual(complete.evaluate("el => getComputedStyle(el).borderRadius"), "0px")
        self.assertEqual(complete.evaluate("el => getComputedStyle(el, '::before').width"), "18px")
        self.assertEqual(complete.evaluate("el => getComputedStyle(el, '::before').height"), "18px")
        self.assertIn(
            "data:image/svg+xml",
            complete.evaluate("el => getComputedStyle(el, '::before').webkitMaskImage"),
        )

        # Current and incomplete share width/caps; only weight and contrast step down.
        self.assertEqual(current_state.evaluate("el => getComputedStyle(el, '::before').width"), "18px")
        self.assertEqual(current_state.evaluate("el => getComputedStyle(el, '::before').height"), "3px")
        self.assertEqual(current_state.evaluate("el => getComputedStyle(el, '::before').borderRadius"), "2px")
        self.assertEqual(current_state.evaluate("el => getComputedStyle(el, '::before').backgroundColor"), "rgb(217, 217, 223)")
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
        self.assertAlmostEqual(optical_y(management), 1.0, delta=0.05)

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
        self.assertAlmostEqual(optical_y(chevron), 1.0, delta=0.05)
        self.assertAlmostEqual(optical_y(back), 1.0, delta=0.05)
        self.assertEqual(back.evaluate("el => getComputedStyle(el).width"), "44px")
        self.assertEqual(back.evaluate("el => getComputedStyle(el).height"), "44px")

        reorder = page.get_by_role("button", name="Reorder example")
        self.assertEqual(reorder.evaluate("el => getComputedStyle(el).fontSize"), "0px")
        self.assertEqual(reorder.evaluate("el => getComputedStyle(el, '::before').width"), "20px")
        self.assertEqual(reorder.evaluate("el => getComputedStyle(el, '::before').height"), "20px")
        self.assertEqual(reorder.evaluate("el => getComputedStyle(el, '::before').top"), "23px")
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

        # The existing horizontal accessory lane stays fixed; this experiment does not alter real G7 geometry.
        accessory_locators = [complete, current_state, incomplete, chevron, reorder, management]
        centers = []
        for locator in accessory_locators:
            box = locator.bounding_box()
            self.assertIsNotNone(box)
            centers.append(box["x"] + box["width"] / 2)
        self.assertLessEqual(max(centers) - min(centers), 1.5)

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