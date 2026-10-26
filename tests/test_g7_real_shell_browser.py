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

    def vertical_gap(self, upper, lower):
        upper_box = upper.bounding_box()
        lower_box = lower.bounding_box()
        self.assertIsNotNone(upper_box)
        self.assertIsNotNone(lower_box)
        return lower_box["y"] - (upper_box["y"] + upper_box["height"])

    def test_real_project_state_marks_and_setup_controls_preserve_geometry(self):
        page = self.open()
        self.open_fixture_project(page)

        current_row = page.locator(".journey-row.current")
        current = page.locator(".journey-row.current .journey-mark.current")
        upcoming = page.locator(".journey-row.upcoming .journey-mark.upcoming").first
        expect(current).to_be_visible()
        expect(upcoming).to_be_visible()

        # State primitives have one visible owner: the pseudo-element artwork.
        for marker in (current, upcoming):
            self.assertEqual(marker.evaluate("el => getComputedStyle(el).fontSize"), "0px")
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

        current_box = current.bounding_box()
        upcoming_box = upcoming.bounding_box()
        self.assertIsNotNone(current_box)
        self.assertIsNotNone(upcoming_box)
        current_center = current_box["x"] + current_box["width"] / 2
        upcoming_center = upcoming_box["x"] + upcoming_box["width"] / 2
        self.assertLessEqual(abs(current_center - upcoming_center), 1.0)

        # The interaction target stays 44px while the visible circular material is quieter inside it.
        back_glyph = page.locator(".back-glyph")
        back_button = page.locator(".toolbar-button.icon-back")
        self.assertEqual(back_glyph.evaluate("el => getComputedStyle(el).fontSize"), "0px")
        self.assertEqual(back_glyph.evaluate("el => getComputedStyle(el).transform"), "none")
        self.assertIn(
            "data:image/svg+xml",
            back_glyph.evaluate("el => getComputedStyle(el, '::before').webkitMaskImage"),
        )
        self.assertEqual(back_button.evaluate("el => getComputedStyle(el).width"), "44px")
        self.assertEqual(back_button.evaluate("el => getComputedStyle(el).height"), "44px")
        self.assertEqual(back_button.evaluate("el => getComputedStyle(el).backgroundColor"), "rgba(0, 0, 0, 0)")
        self.assertEqual(back_button.evaluate("el => getComputedStyle(el).borderTopWidth"), "0px")
        self.assertEqual(back_button.evaluate("el => getComputedStyle(el, '::after').width"), "36px")
        self.assertEqual(back_button.evaluate("el => getComputedStyle(el, '::after').height"), "36px")
        self.assertEqual(back_button.evaluate("el => getComputedStyle(el, '::after').borderRadius"), "50%")

        page.locator('.journey-row[data-route="setup"]').click()
        expect(page.locator("h1")).to_have_text("Setup")

        group_box = page.locator(".form-group").bounding_box()
        self.assertIsNotNone(group_box)
        group_left = group_box["x"]
        group_right = group_box["x"] + group_box["width"]

        value_widths = []
        for selector in ("#tempoInput", "#meterInput"):
            control_box = page.locator(selector).evaluate(
                """el => {
                    const r = el.parentElement.getBoundingClientRect();
                    return { left: r.left, right: r.right, width: r.width };
                }"""
            )
            value_widths.append(control_box["width"])
            self.assertGreaterEqual(control_box["left"], group_left - 1)
            self.assertLessEqual(control_box["right"], group_right + 1)
        self.assertLessEqual(abs(value_widths[0] - value_widths[1]), 1.0)
        self.assertGreaterEqual(value_widths[0], 103)

        meter_value = page.locator("#meterInput").locator("xpath=..")
        self.assertTrue(meter_value.evaluate("el => el.classList.contains('select-value')"))

    def test_sheet_vertical_rhythm_is_shared_across_forms_and_action_menus(self):
        page = self.open()

        # Routine form: project type -> fields -> footer all use the shared 24px major rhythm.
        page.get_by_role("button", name="New Project").click()
        sheet = page.locator(".sheet")
        expect(sheet).to_be_visible()
        project_type = sheet.locator(".project-type-control")
        project_fields = sheet.locator(".project-field-group")
        actions = sheet.locator(".sheet-actions")
        self.assertLessEqual(abs(self.vertical_gap(project_type, project_fields) - 24), 1.0)
        self.assertLessEqual(abs(self.vertical_gap(project_fields, actions) - 24), 1.0)
        self.assertEqual(actions.evaluate("el => getComputedStyle(el).marginTop"), "24px")
        page.get_by_role("button", name="Cancel").click()

        # Action menu: the single Cancel footer uses the same 24px separation instead of a local gap.
        self.open_fixture_project(page)
        page.get_by_role("button", name="Project actions").click()
        menu = page.locator(".action-menu")
        single_actions = page.locator(".sheet-actions.single-action")
        expect(single_actions).to_be_visible()
        self.assertLessEqual(abs(self.vertical_gap(menu, single_actions) - 24), 1.0)
        self.assertEqual(single_actions.evaluate("el => getComputedStyle(el).marginTop"), "24px")

    def test_real_structure_header_alignment_and_adaptive_sheet(self):
        page = self.open()
        width = int(os.environ.get("FIRE_TEST_WIDTH", "390"))
        self.open_fixture_project(page)
        page.locator('.journey-row[data-route="structure"]').click()
        expect(page.locator("h1")).to_have_text("Structure")

        back = page.get_by_role("button", name="Creep")
        add = page.get_by_role("button", name="Add Section")
        title_box = page.locator("h1").bounding_box()
        back_box = back.bounding_box()
        add_box = add.bounding_box()
        self.assertIsNotNone(title_box)
        self.assertIsNotNone(back_box)
        self.assertIsNotNone(add_box)

        # Header actions share one navigation row; title is a separate row beneath them.
        back_center = back_box["y"] + back_box["height"] / 2
        add_center = add_box["y"] + add_box["height"] / 2
        self.assertLessEqual(abs(back_center - add_center), 1.0)
        self.assertGreaterEqual(title_box["y"], max(back_box["y"] + back_box["height"], add_box["y"] + add_box["height"]))

        self.assertEqual(add.evaluate("el => getComputedStyle(el).backgroundColor"), "rgba(0, 0, 0, 0)")
        self.assertEqual(add.evaluate("el => getComputedStyle(el).borderTopWidth"), "0px")
        self.assertEqual(add.evaluate("el => getComputedStyle(el, '::after').width"), "36px")
        self.assertEqual(add.evaluate("el => getComputedStyle(el, '::after').height"), "36px")
        self.assertEqual(add.evaluate("el => getComputedStyle(el, '::before').width"), "20px")
        self.assertIn(
            "data:image/svg+xml",
            add.evaluate("el => getComputedStyle(el, '::before').webkitMaskImage"),
        )

        page.get_by_role("button", name="Add Section").click()
        sheet = page.locator(".sheet")
        backdrop = page.locator(".sheet-backdrop")
        expect(sheet).to_be_visible()
        actions = sheet.locator(".sheet-actions")
        expect(actions).to_be_visible()
        self.assertEqual(actions.evaluate("el => getComputedStyle(el).borderTopWidth"), "0px")
        self.assertEqual(actions.evaluate("el => getComputedStyle(el).paddingTop"), "0px")
        self.assertEqual(actions.evaluate("el => getComputedStyle(el).marginTop"), "24px")
        self.assertEqual(sheet.get_attribute("aria-label"), "Add Section")
        self.assertEqual(sheet.evaluate("el => getComputedStyle(el, '::before').display"), "none")
        self.assertEqual(sheet.locator("h2").count(), 0)

        sheet_box = sheet.bounding_box()
        self.assertIsNotNone(sheet_box)
        viewport_height = page.viewport_size["height"]
        if width < 700:
            # Compact presentation is an edge-attached bottom sheet, not a centered dialog.
            self.assertEqual(backdrop.evaluate("el => getComputedStyle(el).alignItems"), "flex-end")
            self.assertLessEqual(abs(sheet_box["y"] + sheet_box["height"] - viewport_height), 1.0)
            self.assertEqual(sheet.evaluate("el => getComputedStyle(el).borderBottomWidth"), "0px")
            self.assertEqual(sheet.evaluate("el => getComputedStyle(el).borderBottomLeftRadius"), "0px")
        else:
            # Regular width keeps the compact centered-card treatment.
            self.assertEqual(backdrop.evaluate("el => getComputedStyle(el).alignItems"), "center")
            self.assertGreater(sheet_box["y"], 0)
            self.assertLess(sheet_box["y"] + sheet_box["height"], viewport_height)
            self.assertEqual(sheet.evaluate("el => getComputedStyle(el).borderBottomWidth"), "1px")
            self.assertEqual(sheet.evaluate("el => getComputedStyle(el).borderBottomLeftRadius"), "22px")
            self.assertNotIn("inset", sheet.evaluate("el => getComputedStyle(el).boxShadow"))

        groups = sheet.locator(".sheet-content-group")
        first_group = groups.nth(0)
        second_group = groups.nth(1)
        self.assertLessEqual(abs(self.vertical_gap(first_group, second_group) - 24), 1.0)
        self.assertLessEqual(abs(self.vertical_gap(second_group, actions) - 24), 1.0)

        # Custom choices progressively reveal and focus the field with one shared 12px related gap.
        custom_type = sheet.locator('[data-action="choose-section-type"][data-name="Custom"]')
        custom_type.click()
        custom_section = page.locator("#customSectionArea")
        expect(custom_section).to_be_visible()
        expect(page.locator("#customSectionName")).to_be_focused()
        self.assertLessEqual(
            abs(self.vertical_gap(sheet.locator(".section-types"), custom_section) - 12),
            1.0,
        )
        self.assertLessEqual(abs(self.vertical_gap(first_group, second_group) - 24), 1.0)

        custom_bars = sheet.locator('[data-action="choose-section-bars"][data-bars="custom"]')
        custom_bars.click()
        custom_bars_area = page.locator("#customBarsArea")
        expect(custom_bars_area).to_be_visible()
        expect(page.locator("#customBarsInput")).to_be_focused()
        self.assertLessEqual(
            abs(self.vertical_gap(sheet.locator(".bars-grid"), custom_bars_area) - 12),
            1.0,
        )
        self.assertEqual(page.locator("#customBarsInput").evaluate("el => getComputedStyle(el).marginTop"), "0px")
        self.assertLessEqual(abs(self.vertical_gap(second_group, actions) - 24), 1.0)


if __name__ == "__main__":
    unittest.main()
