from pathlib import Path
import re

path = Path("app.js")
app = path.read_text(encoding="utf-8")


def replace_once(old, new, label):
    global app
    if old not in app:
        raise SystemExit(f"missing source block: {label}")
    app = app.replace(old, new, 1)


def sub_once(pattern, replacement, label):
    global app
    app, count = re.subn(pattern, replacement, app, count=1, flags=re.S)
    if count != 1:
        raise SystemExit(f"expected one match for {label}, got {count}")


replace_once(
'''  let ui = {
    route: "projects",
    sectionIndex: 0,
    newType: "original",
    expandedTrackId: null,
    animating: false,
  };
''',
'''  let ui = {
    route: "projects",
    sectionIndex: 0,
    newType: "original",
    expandedTrackId: null,
    setupExpanded: false,
    animating: false,
  };

  // Root scrolling follows rendered content, not a route allowlist. Measuring the
  // in-flow children avoids Safari dynamic-toolbar/dvh reserve creating fake scroll.
  let viewportFitFrame = 0;
  function applyViewportFit() {
    viewportFitFrame = 0;
    if (document.body.classList.contains("sheet-open")) return;
    const viewportHeight = window.visualViewport?.height || window.innerHeight;
    if (!viewportHeight) return;
    const shellRect = app.getBoundingClientRect(),
      style = getComputedStyle(app),
      bottomPadding = Number.parseFloat(style.paddingBottom) || 0,
      flowBottom = [...app.children]
        .filter((el) => getComputedStyle(el).position !== "fixed")
        .reduce(
          (bottom, el) => Math.max(bottom, el.getBoundingClientRect().bottom),
          shellRect.top,
        ),
      contentHeight = flowBottom - shellRect.top + bottomPadding,
      fits = contentHeight <= viewportHeight + 2;
    app.dataset.viewportFit = fits ? "true" : "false";
    document.documentElement.style.overflowY = fits ? "hidden" : "";
    document.body.style.overflowY = fits ? "hidden" : "";
    if (fits && window.scrollY) window.scrollTo(0, 0);
  }
  function queueViewportFit() {
    cancelAnimationFrame(viewportFitFrame);
    viewportFitFrame = requestAnimationFrame(() =>
      requestAnimationFrame(applyViewportFit),
    );
  }
  if (typeof ResizeObserver === "function")
    new ResizeObserver(queueViewportFit).observe(app);
  window.visualViewport?.addEventListener("resize", queueViewportFit);
  window.addEventListener("resize", queueViewportFit);
''',
"ui state and viewport fit controller",
)

replace_once(
'''  function refreshMapProgress() {
    if (ui.route !== "map") return;
    const p = project(), state = canonicalState(p), done = mapCheckpointCount(p);
    const destinations = ["structure", "tracks", sectionStudyCoreDone(p) ? "map-summary" : "section-study"];
    const completed = [state.structure, state.palette, state.study];
    app.querySelectorAll(".checkpoint-head + .progress + .list > .list-row").forEach((row, i) => {
      const html = checkpointRow(["Structure", "Tracks", "Section Study"][i],
        ["Map the form.", "Identify what plays.", "Map each section in time."][i],
        destinations[i], completed[i], !!state.eligible[destinations[i]]);
      row.outerHTML = html;
    });
    const count = app.querySelector(".checkpoint-count"), bar = app.querySelector(".checkpoint-progress span");
    if (count) count.textContent = `${done} of 3`;
    if (bar) bar.style.width = `${done / 3 * 100}%`;
  }
''',
'''  function refreshMapProgress() {
    if (ui.route !== "map") return;
    const p = project(), state = canonicalState(p), done = mapCheckpointCount(p);
    const destinations = ["structure", "tracks", sectionStudyCoreDone(p) ? "map-summary" : "section-study"];
    const completed = [state.structure, state.palette, state.study];
    app.querySelectorAll(".phase-checkpoints .group-card.list > .list-row").forEach((row, i) => {
      const html = checkpointRow(["Structure", "Tracks", "Section Study"][i],
        ["Map the form.", "Identify what plays.", "Map each section in time."][i],
        destinations[i], completed[i], !!state.eligible[destinations[i]]);
      row.outerHTML = html;
    });
    const count = app.querySelector(".checkpoint-count");
    if (count) count.textContent = `${done} of 3`;
    queueViewportFit();
  }
''',
"map live progress",
)

replace_once(
'''    const fromRoute = ui.route,
      fromLabel = routeLabel(fromRoute);
    routeMotion =
''',
'''    const fromRoute = ui.route,
      fromLabel = routeLabel(fromRoute);
    if (route !== fromRoute && (route === "map" || fromRoute === "map"))
      ui.setupExpanded = false;
    routeMotion =
''',
"map disclosure reset on navigation",
)

sub_once(
    r'''  function renderProject\(\) \{.*?\n  \}\n  function renderOriginalOverview\(\) \{''',
'''  function renderProject() {
    const p = project();
    if (!p) return go("projects", {}, false);
    if (p.type === "original") return renderOriginalOverview();
    const phaseIndex = currentStudyPhaseIndex(p),
      phase = STUDY_PHASES[phaseIndex],
      next = STUDY_PHASES[phaseIndex + 1],
      context = [p.artist, "Recreation"].filter(Boolean).join(" · "),
      phaseProgress = phaseIndex === 0
        ? `${mapCheckpointCount(p)} of 3 checkpoints`
        : phaseIndex === 1
          ? `${skeletonCheckpointCount(p)} of 3 checkpoints`
          : "Open roadmap";
    const body = `<div class="project-overview"><section class="project-current"><button class="hero-card project-open" style="border-radius:var(--radius-card);height:auto" data-action="go" data-route="${phase.route}" aria-label="Open ${esc(phase.title)}"><div class="phase-line"><div><h3>${esc(phase.title)}</h3></div><div class="phase-num">Phase ${phaseIndex + 1} of 7</div></div><p class="sub">${esc(phase.desc)}</p><div class="foot"><span>${esc(phaseProgress)}</span><span aria-hidden="true">›</span></div></button></section><section class="project-support">${next ? `<div class="section-kicker">Next</div><div class="group-card list"><div class="list-row static no-status"><div><div class="title">${esc(next.title)}</div><div class="desc">${esc(next.desc)}</div></div></div></div>` : ""}<div class="section-kicker">Project</div><div class="quick-grid"><button class="quick-card" data-action="go" data-route="roadmap"><strong>Roadmap</strong><span>Seven phases to a finished rebuild.</span></button><button class="quick-card" data-action="go" data-route="notes"><strong>Notes</strong><span>Questions and takeaways.</span></button></div></section></div>`;
    app.innerHTML =
      topbar(
        backButton("projects", "Projects"),
        "",
        `<button class="text-btn" data-action="settings" aria-label="Project options">…</button>`,
      ) + workflowPage(p.title, context, body);
  }
  function renderOriginalOverview() {''',
    "project overview",
)

sub_once(
    r'''  function workflowPhaseHome\(index, done, total, checkpointsHtml, beforeHtml = ""\) \{.*?\n  \}\n  function projectPageMotionClass\(\) \{''',
'''  function workflowPhaseHome(index, done, total, checkpointsHtml, beforeHtml = "") {
    const p = project(),
      pct = total ? Math.round((done / total) * 100) : 0,
      progress = index === 0
        ? ""
        : `<div class="progress checkpoint-progress"><span style="width:${pct}%"></span></div>`,
      body = `<div class="phase-layout ${beforeHtml ? "with-setup" : ""}">${beforeHtml ? `<section class="phase-setup">${beforeHtml}</section>` : ""}<section class="phase-checkpoints"><div class="checkpoint-head"><div class="section-kicker">Checkpoints</div><span class="checkpoint-count">${done} of ${total}</span></div>${progress}<div class="group-card list">${checkpointsHtml}</div></section></div>`;
    return (
      topbar(
        backButton("project", p?.title || "Project"),
        "",
        savedMark(),
      ) + workflowPage(STUDY_PHASES[index].title, STUDY_PHASES[index].desc, body)
    );
  }
  function projectPageMotionClass() {''',
    "workflow phase home",
)

sub_once(
    r'''  function renderMapHome\(\) \{.*?\n  \}\n\n  function renderStructure\(\) \{''',
'''  function renderMapHome() {
    const p = project(),
      m = p.map,
      done = mapCheckpointCount(p),
      setupDone = mapSetupComplete(p),
      structureUnlocked = setupDone,
      tracksUnlocked = structureDone(p),
      studyUnlocked = tracksDone(p),
      studyRoute = sectionStudyCoreDone(p) ? "map-summary" : "section-study";
    const setupExpanded = !setupDone || ui.setupExpanded;
    const setup = setupExpanded
      ? `<div class="section-kicker">Song Setup</div><div class="group-card setup-panel"><div class="setup-row"><div class="setup-label">Reference</div><button class="state-control ${m.setup.reference ? "on" : ""}" data-action="toggle-setup" data-field="reference"><span>${m.setup.reference ? "Imported" : "Import"}</span><span class="check-circle"></span></button></div><div class="setup-row"><div class="setup-label">Tempo</div><div class="setup-value"><input id="tempoInput" aria-label="Tempo in BPM" inputmode="decimal" value="${esc(m.setup.tempo)}" placeholder="—"><span class="suffix">BPM</span></div></div><div class="setup-row"><div class="setup-label">Meter</div><div class="setup-value"><select id="meterInput" aria-label="Meter">${["4/4", "3/4", "6/8", "5/4", "7/8"].map((x) => `<option ${m.setup.meter === x ? "selected" : ""}>${x}</option>`).join("")}</select></div></div><div class="setup-row"><div class="setup-label">Grid</div><button class="state-control ${m.setup.grid ? "on" : ""}" data-action="toggle-setup" data-field="grid"><span>${m.setup.grid ? "Aligned" : "Align"}</span><span class="check-circle"></span></button></div></div><div class="spacer-18"></div>${actionCard("First Listen", "Play the full song once without stopping.", m.setup.firstListen, "toggle-setup", false, 'data-field="firstListen"')}`
      : `<div class="group-card list"><button class="list-row" data-action="toggle-setup-disclosure" aria-expanded="false"><span class="round-check on"></span><div><div class="title">Song Setup</div><div class="desc">Ready · ${esc(m.setup.tempo)} BPM · ${esc(m.setup.meter)}</div></div><span class="chev">›</span></button></div>`;
    const checkpoints =
      checkpointRow(
        "Structure",
        "Map the form.",
        "structure",
        structureDone(p),
        structureUnlocked,
      ) +
      checkpointRow(
        "Tracks",
        "Identify what plays.",
        "tracks",
        tracksDone(p),
        tracksUnlocked,
      ) +
      checkpointRow(
        "Section Study",
        "Map each section in time.",
        studyRoute,
        sectionStudyDone(p),
        studyUnlocked,
      );
    app.innerHTML = workflowPhaseHome(0, done, 3, checkpoints, setup);
  }

  function renderStructure() {''',
    "map home",
)

sub_once(
    r'''  function renderRoadmap\(\) \{.*?\n  \}\n  function renderNotes\(\) \{''',
'''  function renderRoadmap() {
    const p = project();
    if (p.type === "original") {
      app.innerHTML =
        topbar(
          backButton("project", "Original Song"),
          "",
          "",
        ) +
        `<h2>Original Song</h2><p class="sub">Anything worth keeping → finished record.</p><div class="spacer-18"></div><div class="roadmap-grid">${ORIGINAL_PHASES.map((ph, i) => `<div class="road-phase ${i === 0 ? "current" : "future"}"><div class="road-top"><div class="road-num">${i + 1}</div><div><h3>${esc(ph[0])}</h3><p>${esc(ph[1])}</p></div></div></div>`).join("")}</div>`;
      return;
    }
    app.innerHTML =
      topbar(backButton("project", "Recreation"), "", "") +
      `<h2>Roadmap</h2><p class="sub">Seven phases from analysis to finished rebuild.</p><div class="spacer-18"></div><div class="roadmap-grid">${STUDY_PHASES.map(
        (ph, i) => {
          const st = studyPhaseStatus(p, i),
            unlocked = studyPhaseUnlocked(p, i),
            tag = unlocked ? "button" : "div",
            status = st === "done"
              ? "Completed"
              : st === "available"
                ? "Available"
                : st === "locked"
                  ? "Locked"
                  : "",
            detail = st === "current"
              ? `<p>${esc(ph.desc)}</p>`
              : status
                ? `<span class="micro">${status}</span>`
                : "",
            checks = st === "current"
              ? `<div class="road-checks">${ph.checkpoints.map((x) => `<span class="road-check">${esc(x)}</span>`).join("")}</div>`
              : "";
          return `<${tag} class="road-phase ${st} ${unlocked ? "clickable" : ""}" ${unlocked ? `data-action="go" data-route="${ph.route}"` : ""}><div class="road-top">${st === "done" ? `<span class="round-check on"></span>` : st === "current" ? `<span class="current-ring"></span>` : `<div class="road-num">${i + 1}</div>`}<div><h3>${esc(ph.title)}</h3>${detail}</div>${unlocked ? `<span class="chev">›</span>` : ""}</div>${checks}</${tag}>`;
        },
      ).join("")}</div>`;
  }
  function renderNotes() {''',
    "roadmap",
)

replace_once(
'''    if (action === "settings") return openSettings();
        if (action === "toggle-setup") {
      p.map.setup[b.dataset.field] = !p.map.setup[b.dataset.field];
      invalidateMapVerification(p);
      save();
      return renderMapHome();
    }
''',
'''    if (action === "settings") return openSettings();
    if (action === "toggle-setup-disclosure") {
      ui.setupExpanded = true;
      return renderMapHome();
    }
    if (action === "toggle-setup") {
      p.map.setup[b.dataset.field] = !p.map.setup[b.dataset.field];
      invalidateMapVerification(p);
      ui.setupExpanded = !mapSetupComplete(p);
      save();
      return renderMapHome();
    }
''',
"map setup click actions",
)

replace_once(
'''  app.addEventListener("change", (e) => {
    if (e.target.id === "meterInput") {
      project().map.setup.meter = e.target.value;
      invalidateMapVerification(project());
      save();
      refreshMapProgress();
    }
  });
''',
'''  app.addEventListener("change", (e) => {
    if (e.target.id === "tempoInput") {
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
  });
''',
"map setup change handling",
)

replace_once(
'''    sheetRoot.setAttribute("aria-hidden", "true");
    clearTimeout(sheetClearTimer);
''',
'''    sheetRoot.setAttribute("aria-hidden", "true");
    queueViewportFit();
    clearTimeout(sheetClearTimer);
''',
"sheet close viewport update",
)

replace_once(
'''        ui = {
          route: "projects",
          sectionIndex: 0,
          newType: "original",
          expandedTrackId: null,
          animating: false,
        };
''',
'''        ui = {
          route: "projects",
          sectionIndex: 0,
          newType: "original",
          expandedTrackId: null,
          setupExpanded: false,
          animating: false,
        };
''',
"import ui reset",
)

replace_once(
'''  initHistory();
  render();
})();
''',
'''  initHistory();
  render();
  queueViewportFit();
})();
''',
"initial viewport fit",
)

path.write_text(app, encoding="utf-8")
print("adaptive composition patch applied")
