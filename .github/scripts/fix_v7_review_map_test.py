from pathlib import Path
p = Path('tests/test_v7_preview.py')
text = p.read_text()
old = '        expect(page.locator(".prereq-card")).to_contain_text("still uses V6")\n'
new = '        expect(page.locator(".prereq-card")).to_contain_text("Review Map isn\'t available in this preview yet.")\n'
if text.count(old) != 1:
    raise SystemExit(f'expected exactly one stale Review Map assertion, found {text.count(old)}')
p.write_text(text.replace(old, new))
print('updated stale Review Map assertion')
