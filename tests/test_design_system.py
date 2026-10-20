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

    def test_parent_navigation_keeps_function_but_loses_pill_chrome(self):
        self.assertIn('.topbar .center .phase-pill {', self.css)
        self.assertIn('background: transparent;', self.css)
        self.assertIn('border: 0;', self.css)
        self.assertIn('.topbar .center .pill-tag {\n  display: none;', self.css)

    def test_structure_and_roadmap_share_grouped_list_language(self):
        self.assertIn('.structure-list {\n  display: block;', self.css)
        self.assertIn('.roadmap-grid {\n  display: block;', self.css)
        self.assertIn('.road-phase:last-child', self.css)

    def test_short_pages_use_dynamic_viewport_without_root_bounce(self):
        self.assertGreaterEqual(self.css.count('min-height: 100dvh;'), 2)
        self.assertIn('overscroll-behavior-y: none;', self.css)

    def test_phone_map_and_roadmap_have_compact_density_rules(self):
        self.assertIn('#app[data-route="map"] .setup-row', self.css)
        self.assertIn('#app[data-route="map"] .phase-checkpoints .list-row .desc', self.css)
        self.assertIn('#app[data-route="roadmap"] .road-phase:not(.current) .road-top p', self.css)
        self.assertIn('.section-builder .builder-status:empty', self.css)
        self.assertIn('.section-builder .sheet-error:empty', self.css)


if __name__ == "__main__":
    unittest.main()
