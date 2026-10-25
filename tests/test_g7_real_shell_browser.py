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

    def test_real_project_current_marker_and_setup_controls_preserve_geometry(self):
        page = self.open()
        self.open_fixture_project(page)

        current = page.locator(".journey-row.current .journey-mark.current")
        expect(current).to_be_visible()
        self.assertEqual(current.evaluate("el => getComputedStyle(el, '::after').position"), "absolute")
        for side in ("top", "right", "bottom", "left"):
            self.assertEqual(current.evaluate(f"el => getComputedStyle(el, '::after').{side}"), "0px")

        page.locator('.journey-row[data-route="setup"]').click()
        expect(page.locator("h1")).to_have_text("Setup")

        group_box = page.locator(".form-group").bounding_box()
        self.assertIsNotNone(group_box)
        group_left = group_box["x"]
        group_right = group_box["x"] + group_box["width"]

        # Tempo and Meter intentionally have different control widths in the base grammar:
        # Tempo uses the regular 86px value control; Meter uses the 72px tight variant.
        # The regression we are guarding is either one collapsing into the 28px accessory lane
        # or escaping the form-group bounds on compact widths.
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

        self.assertTrue(page.locator("#meterInput").locator("xpath=..").evaluate("el => el.classList.contains('tight')"))

        for selector in ("#tempoInput", "#meterInput"):
            form_row = page.locator(selector).locator("xpath=../..")
            columns = form_row.evaluate("el => getComputedStyle(el).gridTemplateColumns").split()
            self.assertNotEqual(columns[-1], "28px")

    def test_real_structure_sheet_has_no_unapproved_hairline(self):
        page = self.open()
        self.open_fixture_project(page)
        page.locator('.journey-row[data-route="structure"]').click()
        expect(page.locator("h1")).to_have_text("Structure")
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
