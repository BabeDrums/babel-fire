from pathlib import Path

css_path = Path('styles.css')
test_path = Path('tests/test_v6.py')
css = css_path.read_text()
tests = test_path.read_text()

# Keep action-card copy geometry stable on compact screens; this prevents
# Review Map verification rows from gaining different heights solely from copy wrap.
css = css.replace(
''' .list-row .desc,
.action-card .copy {
  font-size: 13px;
  line-height: 1.4;
}'''.lstrip(),
''' .list-row .desc {
  font-size: 13px;
  line-height: 1.4;
}'''.lstrip(),
1,
)

# Selected state should be tonal/border-only; no extra inset ring.
css = css.replace(
'''  color: var(--text);
  box-shadow: inset 0 0 0 1px rgba(255, 255, 255, 0.025);
}''',
'''  color: var(--text);
}''',
1,
)

# Structure already had an approved compact 280px desktop Next. Do not enlarge
# it as part of the shared 320px workflow-action rule.
css = css.replace(
'''#app[data-route="structure"] .structure-next,
#app[data-route="tracks"] .primary.full,''',
'''#app[data-route="tracks"] .primary.full,''',
1,
)

# Tests: update intentional copy and adaptive iPad sheet radius, while keeping
# the prior Structure action-width and geometry assertions intact.
tests = tests.replace(
"expect(self.page.locator('.sheet')).to_have_css('border-radius','18px')",
"expect(self.page.locator('.sheet')).to_have_css('border-radius','20px')",
1,
)
tests = tests.replace(
"expect(self.page.locator('.structure-ready-label')).to_have_text('Ready?')",
"expect(self.page.locator('.structure-ready-label')).to_have_text('Finish structure')",
1,
)
# New foundation test must target the actual Tracks Next, because the closed
# Add Section sheet remains mounted in the DOM.
tests = tests.replace(
"self.assertLessEqual(self.page.locator('.primary.full').bounding_box()['width'], 320.5)\n\n        self.canvas_route('skeleton-session')",
"self.assertLessEqual(self.page.locator('[data-action=\"start-section-study\"]').bounding_box()['width'], 320.5)\n\n        self.canvas_route('skeleton-session')",
1,
)

css_path.write_text(css.rstrip() + '\n')
test_path.write_text(tests)
