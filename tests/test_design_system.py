"""Focused regression checks for the consolidated FIRE visual foundation."""
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class FireDesignSystemSource(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.css = (ROOT / "styles.css").read_text(encoding="utf-8")

    def test_no_second_polish_or_fire_override_layer(self):
        self.assertNotIn("FIRE DESIGN SYSTEM FOUNDATION — OCTOBER 2026", self.css)
        self.assertNotIn("--fire-", self.css)
        self.assertNotIn("polish.css", self.css)

    def test_primary_prominence_is_not_full_width_by_default(self):
        self.assertIn("--action-max: 220px", self.css)
        self.assertIn(".primary.full {", self.css)
        self.assertIn("width: min(100%, var(--action-max));", self.css)
        self.assertIn("background: var(--primary-bg);", self.css)

    def test_selection_and_completion_are_separate(self):
        self.assertIn('.choice[aria-pressed]::before', self.css)
        self.assertIn('display: none;', self.css)
        self.assertIn('.round-check.on:after', self.css)

    def test_passive_center_phase_chrome_is_visually_retired(self):
        self.assertIn('.topbar .center .phase-pill', self.css)
        self.assertIn('.topbar .center .pill-tag', self.css)

    def test_structure_and_roadmap_share_grouped_list_language(self):
        self.assertIn('.structure-list {\n  display: block;', self.css)
        self.assertIn('.roadmap-grid {\n  display: block;', self.css)
        self.assertIn('.road-phase:last-child', self.css)


if __name__ == "__main__":
    unittest.main()
