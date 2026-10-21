from pathlib import Path

root = Path(__file__).resolve().parents[1]
app_path = root / "app.js"
css_path = root / "styles.css"
app = app_path.read_text(encoding="utf-8")
css = css_path.read_text(encoding="utf-8")

old = '''  function mapStepCount(p) {
    return [structureDone(p), tracksDone(p), sectionStudyDone(p)].filter(Boolean).length;
  }
  function skeletonStepCount(p) {
    return [sessionDone(p), draftDone(p), bounceDone(p)].filter(Boolean).length;
  }'''
new = '''  function mapStepCount(p) {
    if (!mapSetupComplete(p)) return 0;
    if (!structureDone(p)) return 0;
    if (!tracksDone(p)) return 1;
    if (!sectionStudyDone(p)) return 2;
    return 3;
  }
  function skeletonStepCount(p) {
    if (!mapDone(p)) return 0;
    if (!sessionDone(p)) return 0;
    if (!draftDone(p)) return 1;
    if (!bounceDone(p)) return 2;
    return 3;
  }'''
if app.count(old) != 1:
    raise SystemExit("Step count block changed")
app = app.replace(old, new, 1)

old = '''  function stepState(step) {
    return step.done ? "done" : step.unlocked ? "current" : "locked";
  }'''
new = '''  function stepState(step) {
    if (!step.unlocked) return "locked";
    return step.done ? "done" : "current";
  }'''
if app.count(old) != 1:
    raise SystemExit("Step state block changed")
app = app.replace(old, new, 1)

css = css.replace('''.pill-tag:not(button) {
  cursor: default;
}
''', "", 1)

app_path.write_text(app, encoding="utf-8")
css_path.write_text(css, encoding="utf-8")
