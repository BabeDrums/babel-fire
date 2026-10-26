"""End-to-end regressions for the first FIRE Core decision-cycle proof."""
import json
import os
import unittest

from playwright.sync_api import sync_playwright, expect

CORE_KEY = "production-projects-v1-v7-core-proof"
SOURCE_KEY = "production-projects-v1"
URL = os.environ.get("FIRE_URL", "http://127.0.0.1:8000").rstrip("/") + "/v7-preview/core.html"


class FireCoreProof(unittest.TestCase):
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

    def open(self, hash_value="#projects", width=None, height=844):
        viewport_width = width or int(os.environ.get("FIRE_TEST_WIDTH", "390"))
        context = self.browser.new_context(viewport={"width": viewport_width, "height": height}, has_touch=True)
        self.addCleanup(context.close)
        context.add_init_script(
            "localStorage.setItem(%s,%s); localStorage.removeItem(%s);"
            % (
                json.dumps(SOURCE_KEY),
                json.dumps(json.dumps({"sentinel": "v6-must-not-change"})),
                json.dumps(CORE_KEY),
            )
        )
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
        response = page.goto(URL + "?reset=1" + hash_value)
        self.assertEqual(response.status, 200)
        self.addCleanup(lambda: self.assertEqual(errors, []))
        return page

    def test_projects_seed_cover_and_even_without_touching_v6(self):
        page = self.open()
        expect(page.locator(".title-block h1")).to_have_text("Projects")
        expect(page.get_by_role("button", name="Creep Radiohead · Cover · Match")).to_be_visible()
        expect(page.get_by_role("button", name="Even Babel · Original")).to_be_visible()
        self.assertEqual(
            page.evaluate("(key) => localStorage.getItem(key)", SOURCE_KEY),
            json.dumps({"sentinel": "v6-must-not-change"}),
        )

    def test_cover_helped_result_advances_active_focus_and_persists_meaning(self):
        page = self.open()
        page.get_by_role("button", name="Creep Radiohead · Cover · Match").click()
        expect(page.get_by_text("Arrangement & Roles · Active", exact=True)).to_be_visible()
        expect(page.get_by_text("Prove the verse → chorus lift before matching tone", exact=True)).to_be_visible()
        expect(page.get_by_text("Try in Logic", exact=True)).to_be_visible()

        page.get_by_role("button", name="I tried this").click()
        expect(page.get_by_role("button", name="Helped", exact=True)).to_be_visible()
        page.get_by_role("button", name="Helped", exact=True).click()

        expect(page.get_by_text("Source & Performance · Active", exact=True)).to_be_visible()
        expect(page.get_by_text("Make the chorus source carry the lift before processing it", exact=True)).to_be_visible()
        expect(page.get_by_text("Arrangement & Roles · Helped", exact=True)).to_be_visible()

        state = page.evaluate("(key) => JSON.parse(localStorage.getItem(key))", CORE_KEY)
        project = next(item for item in state["projects"] if item["id"] == "core-creep")
        self.assertEqual(project["core"]["stage"], 1)
        self.assertEqual(project["core"]["mapState"]["Arrangement & Roles"], "provisionally-stable")
        self.assertEqual(project["core"]["mapState"]["Source & Performance"], "active")
        self.assertEqual(project["core"]["history"][-1]["outcome"], "helped")
        self.assertEqual(
            page.evaluate("(key) => localStorage.getItem(key)", SOURCE_KEY),
            json.dumps({"sentinel": "v6-must-not-change"}),
        )

    def test_even_uses_existing_intention_and_new_evidence_reopens_focus(self):
        page = self.open()
        page.get_by_role("button", name="Even Babel · Original").click()
        expect(page.get_by_text("Prove the emotional escalation before polishing sounds", exact=True)).to_be_visible()
        expect(page.get_by_text("Target", exact=True)).to_be_visible()
        expect(page.get_by_text("Start playful and slightly off-balance", exact=False)).to_be_visible()

        page.get_by_role("button", name="I tried this").click()
        page.get_by_role("button", name="Revealed something else", exact=True).click()
        note = page.get_by_role("textbox", name="What did it reveal?")
        note.fill("The chorus gets bigger, but the vocal suddenly feels emotionally farther away.")
        page.get_by_role("button", name="Save", exact=True).click()

        expect(page.get_by_text("Arrangement & Roles · Reopened", exact=True)).to_be_visible()
        expect(page.get_by_text("Follow the new evidence before continuing the route", exact=True)).to_be_visible()
        expect(page.get_by_text("The chorus gets bigger, but the vocal suddenly feels emotionally farther away.", exact=False)).to_be_visible()

        state = page.evaluate("(key) => JSON.parse(localStorage.getItem(key))", CORE_KEY)
        project = next(item for item in state["projects"] if item["id"] == "core-even")
        self.assertEqual(project["core"]["mapState"]["Arrangement & Roles"], "reopened")
        self.assertEqual(project["core"]["history"][-1]["outcome"], "revealed")

    def test_didnt_help_keeps_domain_active_but_changes_experiment(self):
        page = self.open()
        page.get_by_role("button", name="Creep Radiohead · Cover · Match").click()
        original_experiment = page.locator(".note-card").filter(has_text="Try in Logic").inner_text()
        page.get_by_role("button", name="I tried this").click()
        page.get_by_role("button", name="Didn't help", exact=True).click()
        expect(page.get_by_text("Arrangement & Roles · Active", exact=True)).to_be_visible()
        new_experiment = page.locator(".note-card").filter(has_text="Try in Logic").inner_text()
        self.assertNotEqual(original_experiment, new_experiment)


if __name__ == "__main__":
    unittest.main()
