from pathlib import Path

root = Path(__file__).resolve().parents[1]
app_path = root / "app.js"
css_path = root / "styles.css"
v6_path = root / "V6.md"
app = app_path.read_text(encoding="utf-8")
css = css_path.read_text(encoding="utf-8")
v6 = v6_path.read_text(encoding="utf-8")

old = '''    const phaseIndex = currentStudyPhaseIndex(p),
      phase = STUDY_PHASES[phaseIndex],
      context = [p.artist, "Recreation"].filter(Boolean).join(" · "),
      phaseProgress ='''
new = '''    const phaseIndex = currentStudyPhaseIndex(p),
      phase = STUDY_PHASES[phaseIndex],
      phaseRoute =
        phaseIndex === 0 && sectionStudyDone(p) && !mapDone(p)
          ? "map-summary"
          : phase.route,
      context = [p.artist, "Recreation"].filter(Boolean).join(" · "),
      phaseProgress ='''
if app.count(old) != 1:
    raise SystemExit("renderProject phase block changed")
app = app.replace(old, new, 1)

old = '''      phase.title,
      phaseProgress,
      phase.route,
      "Seven phases to a finished rebuild.",'''
new = '''      phase.title,
      phaseProgress,
      phaseRoute,
      "Seven phases to a finished rebuild.",'''
if app.count(old) != 1:
    raise SystemExit("project overview route block changed")
app = app.replace(old, new, 1)

old = '''    const phaseIndex = phaseIndexForRoute(ui.route),
      phase = STUDY_PHASES[phaseIndex],
      steps = phaseStepDefinitions(p, phaseIndex);
    sheetRoot.innerHTML = `<div class="sheet context-nav-sheet"><div class="context-nav-head"><div><span class="micro">Navigate</span><strong>${esc(p.title)}</strong></div><button class="context-nav-close" data-action="close-sheet" aria-label="Close navigation">×</button></div><div class="context-nav-group">${contextNavRow("Project Overview", "project")}${contextNavRow("Roadmap", "roadmap")}${contextNavRow("Notes", "notes")}</div><div class="context-nav-phase">${esc(phase.title)}</div><div class="context-nav-group">${contextNavRow(phase.title, phase.route, "Phase")}${steps.map((step) => { const state = stepState(step); return contextNavRow(step.title, step.route, state === "done" ? "Done" : state === "current" ? "Current" : "Locked", state === "locked"); }).join("")}</div></div>`;'''
new = '''    const phaseIndex = phaseIndexForRoute(ui.route),
      phase = STUDY_PHASES[phaseIndex],
      steps = phaseStepDefinitions(p, phaseIndex),
      review =
        phaseIndex === 0 && sectionStudyCoreDone(p)
          ? contextNavRow("Review Map", "map-summary", mapDone(p) ? "Complete" : "Review")
          : "";
    sheetRoot.innerHTML = `<div class="sheet context-nav-sheet"><div class="context-nav-head"><div><span class="micro">Navigate</span><strong>${esc(p.title)}</strong></div><button class="context-nav-close" data-action="close-sheet" aria-label="Close navigation">×</button></div><div class="context-nav-group">${contextNavRow("Project Overview", "project")}${contextNavRow("Roadmap", "roadmap")}${contextNavRow("Notes", "notes")}</div><div class="context-nav-phase">${esc(phase.title)}</div><div class="context-nav-group">${contextNavRow(phase.title, phase.route, "Phase")}${steps.map((step) => { const state = stepState(step); return contextNavRow(step.title, step.route, state === "done" ? "Done" : state === "current" ? "Current" : "Locked", state === "locked"); }).join("")}${review}</div></div>`;'''
if app.count(old) != 1:
    raise SystemExit("context navigator phase block changed")
app = app.replace(old, new, 1)

css = css.replace('#app[data-route="map"] .phase-steps .list-row {', '#app[data-route="map"] .phase-steps .step-row {', 1)
css = css.replace('''  #app[data-route="map"] .phase-steps .list-row .desc {
    display: none;
  }
''', "", 1)

v6 = v6.replace(
    "Browser Back/Forward and FIRE's visible Back must remain coherent. Parent-pill navigation does not redefine or overwrite the actual entry history.",
    "Browser Back/Forward and FIRE's visible Back must remain coherent. Context navigation does not redefine or overwrite the actual entry history.",
    1,
)

app_path.write_text(app, encoding="utf-8")
css_path.write_text(css, encoding="utf-8")
v6_path.write_text(v6, encoding="utf-8")
