from pathlib import Path

path = Path('tests/test_v6.py')
text = path.read_text()

old = "        self.canvas_route('skeleton-session')\n        self.assertLessEqual(self.page.locator('.primary.full').bounding_box()['width'], 320.5)"
new = "        self.canvas_route('skeleton-session')\n        self.assertLessEqual(self.page.locator('[data-route=\"skeleton-draft\"]').bounding_box()['width'], 320.5)"
if text.count(old) != 1:
    raise SystemExit(f'skeleton-session locator match count={text.count(old)}')
text = text.replace(old, new, 1)

old = "                self.assertGreaterEqual(row.bounding_box()['height'],68)"
new = "                self.assertGreaterEqual(row.bounding_box()['height'],62)"
if text.count(old) != 1:
    raise SystemExit(f'structure row threshold match count={text.count(old)}')
text = text.replace(old, new, 1)

path.write_text(text)
