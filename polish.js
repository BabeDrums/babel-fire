(() => {
  "use strict";

  const KEY = "production-projects-v1";
  const app = document.getElementById("app");
  const undoNotice = document.getElementById("undoNotice");
  if (!app) return;

  const trashSvg = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5.5 7.5h13M9.5 7.5V5.25h5v2.25M8 9.5l.7 9.25h6.6L16 9.5M10.5 10.5v5.75M13.5 10.5v5.75"/></svg>';

  function currentSectionIndex() {
    const text = app.querySelector(".work-position")?.textContent || "";
    const match = text.match(/Section Study\s*·\s*(\d+)\s+of/i);
    return match ? Math.max(0, Number(match[1]) - 1) : Number(history.state?.sectionIndex || 0);
  }

  function navigate(route, extra = {}) {
    const state = {
      ...(history.state || {}),
      route,
      ...extra,
      projectId: JSON.parse(localStorage.getItem(KEY) || "{}")?.currentProjectId || history.state?.projectId,
      fromRoute: app.dataset.route || history.state?.route || null,
      fromLabel: app.dataset.route === "map-summary" ? "Review Map" : history.state?.fromLabel || null,
    };
    history.pushState(state, "", location.pathname + location.search);
    window.dispatchEvent(new PopStateEvent("popstate", { state }));
  }

  function enhanceNewProjectKeyboard() {
    if (app.dataset.route !== "new-project") return;
    const title = document.getElementById("newTitle");
    const artist = document.getElementById("newArtist");
    if (title && !title.dataset.enterPolish) {
      title.dataset.enterPolish = "1";
      title.addEventListener("keydown", (event) => {
        if (event.key !== "Enter" || event.shiftKey || event.isComposing) return;
        event.preventDefault();
        if (artist && !artist.hidden) {
          artist.focus();
          artist.select?.();
        } else {
          app.querySelector('[data-action="create-project"]')?.click();
        }
      });
    }
    if (artist && !artist.dataset.enterPolish) {
      artist.dataset.enterPolish = "1";
      artist.addEventListener("keydown", (event) => {
        if (event.key !== "Enter" || event.shiftKey || event.isComposing) return;
        event.preventDefault();
        app.querySelector('[data-action="create-project"]')?.click();
      });
    }
  }

  function enhanceRemoveButtons() {
    app.querySelectorAll('.mini-btn.remove:not([data-polished-remove])').forEach((button) => {
      button.dataset.polishedRemove = "1";
      const label = button.getAttribute("aria-label") || "Remove";
      button.title = label;
      button.innerHTML = trashSvg;
    });
  }

  function enhanceContinuationMarkers() {
    if (app.dataset.route !== "section-study") return;
    const firstLane = app.querySelector(".timeline-lane");
    const bars = Number(firstLane ? getComputedStyle(firstLane).getPropertyValue("--bars") : 0) ||
      Number((app.querySelector(".study-pane > .sub")?.textContent || "").match(/\d+/)?.[0] || 0);
    if (!bars) return;

    const ruler = app.querySelector(".timeline-ruler");
    if (ruler && !ruler.querySelector(".timeline-continuation-marker")) {
      const marker = document.createElement("span");
      marker.className = "timeline-continuation-marker";
      marker.textContent = String(bars + 1);
      marker.setAttribute("aria-hidden", "true");
      ruler.appendChild(marker);
    }
    app.querySelectorAll(".timeline-lane").forEach((lane) => {
      if (lane.querySelector(":scope > .timeline-continuation-marker")) return;
      const marker = document.createElement("span");
      marker.className = "timeline-continuation-marker";
      marker.textContent = String(bars + 1);
      marker.setAttribute("aria-hidden", "true");
      lane.appendChild(marker);
    });
  }

  function enhanceSummary() {
    if (app.dataset.route !== "map-summary") return;
    const lists = [...app.querySelectorAll(".chip-list")];
    const structure = lists[0];
    const tracks = lists[1];

    structure?.querySelectorAll(":scope > .chip").forEach((chip, index) => {
      if (chip.tagName === "BUTTON") return;
      const button = document.createElement("button");
      button.className = "summary-nav-chip";
      button.type = "button";
      button.textContent = chip.textContent;
      button.setAttribute("aria-label", `Open ${chip.textContent}`);
      button.addEventListener("click", () => navigate("section-study", { sectionIndex: index, expandedTrackId: null }));
      chip.replaceWith(button);
    });

    tracks?.querySelectorAll(":scope > .chip").forEach((chip) => {
      if (chip.tagName === "BUTTON") return;
      const button = document.createElement("button");
      button.className = "summary-nav-chip";
      button.type = "button";
      button.textContent = chip.textContent;
      button.setAttribute("aria-label", `Open Tracks for ${chip.textContent}`);
      button.addEventListener("click", () => navigate("tracks"));
      chip.replaceWith(button);
    });

    app.querySelectorAll('.review-sections [data-action="summary-jump"]').forEach((button) => button.remove());
  }

  function enhanceDraftHierarchy() {
    if (app.dataset.route !== "skeleton-draft") return;
    app.querySelectorAll("[data-draft-section]").forEach((details) => {
      const summary = details.querySelector("summary");
      const status = summary?.querySelector(".round-check");
      const copy = summary?.querySelector(".copy");
      if (!summary || !status || !copy) return;
      status.classList.add("derived-status");
      status.setAttribute("aria-hidden", "true");
      const match = copy.textContent.match(/(\d+)\s+of\s+(\d+)\s+tracks/i);
      if (match) {
        const done = Number(match[1]), total = Math.max(1, Number(match[2]));
        status.style.setProperty("--draft-progress", `${Math.round(done / total * 100)}%`);
        const holder = copy.parentElement;
        if (holder && !holder.querySelector(".draft-progress")) {
          const bar = document.createElement("span");
          bar.className = "draft-progress";
          bar.setAttribute("aria-hidden", "true");
          bar.innerHTML = `<span style="width:${Math.round(done / total * 100)}%"></span>`;
          holder.appendChild(bar);
        } else {
          holder?.querySelector(".draft-progress > span")?.setAttribute("style", `width:${Math.round(done / total * 100)}%`);
        }
        const checks = details.querySelector(".draft-checks");
        if (checks && !checks.querySelector(".draft-child-label")) {
          const label = document.createElement("div");
          label.className = "draft-child-label";
          label.textContent = done === total ? "Tracks complete" : "Complete tracks below";
          checks.prepend(label);
        } else if (checks?.querySelector(".draft-child-label")) {
          checks.querySelector(".draft-child-label").textContent = done === total ? "Tracks complete" : "Complete tracks below";
        }
      }
    });
  }

  function restorePolishUndo() {
    const prior = sessionStorage.getItem("fire-polish-undo");
    if (!prior || !undoNotice || undoNotice.dataset.polishUndoShown) return;
    undoNotice.dataset.polishUndoShown = "1";
    undoNotice.hidden = false;
    undoNotice.innerHTML = '<span>Continuation changed</span><button type="button" id="polishUndo">Undo</button>';
    document.getElementById("polishUndo")?.addEventListener("click", () => {
      localStorage.setItem(KEY, prior);
      sessionStorage.removeItem("fire-polish-undo");
      location.reload();
    });
    setTimeout(() => {
      if (undoNotice.dataset.polishUndoShown === "1") {
        undoNotice.hidden = true;
        sessionStorage.removeItem("fire-polish-undo");
        delete undoNotice.dataset.polishUndoShown;
      }
    }, 12000);
  }

  function enhance() {
    enhanceNewProjectKeyboard();
    enhanceRemoveButtons();
    enhanceContinuationMarkers();
    enhanceSummary();
    enhanceDraftHierarchy();
    restorePolishUndo();
  }

  let queued = false;
  const observer = new MutationObserver(() => {
    if (queued) return;
    queued = true;
    requestAnimationFrame(() => {
      queued = false;
      enhance();
    });
  });
  observer.observe(app, { childList: true, subtree: true });
  enhance();

  let drag = null;
  document.addEventListener("pointerdown", (event) => {
    const handle = event.target.closest?.('.presence-handle.right[data-range-id]:not(.open-continuation)');
    if (!handle || app.dataset.route !== "section-study") return;
    const lane = handle.closest(".timeline-lane");
    if (!lane) return;
    drag = {
      pointerId: event.pointerId,
      rangeId: handle.dataset.rangeId,
      rect: lane.getBoundingClientRect(),
      originX: event.clientX,
      originY: event.clientY,
      crossed: false,
      before: localStorage.getItem(KEY),
      lane,
    };
  }, true);

  document.addEventListener("pointermove", (event) => {
    if (!drag || event.pointerId !== drag.pointerId) return;
    const dx = event.clientX - drag.originX;
    const dy = Math.abs(event.clientY - drag.originY);
    drag.crossed = dx > 8 && dy < 28 && event.clientX > drag.rect.right + 10;
    drag.lane?.classList.toggle("continuation-armed", drag.crossed);
  }, true);

  function finishContinuation(event, cancelled) {
    if (!drag || event.pointerId !== drag.pointerId) return;
    const state = drag;
    state.lane?.classList.remove("continuation-armed");
    drag = null;
    if (cancelled || !state.crossed || !state.before) return;
    setTimeout(() => {
      try {
        const db = JSON.parse(localStorage.getItem(KEY) || "null");
        const project = db?.projects?.find((item) => item.id === db.currentProjectId);
        const range = project?.map?.timeline?.presence?.find((item) => item.id === state.rangeId);
        if (!range || range.end == null) return;
        sessionStorage.setItem("fire-polish-undo", state.before);
        range.end = null;
        if (project.map) {
          project.map.mapVerified = false;
          project.map.teachBack = false;
        }
        if (project.skeleton?.draft?.parts) {
          Object.values(project.skeleton.draft.parts).forEach((parts) => {
            if (parts && range.trackId in parts) parts[range.trackId] = false;
          });
        }
        if (project.skeleton?.bounce) {
          project.skeleton.bounce.exported = false;
          project.skeleton.bounce.listened = false;
        }
        localStorage.setItem(KEY, JSON.stringify(db));
        history.replaceState({ ...(history.state || {}), sectionIndex: currentSectionIndex() }, "", location.pathname + location.search);
        location.reload();
      } catch (_) {}
    }, 0);
  }

  document.addEventListener("pointerup", (event) => finishContinuation(event, false), true);
  document.addEventListener("pointercancel", (event) => finishContinuation(event, true), true);
})();
