"""Browser regressions for shared shell primitives inside the actual G7 project flow.

Shell Test is necessary but not sufficient: these checks deliberately click through real
Project -> Setup -> Structure UI so shared primitive changes cannot pass certification
while breaking the product fixture on phone or regular-width layouts.
"""
import os
import unittest

from playwright.sync_api import expect, sync_playwright

BASE = os.environ.get("FIRE_URL", "http://127.0.0.1:8000").rstrip("/")
URL = BASE + "/v7-preview/?reset=1"


class G7RealShellBrowser(unittest.TestCase):
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

    def open_fixture_project(self, page):
        page.locator('[data-project="preview-creep"]').click()
        expect(page.locator("h1")).to_have_text("Creep")

    def test_real_project_state_marks_and_setup_controls_preserve_geometry(self):
        page = self.open()
        self.open_fixture_project(page)

        current_row = page.locator(".journey-row.current")
        current = page.locator(".journey-row.current .journey-mark.current")
        upcoming = page.locator(".journey-row.upcoming .journey-mark.upcoming").first
        expect(current).to_be_visible()
        expect(upcoming).to_be_visible()

        # Current/upcoming containers are visually empty; symmetric bars center without a shared nudge.
        for marker in (current, upcoming):
            self.assertEqual(marker.evaluate("el => getComputedStyle(el).borderTopWidth"), "0px")
            self.assertEqual(marker.evaluate("el => getComputedStyle(el).backgroundColor"), "rgba(0, 0, 0, 0)")
            self.assertEqual(marker.evaluate("el => getComputedStyle(el, '::before').transform"), "none")
        self.assertEqual(current.evaluate("el => getComputedStyle(el, '::before').width"), "18px")
        self.assertEqual(current.evaluate("el => getComputedStyle(el, '::before').height"), "3px")
        self.assertEqual(current.evaluate("el => getComputedStyle(el, '::before').borderRadius"), "2px")
        self.assertEqual(current.evaluate("el => getComputedStyle(el, '::before').backgroundColor"), "rgb(217, 217, 223)")
        self.assertEqual(upcoming.evaluate("el => getComputedStyle(el, '::before').width"), "18px")
        self.assertEqual(upcoming.evaluate("el => getComputedStyle(el, '::before').height"), "2px")
        self.assertEqual(upcoming.evaluate("el => getComputedStyle(el, '::before').borderRadius"), "2px")
        self.assertEqual(current_row.evaluate("el => getComputedStyle(el).backgroundColor"), "rgba(0, 0, 0, 0)")

        # Current and upcoming still occupy the same trailing lane center.
        current_box = current.bounding_box()
        upcoming_box = upcoming.bounding_box()
        self.assertIsNotNone(current_box)
        self.assertIsNotNone(upcoming_box)
        current_center = current_box["x"] + current_box["width"] / 2
        upcoming_center = upcoming_box["x"] + upcoming_box["width"] / 2
        self.assertLessEqual(abs(current_center - upcoming_center), 1.0)

        # Real project Back now uses the promoted symbol-owned asset inside the simple circle control.
        back_glyph = page.locator(".back-glyph")
        back_button = page.locator(".toolbar-button.icon-back")
        self.assertEqual(back_glyph.evaluate("el => getComputedStyle(el).fontSize"), "0px")
        self.assertIn(
            "data:image/svg+xml",
            back_glyph.evaluate("el => getComputedStyle(el, '::before').webkitMaskImage"),
        )
        self.assertEqual(back_glyph.evaluate("el => getComputedStyle(el, '::before').transform"), "none")
        self.assertEqual(back_button.evaluate("el => getComputedStyle(el).width"), "44px")
        self.assertEqual(back_button.evaluate("el => getComputedStyle(el).height"), "44px")
        self.assertEqual(back_button.evaluate("el => getComputedStyle(el).borderRadius"), "50%")
        self.assertEqual(back_button.evaluate("el => getComputedStyle(el).borderTopWidth"), "1px")
        self.assertEqual(back_button.evaluate("el => getComputedStyle(el).backgroundColor"), "rgb(23, 23, 26)")

        page.locator('.journey-row[data-route="setup"]').click()
        expect(page.locator("h1")).to_have_text("Setup")

        group_box = page.locator(".form-group").bounding_box()
        self.assertIsNotNone(group_box)
        group_left = group_box["x"]
        group_right = group_box["x"] + group_box["width"]

        expected_min_width = {
            "#tempoInput": 85,
            "#meterInput": 71,
        }
        for selector, min_width in expected_min_width.items():
            control = page.locator(selector)
            control_box = control.evaluate(
                """el => {
                    const r = el.parentElement.getBoundingClientRect();
                    return { left: r.left, right: r.right, width: r.width };
                }"""
            )
            self.assertGreaterEqual(control_box["width"], min_width)
            self.assertGreaterEqual(control_box["left"], group_left - 1)
            self.assertLessEqual(control_box["right"], group_right + 1)

        meter_value = page.locator("#meterInput").locator("xpath=..")
        self.assertTrue(meter_value.evaluate("el => el.classList.contains('select-value')"))

        for selector in ("#tempoInput", "#meterInput"):
            form_row = page.locator(selector).locator("xpath=../..")
            columns = form_row.evaluate("el => getComputedStyle(el).gridTemplateColumns").split()
            self.assertNotEqual(columns[-1], "28px")

    def test_real_structure_header_alignment_and_sheet_chrome(self):
        page = self.open()
        self.open_fixture_project(page)
        page.locator('.journey-row[data-route="structure"]').click()
        expect(page.locator("h1")).to_have_text("Structure")

        add = page.get_by_role("button", name="Add Section")
        title_box = page.locator("h1").bounding_box()
        add_box = add.bounding_box()
        self.assertIsNotNone(title_box)
        self.assertIsNotNone(add_box)
        title_center = title_box["y"] + title_box["height"] / 2
        add_center = add_box["y"] + add_box["height"] / 2
        self.assertLessEqual(abs(title_center - add_center), 2.0)
        self.assertEqual(add.evaluate("el => getComputedStyle(el).backgroundColor"), "rgb(23, 23, 26)")
        self.assertEqual(add.evaluate("el => getComputedStyle(el).borderTopWidth"), "1px")
        self.assertEqual(add.evaluate("el => getComputedStyle(el).borderRadius"), "50%")
        self.assertEqual(add.evaluate("el => getComputedStyle(el, '::before').width"), "20px")
        self.assertEqual(add.evaluate("el => getComputedStyle(el, '::before').transform"), "none")
        self.assertIn(
            "data:image/svg+xml",
            add.evaluate("el => getComputedStyle(el, '::before').webkitMaskImage"),
        )

        page.get_by_role("button", name="Add Section").click()
        sheet = page.locator(".sheet")
        expect(sheet).to_be_visible()
        actions = sheet.locator(".sheet-actions")
        expect(actions).to_be_visible()
        self.assertEqual(actions.evaluate("el => getComputedStyle(el).borderTopWidth"), "0px")
        self.assertEqual(actions.evaluate("el => getComputedStyle(el).paddingTop"), "0px")
        self.assertNotIn("inset", sheet.evaluate("el => getComputedStyle(el).boxShadow"))


if __name__ == "__main__":
    unittest.main()
