from pathlib import Path

app_path = Path('app.js')
app = app_path.read_text()
old = '''  function projectPageMotionClass() {\n    return routeMotion ? ` ${routeMotion}` : "";\n  }\n'''
new = '''  function projectPageMotionClass() {\n    const className = routeMotion ? ` ${routeMotion}` : "";\n    routeMotion = "";\n    return className;\n  }\n'''
if app.count(old) != 1:
    raise SystemExit(f'projectPageMotionClass count={app.count(old)}')
app = app.replace(old, new, 1)
app_path.write_text(app)

tests_path = Path('tests/test_v6.py')
tests = tests_path.read_text()
old = '''                self.assertEqual(self.page.locator('.project-page.route-forward').count(), 1)\n                new_shell = self.page.locator('.project-page').bounding_box()\n'''
new = '''                self.assertEqual(self.page.locator('.project-page.route-forward').count(), 1)\n                self.page.locator('.project-page').evaluate('async el=>{await Promise.all(el.getAnimations().map(a=>a.finished))}')\n                new_shell = self.page.locator('.project-page').bounding_box()\n'''
if tests.count(old) != 1:
    raise SystemExit(f'animation settle count={tests.count(old)}')
tests = tests.replace(old, new, 1)
tests_path.write_text(tests)
