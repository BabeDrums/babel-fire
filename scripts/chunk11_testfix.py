from pathlib import Path

path = Path('tests/test_v6.py')
text = path.read_text(encoding='utf-8')
old = '''                if width >= 1180:
                    self.assertLessEqual(self.page.locator('#app').bounding_box()['width'], 880)
'''
new = '''                if width >= 1180:
                    self.assertLessEqual(heading['width'], 760.1)
                    self.assertLessEqual(card['width'], 760.1)
'''
count = text.count(old)
if count != 1:
    raise SystemExit(f'expected 1 stale desktop assertion, found {count}')
path.write_text(text.replace(old, new, 1), encoding='utf-8')
