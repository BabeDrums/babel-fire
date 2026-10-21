"""One-shot repository patch for the approved Steps/navigation consolidation.

This script is executed by a temporary branch-only workflow and removes no
product data. The workflow deletes this script and itself before committing the
result, so neither implementation helper ships to main.
"""
from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected one match, found {count}")
    return text.replace(old, new, 1)


def sub_once(text: str, pattern: str, repl: str, label: str, flags: int = re.S) -> str:
    text, count = re.subn(pattern, repl, text, count=1, flags=flags)
    if count != 1:
        raise RuntimeError(f"{label}: expected one match, found {count}")
    return text


# --- app.js -----------------------------------------------------------------
app = read("app.js")

if app.count("      checkpoints:") != 7:
    raise RuntimeError("STUDY_PHASES checkpoint property count changed")
app = app.replace("      checkpoints:", "      steps:")
app = app.replace("ph.checkpoints.map", "ph.steps.map")
app = app.replace("mapCheckpointCount", "mapStepCount")
app = app.replace("skeletonCheckpointCount", "skeletonStepCount")

app = replace_once(
    app,
    '      projects: "Projects",\n      project:',
    '      projects: "Projects",\n      "new-project": "Projects",\n      project:',
    "new-project route label",
)

app = replace_once(
    app,
    '      style = getComputedStyle(app),\n      bottomPadding = Number.parseFloat(style.paddingBottom) || 0,',
    '      style = getComputedStyle(app),\n      bottomPadding = Number.parseFloat(style.paddingBottom) || 0,\n      scrollClearance =\n        Number.parseFloat(style.getPropertyValue("--scroll-end-clearance")) || 0,',
    "viewport clearance read",
)
app = replace_once(
    app,
    '      contentHeight = flowBottom - shellRect.top + bottomPadding,',
    '      contentHeight =\n        flowBottom - shellRect.top + Math.max(0, bottomPadding - scrollClearance),',
    "viewport clearance measurement",
)

app = sub_once(
    app,
    r"  // Live Setup updates replace only derived controls, preserving text/caret/IME\.\n  function refreshMapProgress\(\) \{.*?\n  \}\n  let cancelGesture = null;",
    '''  // Live Setup updates replace only derived Step navigation, preserving text/caret/IME.
  function refreshMapProgress() {
    const p = project(),
      holder = app.querySelector(".phase-steps .group-card"),
      count = app.querySelector(".step-count"),
      done = mapStepCount(p);
    if (count) count.textContent = `${done} of 3 complete`;
    if (holder) holder.innerHTML = phaseStepsHtml(p, 0);
    queueViewportFit();
  }
  let cancelGesture = null;''',
    "refresh Map Steps",
)

app = re.sub(
    r'    if \(route !== fromRoute && \(route === "map" \|\| fromRoute === "map"\)\)\n      ui\.setupExpanded = false;\n',
    "",
    app,
    count=1,
)

app = replace_once(
    app,
    '  function topbar(left = "", center = "", right = "") {\n',
    '''  function contextButton(label) {
    return `<button class="context-nav-button" data-action="open-context-nav" aria-haspopup="dialog" aria-label="Navigate ${esc(label)}"><span>${esc(label)}</span><span class="context-caret" aria-hidden="true">⌄</span></button>`;
  }
  function phaseIndexForRoute(route) {
    if (["skeleton", "skeleton-session", "skeleton-draft", "skeleton-bounce"].includes(route)) return 1;
    if (["map", "structure", "tracks", "section-study", "map-summary"].includes(route)) return 0;
    return Math.min(currentStudyPhaseIndex(project()), 1);
  }
  function topbar(left = "", center = "", right = "") {
''',
    "context button helpers",
)

app = sub_once(
    app,
    r"  function workflowPhaseHome\(index, done, total, checkpointsHtml, beforeHtml = \"\"\) \{.*?\n  \}\n  function projectPageMotionClass",
    '''  function workflowPhaseHome(index, done, total, stepsHtml, beforeHtml = "") {
    const p = project(),
      body = `<div class="phase-layout ${beforeHtml ? "with-setup" : ""}">${beforeHtml ? `<section class="phase-setup">${beforeHtml}</section>` : ""}<section class="phase-steps"><div class="step-head"><div class="section-kicker">Steps</div><span class="step-count">${done} of ${total} complete</span></div><div class="group-card list">${stepsHtml}</div></section></div>`;
    return (
      topbar(
        backButton("project", p?.title || "Project"),
        contextButton(p?.title || "Project"),
        savedMark(),
      ) + workflowPage(STUDY_PHASES[index].title, STUDY_PHASES[index].desc, body)
    );
  }
  function projectPageMotionClass''',
    "shared Phase Home",
)

app = sub_once(
    app,
    r"  function phasePill\(index\) \{.*?\n  \}\n",
    "",
    "remove phase pill helper",
)

app = sub_once(
    app,
    r"  function mapStepCount\(p\) \{.*?\n  \}\n  function skeletonStepCount\(p\) \{.*?\n  \}",
    '''  function mapStepCount(p) {
    return [structureDone(p), tracksDone(p), sectionStudyDone(p)].filter(Boolean).length;
  }
  function skeletonStepCount(p) {
    return [sessionDone(p), draftDone(p), bounceDone(p)].filter(Boolean).length;
  }
  function mapNextStepLabel(p) {
    if (!mapSetupComplete(p)) return "Song Setup";
    if (!structureDone(p)) return "Structure";
    if (!tracksDone(p)) return "Tracks";
    if (!sectionStudyDone(p)) return "Section Study";
    if (!mapDone(p)) return "Review Map";
    return "Complete";
  }
  function skeletonNextStepLabel(p) {
    if (!sessionDone(p)) return "Session";
    if (!draftDone(p)) return "Draft";
    if (!bounceDone(p)) return "Bounce";
    return "Complete";
  }''',
    "Step counts and next Step labels",
)

app = sub_once(
    app,
    r"  function projectListStatus\(p\) \{.*?\n  \}\n  function projectOverviewBody",
    '''  function projectListStatus(p) {
    if (p.type !== "study")
      return originalSparkDone(p) ? "The Direction" : "The Spark";
    const index = currentStudyPhaseIndex(p),
      phase = STUDY_PHASES[index].title,
      next = index === 0
        ? mapNextStepLabel(p)
        : index === 1
          ? skeletonNextStepLabel(p)
          : "";
    return [phase, next].filter(Boolean).join(" · ");
  }
  function projectOverviewBody''',
    "project list current Step",
)

app = sub_once(
    app,
    r"      phaseProgress =\n        phaseIndex === 0\n          \? `\$\{mapStepCount\(p\)\} of 3 checkpoints`\n          : phaseIndex === 1\n            \? `\$\{skeletonStepCount\(p\)\} of 3 checkpoints`\n            : \"Open roadmap\";",
    '''      phaseProgress =
        phaseIndex === 0
          ? `Next: ${mapNextStepLabel(p)}`
          : phaseIndex === 1
            ? `Next: ${skeletonNextStepLabel(p)}`
            : "Open roadmap";''',
    "project overview current Step",
)

app = sub_once(
    app,
    r"  function checkpointRow\(title, desc, route, done, unlocked = true\) \{.*?\n  \}",
    '''  function phaseStepDefinitions(p, index) {
    if (index === 0)
      return [
        { title: "Structure", route: "structure", done: structureDone(p), unlocked: mapSetupComplete(p) },
        { title: "Tracks", route: "tracks", done: tracksDone(p), unlocked: structureDone(p) },
        { title: "Section Study", route: "section-study", done: sectionStudyDone(p), unlocked: tracksDone(p) },
      ];
    if (index === 1)
      return [
        { title: "Session", route: "skeleton-session", done: sessionDone(p), unlocked: mapDone(p) },
        { title: "Draft", route: "skeleton-draft", done: draftDone(p), unlocked: sessionDone(p) },
        { title: "Bounce", route: "skeleton-bounce", done: bounceDone(p), unlocked: draftDone(p) },
      ];
    return STUDY_PHASES[index].steps.map((title) => ({ title, route: "roadmap", done: false, unlocked: false }));
  }
  function stepState(step) {
    return step.done ? "done" : step.unlocked ? "current" : "locked";
  }
  function stepRow(step) {
    const state = stepState(step),
      stateLabel = state === "done" ? "Done" : state === "current" ? "Current" : "Locked";
    return `<button class="step-row ${state}" data-action="go" data-route="${step.route}" aria-label="${esc(step.title)}, ${stateLabel}" ${state === "locked" ? "disabled" : ""}><span class="title">${esc(step.title)}</span><span class="step-trailing"><span class="step-state">${stateLabel}</span>${state === "locked" ? "" : '<span class="chev" aria-hidden="true">›</span>'}</span></button>`;
  }
  function phaseStepsHtml(p, index) {
    return phaseStepDefinitions(p, index).map(stepRow).join("");
  }''',
    "Step row component",
)

app = sub_once(
    app,
    r"  function phaseHome\(index, done, total, checkpointsHtml, beforeHtml = \"\"\) \{.*?\n  \}\n",
    "",
    "remove duplicate legacy phaseHome",
)

app = sub_once(
    app,
    r"  function renderMapHome\(\) \{.*?\n  \}\n\n  function renderStructure",
    '''  function renderMapHome() {
    const p = project(),
      m = p.map,
      done = mapStepCount(p);
    const setup = `<div class="section-kicker">Song Setup</div><div class="group-card setup-panel"><div class="setup-row"><div class="setup-label">Reference</div><button class="state-control ${m.setup.reference ? "on" : ""}" data-action="toggle-setup" data-field="reference"><span>${m.setup.reference ? "Imported" : "Import"}</span><span class="check-circle"></span></button></div><div class="setup-row"><div class="setup-label">Tempo</div><div class="setup-value"><input id="tempoInput" aria-label="Tempo in BPM" inputmode="decimal" value="${esc(m.setup.tempo)}" placeholder="—"><span class="suffix">BPM</span></div></div><div class="setup-row"><div class="setup-label">Meter</div><div class="setup-value"><select id="meterInput" aria-label="Meter">${["4/4", "3/4", "6/8", "5/4", "7/8"].map((x) => `<option ${m.setup.meter === x ? "selected" : ""}>${x}</option>`).join("")}</select></div></div><div class="setup-row"><div class="setup-label">Grid</div><button class="state-control ${m.setup.grid ? "on" : ""}" data-action="toggle-setup" data-field="grid"><span>${m.setup.grid ? "Aligned" : "Align"}</span><span class="check-circle"></span></button></div><button class="setup-listen-row ${m.setup.firstListen ? "on" : ""}" data-action="toggle-setup" data-field="firstListen" aria-pressed="${!!m.setup.firstListen}"><div><strong>First Listen</strong><span>Play the full song once without stopping.</span></div><span class="round-check ${m.setup.firstListen ? "on" : ""}"></span></button></div>`;
    app.innerHTML = workflowPhaseHome(0, done, 3, phaseStepsHtml(p, 0), setup);
  }

  function renderStructure''',
    "Map Phase Steps",
)

app = replace_once(
    app,
    '      topbar(historyBackButton("map", "The Map"), "", savedMark()) +\n      workflowPage("Structure", "Build the song one section at a time.", body, "1 of 3");',
    '      topbar(historyBackButton("map", "The Map"), contextButton("The Map"), savedMark()) +\n      workflowPage("Structure", "Build the song one section at a time.", body, "Step 1 of 3");',
    "Structure context navigation",
)
app = replace_once(
    app,
    '      topbar(historyBackButton("structure", "Structure"), "", savedMark()) +\n      workflowPage("Tracks", "Select everything that appears somewhere in the song.", body, "2 of 3");',
    '      topbar(historyBackButton("structure", "Structure"), contextButton("The Map"), savedMark()) +\n      workflowPage("Tracks", "Select everything that appears somewhere in the song.", body, "Step 2 of 3");',
    "Tracks context navigation",
)

app = app.replace('phasePill(0)', 'contextButton("The Map")')
app = app.replace('phasePill(1)', 'contextButton("The Skeleton")')

app = sub_once(
    app,
    r"  function renderSkeletonHome\(\) \{.*?\n  \}\n  function refreshSkeletonChecks",
    '''  function renderSkeletonHome() {
    const p = project(),
      done = skeletonStepCount(p);
    app.innerHTML = workflowPhaseHome(1, done, 3, phaseStepsHtml(p, 1));
  }
  function refreshSkeletonChecks''',
    "Skeleton shared Phase Home",
)

app = app.replace('<div class="work-position">1 of 3</div><h2>Session</h2>', '<div class="work-position">Step 1 of 3</div><h2>Session</h2>')
app = app.replace('<div class="work-position">2 of 3</div><h2>Draft</h2>', '<div class="work-position">Step 2 of 3</div><h2>Draft</h2>')
app = app.replace('<div class="work-position">3 of 3</div><h2>Bounce</h2>', '<div class="work-position">Step 3 of 3</div><h2>Bounce</h2>')

app = replace_once(
    app,
    '      topbar(backButton("project", "Recreation"), "", "") +',
    '      topbar(backButton("project", "Recreation"), contextButton(p.title), "") +',
    "Roadmap project context",
)
app = replace_once(
    app,
    '      topbar(backButton("project", p.type === "study" ? "Recreation" : "Original Song"), "", "") +',
    '      topbar(backButton("project", p.type === "study" ? "Recreation" : "Original Song"), contextButton(p.title), "") +',
    "Notes project context",
)

context_nav = '''
  function contextNavRow(title, route, status = "", disabled = false) {
    return `<button class="context-nav-row" data-action="context-go" data-route="${route}" ${disabled ? "disabled" : ""}><span>${esc(title)}</span>${status ? `<span class="context-nav-status">${esc(status)}</span>` : ""}</button>`;
  }
  function openContextNavigator() {
    const p = project();
    if (!p) return;
    const phaseIndex = phaseIndexForRoute(ui.route),
      phase = STUDY_PHASES[phaseIndex],
      steps = phaseStepDefinitions(p, phaseIndex);
    sheetRoot.innerHTML = `<div class="sheet context-nav-sheet"><div class="context-nav-head"><div><span class="micro">Navigate</span><strong>${esc(p.title)}</strong></div><button class="context-nav-close" data-action="close-sheet" aria-label="Close navigation">×</button></div><div class="context-nav-group">${contextNavRow("Project Overview", "project")}${contextNavRow("Roadmap", "roadmap")}${contextNavRow("Notes", "notes")}</div><div class="context-nav-phase">${esc(phase.title)}</div><div class="context-nav-group">${contextNavRow(phase.title, phase.route, "Phase")}${steps.map((step) => { const state = stepState(step); return contextNavRow(step.title, step.route, state === "done" ? "Done" : state === "current" ? "Current" : "Locked", state === "locked"); }).join("")}</div></div>`;
    openSheet();
  }
'''
app = replace_once(
    app,
    '  function openSettings() {\n',
    context_nav + '  function openSettings() {\n',
    "context navigator renderer",
)

app = replace_once(
    app,
    '    if (action === "go") return go(b.dataset.route);',
    '    if (action === "open-context-nav") return openContextNavigator();\n    if (action === "go") return go(b.dataset.route);',
    "context navigator opener",
)
app = replace_once(
    app,
    '    if (action === "close-sheet") return closeSheet();',
    '    if (action === "close-sheet") return closeSheet();\n    if (action === "context-go") {\n      const route = b.dataset.route;\n      closeSheet();\n      return go(route);\n    }',
    "context navigator destination",
)

app = re.sub(
    r'    if \(action === "export-backup"\) return exportBackup\(\);\n    if \(action === "import-backup"\) \{\n      document\.getElementById\("importFile"\)\.click\(\);\n      return;\n    \}\n',
    "",
    app,
    count=1,
)
app = sub_once(
    app,
    r"  function exportBackup\(\) \{.*?\n  \}\n  document\n    \.getElementById\(\"importFile\"\)\n    \.addEventListener\(\"change\", async \(e\) => \{.*?\n    \}\);\n",
    "",
    "remove dormant Backup/Restore implementation",
)

write("app.js", app)

# --- index.html --------------------------------------------------------------
index = read("index.html")
index = sub_once(index, r"    <style>.*?</style>\n", "", "remove inline timeline style")
index = replace_once(
    index,
    '    <input id="importFile" type="file" accept="application/json" hidden />\n',
    "",
    "remove hidden backup import input",
)
write("index.html", index)

# --- styles.css --------------------------------------------------------------
css = read("styles.css")
css = replace_once(
    css,
    ':is(.list-row, .project-open, .quick-card, .nav-btn, .text-btn, .mini-btn, .sheet-close, .mix-toggle, .top-icon-btn, .project-menu, .segment-choice):not(:disabled):active {',
    ':is(.list-row, .step-row, .project-open, .quick-card, .nav-btn, .context-nav-button, .text-btn, .mini-btn, .sheet-close, .mix-toggle, .top-icon-btn, .project-menu, .segment-choice):not(:disabled):active {',
    "active state includes navigation",
)
css = sub_once(
    css,
    r"\.topbar \.center \.phase-pill \{.*?\n\}\n",
    '''.context-nav-button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 5px;
  min-width: 44px;
  min-height: 44px;
  max-width: min(44vw, 250px);
  padding: 0 8px;
  border-radius: 9px;
  color: var(--muted);
  font-size: 14px;
  font-weight: 620;
}
.context-nav-button > span:first-child {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
.context-caret {
  flex: 0 0 auto;
  color: var(--quiet);
  font-size: 13px;
  transform: translateY(-1px);
}
''',
    "context title style",
)
css = sub_once(
    css,
    r"\.checkpoint-head \{.*?\.checkpoint-progress \{\n  margin: 0 0 12px;\n\}\n",
    '''.step-head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  margin: 30px 2px 9px;
}
.step-head .section-kicker {
  margin: 0;
}
.step-count {
  font-size: 12px;
  color: var(--meta-text);
  font-variant-numeric: tabular-nums;
}
.step-row {
  width: 100%;
  min-height: 56px;
  display: grid;
  grid-template-columns: minmax(0, 1fr) auto;
  align-items: center;
  gap: 12px;
  padding: 9px var(--space-4);
  border-bottom: 1px solid var(--line);
  border-radius: 0;
  text-align: left;
}
.step-row:last-child {
  border-bottom: 0;
}
.step-row .title {
  font-size: 16px;
  font-weight: 670;
}
.step-trailing {
  display: inline-flex;
  align-items: center;
  justify-content: flex-end;
  gap: 7px;
}
.step-state {
  color: var(--meta-text);
  font-size: 12px;
  font-weight: 560;
}
.step-row.current .step-state {
  color: var(--accent-text);
}
.step-row.done .step-state {
  color: var(--muted);
}
.step-row.locked {
  opacity: 0.5;
}
''',
    "Step list styles",
)
css = sub_once(
    css,
    r"\.checkpoint-locked-message \{.*?\.checkpoint-locked-message \.title \{.*?\n\}\n",
    "",
    "remove obsolete locked checkpoint card styles",
)
css = replace_once(
    css,
    '.presence-handle, .event-handle {\n  position: absolute;',
    '.presence-handle, .event-handle {\n  position: absolute;\n  z-index: 7;',
    "timeline handle z-index",
)
# Change markers already have their own rule; keep the same stacking contract moved from index.html.
css = replace_once(
    css,
    '.change-marker {\n  position: absolute;',
    '.change-marker {\n  position: absolute;\n  z-index: 7;',
    "change marker z-index",
)
css = replace_once(
    css,
    '.tracks-next-wrap {\n  display: flex;\n  justify-content: flex-end;\n  margin-top: 18px;\n}',
    '.tracks-next-wrap {\n  display: flex;\n  justify-content: flex-end;\n  margin-top: 26px;\n}',
    "Tracks continuation separation",
)
css = replace_once(
    css,
    '.workflow-page .phase-checkpoints > .checkpoint-head:first-child {',
    '.workflow-page .phase-steps > .step-head:first-child {',
    "Phase Steps heading reset",
)
css = replace_once(
    css,
    '.phase-setup, .phase-checkpoints, .arrangement-region, .study-observations {',
    '.phase-setup, .phase-steps, .arrangement-region, .study-observations {',
    "Phase Steps min width",
)

context_css = '''
.context-nav-sheet {
  width: min(360px, calc(100vw - 28px));
  max-width: 360px;
  max-height: calc(100dvh - env(safe-area-inset-top) - 84px);
  position: fixed;
  top: calc(env(safe-area-inset-top) + 58px);
  left: 50%;
  bottom: auto;
  transform: translateX(-50%);
  border: 1px solid var(--line-strong);
  border-radius: var(--radius-card);
  padding: var(--space-3);
  animation: none;
}
.context-nav-head {
  min-height: 48px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  padding: 2px 4px 10px;
}
.context-nav-head strong {
  display: block;
  margin-top: 2px;
  font-size: 16px;
}
.context-nav-close {
  width: 44px;
  height: 44px;
  display: grid;
  place-items: center;
  color: var(--muted);
  font-size: 24px;
}
.context-nav-group {
  overflow: hidden;
  border: 1px solid var(--line);
  border-radius: var(--radius-control);
  background: var(--surface);
}
.context-nav-row {
  width: 100%;
  min-height: 48px;
  display: grid;
  grid-template-columns: minmax(0, 1fr) auto;
  align-items: center;
  gap: 12px;
  padding: 0 13px;
  border-bottom: 1px solid var(--line);
  border-radius: 0;
  text-align: left;
  font-size: 14px;
}
.context-nav-row:last-child {
  border-bottom: 0;
}
.context-nav-status {
  color: var(--meta-text);
  font-size: 11px;
}
.context-nav-phase {
  margin: 14px 4px 7px;
  color: var(--meta-text);
  font-size: 11px;
  font-weight: 650;
}
.presence-handle,
.event-handle,
.change-marker {
  z-index: 7;
}
'''
css = replace_once(
    css,
    '.sheet-backdrop {\n',
    context_css + '.sheet-backdrop {\n',
    "context navigator styles",
)

css = replace_once(
    css,
    '  .app-shell {\n    /* Let intrinsic content decide whether the page scrolls; do not reserve a fake toolbar-height tail. */\n    padding-bottom: calc(24px + env(safe-area-inset-bottom));\n  }',
    '''  .app-shell {
    /* Short pages stay planted; true scroll pages get clearance above Safari chrome. */
    --scroll-end-clearance: 0px;
    padding-bottom: calc(24px + env(safe-area-inset-bottom) + var(--scroll-end-clearance));
  }
  .app-shell[data-viewport-fit="false"] {
    --scroll-end-clearance: 72px;
  }''',
    "dynamic Safari scroll clearance",
)
css = css.replace('#app[data-route="map"] .phase-checkpoints', '#app[data-route="map"] .phase-steps')
css = sub_once(
    css,
    r'  #app\[data-route="map"\] \.checkpoint-progress \{\n    margin-bottom: 8px;\n  \}\n',
    "",
    "remove mobile checkpoint progress rule",
)
css = replace_once(
    css,
    ':is(.list-row, .project-open, .quick-card, .nav-btn, .text-btn, .mini-btn, .sheet-close, .mix-toggle, .top-icon-btn, .project-menu, .segment-choice):not(:disabled):hover, summary:hover, .structure-row:hover {',
    ':is(.list-row, .step-row, .project-open, .quick-card, .nav-btn, .context-nav-button, .context-nav-row, .text-btn, .mini-btn, .sheet-close, .mix-toggle, .top-icon-btn, .project-menu, .segment-choice):not(:disabled):hover, summary:hover, .structure-row:hover {',
    "hover state includes navigation",
)
# iPad should keep the context navigator anchored instead of becoming a centered task sheet.
css = replace_once(
    css,
    '  .grabber {\n    display: none;\n  }\n}',
    '''  .grabber {
    display: none;
  }
  .context-nav-sheet {
    width: min(380px, calc(100vw - 64px));
    max-width: 380px;
    position: fixed;
    top: calc(env(safe-area-inset-top) + 58px);
    left: 50%;
    bottom: auto;
    padding: var(--space-3);
    border-radius: var(--radius-card);
    transform: translateX(-50%);
  }
}''',
    "iPad anchored context navigator",
)
write("styles.css", css)

# --- V6.md ------------------------------------------------------------------
v6 = read("V6.md")
v6 = sub_once(
    v6,
    r"### 3\.1 One hierarchy\n.*?### 3\.3 Back, Next, disclosure, and route entry",
    '''### 3.1 One hierarchy

**Project type → Phase → Step → Musical content**

Examples: **Recreation → The Skeleton → Draft → Verse / mapped tracks**, and **Recreation → The Map → Section Study → Chorus**. Project identity (song/artist) belongs alongside its project context; it is not another interchangeable phase/Step label.

Use nouns for locations: **Structure**, **Tracks**, **Session**, **Draft**, **Bounce**, **Notes**, **Roadmap**. The title says where the user is; one short supporting sentence says what to do.

The Map has three ordered Steps: **Structure, Tracks, Section Study**. The Skeleton has **Session, Draft, Bounce**. Step completion is automatically derived from canonical project state; phase navigation must not look like a manual checklist. Completed Steps remain navigable for editing, the next eligible Step is current, and later Steps remain visible but quiet/locked when their prerequisites are not satisfied. **Review Map** is the concluding review location inside The Map, not a fourth Step.

Later Recreation phases remain visible on Roadmap but have no fabricated Step experiences. Original keeps its flexible progression rather than inheriting Recreation's strict sequencing.

### 3.2 Headers and orientation: four separate navigation concepts

**Back = previous history. Context title = fast in-project navigation. Roadmap = whole journey. Future app tabs/sidebar = top-level areas only when earned.**

Use one reusable header composition:

- Top-left Back follows actual eligible browser/history state and uses a truthful previous-screen label when space permits.
- The center is normally quiet. When project-local navigation is useful, show a restrained interactive context title with a disclosure indicator and a full touch target.
- On The Map/The Skeleton phase homes, the context title is the project name. On their Step/review screens, it is the parent Phase name. Roadmap/Notes may use the project name.
- Tapping the context title opens a compact navigator containing **Project Overview, Roadmap, Notes, the current Phase, and its relevant Steps**. It is not a duplicate seven-phase Roadmap.
- Passive center pills/labels are prohibited. If the center element looks interactive, it must navigate.
- The primary page title identifies the current location. Quiet positional information follows §3.4; supporting text appears only when useful.
- Trailing toolbar space is reserved for contextual action/status such as Saved.

Do not add persistent breadcrumb strings. Back, the real context navigator, the current title, Steps, and Roadmap provide orientation without another hierarchy display.

A persistent Projects/Notes tab bar or iPad sidebar is intentionally deferred until the planned global Notes hub becomes a genuine app-level destination. Do not spend phone height on top-level chrome before the information architecture earns it.

### 3.3 Back, Next, disclosure, and route entry''',
    "V6 Steps/navigation architecture",
)
v6 = v6.replace("project/phase/checkpoint entry", "project/phase/Step entry")
v6 = v6.replace("remembered checkpoint entry", "remembered Step entry")
v6 = v6.replace("parent-pill navigation", "context navigation")
v6 = v6.replace("parent access", "context access")
v6 = sub_once(
    v6,
    r"### 3\.4 Contextual progress by hierarchy level\n.*?\n## 4\. Shared visual and component system",
    '''### 3.4 Contextual progress by hierarchy level

**Home screens = visual progression. Working screens = quiet positional progress. Nested musical work = local musical position.** Do not display multiple competing progress systems simultaneously.

- **Recreation project home:** current Phase and the next useful destination; Roadmap owns the seven-phase journey detail.
- **The Map / The Skeleton phase home:** a compact **Steps** list is the detailed progression surface. A quiet `2 of 3 complete` summary is sufficient; no redundant progress bar or leading checklist circles.
- **Normal Step work:** quiet position such as `Step 1 of 3`, `Step 2 of 3`, etc. This indicates location, not a manual completion control.
- **Section Study:** prioritize local song-section position (`Section Study · 2 of 8`, `Chorus`, `8 bars`) rather than stacking another Step counter on top.
- **Review Map:** clear Review Map title and The Map context; it remains a concluding review, never a fictional fourth Step.

All displayed completion, Step states, availability, and route guards derive from the same current canonical state (§6). Previously entered downstream work may remain stored when an upstream prerequisite becomes invalid, while visible valid progression reflects the dependency truthfully.

## 4. Shared visual and component system''',
    "V6 progression display",
)
v6 = v6.replace("Setup fields, checkpoints, Session checks, secondary destinations", "Setup fields, phase Steps, Session checks, secondary destinations")
write("V6.md", v6)

# --- CONTEXT.md --------------------------------------------------------------
context = read("CONTEXT.md")
context = replace_once(
    context,
    "Historically this was designed as 3 checkpoints per phase / 21 checkpoints total.",
    "Earlier versions described three checkpoints per phase / 21 checkpoints total. The current user-facing progression model calls ordered work inside a Phase **Steps**; completion is derived automatically and Phase homes must not look like manual checklists.",
    "CONTEXT progression vocabulary",
)
context = replace_once(
    context,
    "   - Balance → Shape → World as mix sub-checkpoints",
    "   - Balance → Shape → World as mix sub-steps",
    "CONTEXT Original vocabulary",
)
context = replace_once(
    context,
    "Then show Checkpoints below. Do not hide setup behind a separate page, disclosure, compact row, or pill strip.",
    "Then show the three ordered Steps below. Structure / Tracks / Section Study remain visible for orientation even when locked; do not replace them with one generic prerequisite card. Do not hide setup behind a separate page, disclosure, compact row, or pill strip.",
    "CONTEXT Map Step behavior",
)
context = replace_once(
    context,
    "Checkpoint 3 of The Map is:",
    "Step 3 of The Map is:",
    "CONTEXT Section Study Step",
)
nav_note = '''
### Current progression and navigation vocabulary — LOCKED

FIRE's user-facing hierarchy is **Project → Phase → Step → Musical content**. `Checkpoint` is historical/internal wording only and must not return as the phase-home checklist metaphor.

- **Back** follows actual browser/history navigation.
- A quiet **interactive center context title** provides fast in-project navigation without becoming another passive pill. Phase homes use the project context; Step/review screens use their parent Phase context.
- The context navigator may expose Project Overview, Roadmap, Notes, the current Phase, and relevant Steps. It does not duplicate the full seven-phase Roadmap.
- **Roadmap** remains the whole-journey view.
- Persistent app-level Projects/Notes navigation is deferred until the global Notes hub is a real top-level destination.

'''
context = replace_once(
    context,
    "### Goal of a Recreation\n",
    nav_note + "### Goal of a Recreation\n",
    "CONTEXT navigation note",
)
write("CONTEXT.md", context)

# --- changelog ---------------------------------------------------------------
changelog = read("CHANGELOG.md")
changelog = replace_once(
    changelog,
    "## V6\n\n",
    "## V6\n\n- Phase progression/navigation consolidation: user-facing Checkpoints become ordered Steps with derived done/current/locked state; Map and Skeleton share one Phase Home system; a real center context navigator provides fast project-local jumps while Back remains truthful history; true scrolling pages gain Safari end clearance; dormant Backup/Restore code is removed; and zero-context handoff freshness is CI-enforced.\n",
    "V6 milestone",
)
write("CHANGELOG.md", changelog)
