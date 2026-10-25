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
        back_control = page.locator(".shell-test-link")
        self.assertEqual(add.evaluate("el => getComputedStyle(el).fontSize"), "0px")
        self.assertEqual(add.evaluate("el => getComputedStyle(el).backgroundColor"), "rgba(0, 0, 0, 0)")
        self.assertEqual(add.evaluate("el => getComputedStyle(el).borderTopWidth"), "0px")
        self.assertEqual(add.evaluate("el => getComputedStyle(el).borderRadius"), "50%")
        self.assertEqual(add.evaluate("el => getComputedStyle(el).boxShadow"), "none")
        self.assertEqual(add.evaluate("el => getComputedStyle(el, '::before').width"), "20px")
        self.assertIn(
            "data:image/svg+xml",
            add.evaluate("el => getComputedStyle(el, '::before').webkitMaskImage"),
        )
        self.assertEqual(add.evaluate("el => getComputedStyle(el, '::after').width"), "36px")
        self.assertEqual(add.evaluate("el => getComputedStyle(el, '::after').height"), "36px")
        self.assertEqual(add.evaluate("el => getComputedStyle(el, '::after').borderRadius"), "50%")

        title_box = page.locator("h1").bounding_box()
        add_box = add.bounding_box()
        back_box = back_control.bounding_box()
        self.assertIsNotNone(title_box)
        self.assertIsNotNone(add_box)
        self.assertIsNotNone(back_box)
        add_center = add_box["y"] + add_box["height"] / 2
        back_center = back_box["y"] + back_box["height"] / 2
        self.assertLessEqual(abs(add_center - back_center), 1.0)
        self.assertGreaterEqual(title_box["y"], add_box["y"] + add_box["height"])

        comparison = page.locator(".symbol-comparison-stage")
        expect(comparison).to_be_visible()
        self.assertEqual(comparison.evaluate("el => getComputedStyle(el).backgroundColor"), "rgb(20, 20, 22)")
        self.assertEqual(comparison.evaluate("el => getComputedStyle(el).borderRadius"), "16px")
        variants = comparison.locator(".symbol-variant")
        self.assertEqual(variants.count(), 2)
        buttons = comparison.locator(".symbol-button")
        symbols = comparison.locator(".normalized-symbol")
        self.assertEqual(buttons.count(), 12)
        self.assertEqual(symbols.count(), 12)
        self.assertEqual(comparison.locator(".symbol-button-glass").count(), 0)

        for button in buttons.all():
            self.assertEqual(button.evaluate("el => getComputedStyle(el).width"), "44px")
            self.assertEqual(button.evaluate("el => getComputedStyle(el).height"), "44px")

        for symbol in symbols.all():
            self.assertEqual(symbol.get_attribute("data-normalized"), "true")
            self.assertEqual(symbol.evaluate("el => getComputedStyle(el).width"), "20px")
            self.assertEqual(symbol.evaluate("el => getComputedStyle(el).height"), "20px")
            optical_x = float(symbol.get_attribute("data-optical-shift-x"))
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
            self.assertAlmostEqual(center["x"], 12.0 + optical_x, delta=0.01)
            self.assertAlmostEqual(center["y"], 12.0, delta=0.01)

        back_symbol = comparison.locator('.normalized-symbol[data-symbol="back"]').first
        forward_symbol = comparison.locator('.normalized-symbol[data-symbol="forward"]').first
        back_optical = float(back_symbol.get_attribute("data-optical-shift-x"))
        forward_optical = float(forward_symbol.get_attribute("data-optical-shift-x"))
        self.assertEqual(back_symbol.get_attribute("data-alignment-model"), "convex-hull-centroid")
        self.assertEqual(forward_symbol.get_attribute("data-alignment-model"), "convex-hull-centroid")
        self.assertLess(back_optical, 0)
        self.assertGreater(forward_optical, 0)
        self.assertAlmostEqual(back_optical, -forward_optical, delta=0.001)
        self.assertAlmostEqual(abs(back_optical), 1.0, delta=0.001)

        for symbol in (back_symbol, forward_symbol):
            optical_anchor = symbol.evaluate(
                """el => {
                    const art = el.querySelector('.symbol-art');
                    const polyline = art.querySelector('polyline');
                    const points = Array.from(
                        {length: polyline.points.numberOfItems},
                        (_, i) => polyline.points.getItem(i)
                    );
                    const m = art.transform.baseVal.consolidate()?.matrix;
                    return {
                        x: points.reduce((sum, point) => sum + point.x, 0) / points.length + (m?.e || 0),
                        y: points.reduce((sum, point) => sum + point.y, 0) / points.length + (m?.f || 0)
                    };
                }"""
            )
            self.assertAlmostEqual(optical_anchor["x"], 12.0, delta=0.01)
            self.assertAlmostEqual(optical_anchor["y"], 12.0, delta=0.01)

        for name in ("plus", "check", "reorder", "more"):
            symbol = comparison.locator(f'.normalized-symbol[data-symbol="{name}"]').first
            self.assertEqual(symbol.get_attribute("data-alignment-model"), "geometry-bounds")
            self.assertEqual(float(symbol.get_attribute("data-optical-shift-x")), 0.0)

        current = comparison.locator('[data-symbol-variant="symbol-button-current"] .symbol-button').first
        circle = comparison.locator('[data-symbol-variant="symbol-button-circle"] .symbol-button').first
        self.assertEqual(current.evaluate("el => getComputedStyle(el).borderRadius"), "12px")
        self.assertEqual(circle.evaluate("el => getComputedStyle(el).borderRadius"), "50%")
        self.assertEqual(current.evaluate("el => getComputedStyle(el).boxShadow"), "none")
        self.assertEqual(circle.evaluate("el => getComputedStyle(el).boxShadow"), "none")

        complete = page.locator(".checkmark").first
        current_state = page.locator(".journey-mark.current")
        incomplete = page.locator(".completion-ring").first
        for marker in (complete, current_state, incomplete):
            self.assertEqual(marker.evaluate("el => getComputedStyle(el).width"), "24px")
            self.assertEqual(marker.evaluate("el => getComputedStyle(el).height"), "24px")
            self.assertEqual(marker.evaluate("el => getComputedStyle(el).fontSize"), "0px")
            self.assertEqual(marker.evaluate("el => getComputedStyle(el).borderTopWidth"), "0px")
            self.assertEqual(marker.evaluate("el => getComputedStyle(el).backgroundColor"), "rgba(0, 0, 0, 0)")
            self.assertEqual(marker.evaluate("el => getComputedStyle(el, '::before').transform"), "none")

        self.assertEqual(complete.evaluate("el => getComputedStyle(el).borderRadius"), "0px")
        self.assertEqual(complete.evaluate("el => getComputedStyle(el, '::before').width"), "18px")
        self.assertEqual(complete.evaluate("el => getComputedStyle(el, '::before').height"), "18px")
        self.assertIn(
            "data:image/svg+xml",
            complete.evaluate("el => getComputedStyle(el, '::before').webkitMaskImage"),
        )

        self.assertEqual(current_state.evaluate("el => getComputedStyle(el, '::before').width"), "18px")
        self.assertEqual(current_state.evaluate("el => getComputedStyle(el, '::before').height"), "3px")
        self.assertEqual(current_state.evaluate("el => getComputedStyle(el, '::before').borderRadius"), "2px")
        self.assertEqual(current_state.evaluate("el => getComputedStyle(el, '::before').backgroundColor"), "rgb(217, 217, 223)")
        self.assertEqual(incomplete.evaluate("el => getComputedStyle(el, '::before').width"), "18px")
        self.assertEqual(incomplete.evaluate("el => getComputedStyle(el, '::before').height"), "2px")
        self.assertEqual(incomplete.evaluate("el => getComputedStyle(el, '::before').borderRadius"), "2px")

        current_row = current_state.locator("xpath=..")
        self.assertEqual(current_row.evaluate("el => getComputedStyle(el).backgroundColor"), "rgba(0, 0, 0, 0)")

        management = page.get_by_role("button", name="Example row actions")
        self.assertEqual(management.evaluate("el => getComputedStyle(el).borderLeftWidth"), "0px")
        self.assertEqual(management.evaluate("el => getComputedStyle(el).borderTopWidth"), "0px")
        self.assertEqual(management.evaluate("el => getComputedStyle(el).backgroundColor"), "rgba(0, 0, 0, 0)")
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
        self.assertNotEqual(forward_mask, back_mask)
        self.assertIn("data:image/svg+xml", forward_mask)
        self.assertIn("data:image/svg+xml", back_mask)
        self.assertEqual(chevron.evaluate("el => getComputedStyle(el, '::after').content"), "none")
        self.assertEqual(back.evaluate("el => getComputedStyle(el).width"), "44px")
        self.assertEqual(back.evaluate("el => getComputedStyle(el).height"), "44px")
        self.assertEqual(back.evaluate("el => getComputedStyle(el).backgroundColor"), "rgba(0, 0, 0, 0)")
        self.assertEqual(back.evaluate("el => getComputedStyle(el, '::after').width"), "36px")
        self.assertEqual(back.evaluate("el => getComputedStyle(el, '::after').height"), "36px")
        self.assertEqual(back.evaluate("el => getComputedStyle(el, '::after').borderRadius"), "50%")

        reorder = page.get_by_role("button", name="Reorder example")
        self.assertEqual(reorder.evaluate("el => getComputedStyle(el).fontSize"), "0px")
        self.assertEqual(reorder.evaluate("el => getComputedStyle(el, '::before').width"), "20px")
        self.assertEqual(reorder.evaluate("el => getComputedStyle(el, '::before').height"), "20px")
        self.assertEqual(reorder.evaluate("el => getComputedStyle(el, '::before').top"), "22px")
        self.assertIn(
            "data:image/svg+xml",
            reorder.evaluate("el => getComputedStyle(el, '::before').webkitMaskImage"),
        )

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
        self.assertEqual(dialog.evaluate("el => getComputedStyle(el).borderBottomWidth"), "1px")
        self.assertEqual(dialog.evaluate("el => getComputedStyle(el).borderBottomLeftRadius"), "22px")
        self.assertNotIn("inset", dialog.evaluate("el => getComputedStyle(el).boxShadow"))
        self.assertEqual(dialog.evaluate("el => getComputedStyle(el, '::before').content"), '"Shell Test dialog"')
        dialog_box = dialog.bounding_box()
        self.assertIsNotNone(dialog_box)
        self.assertGreater(dialog_box["y"], 0)
        self.assertLess(dialog_box["y"] + dialog_box["height"], page.viewport_size["height"])
        page.keyboard.press("Escape")
        expect(dialog).to_be_hidden()
        self.assertEqual(page.evaluate("document.body.style.overflow"), "")


if __name__ == "__main__":
    unittest.main()
