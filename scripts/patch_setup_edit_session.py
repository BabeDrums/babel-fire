from pathlib import Path

path = Path("app.js")
text = path.read_text(encoding="utf-8")
old = '''    if (e.target.id === "tempoInput") {
      if (mapSetupComplete(project())) {
        ui.setupExpanded = false;
        renderMapHome();
      }
      return;
    }
    if (e.target.id === "meterInput") {
      project().map.setup.meter = e.target.value;
      invalidateMapVerification(project());
      save();
      if (mapSetupComplete(project())) {
        ui.setupExpanded = false;
        renderMapHome();
      } else refreshMapProgress();
    }
'''
new = '''    if (e.target.id === "tempoInput") {
      // When setup is open because it is incomplete, completing the last field
      // can collapse it. When the musician explicitly reopened a completed
      // summary to edit, keep that edit session open so blur cannot swallow the
      // next navigation tap by replacing the DOM underneath it.
      if (mapSetupComplete(project()) && !ui.setupExpanded) renderMapHome();
      return;
    }
    if (e.target.id === "meterInput") {
      project().map.setup.meter = e.target.value;
      invalidateMapVerification(project());
      save();
      if (mapSetupComplete(project()) && !ui.setupExpanded) renderMapHome();
      else refreshMapProgress();
    }
'''
if old not in text:
    raise SystemExit("setup change block not found")
path.write_text(text.replace(old, new, 1), encoding="utf-8")
print("patched setup edit-session behavior")
