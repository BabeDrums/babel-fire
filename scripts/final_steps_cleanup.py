from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
app_path = ROOT / "app.js"
css_path = ROOT / "styles.css"
test_path = ROOT / "tests" / "test_design_system.py"
app = app_path.read_text(encoding="utf-8")
css = css_path.read_text(encoding="utf-8")
test = test_path.read_text(encoding="utf-8")


def replace_once(text, old, new, label):
    if text.count(old) != 1:
        raise RuntimeError(f"{label}: expected one match, found {text.count(old)}")
    return text.replace(old, new, 1)


def sub_once(text, pattern, repl, label):
    text, count = re.subn(pattern, repl, text, count=1, flags=re.S)
    if count != 1:
        raise RuntimeError(f"{label}: expected one match, found {count}")
    return text

# Remove superseded passive-phase/progress helpers.
app = sub_once(
    app,
    r"  function phaseTag\(text\) \{.*?\n  \}\n  function progressBar\(done, total\) \{.*?\n  \}\n",
    "",
    "dead phase/progress helpers",
)
app = replace_once(
    app,
    '        phaseTag("The Spark"),',
    '        contextButton(p.title),',
    "Original Spark context title",
)

# Make the context navigator valid for the implemented Original mode too.
original_nav = '''    if (p.type === "original") {
      sheetRoot.innerHTML = `<div class="sheet context-nav-sheet"><div class="context-nav-head"><div><span class="micro">Navigate</span><strong>${esc(p.title)}</strong></div><button class="context-nav-close" data-action="close-sheet" aria-label="Close navigation">×</button></div><div class="context-nav-group">${contextNavRow("Project Overview", "project")}${contextNavRow("Roadmap", "roadmap")}${contextNavRow("Notes", "notes")}</div><div class="context-nav-phase">The Spark</div><div class="context-nav-group">${contextNavRow("The Spark", "original-spark", "Phase")}</div></div>`;
      openSheet();
      return;
    }
'''
app = replace_once(
    app,
    '    if (!p) return;\n    const phaseIndex = phaseIndexForRoute(ui.route),',
    '    if (!p) return;\n' + original_nav + '    const phaseIndex = phaseIndexForRoute(ui.route),',
    "Original context navigator",
)

# Ensure every dialog has an accessible name and receives focus even without h3.
app = replace_once(
    app,
    '''    if (heading) {
      heading.id = "sheetTitle";
      sheetRoot.setAttribute("aria-labelledby", "sheetTitle");
    }
    sheetRoot.setAttribute("role", "dialog");''',
    '''    if (heading) {
      heading.id = "sheetTitle";
      sheetRoot.setAttribute("aria-labelledby", "sheetTitle");
      sheetRoot.removeAttribute("aria-label");
    } else {
      sheetRoot.removeAttribute("aria-labelledby");
      sheetRoot.setAttribute("aria-label", "Project navigation");
    }
    sheetRoot.setAttribute("role", "dialog");''',
    "sheet accessible name",
)
app = replace_once(
    app,
    '    if (heading) { heading.tabIndex = -1; heading.focus({ preventScroll: true }); }',
    '    const focusTarget = heading || sheetRoot.querySelector("button:not(:disabled), input:not(:disabled), textarea:not(:disabled), select:not(:disabled)");\n    if (heading) heading.tabIndex = -1;\n    focusTarget?.focus({ preventScroll: true });',
    "sheet initial focus",
)

# Remove old passive-pill/progress CSS now that the final app emits neither.
css = sub_once(css, r"\.topbar \.center \.pill-tag \{.*?\n\}\n", "", "hidden pill tag rule")
css = sub_once(css, r"\.pill-tag, \.phase-pill \{.*?\n\}\n", "", "pill/phase pill component")
css = replace_once(
    css,
    '.section-tab, .pill-tag, .phase-pill {\n  min-height: 44px;\n}',
    '.section-tab {\n  min-height: 44px;\n}',
    "section tab touch target",
)
css = sub_once(css, r"\.progress \{.*?\n\}\n\.progress > span \{.*?\n\}\n\.progress-meta \{.*?\n\}\n", "", "retired progress component")
css = sub_once(
    css,
    r"\.presence-handle,\n\.event-handle,\n\.change-marker \{\n  z-index: 7;\n\}\n",
    "",
    "duplicate timeline z-index grouping",
)

# Update the focused source regression to reflect full removal instead of hiding.
test = replace_once(
    test,
    "        self.assertNotIn('.topbar .center .phase-pill {', self.css)\n        self.assertIn('.topbar .center .pill-tag {\\n  display: none;', self.css)",
    "        self.assertNotIn('.topbar .center .phase-pill {', self.css)\n        self.assertNotIn('pill-tag', self.app)",
    "design-system passive center assertion",
)

app_path.write_text(app, encoding="utf-8")
css_path.write_text(css, encoding="utf-8")
test_path.write_text(test, encoding="utf-8")
