(() => {
  "use strict";

  const DB_KEY = "production-projects-v1";
  const SCHEMA_VERSION = 5;
  const LEGACY_KEYS = [
    "smithereens-map-v6",
    "smithereens-map-v5",
    "smithereens-map-v2",
  ];
  const FEEL_SCALES = {
    depth: ["Close", "Mixed", "Distant"],
    space: ["Dry", "Mixed", "Wet"],
    width: ["Narrow", "Mixed", "Wide"],
    density: ["Sparse", "Balanced", "Dense"],
    energy: ["Low", "Medium", "High"],
  };
  const FEEL_LABELS = {
    depth: "Depth",
    space: "Space",
    width: "Width",
    density: "Density",
    energy: "Energy",
  };
  const SECTION_TYPES = [
    "Intro",
    "Verse",
    "Pre-Chorus",
    "Chorus",
    "Bridge",
    "Instrumental",
    "Outro",
  ];
  const COMMON_TRACKS = [
    "Vocal",
    "Drums",
    "Bass",
    "Ukulele",
    "Guitar",
    "Piano",
    "Synth",
    "Backing vocals",
    "Percussion",
    "FX",
  ];
  const CHANGE_DEFS = {
    Widens: {
      group: "space",
      groupLabel: "Space",
      property: "width",
      kind: "range",
      tone: "space",
    },
    Narrows: {
      group: "space",
      groupLabel: "Space",
      property: "width",
      kind: "range",
      tone: "space",
    },
    Louder: {
      group: "level",
      groupLabel: "Level",
      property: "level",
      kind: "range",
      tone: "level",
    },
    Softer: {
      group: "level",
      groupLabel: "Level",
      property: "level",
      kind: "range",
      tone: "level",
    },
    Doubles: {
      group: "performance",
      groupLabel: "Performance",
      property: "doubling",
      kind: "range",
      tone: "performance",
    },
    "Pattern shift": {
      group: "performance",
      groupLabel: "Performance",
      property: "pattern",
      kind: "marker",
      tone: "performance",
    },
    "Register shift": {
      group: "performance",
      groupLabel: "Performance",
      property: "register",
      kind: "marker",
      tone: "performance",
    },
    "Effect shift": {
      group: "sound",
      groupLabel: "Sound",
      property: "effect",
      kind: "range",
      tone: "sound",
    },
  };
  const CHANGE_GROUPS = [
    { key: "space", label: "Width" },
    { key: "level", label: "Level" },
    { key: "performance", label: "Performance" },
    { key: "sound", label: "Sound" },
  ];
  const STUDY_PHASES = [
    {
      key: "map",
      title: "The Map",
      desc: "Understand the song before rebuilding it.",
      route: "map",
      checkpoints: ["Structure", "Tracks", "Section Study"],
    },
    {
      key: "skeleton",
      title: "The Skeleton",
      desc: "Build the complete draft.",
      route: "skeleton",
      checkpoints: ["Session", "Draft", "Bounce"],
    },
    {
      key: "sounds",
      title: "The Sounds",
      desc: "Match sounds and performances.",
      route: "roadmap",
      checkpoints: ["Sources", "Performance", "Character"],
    },
    {
      key: "balance",
      title: "The Balance",
      desc: "Set levels, pan, and hierarchy.",
      route: "roadmap",
      checkpoints: ["Levels", "Pan", "Hierarchy"],
    },
    {
      key: "shape",
      title: "The Shape",
      desc: "Shape tone and dynamics.",
      route: "roadmap",
      checkpoints: ["Frequency", "Dynamics", "Character"],
    },
    {
      key: "world",
      title: "The World",
      desc: "Create depth, width, and movement.",
      route: "roadmap",
      checkpoints: ["Depth", "Width", "Movement"],
    },
    {
      key: "finish",
      title: "The Finish",
      desc: "Compare, revise, finish.",
      route: "roadmap",
      checkpoints: ["A/B", "Revise", "Deliver"],
    },
  ];
  const ORIGINAL_PHASES = [
    ["The Spark", "Capture the thing worth making."],
    ["The Direction", "Decide where the idea wants to go."],
    ["The Skeleton", "Build a rough song from beginning to end."],
    ["The Production", "Develop arrangement, transitions, and identity."],
    ["The Recording", "Replace placeholders with intentional performances."],
    ["The Mix", "Balance, shape, and place the record."],
    ["The Finish", "Reference, revise, and commit."],
  ];

  const app = document.getElementById("app");
  const sheetRoot = document.getElementById("sheetRoot");
  const esc = (s) =>
    String(s ?? "").replace(
      /[&<>"']/g,
      (m) =>
        ({
          "&": "&amp;",
          "<": "&lt;",
          ">": "&gt;",
          '"': "&quot;",
          "'": "&#39;",
        })[m],
    );
  const clean = (s) => String(s ?? "").trim();
  const uid = () =>
    crypto?.randomUUID?.() ||
    "id-" + Date.now().toString(36) + Math.random().toString(36).slice(2);
  const clamp = (n, min, max) => Math.min(max, Math.max(min, n));
  function changeMeta(label) {
    return (
      CHANGE_DEFS[label] || {
        group: "other",
        groupLabel: "Other",
        property: "custom:" + String(label || "change").toLowerCase(),
        kind: "range",
        tone: "other",
      }
    );
  }
  function eventTone(e) {
    return e?.tone || changeMeta(e?.label).tone || "other";
  }
  function eventColorVar(e) {
    return `var(--change-${eventTone(e)})`;
  }
  let saveFlashTimer = null;
  let sheetClearTimer = null;
  let ui = {
    route: "projects",
    sectionIndex: 0,
    newType: "original",
    expandedTrackId: null,
    animating: false,
  };

  function makeSectionData() {
    return {
      feel: {
        depth: null,
        space: null,
        width: null,
        density: null,
        energy: null,
      },
      focusIds: [],
      focusState: "",
      silence: false,
      parking: "",
      takeaway: "",
    };
  }
  function makeStudyProject(
    title = "Smithereens",
    artist = "Twenty One Pilots",
  ) {
    return {
      id: uid(),
      type: "study",
      title,
      artist,
      createdAt: Date.now(),
      schemaVersion: SCHEMA_VERSION,
      map: {
        setup: {
          reference: false,
          tempo: "",
          meter: "4/4",
          grid: false,
          firstListen: false,
        },
        sections: [],
        structureVerified: false,
        tracks: [],
        timeline: { presence: [], events: [] },
        sectionData: {},
        mapVerified: false,
        teachBack: false,
        phaseParking: "",
        phaseTakeaway: "",
      },
      skeleton: {
        session: { tracks: {}, markers: {} },
        draft: { parts: {} },
        bounce: { exported: false, listened: false },
      },
      notes: [],
    };
  }
  function makeOriginalProject(title = "", artist = "") {
    return {
      id: uid(),
      type: "original",
      title,
      artist,
      createdAt: Date.now(),
      schemaVersion: SCHEMA_VERSION,
      spark: { starts: [], idea: "", reasons: [], anchor: "" },
      notes: [],
    };
  }
  function seedDB() {
    const p = makeStudyProject();
    p.id = "smithereens";
    return { version: SCHEMA_VERSION, currentProjectId: p.id, projects: [p] };
  }

  function migrateLegacyStorage() {
    for (const key of LEGACY_KEYS) {
      try {
        const old = JSON.parse(localStorage.getItem(key));
        if (!old) continue;
        const p = makeStudyProject();
        p.id = "smithereens";
        p.map.setup = {
          reference: !!old.setup?.reference,
          tempo: old.setup?.tempo || "",
          meter: old.setup?.meter || "4/4",
          grid: !!(old.setup?.grid ?? old.setup?.alignment),
          firstListen: !!(old.setup?.firstListen ?? old.setup?.listen),
        };
        p.map.sections = (old.sections || []).map((s, i) =>
          typeof s === "string"
            ? { id: "legacy-" + i + "-" + uid(), name: s, lengthBars: null }
            : {
                id: s.id || uid(),
                name: s.name || "Section",
                lengthBars: s.lengthBars || null,
              },
        );
        p.map.structureVerified = !!(
          old.structureVerified ?? old.transitionsChecked
        );
        p.map.ingredients = [...(old.ingredients || old.parts || [])];
        p.map.unknowns = [...(old.unknowns || [])];
        p.map.analysis = old.analysis || old.sectionAnalysis || {};
        p.map.transitions = old.transitions || {};
        p.map.phaseParking = old.phaseParking || old.parkingLot || "";
        p.map.phaseTakeaway = old.phaseTakeaway || old.babelTakeaway || "";
        p.map.mapVerified = !!old.mapVerified;
        p.map.teachBack = !!old.teachBack;
        return { version: 1, currentProjectId: p.id, projects: [p] };
      } catch (e) {}
    }
    return null;
  }
  function loadDB() {
    try {
      const saved = JSON.parse(localStorage.getItem(DB_KEY));
      if (Array.isArray(saved?.projects)) return saved;
    } catch (e) {}
    return migrateLegacyStorage() || seedDB();
  }
  let db = loadDB();

  function normalizeDatabase(candidate) {
    const out =
      candidate && Array.isArray(candidate.projects) ? candidate : seedDB();
    out.version = SCHEMA_VERSION;
    out.projects.forEach((p) => {
      p.schemaVersion = SCHEMA_VERSION;
      if (p.type === "original") {
        p.artist = p.artist || "";
        p.spark = p.spark || { starts: [], idea: "", reasons: [], anchor: "" };
        p.spark.starts = p.spark.starts || [];
        p.spark.reasons = p.spark.reasons || [];
        p.spark.idea = p.spark.idea || "";
        p.spark.anchor = p.spark.anchor || "";
        p.notes = p.notes || [];
        return;
      }
      p.type = "study";
      p.map = p.map || {};
      const m = p.map;
      m.setup = m.setup || {
        reference: false,
        tempo: "",
        meter: "4/4",
        grid: false,
        firstListen: false,
      };
      m.sections = (m.sections || []).map((s, i) =>
        typeof s === "string"
          ? { id: uid(), name: s, lengthBars: null }
          : {
              id: s.id || uid(),
              name: s.name || `Section ${i + 1}`,
              lengthBars: validBars(s.lengthBars) ? Number(s.lengthBars) : null,
            },
      );
      const oldAnalysis = m.analysis || {};
      const oldTransitions = m.transitions || {};
      let tracks = Array.isArray(m.tracks)
        ? m.tracks
            .filter(Boolean)
            .map((t) =>
              typeof t === "string"
                ? { id: uid(), name: t }
                : { id: t.id || uid(), name: t.name || "Track" },
            )
        : [];
      if (!tracks.length) {
        const names = [
          ...new Set(
            [...(m.ingredients || []), ...(m.unknowns || [])]
              .map(clean)
              .filter(Boolean),
          ),
        ];
        tracks = names.map((name) => ({ id: uid(), name }));
      }
      const usedNames = new Set();
      tracks = tracks.filter((t) => {
        const k = t.name.toLowerCase();
        if (!t.name || usedNames.has(k)) return false;
        usedNames.add(k);
        return true;
      });
      m.tracks = tracks;
      const nameToId = new Map(tracks.map((t) => [t.name, t.id]));
      m.sectionData = m.sectionData || {};
      m.sections.forEach((s) => {
        const existing = m.sectionData[s.id] || {};
        const old = oldAnalysis[s.id] || {};
        m.sectionData[s.id] = {
          feel: {
            ...makeSectionData().feel,
            ...(old.feel || {}),
            ...(existing.feel || {}),
          },
          focusIds: Array.isArray(existing.focusIds)
            ? existing.focusIds.filter((id) => tracks.some((t) => t.id === id))
            : (old.focus || []).map((x) => nameToId.get(x)).filter(Boolean),
          focusState: existing.focusState || old.focusState || "",
          silence: existing.silence ?? old.partsStatus === "silence",
          parking: existing.parking ?? old.parking ?? "",
          takeaway: existing.takeaway ?? old.takeaway ?? "",
        };
        if (m.sectionData[s.id].focusState === "unsure")
          m.sectionData[s.id].focusState = "";
      });
      Object.keys(m.sectionData).forEach((id) => {
        if (!m.sections.some((s) => s.id === id)) delete m.sectionData[id];
      });
      m.timeline = m.timeline || { presence: [], events: [] };
      m.timeline.presence = Array.isArray(m.timeline.presence)
        ? m.timeline.presence
        : [];
      m.timeline.events = Array.isArray(m.timeline.events)
        ? m.timeline.events
        : [];
      if (!m.timeline.presence.length && Object.keys(oldAnalysis).length) {
        tracks.forEach((track) => {
          let runStart = -1;
          for (let i = 0; i <= m.sections.length; i++) {
            const active =
              i < m.sections.length &&
              (oldAnalysis[m.sections[i].id]?.parts || []).includes(track.name);
            if (active && runStart < 0) runStart = i;
            if ((!active || i === m.sections.length) && runStart >= 0) {
              const endIndex = i - 1;
              m.timeline.presence.push({
                id: uid(),
                trackId: track.id,
                start: { sectionId: m.sections[runStart].id, bar: 0 },
                end: { sectionId: m.sections[endIndex].id, bar: "end" },
              });
              runStart = -1;
            }
          }
        });
      }
      if (!m.timeline.events.length && Object.keys(oldTransitions).length) {
        for (let i = 1; i < m.sections.length; i++) {
          const prev = m.sections[i - 1],
            cur = m.sections[i];
          const t = oldTransitions[`${prev.id}→${cur.id}`];
          (t?.changes || []).forEach((c) => {
            if (c.action === "Enters" || c.action === "Leaves") return;
            const trackId = nameToId.get(c.target);
            m.timeline.events.push({
              id: uid(),
              targetType: trackId ? "track" : "mix",
              targetId: trackId || null,
              label: trackId ? c.action : `${c.target} · ${c.action}`,
              kind: "marker",
              point: { sectionId: cur.id, bar: 0 },
            });
          });
        }
      }
      m.timeline.presence = m.timeline.presence
        .filter(
          (r) =>
            tracks.some((t) => t.id === r.trackId) &&
            anchorSectionExists(m, r.start) &&
            (r.end == null || anchorSectionExists(m, r.end)),
        )
        .map((r) => ({
          id: r.id || uid(),
          trackId: r.trackId,
          start: normalizeAnchor(m, r.start, "start"),
          end: r.end == null ? null : normalizeAnchor(m, r.end, "end"),
        }));
      m.timeline.events = m.timeline.events
        .filter(
          (e) =>
            e &&
            e.kind &&
            ((e.kind === "marker" && anchorSectionExists(m, e.point)) ||
              (e.kind === "range" &&
                anchorSectionExists(m, e.start) &&
                (e.end == null || anchorSectionExists(m, e.end)))),
        )
        .map((e) => {
          const label = e.label || e.action || "Change",
            meta = changeMeta(label);
          return {
            id: e.id || uid(),
            targetType: e.targetType === "mix" ? "mix" : "track",
            targetId: e.targetType === "mix" ? null : e.targetId,
            label,
            kind: e.kind || meta.kind,
            group: e.group || meta.group,
            property: e.property || meta.property,
            tone: e.tone || meta.tone,
            point:
              e.kind === "marker"
                ? normalizeAnchor(m, e.point, "start")
                : undefined,
            start:
              e.kind === "range"
                ? normalizeAnchor(m, e.start, "start")
                : undefined,
            end:
              e.kind === "range"
                ? e.end == null
                  ? null
                  : normalizeAnchor(m, e.end, "end")
                : undefined,
          };
        });
      m.structureVerified = !!m.structureVerified;
      m.mapVerified = !!m.mapVerified;
      m.teachBack = !!m.teachBack;
      m.phaseParking = m.phaseParking || "";
      m.phaseTakeaway = m.phaseTakeaway || "";
      if (!m.sections.every((s) => validBars(s.lengthBars))) {
        m.structureVerified = false;
        m.mapVerified = false;
        m.teachBack = false;
      }
      const oldSkeleton = p.skeleton || {};
      const oldSession = oldSkeleton.session || {};
      const oldDraft = oldSkeleton.draft || {};
      const oldRough = oldSkeleton.rough || {};
      const sessionTracks = {};
      tracks.forEach(
        (t) =>
          (sessionTracks[t.id] = !!(
            oldSession.tracks?.[t.id] ?? oldSession.tracks?.[t.name]
          )),
      );
      let markers = {};
      if (typeof oldSession.markers === "boolean") {
        if (oldSession.markers)
          m.sections.forEach((s) => (markers[s.id] = true));
      } else markers = { ...(oldSession.markers || {}) };
      const draftParts = {};
      m.sections.forEach((s) => {
        draftParts[s.id] = {};
        const legacy = oldDraft.parts?.[s.id] || oldRough.parts?.[s.id] || {};
        tracks.forEach(
          (t) => (draftParts[s.id][t.id] = !!(legacy[t.id] ?? legacy[t.name])),
        );
      });
      p.skeleton = {
        session: { tracks: sessionTracks, markers },
        draft: { parts: draftParts },
        bounce: {
          exported: !!(oldSkeleton.bounce?.exported ?? oldRough.bounce),
          listened: !!oldSkeleton.bounce?.listened,
        },
      };
      delete m.ingredients;
      delete m.unknowns;
      delete m.analysis;
      delete m.transitions;
      delete p.guidance;
      p.notes = p.notes || [];
      if (lengthsComplete(p))
        tracks.forEach((t) => mergePresenceForTrack(p, t.id, false));
    });
    if (
      !out.currentProjectId ||
      !out.projects.some((p) => p.id === out.currentProjectId)
    )
      out.currentProjectId = out.projects[0]?.id || null;
    return out;
  }
  function validBars(v) {
    const n = Number(v);
    return Number.isFinite(n) && n >= 1 && n <= 256 && Math.floor(n) === n;
  }
  function anchorSectionExists(m, a) {
    return !!a && m.sections.some((s) => s.id === a.sectionId);
  }
  function normalizeAnchor(m, a, edge) {
    const s = m.sections.find((x) => x.id === a?.sectionId) || m.sections[0];
    if (!s) return { sectionId: "", bar: 0 };
    if (a?.bar === "end") return { sectionId: s.id, bar: "end" };
    const n = Number(a?.bar);
    return {
      sectionId: s.id,
      bar: Number.isFinite(n) ? Math.max(0, n) : edge === "end" ? "end" : 0,
    };
  }
  function persist() {
    try {
      localStorage.setItem(DB_KEY, JSON.stringify(db));
    } catch (e) {}
  }
  db = normalizeDatabase(db);
  persist();

  function save() {
    clearUndo();
    persist();
    clearTimeout(saveFlashTimer);
    document
      .querySelectorAll(".saved")
      .forEach((el) => el.classList.add("show"));
    saveFlashTimer = setTimeout(
      () =>
        document
          .querySelectorAll(".saved")
          .forEach((el) => el.classList.remove("show")),
      650,
    );
  }
  function project() {
    return (
      db.projects.find((p) => p.id === db.currentProjectId) || db.projects[0]
    );
  }
  function routeLabel(route) {
    const labels = {
      projects: "Projects",
      project: project()?.type === "study" ? "Recreation" : "Original Song",
      map: "The Map",
      structure: "Structure",
      tracks: "Tracks",
      "section-study": "Section Study",
      "map-summary": "Review Map",
      skeleton: "The Skeleton",
      "skeleton-session": "Session",
      "skeleton-draft": "Draft",
      "draft-section": "Draft",
      "skeleton-bounce": "Bounce",
      roadmap: "Roadmap",
      notes: "Notes",
      "original-spark": "Original Song",
    };
    return labels[route] || "Back";
  }
  function canonicalState(p) {
    if (!p || p.type !== "study") return null;
    const setup = mapSetupComplete(p), structure = structureDone(p), palette = tracksDone(p),
      study = sectionStudyDone(p), map = mapDone(p), session = sessionDone(p),
      draft = draftDone(p), bounce = bounceDone(p);
    return { setup, structure, palette, study, map, session, draft, bounce,
      eligible: { map: true, structure: setup, tracks: structure,
        "section-study": palette, "map-summary": palette && sectionStudyCoreDone(p),
        skeleton: map, "skeleton-session": map, "skeleton-draft": session,
        "draft-section": session, "skeleton-bounce": draft } };
  }
  function resolveRoute(route, p = project()) {
    if (["projects", "new-project"].includes(route)) return route;
    if (!p) return "projects";
    if (["project", "roadmap", "notes"].includes(route)) return route;
    if (p.type === "original") return route === "original-spark" ? route : "project";
    const state = canonicalState(p);
    if (state.eligible[route]) return route === "draft-section" ? "skeleton-draft" : route;
    if (!(route in state.eligible)) return "roadmap";
    if (!state.setup) return "map";
    if (!state.structure) return "structure";
    if (!state.palette) return "tracks";
    if (!state.map) return "section-study";
    if (!state.session) return "skeleton-session";
    return "skeleton-draft";
  }
  function repairRoute() {
    const route = resolveRoute(ui.route);
    if (ui.route === "draft-section") ui.draftOpenId = sections()[ui.sectionIndex]?.id;
    if (route !== ui.route) {
      ui.route = route;
      history.replaceState({ ...history.state, route }, "", location.pathname + location.search);
    }
  }
  // Live Setup updates replace only derived controls, preserving text/caret/IME.
  function refreshMapProgress() {
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
  let cancelGesture = null;
  function go(route, extra = {}, push = true) {
    cancelGesture?.();
    clearBoundarySelection();
    route = resolveRoute(route);
    ui.animating = false;
    ui.selectedEventId = null;
    ui.selectedPresenceId = null;
    const fromRoute = ui.route,
      fromLabel = routeLabel(fromRoute);
    ui = { ...ui, ...extra, route };
    const state = {
      route,
      ...extra,
      fromRoute,
      fromLabel,
      projectId: db.currentProjectId,
    };
    if (push) {
      try {
        history.pushState(state, "", location.pathname + location.search);
      } catch (e) {}
    } else {
      try {
        history.replaceState(state, "", location.pathname + location.search);
      } catch (e) {}
    }
    render();
    window.scrollTo(0, 0);
  }
  window.addEventListener("popstate", (e) => {
    cancelGesture?.();
    clearBoundarySelection();
    closeSheet();
    const st = e.state || {};
    if (st.projectId && db.projects.some((p) => p.id === st.projectId))
      db.currentProjectId = st.projectId;
    ui = { ...ui, ...st, route: st.route || "projects", animating: false };
    render();
    window.scrollTo(0, 0);
  });
  function initHistory() {
    const st = history.state;
    if (!st?.route) {
      history.replaceState(
        {
          route: "projects",
          projectId: db.currentProjectId,
          fromRoute: null,
          fromLabel: null,
        },
        "",
        location.pathname + location.search,
      );
    } else {
      ui = { ...ui, ...st, route: st.route };
      if (st.projectId && db.projects.some((p) => p.id === st.projectId))
        db.currentProjectId = st.projectId;
    }
  }
  function backButton(target = "project", label = "Back") {
    return historyBackButton(target, label);
  }
  function historyBackButton(
    fallbackRoute = "project",
    fallbackLabel = "Back",
  ) {
    const state = history.state || {},
      label = state.fromRoute ? routeLabel(resolveRoute(state.fromRoute)) : fallbackLabel;
    return `<button class="nav-btn left" data-action="history-back" data-fallback-route="${fallbackRoute}"><span class="arrow">‹</span>${esc(label)}</button>`;
  }
  function topbar(left = "", center = "", right = "") {
    // Canvas size follows content, not the user's device or input method.
    app.dataset.route = ui.route;
    app.dataset.layout = ui.route === "section-study" ? "arrangement"
      : ui.route === "skeleton-draft" ? "draft"
      : ["new-project", "original-spark", "skeleton-bounce", "skeleton"].includes(ui.route) ? "focused" : "overview";
    return `<div class="topbar"><div class="left">${left}</div><div class="center">${center}</div><div class="right">${right}</div></div>`;
  }
  function savedMark() {
    return `<span class="saved">Saved</span>`;
  }
  function phaseTag(text) {
    return `<span class="pill-tag">${esc(text)}</span>`;
  }
  function phasePill(index) {
    const ph = STUDY_PHASES[index];
    return `<button class="phase-pill" data-action="go" data-route="${ph.route}" aria-label="Open ${esc(ph.title)}">${esc(ph.title)}</button>`;
  }
  function progressBar(done, total) {
    const pct = total ? Math.round((done / total) * 100) : 0;
    return `<div class="progress"><span style="width:${pct}%"></span></div><div class="progress-meta"><span>${done} of ${total}</span></div>`;
  }

  function sections(p = project()) {
    return p?.map?.sections || [];
  }
  function tracks(p = project()) {
    return p?.map?.tracks || [];
  }
  function trackById(p, id) {
    return tracks(p).find((t) => t.id === id);
  }
  function sectionIndexById(p, id) {
    return sections(p).findIndex((s) => s.id === id);
  }
  function sectionLabels(p) {
    const counts = {};
    sections(p).forEach((s) => (counts[s.name] = (counts[s.name] || 0) + 1));
    const seen = {};
    return sections(p).map((s) => {
      if (counts[s.name] > 1) {
        seen[s.name] = (seen[s.name] || 0) + 1;
        return `${s.name} ${seen[s.name]}`;
      }
      return s.name;
    });
  }
  function sectionData(p, id) {
    if (!p.map.sectionData[id]) p.map.sectionData[id] = makeSectionData();
    return p.map.sectionData[id];
  }
  function lengthsComplete(p) {
    return (
      sections(p).length > 0 &&
      sections(p).every((s) => !!s.id && !!clean(s.name) && validBars(s.lengthBars))
    );
  }
  function sectionStarts(p) {
    let sum = 0;
    return sections(p).map((s) => {
      const start = sum;
      sum += Number(s.lengthBars) || 0;
      return start;
    });
  }
  function songLength(p) {
    return sections(p).reduce((n, s) => n + (Number(s.lengthBars) || 0), 0);
  }
  function anchorValueInSection(s, a) {
    if (!s) return 0;
    if (a?.bar === "end") return Number(s.lengthBars) || 0;
    return clamp(Number(a?.bar) || 0, 0, Number(s.lengthBars) || 0);
  }
  function anchorAbs(p, a) {
    const i = sectionIndexById(p, a?.sectionId);
    if (i < 0) return NaN;
    const starts = sectionStarts(p),
      s = sections(p)[i];
    return starts[i] + anchorValueInSection(s, a);
  }
  function anchorAtAbs(p, abs, preferPreviousEnd = false) {
    const ss = sections(p),
      starts = sectionStarts(p),
      total = songLength(p);
    abs = clamp(abs, 0, total);
    for (let i = 0; i < ss.length; i++) {
      const start = starts[i],
        end = start + Number(ss[i].lengthBars);
      if (abs < end - 1e-6)
        return { sectionId: ss[i].id, bar: Math.max(0, abs - start) };
      if (Math.abs(abs - end) < 1e-6) {
        if (preferPreviousEnd || i === ss.length - 1)
          return { sectionId: ss[i].id, bar: "end" };
        return { sectionId: ss[i + 1].id, bar: 0 };
      }
    }
    return ss.length
      ? { sectionId: ss[ss.length - 1].id, bar: "end" }
      : { sectionId: "", bar: 0 };
  }
  function rangeAbs(p, r) {
    const start = anchorAbs(p, r.start);
    let end;
    if (r.end != null) end = anchorAbs(p, r.end);
    else if (r.targetType === "track" && r.targetId) {
      const holder = presenceForTrack(p, r.targetId)
        .map((pr) => ({
          pr,
          start: anchorAbs(p, pr.start),
          end: pr.end == null ? songLength(p) : anchorAbs(p, pr.end),
        }))
        .find((x) => start >= x.start - 1e-6 && start < x.end - 1e-6);
      end = holder ? holder.end : songLength(p);
    } else end = songLength(p);
    return { start, end };
  }
  function mergePresenceForTrack(p, trackId, doSave = true) {
    if (!lengthsComplete(p)) return;
    const mine = p.map.timeline.presence
      .filter((r) => r.trackId === trackId)
      .sort((a, b) => anchorAbs(p, a.start) - anchorAbs(p, b.start));
    const other = p.map.timeline.presence.filter((r) => r.trackId !== trackId);
    const merged = [];
    for (const r of mine) {
      const ra = rangeAbs(p, r);
      if (
        !Number.isFinite(ra.start) ||
        !Number.isFinite(ra.end) ||
        ra.end <= ra.start
      )
        continue;
      if (!merged.length) {
        merged.push(r);
        continue;
      }
      const last = merged[merged.length - 1],
        la = rangeAbs(p, last);
      if (ra.start <= la.end + 1e-6) {
        if (last.end == null || r.end == null) last.end = null;
        else if (ra.end > la.end) last.end = r.end;
      } else merged.push(r);
    }
    p.map.timeline.presence = [...other, ...merged];
    if (doSave) save();
  }
  function localSegmentsForRange(p, obj) {
    if (!lengthsComplete(p)) return [obj];
    const a = rangeAbs(p, obj),
      starts = sectionStarts(p),
      out = [];
    sections(p).forEach((sec, i) => {
      const secStart = starts[i],
        secEnd = secStart + Number(sec.lengthBars),
        start = Math.max(a.start, secStart),
        end = Math.min(a.end, secEnd);
      if (end <= start + 1e-6) return;
      const startAnchor = {
        sectionId: sec.id,
        bar: start <= secStart + 1e-6 ? 0 : start - secStart,
      };
      const endAnchor = {
        sectionId: sec.id,
        bar: end >= secEnd - 1e-6 ? "end" : end - secStart,
      };
      out.push({ start: startAnchor, end: endAnchor });
    });
    return out;
  }
  // Preserve musical section coverage before structure mutations. Fragment metadata
  // exists only during this synchronous mutation and is never saved.
  function splitTimelineAtSections(p) {
    if (!lengthsComplete(p)) return;
    const split = (obj) =>
      localSegmentsForRange(p, obj).map((seg, i) => ({
        ...obj,
        id: i === 0 ? obj.id : uid(),
        start: seg.start,
        end: seg.end,
        _sourceId: obj.id,
        _wasOpen: obj.end == null,
      }));
    const presence = p.map.timeline.presence.flatMap(split);
    const events = p.map.timeline.events.flatMap((e) =>
      e.kind === "range" ? split(e) : [e],
    );
    p.map.timeline.presence = presence;
    p.map.timeline.events = events;
  }
  function finalizeTimelineFragments(p, items) {
    const groups = new Map();
    for (const item of items) {
      if (!item._sourceId) continue;
      const key = item._sourceId;
      if (!groups.has(key)) groups.set(key, []);
      groups.get(key).push(item);
    }
    for (const [id, pieces] of groups) {
      pieces.sort((a, b) => anchorAbs(p, a.start) - anchorAbs(p, b.start));
      pieces.forEach((piece, i) => {
        if (i === 0) piece.id = id;
        else if (piece.id === id) piece.id = uid();
      });
      const last = pieces[pieces.length - 1];
      // Only an actual tail stays open. Never spread presence into unrelated
      // sections merely because its former last section moved earlier.
      if (
        last._wasOpen &&
        last.end?.sectionId === sections(p).at(-1)?.id &&
        last.end?.bar === "end"
      )
        last.end = null;
    }
    items.forEach((item) => {
      delete item._sourceId;
      delete item._wasOpen;
    });
  }
  function mergeEventRanges(p) {
    if (!lengthsComplete(p)) return;
    const markers = p.map.timeline.events.filter((e) => e.kind !== "range"),
      ranges = p.map.timeline.events.filter((e) => e.kind === "range"),
      groups = new Map();
    ranges.forEach((e) => {
      const key = [e.targetType, e.targetId || "", e.label].join("|");
      if (!groups.has(key)) groups.set(key, []);
      groups.get(key).push(e);
    });
    const merged = [];
    groups.forEach((items) => {
      items.sort((a, b) => anchorAbs(p, a.start) - anchorAbs(p, b.start));
      items.forEach((e) => {
        const a = rangeAbs(p, e),
          last = merged.length ? merged[merged.length - 1] : null;
        if (
          last &&
          last.__key === [e.targetType, e.targetId || "", e.label].join("|")
        ) {
          const z = rangeAbs(p, last);
          if (a.start <= z.end + 1e-6) {
            if (last.end == null || e.end == null) last.end = null;
            else if (a.end > z.end) last.end = e.end;
            return;
          }
        }
        merged.push({
          ...e,
          __key: [e.targetType, e.targetId || "", e.label].join("|"),
        });
      });
    });
    p.map.timeline.events = [...markers, ...merged.map(({ __key, ...e }) => e)];
  }
  function reconcileTimelineAfterStructureChange(p) {
    p.map.timeline.presence = p.map.timeline.presence.filter(
      (r) =>
        anchorSectionExists(p.map, r.start) &&
        (r.end == null || anchorSectionExists(p.map, r.end)),
    );
    p.map.timeline.events = p.map.timeline.events.filter((e) =>
      e.kind === "marker"
        ? anchorSectionExists(p.map, e.point)
        : anchorSectionExists(p.map, e.start) &&
          (e.end == null || anchorSectionExists(p.map, e.end)),
    );
    finalizeTimelineFragments(p, p.map.timeline.presence);
    finalizeTimelineFragments(p, p.map.timeline.events);
    if (lengthsComplete(p)) {
      tracks(p).forEach((t) => mergePresenceForTrack(p, t.id, false));
      mergeEventRanges(p);
    }
    normalizeAllFocus(p);
  }
  function rangePortion(p, r, index) {
    if (!lengthsComplete(p)) return null;
    const starts = sectionStarts(p),
      s = sections(p)[index],
      secStart = starts[index],
      secEnd = secStart + Number(s.lengthBars),
      a = rangeAbs(p, r),
      openEnd =
        r.end == null &&
        (r.targetType !== "track" ||
          presenceForTrack(p, r.targetId).some(
            (pr) => pr.end == null && a.start >= anchorAbs(p, pr.start),
          ));
    if (!(a.end > secStart + 1e-6 && a.start < secEnd - 1e-6)) return null;
    const visibleStart = Math.max(a.start, secStart),
      visibleEnd = Math.min(a.end, secEnd),
      len = Number(s.lengthBars);
    return {
      left: ((visibleStart - secStart) / len) * 100,
      right: 100 - ((visibleEnd - secStart) / len) * 100,
      continuesIn: a.start < secStart - 1e-6,
      continuesOut: openEnd || a.end > secEnd + 1e-6,
      startHere: a.start >= secStart - 1e-6 && a.start < secEnd - 1e-6,
      endHere: !openEnd && a.end > secStart + 1e-6 && a.end <= secEnd + 1e-6,
      startAbs: a.start,
      endAbs: a.end,
      openEnd,
    };
  }
  function markerPortion(p, e, index) {
    if (!lengthsComplete(p)) return null;
    const starts = sectionStarts(p),
      s = sections(p)[index],
      secStart = starts[index],
      secEnd = secStart + Number(s.lengthBars),
      point = anchorAbs(p, e.point);
    if (point < secStart - 1e-6 || point >= secEnd - 1e-6) return null;
    return {
      left: ((point - secStart) / Number(s.lengthBars)) * 100,
      abs: point,
    };
  }
  function presenceForTrack(p, trackId) {
    return p.map.timeline.presence.filter((r) => r.trackId === trackId);
  }
  function visiblePresence(p, trackId, index) {
    return presenceForTrack(p, trackId)
      .map((r) => ({ range: r, portion: rangePortion(p, r, index) }))
      .filter((x) => x.portion);
  }
  function trackIdsInSection(p, index) {
    return tracks(p)
      .filter((t) => visiblePresence(p, t.id, index).length)
      .map((t) => t.id);
  }
  function eventsForTarget(p, targetType, targetId) {
    return p.map.timeline.events.filter(
      (e) =>
        e.targetType === targetType &&
        (targetType === "mix" || e.targetId === targetId),
    );
  }
  function visibleEvents(p, targetType, targetId, index) {
    return eventsForTarget(p, targetType, targetId)
      .map((e) => ({
        event: e,
        portion:
          e.kind === "range"
            ? rangePortion(p, e, index)
            : markerPortion(p, e, index),
      }))
      .filter((x) => x.portion);
  }
  function trackUsedAnywhere(p, trackId) {
    return presenceForTrack(p, trackId).length > 0;
  }
  function focusName(p, id) {
    return trackById(p, id)?.name || "";
  }
  function feelComplete(d) {
    return Object.keys(FEEL_SCALES).every((k) => FEEL_SCALES[k].includes(d.feel?.[k]));
  }
  function sectionComplete(p, index) {
    const s = sections(p)[index];
    if (!s || !validBars(s.lengthBars)) return false;
    const d = sectionData(p, s.id),
      present = trackIdsInSection(p, index);
    const presenceDone = present.length > 0 || d.silence;
    const focusDone =
      d.focusState === "none" ||
      (d.focusState === "selected" && d.focusIds.length > 0 && d.focusIds.every((id) => present.includes(id)));
    return presenceDone && feelComplete(d) && focusDone && !(present.length && d.silence);
  }
  function structureDone(p) {
    return mapSetupComplete(p) && lengthsComplete(p) && !!p.map.structureVerified;
  }
  function tracksDone(p) {
    return structureDone(p) && tracks(p).length > 0;
  }
  function tracksUsedDone(p) {
    return (
      tracks(p).length > 0 && tracks(p).every((t) => trackUsedAnywhere(p, t.id))
    );
  }
  function sectionStudyCoreDone(p) {
    return (
      sections(p).length > 0 &&
      sections(p).every((_, i) => sectionComplete(p, i))
    );
  }
  function sectionStudyDone(p) {
    return tracksDone(p) && sectionStudyCoreDone(p) && tracksUsedDone(p);
  }
  function mapSetupComplete(p) {
    const s = p.map.setup || {};
    return !!(
      s.reference &&
      /^(?:\d+\.?\d*|\.\d+)$/.test(clean(s.tempo)) && Number.isFinite(Number(s.tempo)) && Number(s.tempo) > 0 &&
      s.meter &&
      s.grid &&
      s.firstListen
    );
  }
  function mapDone(p) {
    return (
      mapSetupComplete(p) &&
      structureDone(p) &&
      tracksDone(p) &&
      sectionStudyDone(p) &&
      p.map.mapVerified &&
      p.map.teachBack
    );
  }
  function sessionDone(p) {
    return (
      mapDone(p) &&
      tracks(p).length > 0 &&
      sections(p).length > 0 &&
      tracks(p).every((t) => p.skeleton.session.tracks[t.id]) &&
      sections(p).every((s) => p.skeleton.session.markers[s.id])
    );
  }
  function draftRequirements(p, index) {
    return trackIdsInSection(p, index);
  }
  function draftSectionDone(p, index) {
    const req = draftRequirements(p, index);
    if (!req.length) return sectionData(p, sections(p)[index].id).silence;
    const state = p.skeleton.draft.parts[sections(p)[index].id] || {};
    return req.every((id) => !!state[id]);
  }
  function draftDone(p) {
    return (
      sessionDone(p) &&
      sections(p).length > 0 &&
      sections(p).every((_, i) => draftSectionDone(p, i))
    );
  }
  function bounceDone(p) {
    return draftDone(p) && !!p.skeleton.bounce.exported && !!p.skeleton.bounce.listened;
  }
  function skeletonDone(p) {
    return sessionDone(p) && draftDone(p) && bounceDone(p);
  }
  function mapCheckpointCount(p) {
    return [structureDone(p), tracksDone(p), sectionStudyDone(p)].filter(
      Boolean,
    ).length;
  }
  function skeletonCheckpointCount(p) {
    return [sessionDone(p), draftDone(p), bounceDone(p)].filter(Boolean).length;
  }
  function currentStudyPhaseIndex(p) {
    if (!mapDone(p)) return 0;
    if (!skeletonDone(p)) return 1;
    return 2;
  }
  function studyPhaseDone(p, index) {
    if (index === 0) return mapDone(p);
    if (index === 1) return skeletonDone(p);
    return false;
  }
  function studyPhaseUnlocked(p, index) {
    return index < 2 && (index === 0 || mapDone(p));
  }
  function studyPhaseStatus(p, i) {
    if (studyPhaseDone(p, i)) return "done";
    if (i >= 2) return "unimplemented";
    if (currentStudyPhaseIndex(p) === i) return "current";
    return studyPhaseUnlocked(p, i) ? "available" : "locked";
  }
  function originalSparkDone(p) {
    return (
      !!(p.spark?.idea?.trim() || p.spark?.starts?.length) &&
      !!(p.spark?.anchor?.trim() || p.spark?.reasons?.length)
    );
  }

  function invalidateMapVerification(p) {
    p.map.mapVerified = false;
    p.map.teachBack = false;
  }
  function invalidateBounce(p) {
    p.skeleton.bounce.exported = false;
    p.skeleton.bounce.listened = false;
  }
  const DRAFT_RELEVANT_CHANGES = new Set([
    "Doubles",
    "Pattern shift",
    "Register shift",
    "Transition cue",
  ]);
  function uniqueSectionIds(ids) {
    return [...new Set((ids || []).filter(Boolean))];
  }
  function sectionIdsForRange(p, r) {
    if (!r) return [];
    if (!lengthsComplete(p))
      return uniqueSectionIds(
        [r.start?.sectionId, r.end?.sectionId].filter(Boolean),
      );
    const a = rangeAbs(p, r),
      starts = sectionStarts(p),
      ids = [];
    sections(p).forEach((s, i) => {
      const z = starts[i] + Number(s.lengthBars);
      if (a.end > starts[i] + 1e-6 && a.start < z - 1e-6) ids.push(s.id);
    });
    return ids;
  }
  function sectionIdsForEvent(p, e) {
    if (!e) return [];
    return e.kind === "marker"
      ? [e.point?.sectionId]
      : sectionIdsForRange(p, e);
  }
  function invalidateDraftTrack(p, trackId, sectionIds) {
    const ids = uniqueSectionIds(sectionIds);
    ids.forEach((sectionId) => {
      const state = p.skeleton.draft.parts?.[sectionId];
      if (state && trackId in state) state[trackId] = false;
    });
    if (ids.length) invalidateBounce(p);
  }
  function invalidateDraftSection(p, sectionId) {
    const state = p.skeleton.draft.parts?.[sectionId];
    if (state) Object.keys(state).forEach((id) => (state[id] = false));
    invalidateBounce(p);
  }
  function invalidateMarkersFrom(p, index) {
    sections(p)
      .slice(Math.max(0, index))
      .forEach((s) => {
        p.skeleton.session.markers[s.id] = false;
      });
    invalidateBounce(p);
  }
  function invalidateStructureVerification(p) {
    p.map.structureVerified = false;
    invalidateMapVerification(p);
  }
  function eventAffectsDraft(e) {
    return (
      !!e && e.targetType === "track" && DRAFT_RELEVANT_CHANGES.has(e.label)
    );
  }
  function invalidateEventDraft(p, e, sectionIds) {
    if (eventAffectsDraft(e)) invalidateDraftTrack(p, e.targetId, sectionIds);
  }
  function cleanupFocusForSection(p, index) {
    const s = sections(p)[index],
      d = sectionData(p, s.id),
      present = new Set(trackIdsInSection(p, index));
    d.focusIds = d.focusIds.filter((id) => present.has(id));
    if (!d.focusIds.length && d.focusState === "selected") d.focusState = "";
    if (present.size) d.silence = false;
    if (d.silence) {
      d.focusIds = [];
      d.focusState = "none";
    }
  }
  function normalizeAllFocus(p) {
    sections(p).forEach((_, i) => cleanupFocusForSection(p, i));
  }

  function render() {
    repairRoute();
    switch (ui.route) {
      case "projects":
        return renderProjects();
      case "new-project":
        return renderNewProject();
      case "roadmap":
        return renderRoadmap();
      case "notes":
        return renderNotes();
      case "map":
        return renderMapHome();
      case "structure":
        return renderStructure();
      case "tracks":
        return renderTracks();
      case "section-study":
        return renderSectionStudy();
      case "map-summary":
        return renderMapSummary();
      case "skeleton":
        return renderSkeletonHome();
      case "skeleton-session":
        return renderSkeletonSession();
      case "skeleton-draft":
        return renderSkeletonDraft();
      case "skeleton-bounce":
        return renderSkeletonBounce();
      case "original-spark":
        return renderOriginalSpark();
      default:
        return renderProject();
    }
  }

  // Pages supplies its deployed revision; the local server supplies Git HEAD.
  let buildCommitRequest;
  function showBuildStamp() {
    buildCommitRequest ||= fetch("build-info.json", { cache: "no-store" })
      .then((response) => {
        if (!response.ok) throw new Error("Build metadata unavailable");
        return response.json();
      })
      .then((info) => {
        if (!/^[0-9a-f]{40}$/i.test(info.commit))
          throw new Error("Invalid build revision");
        return info.commit.slice(0, 7);
      })
      .catch(() => "unavailable");
    buildCommitRequest.then((commit) => {
      const stamp = document.getElementById("buildStamp");
      if (stamp) stamp.textContent = `FIRE V6 DEV · ${commit}`;
    });
  }
  function renderProjects() {
    app.innerHTML =
      `<header class="projects-heading"><div><h1>Projects</h1><p class="sub">Original songs and recreations.</p></div><button class="top-icon-btn" data-action="new-project" aria-label="New project"><span aria-hidden="true">+</span></button></header><div class="projects-grid">${
        db.projects.length
          ? db.projects
              .map((p) => {
                const phase =
                  p.type === "study"
                    ? STUDY_PHASES[currentStudyPhaseIndex(p)].title
                    : originalSparkDone(p)
                      ? "The Direction"
                      : "The Spark";
                return `<div class="project-card"><button class="project-open" data-action="open-project" data-id="${p.id}"><div class="type">${p.type === "study" ? "Recreation" : "Original Song"}</div><strong>${esc(p.title)}</strong>${p.artist ? `<div class="artist">${esc(p.artist)}</div>` : ""}<div class="foot"><span>${esc(phase)}</span><span aria-hidden="true">›</span></div></button><button class="project-menu" data-action="project-menu" data-id="${p.id}" aria-label="Project options">…</button></div>`;
              })
              .join("")
          : ""
      }</div><footer id="buildStamp" class="build-stamp">FIRE V6 DEV · …</footer>`;
    showBuildStamp();
  }
  function renderProject() {
    const p = project();
    if (!p) return go("projects", {}, false);
    if (p.type === "original") return renderOriginalOverview();
    const phaseIndex = currentStudyPhaseIndex(p),
      phase = STUDY_PHASES[phaseIndex],
      done =
        phaseIndex === 0
          ? mapCheckpointCount(p)
          : phaseIndex === 1
            ? skeletonCheckpointCount(p)
            : 0,
      next = STUDY_PHASES[phaseIndex + 1];
    app.innerHTML =
      topbar(
        `<button class="nav-btn" data-action="go" data-route="projects"><span class="arrow">‹</span>Projects</button>`,
        phaseTag("Recreation"),
        `<button class="text-btn" data-action="settings">•••</button>`,
      ) +
      `<div class="eyebrow">${esc(p.artist || "Recreation")}</div><h1>${esc(p.title)}</h1><div class="spacer-18"></div><div class="project-overview"><section class="project-current"><div class="hero-card"><div class="phase-line"><div><div class="eyebrow" style="margin:0 0 6px">Current Phase</div><h3>${esc(phase.title)}</h3></div><div class="phase-num">Phase ${phaseIndex + 1} of 7</div></div><p class="sub">${esc(phase.desc)}</p>${progressBar(phaseIndex, 7).replace(/<div class="progress-meta">.*?<\/div>/, "")}<div class="spacer-18"></div><button class="primary full" data-action="go" data-route="${phase.route}">${phaseIndex === 0 ? (mapCheckpointCount(p) ? "Continue The Map" : "Start The Map") : phaseIndex === 1 ? (skeletonCheckpointCount(p) ? "Continue The Skeleton" : "Start The Skeleton") : "View Roadmap"}</button></div></section><section class="project-support">${next ? `<div class="section-kicker">Next</div><div class="group-card list"><div class="list-row static no-status"><div><div class="title">${esc(next.title)}</div><div class="desc">${esc(next.desc)}</div></div></div></div>` : ""}<div class="section-kicker">Project</div><div class="quick-grid"><button class="quick-card" data-action="go" data-route="roadmap"><strong>Roadmap</strong><span>Seven phases to a finished rebuild.</span></button><button class="quick-card" data-action="go" data-route="notes"><strong>Notes</strong><span>Questions and takeaways.</span></button></div></section></div>`;
  }
  function renderOriginalOverview() {
    const p = project(),
      done = originalSparkDone(p);
    app.innerHTML =
      topbar(
        `<button class="nav-btn" data-action="go" data-route="projects"><span class="arrow">‹</span>Projects</button>`,
        phaseTag("Original Song"),
        `<button class="text-btn" data-action="settings">•••</button>`,
      ) +
      `<h1>${esc(p.title)}</h1><p class="sub">Take anything worth keeping and turn it into a finished record.</p><div class="spacer-24"></div><div class="hero-card"><div class="phase-line"><div><div class="eyebrow" style="margin:0 0 6px">Current Phase</div><h3>The Spark</h3></div><div class="phase-num">Phase 1 of 7</div></div><p class="sub">Capture the thing worth making before you overthink it.</p>${progressBar(done ? 1 : 0, 1)}<div class="spacer-18"></div><button class="primary full" data-action="go" data-route="original-spark">${done ? "Open The Spark" : "Start The Spark"}</button></div>`;
  }
  function renderNewProject() {
    app.innerHTML =
      topbar(backButton("projects", "Projects"), "", "") +
      `<h2>New project</h2><p class="sub">Start original or rebuild a reference.</p><div class="spacer-24"></div><div class="project-type-control" role="group" aria-label="Project type"><button class="segment-choice ${ui.newType === "original" ? "selected" : ""}" data-action="set-new-type" data-type="original" aria-pressed="${ui.newType === "original"}">Original</button><button class="segment-choice ${ui.newType === "study" ? "selected" : ""}" data-action="set-new-type" data-type="study" aria-pressed="${ui.newType === "study"}">Recreation</button></div><div class="section-kicker project-field-label">Project</div><input class="field" id="newTitle" aria-label="Song title" enterkeyhint="next" autocomplete="off" autocapitalize="words" placeholder="Song title"><input class="field custom-length" id="newArtist" aria-label="Artist" enterkeyhint="done" autocomplete="off" autocapitalize="words" placeholder="Artist"><div class="spacer-24"></div><button class="primary full" data-action="create-project">Create Project</button>`;
  }

  function checkpointRow(title, desc, route, done, unlocked = true) {
    return `<button class="list-row" data-action="go" data-route="${route}" ${unlocked ? "" : "disabled"}>${done ? `<span class="round-check on"></span>` : unlocked ? `<span class="status-dot"></span>` : `<span class="lock-dot">•</span>`}<div><div class="title">${esc(title)}</div><div class="desc">${esc(desc)}</div></div><span class="chev">${unlocked ? "›" : ""}</span></button>`;
  }
  function actionCard(title, copy, on, action, disabled = false, attrs = "") {
    return `<button class="action-card ${on ? "on" : ""}" data-action="${action}" aria-pressed="${!!on}" ${attrs} ${disabled ? "disabled" : ""}><div><strong>${esc(title)}</strong>${copy ? `<span class="copy">${esc(copy)}</span>` : ""}</div><span class="round-check ${on ? "on" : ""}"></span></button>`;
  }
  function phaseHome(index, done, total, checkpointsHtml, beforeHtml = "") {
    const pct = total ? Math.round((done / total) * 100) : 0;
    return (
      topbar(
        backButton("project", "Recreation"),
        `<button class="phase-pill" data-action="go" data-route="project">Recreation</button>`,
        savedMark(),
      ) +
      `<h2>${STUDY_PHASES[index].title}</h2><div class="phase-layout ${beforeHtml ? "with-setup" : ""}">${beforeHtml ? `<section class="phase-setup">${beforeHtml}</section>` : ""}<section class="phase-checkpoints"><div class="checkpoint-head"><div class="section-kicker">Checkpoints</div><span class="checkpoint-count">${done} of ${total}</span></div><div class="progress checkpoint-progress"><span style="width:${pct}%"></span></div><div class="group-card list">${checkpointsHtml}</div></section></div>`
    );
  }
  function renderMapHome() {
    const p = project(),
      m = p.map,
      done = mapCheckpointCount(p),
      setupDone = mapSetupComplete(p),
      structureUnlocked = setupDone,
      tracksUnlocked = structureDone(p),
      studyUnlocked = tracksDone(p),
      studyRoute = sectionStudyCoreDone(p) ? "map-summary" : "section-study";
    const setup = `<div class="section-kicker">Song Setup</div><div class="group-card setup-panel"><div class="setup-row"><div class="setup-label">Reference</div><button class="state-control ${m.setup.reference ? "on" : ""}" data-action="toggle-setup" data-field="reference"><span>${m.setup.reference ? "Imported" : "Import"}</span><span class="check-circle"></span></button></div><div class="setup-row"><div class="setup-label">Tempo</div><div class="setup-value"><input id="tempoInput" aria-label="Tempo in BPM" inputmode="decimal" value="${esc(m.setup.tempo)}" placeholder="—"><span class="suffix">BPM</span></div></div><div class="setup-row"><div class="setup-label">Meter</div><div class="setup-value"><select id="meterInput" aria-label="Meter">${["4/4", "3/4", "6/8", "5/4", "7/8"].map((x) => `<option ${m.setup.meter === x ? "selected" : ""}>${x}</option>`).join("")}</select></div></div><div class="setup-row"><div class="setup-label">Grid</div><button class="state-control ${m.setup.grid ? "on" : ""}" data-action="toggle-setup" data-field="grid"><span>${m.setup.grid ? "Aligned" : "Align"}</span><span class="check-circle"></span></button></div></div><div class="spacer-18"></div>${actionCard("First Listen", "Play the full song once without stopping.", m.setup.firstListen, "toggle-setup", false, 'data-field="firstListen"')}`;
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
    app.innerHTML = phaseHome(0, done, 3, checkpoints, setup);
  }

  function renderStructure() {
    const p = project(),
      labels = sectionLabels(p),
      done = structureDone(p);
    app.innerHTML =
      topbar(historyBackButton("map", "The Map"), phasePill(0), savedMark()) +
      `<div class="work-position">1 of 3</div><h2>Structure</h2><p class="sub">Build the song one section at a time.</p><div class="section-kicker">Structure</div><div class="structure-list" id="sortList">${
        sections(p).length
          ? sections(p)
              .map(
                (s, i) =>
                  `<div class="structure-row sort-row" role="button" tabindex="0" data-action="edit-section" data-section-id="${s.id}"><div class="index">${i + 1}</div><div class="name">${esc(labels[i])}</div><span class="bars-badge">${s.lengthBars} bars</span><button class="delete-section" data-action="delete-section" data-id="${s.id}" aria-label="Delete ${esc(labels[i])}"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 7h16M9 7V4h6v3M7 7l1 13h8l1-13M10 10v7M14 10v7"/></svg></button><div class="drag-handle" data-drag-handle role="button" tabindex="0" aria-label="Reorder ${esc(labels[i])}">≡</div></div>`,
              )
              .join("")
          : `<div class="empty">No sections yet.</div>`
      }</div><button class="add-section-row" data-action="open-add-section">+ Add section</button><div class="section-kicker">Verify</div>${actionCard("Verify structure", "Confirm the order, lengths, and boundaries.", p.map.structureVerified, "toggle-structure-verified", !lengthsComplete(p))}<div class="spacer-24"></div><button class="primary full" data-action="go" data-route="tracks" ${done ? "" : "disabled"}>Next</button>`;
    installSorting();
  }
  function renderTracks() {
    const p = project(),
      selectedNames = new Set(tracks(p).map((t) => t.name)),
      custom = tracks(p).filter((t) => !COMMON_TRACKS.includes(t.name)),
      choices = [...COMMON_TRACKS, ...custom.map((t) => t.name)];
    app.innerHTML =
      topbar(historyBackButton("map", "The Map"), phasePill(0), savedMark()) +
      `<div class="work-position">2 of 3</div><h2>Tracks</h2><p class="sub">Select everything that appears somewhere in the song.</p><div class="section-kicker">Tracks</div><div class="choice-wrap">${choices.map((name) => `<button class="choice ${selectedNames.has(name) ? "selected" : ""}" data-action="toggle-track-choice" data-name="${esc(name)}" aria-pressed="${selectedNames.has(name)}">${esc(name)}</button>`).join("")}</div><div class="inline-add"><input aria-label="Custom track name" class="field" id="customTrack" placeholder="Other..."><button class="secondary" data-action="add-custom-track">Add</button></div><div class="spacer-24"></div><button class="primary full" data-action="start-section-study" ${tracksDone(p) ? "" : "disabled"}>Next</button>`;
  }

  function rulerHtml(bars) {
    const step = bars > 16 ? 1 : Math.max(1, 2 ** Math.ceil(Math.log2(bars / 12))),
      labels = [];
    for (let i = 0; i < bars; i += step)
      labels.push(
        `<span class="ruler-label ${i === 0 ? "first" : ""}" style="left:${(i / bars) * 100}%">${i + 1}</span>`,
      );
    return labels.join("");
  }
  function timingSummary(p, trackId, index) {
    const pieces = visiblePresence(p, trackId, index);
    if (!pieces.length) return "Not present";
    const len = Number(sections(p)[index].lengthBars),
      x = pieces[0].portion;
    const startBar = Math.floor((x.left / 100) * len) + 1,
      endBar = Math.round(((100 - x.right) / 100) * len);
    if (pieces.length > 1) return "Stops and resumes";
    if (x.continuesIn && x.continuesOut) return "Continues through";
    if (x.left < 0.01 && x.right < 0.01) return "Full section";
    if (x.continuesIn) return `Continues · through bar ${endBar}`;
    if (x.continuesOut) return `Starts bar ${startBar} · continues`;
    return startBar === endBar
      ? `Bar ${startBar}`
      : `Bars ${startBar}–${endBar}`;
  }
  function presenceSegmentHtml(p, item, index, expanded) {
    const { range: r, portion: x } = item,
      selected =
        expanded && ui.selectedPresenceId === r.id && !ui.selectedEventId;
    return `<div data-graphic="${r.id}" class="presence-segment ${x.continuesIn ? "continue-in" : "real-start"} ${x.continuesOut ? "continue-out" : "real-stop"} ${selected ? "selected" : ""}" style="left:${x.left}%;right:${x.right}%"></div><button class="presence-hit" tabindex="0" data-action="select-presence" data-track-id="${r.trackId}" data-range-id="${r.id}" style="left:${x.left}%;width:${100 - x.left - x.right}%" aria-label="Select ${esc(trackById(p, r.trackId)?.name)} block"></button>${selected ? rangeHandles(r.id, "presence", x) : ""}`;
  }
  function boundaryLabel(edge, value) {
    if(edge === "end") return value === 0 ? "Stop before bar 1" : `Stop after bar ${value}`;
    if(value === Number(sections()[ui.sectionIndex].lengthBars)) return `After bar ${value}`;
    return `${edge === "point" ? "Change at" : "Start at"} bar ${value + 1}`;
  }
  function rangeHandles(id, type, x) {
    const p = project(), obj = selectedObject(type,id), len = Number(sections(p)[ui.sectionIndex].lengthBars);
    return ["start","end"].filter(edge=> edge === "start" ? x.startHere : x.endHere || x.openEnd).map(edge=>{
      const open = edge === "end" && x.openEnd, value = Math.round((edge === "start" ? x.left : 100-x.right)/100*len);
      return `<button class="${type}-handle ${edge === "start" ? "left" : "right"} ${open ? "open-continuation" : ""}" data-${type}-handle data-${type === "presence" ? "range" : "event"}-id="${id}" data-edge="${edge}" ${open ? 'data-open-tail' : ''} style="left:${edge === "start" ? x.left : 100-x.right}%" aria-label="${esc(type === "presence" ? trackById(p,obj.trackId).name : obj.label)}, ${open ? `Open continuation after bar ${value}; set stop` : boundaryLabel(edge,value)}" aria-pressed="false"></button>`;
    }).join("");
  }
  function eventDetailRows(p, targetType, targetId, index) {
    if (targetType === "track" && !visiblePresence(p, targetId, index).length) return "";
    const selected = visibleEvents(p, targetType, targetId, index).find((x) => x.event.id === ui.selectedEventId);
    return `<div class="selection-actions"><button class="mini-btn" data-action="open-add-change" data-target-type="${targetType}" ${targetId ? `data-target-id="${targetId}"` : ""}>+ Change</button>${selected ? `<button class="mini-btn remove" data-action="remove-selected" data-kind="event" data-id="${selected.event.id}" aria-label="Remove ${esc(selected.event.label)}">Remove</button>` : ""}</div>`;
  }
  function trackDetailHtml(p, track, index) {
    const r = visiblePresence(p, track.id, index).find((x) => x.range.id === ui.selectedPresenceId)?.range;
    if(!visiblePresence(p,track.id,index).length)return "";
    return `<div class="track-detail">${r && !ui.selectedEventId ? `<button class="mini-btn remove" data-action="remove-selected" data-kind="presence" data-id="${r.id}" aria-label="Remove ${esc(track.name)} block">Remove</button>` : ""}${eventDetailRows(p, "track", track.id, index)}</div>`;
  }
  function alignedEventsHtml(p, targetType, targetId, index) {
    return visibleEvents(p, targetType, targetId, index).map(({event:e, portion:x}, i) => {
      const selected = e.id === ui.selectedEventId;
      return `<div class="event-line ${selected ? "selected" : ""}" data-event-line="${e.id}" style="top:${64 + i * 44}px;--event-color:${eventColorVar(e)}"><span class="event-label">${esc(e.label)}</span>${e.kind === "marker" ? `<button class="change-marker" data-event-marker data-action="select-event" data-event-id="${e.id}" data-edge="point" style="left:${x.left}%" aria-label="${esc(e.label)}, ${boundaryLabel("point", Math.round(x.left / 100 * Number(sections(p)[index].lengthBars)))}"></button>` : `<div data-graphic="${e.id}" class="change-range ${x.continuesIn ? "continue-in" : "real-start"} ${x.continuesOut ? "continue-out" : "real-stop"} ${selected ? "selected" : ""}" style="left:${x.left}%;right:${x.right}%"></div><button class="event-hit" data-action="select-event" data-event-id="${e.id}" style="left:${x.left}%;width:${100-x.left-x.right}%" aria-label="Select ${esc(e.label)}"></button>${selected ? rangeHandles(e.id, "event", x) : ""}`}</div>`;
    }).join("");
  }
  function presenceLaneHtml(p, track, index, expanded) {
    const bars = Number(sections(p)[index].lengthBars);
    return `<button class="lane-input" data-presence-surface data-track-id="${track.id}" aria-label="Start or resume ${esc(track.name)}; use arrow keys to choose a bar"></button>${visiblePresence(p,track.id,index).map(item=>presenceSegmentHtml(p,item,index,expanded)).join("")}<span class="snap-guide" hidden></span>${alignedEventsHtml(p,"track",track.id,index)}`;
  }
  function transitionIntent(p, trackId, boundary) {
    const base = sectionStarts(p)[ui.sectionIndex], len = Number(sections(p)[ui.sectionIndex].lengthBars), abs = base + boundary;
    const spans = presenceForTrack(p, trackId).map((range) => ({ range, ...rangeAbs(p, range) })).sort((a, b) => a.start - b.start);
    const edge = spans.find((a) => Math.abs(a.start - abs) < 1e-6);
    if (edge) return { action: "none", label: "Existing boundary · drag the handle to move it" };
    const inside = spans.find((a) => a.start < abs && a.end > abs);
    if (inside) return { action: "none" };
    if (abs >= songLength(p)) return { action: "none", label: "End of song" };
    const next = spans.find((a) => a.start > abs), resume = spans.some((a) => a.end <= abs);
    return { action: "start", range: next?.range, abs, label: `${resume ? "Resume" : "Start"} ${boundary === len ? "in the next section" : `at bar ${boundary + 1}`}` };
  }
  function commitPresenceTransition(trackId, boundary) {
    const p = project(), intent = transitionIntent(p, trackId, boundary);
    if (intent.action === "none") return false;
    const before = copyProject();
    let range = intent.range;
    if (range) {
      // Starting inside an existing gap extends its next piece backwards. Its stop
      // and every later gap/re-entry remain intact; retain that piece's identity.
      range.start = anchorAtAbs(p, intent.abs);
    } else {
      range = { id: uid(), trackId, start: anchorAtAbs(p, intent.abs), end: null };
      p.map.timeline.presence.push(range);
    }
    ui.expandedTrackId = trackId;
    ui.selectedPresenceId = range.id;
    ui.selectedEventId = null;
    finishTimelineEdit(before, range, "presence", intent.label);
    return true;
  }
  function timelineTrackRow(p, track, index) {
    const bars = Number(sections(p)[index].lengthBars),
      ranges = visiblePresence(p, track.id, index),
      expanded = ui.expandedTrackId === track.id,
      absent = !ranges.length;
    const eventHeight = visibleEvents(p,"track",track.id,index).length * 44;
    return `<div class="timeline-row ${expanded ? "expanded" : ""} ${absent ? "absent" : ""}" data-track-row="${track.id}"><button class="timeline-label" data-action="toggle-timeline-track" data-track-id="${track.id}" aria-expanded="${expanded}"><strong>${esc(track.name)}</strong></button><div class="timeline-lane" style="--bars:${bars};min-height:${64+eventHeight}px">${presenceLaneHtml(p, track, index, expanded)}</div>${expanded ? trackDetailHtml(p, track, index) : ""}</div>`;
  }
  function refreshArrangement() {
    cancelGesture?.();
    clearBoundarySelection();
    const p = project(), index = ui.sectionIndex, active = document.activeElement;
    const focusData = active?.dataset ? { ...active.dataset } : null;
    app.querySelectorAll("[data-track-row]").forEach((row) => {
      const track = trackById(p, row.dataset.trackRow), expanded = ui.expandedTrackId === track.id,
        ranges = visiblePresence(p, track.id, index), lane = row.querySelector(".timeline-lane");
      row.classList.toggle("expanded", expanded);
      row.querySelector(".timeline-label").setAttribute("aria-expanded", String(expanded));
      // The label/row and all unrelated Feel/Focus/Notes nodes survive selection.
      lane.innerHTML = presenceLaneHtml(p, track, index, expanded);
      lane.style.minHeight = `${64 + visibleEvents(p,"track",track.id,index).length*44}px`;
      row.querySelector(".track-detail")?.remove();
      if (expanded) row.insertAdjacentHTML("beforeend", trackDetailHtml(p, track, index));
    });
    app.querySelector(".mix-utility")?.remove();
    app.querySelector(".timeline-content").insertAdjacentHTML("beforeend", mixTimelineRow(p, index));
    const mix = app.querySelector(".mix-toggle");
    mix.setAttribute("aria-expanded", String(ui.expandedTrackId === "__mix__"));
    installTimelineInteractions();
    if (focusData && !active.isConnected) {
      const match = [...app.querySelectorAll("button")].find((el) => Object.entries(focusData).every(([key, value]) => el.dataset[key] === value));
      match?.focus({ preventScroll: true });
    }
  }
  function mixControl(p, index) {
    const expanded = ui.expandedTrackId === "__mix__";
    return `<button class="mix-toggle" data-action="toggle-timeline-track" data-track-id="__mix__" aria-expanded="${expanded}" aria-label="Mix changes">Mix${visibleEvents(p, "mix", null, index).length ? " •" : ""}</button>`;
  }
  function mixTimelineRow(p, index) {
    const events = visibleEvents(p, "mix", null, index), expanded = ui.expandedTrackId === "__mix__";
    if (!events.length) return expanded ? `<div class="mix-utility">${eventDetailRows(p,"mix",null,index)}</div>` : "";
    return `<div class="mix-utility timeline-row" aria-label="Mix changes"><span class="timeline-label">Mix</span><div class="timeline-lane" style="min-height:${64+events.length*44}px;--bars:${sections(p)[index].lengthBars}">${alignedEventsHtml(p,"mix",null,index)}<span class="snap-guide" hidden></span></div>${expanded ? `<div class="track-detail">${eventDetailRows(p,"mix",null,index)}</div>` : ""}</div>`;
  }
  function sectionStudyPaneHtml(p, index) {
    const s = sections(p)[index],
      labels = sectionLabels(p),
      d = sectionData(p, s.id),
      presentIds = trackIdsInSection(p, index),
      focusOptions = presentIds.map((id) => trackById(p, id)).filter(Boolean),
      done = sectionComplete(p, index);
    return `<div class="study-pane"><div class="work-position">Section Study · ${index + 1} of ${sections(p).length}</div><h2>${esc(labels[index])}</h2><p class="sub">${s.lengthBars} bars</p><div class="study-workspace"><section class="arrangement-region" aria-label="Arrangement"><div class="timeline-card"><div class="timeline-head"><strong>Arrangement</strong>${mixControl(p, index)}</div><div class="timeline-scroll" tabindex="0" aria-label="Section timeline"><div class="timeline-content" style="--dense-width:${Number(s.lengthBars)>16 ? 168+Number(s.lengthBars)*44 : 0}px"><div class="ruler-gutter" aria-hidden="true"></div><div class="timeline-ruler">${rulerHtml(Number(s.lengthBars))}</div>${tracks(
      p,
    )
      .map((t) => timelineTrackRow(p, t, index))
      .join(
        "",
      )}${mixTimelineRow(p, index)}</div></div></div>${!presentIds.length ? `<div class="spacer-12"></div><button class="choice quiet ${d.silence ? "selected" : ""}" data-action="toggle-section-silence">No active tracks</button>` : ""}</section><aside class="study-observations" aria-label="Section observations"><div class="study-block"><div class="block-head"><strong>Feel</strong></div><div class="segment-stack">${Object.keys(
      FEEL_SCALES,
    )
      .map((k) => renderScale(k, d))
      .join(
        "",
      )}</div></div><div class="study-block"><div class="block-head"><strong>Focus</strong></div><div class="choice-wrap">${focusOptions.map((t) => `<button class="choice ${d.focusIds.includes(t.id) ? "selected" : ""}" data-action="toggle-focus" data-track-id="${t.id}" aria-pressed="${d.focusIds.includes(t.id)}">${esc(t.name)}</button>`).join("")}</div><div class="spacer-8"></div><button class="choice quiet ${d.focusState === "none" ? "selected" : ""}" data-action="focus-none" aria-pressed="${d.focusState === "none"}">No clear focus</button></div><details class="note-disclosure"><summary>Notes</summary><div class="note-grid"><div><label>Parking Lot</label><textarea class="textarea" data-input="section-parking" placeholder="Question or mystery for later">${esc(d.parking)}</textarea></div><div><label>Takeaway</label><textarea class="textarea" data-input="section-takeaway" placeholder="Something worth remembering">${esc(d.takeaway)}</textarea></div></div></details></aside></div><div class="action-row study-actions"><button class="secondary" data-action="prev-section" ${index === 0 ? "disabled" : ""}>Previous</button><button class="primary" data-action="next-section" ${done ? "" : "disabled"}>${index === sections(p).length - 1 ? "Review Map" : "Next"}</button></div></div>`;
  }
  function renderScale(key, d) {
    const value = d.feel?.[key];
    return `<div class="scale-row"><div class="scale-label">${FEEL_LABELS[key]}</div><div class="segmented">${FEEL_SCALES[key].map((opt) => `<button class="segment ${value === opt ? "selected" : ""}" data-action="set-feel" data-scale="${key}" data-value="${opt}" aria-pressed="${value === opt}">${opt}</button>`).join("")}</div></div>`;
  }
  function renderSectionStudy() {
    cancelGesture?.();
    clearBoundarySelection();
    const p = project();
    if (!structureDone(p) || !tracksDone(p)) {
      app.innerHTML =
        topbar(historyBackButton("map", "The Map"), phasePill(0), savedMark()) +
        `<h2>Section Study</h2><p class="sub">Finish Structure and Tracks first.</p>`;
      return;
    }
    ui.sectionIndex = clamp(ui.sectionIndex, 0, sections(p).length - 1);
    const firstIncomplete = sections(p).findIndex((_, i) => !sectionComplete(p, i));
    if (firstIncomplete >= 0) ui.sectionIndex = Math.min(ui.sectionIndex, firstIncomplete);
    const labels = sectionLabels(p);
    app.innerHTML =
      topbar(
        historyBackButton("map", "The Map"),
        phasePill(0),
        savedMark(),
      ) +
      `<div class="horizontal-nav">${sections(p)
        .map((s, i) => {
          const unlocked =
            i === 0 ||
            sections(p)
              .slice(0, i)
              .every((_, j) => sectionComplete(p, j));
          return `<button class="section-tab ${i === ui.sectionIndex ? "current" : ""} ${sectionComplete(p, i) ? "done" : ""}" data-action="jump-section" data-index="${i}" ${unlocked ? "" : "disabled"}>${esc(labels[i])}</button>`;
        })
        .join(
          "",
        )}</div><div class="spacer-12"></div><div class="study-viewport"><div class="study-single">${sectionStudyPaneHtml(p, ui.sectionIndex)}</div></div>`;
    installTimelineInteractions();
  }
  function animateSectionTo(newIndex) {
    cancelGesture?.();
    clearBoundarySelection();
    ui.selectedEventId = null;
    ui.selectedPresenceId = null;
    const p = project();
    newIndex = clamp(newIndex, 0, sections(p).length - 1);
    if (!tracksDone(p) || sections(p).slice(0, newIndex).some((_, i) => !sectionComplete(p, i))) return;
    if (newIndex === ui.sectionIndex || ui.animating) return;
    if (matchMedia("(prefers-reduced-motion: reduce)").matches) {
      ui.sectionIndex = newIndex;
      ui.expandedTrackId = null;
      return renderSectionStudy();
    }
    ui.expandedTrackId = null;
    renderSectionStudy();
    const viewport = app.querySelector(".study-viewport"),
      current = viewport?.querySelector(".study-pane");
    if (!viewport || !current) {
      ui.sectionIndex = newIndex;
      return renderSectionStudy();
    }
    ui.animating = true;
    const entry = history.state;
    const forward = newIndex > ui.sectionIndex,
      stage = document.createElement("div");
    stage.className = "study-transition-stage";
    const incoming = document.createElement("div");
    incoming.innerHTML = sectionStudyPaneHtml(p, newIndex);
    const newPane = incoming.firstElementChild,
      oldPane = current.cloneNode(true);
    viewport.innerHTML = "";
    if (forward) {
      stage.append(oldPane, newPane);
      stage.style.transform = "translateX(0)";
    } else {
      stage.append(newPane, oldPane);
      stage.style.transform = "translateX(-50%)";
    }
    viewport.append(stage);
    requestAnimationFrame(() =>
      requestAnimationFrame(
        () =>
          (stage.style.transform = forward
            ? "translateX(-50%)"
            : "translateX(0)"),
      ),
    );
    setTimeout(() => {
      if (ui.route !== "section-study" || history.state !== entry) { ui.animating = false; return; }
      ui.sectionIndex = newIndex;
      ui.expandedTrackId = null;
      ui.animating = false;
      renderSectionStudy();
    }, 360);
  }

  function renderMapSummary() {
    const p = project(),
      labels = sectionLabels(p),
      unused = tracks(p).filter((t) => !trackUsedAnywhere(p, t.id));
    app.innerHTML =
      topbar(historyBackButton("map", "The Map"), phasePill(0), savedMark()) +
      `<h2>Review Map</h2><p class="sub">Listen once more and fix anything that doesn’t match.</p><div class="section-kicker">Structure</div><div class="chip-list">${sections(
        p,
      )
        .map(
          (s, i) =>
            `<span class="chip">${esc(labels[i])} · ${s.lengthBars} bars</span>`,
        )
        .join(
          "",
        )}</div><div class="section-kicker">Tracks</div><div class="chip-list">${tracks(
        p,
      )
        .map((t) => `<span class="chip">${esc(t.name)}</span>`)
        .join(
          "",
        )}</div>${unused.length ? `<div class="spacer-18"></div><button class="warning-card" data-action="go" data-route="tracks" style="width:100%;text-align:left"><strong>Unused tracks</strong><p>${esc(unused.map((t) => t.name).join(" · "))} ${unused.length === 1 ? "does" : "do"} not appear in any section.</p></button>` : ""}<div class="section-kicker">Sections</div><div class="review-sections">${sections(
        p,
      )
        .map((s, i) => renderSummaryCard(p, i, labels[i]))
        .join(
          "",
        )}</div><details class="note-disclosure"><summary>Notes</summary><div class="note-grid"><div><label>Parking Lot</label><textarea class="textarea" data-input="phase-parking">${esc(p.map.phaseParking)}</textarea></div><div><label>Takeaway</label><textarea class="textarea" data-input="phase-takeaway">${esc(p.map.phaseTakeaway)}</textarea></div></div></details><div class="section-kicker">Verify</div>${actionCard("Map verified", "Listen once more with the finished map.", p.map.mapVerified, "toggle-map-verified", !sectionStudyDone(p))}${actionCard("Teach it back", "Explain the map in your own words.", p.map.teachBack, "toggle-teach-back", !p.map.mapVerified)}<div class="spacer-24"></div><button class="primary full" data-action="go" data-route="skeleton" ${mapDone(p) ? "" : "disabled"}>Continue to The Skeleton</button>`;
  }
  function renderSummaryCard(p, index, label) {
    const s = sections(p)[index],
      d = sectionData(p, s.id),
      ids = trackIdsInSection(p, index),
      names = ids.map((id) => focusName(p, id)),
      eventCount = p.map.timeline.events
        .filter((e) => e.targetType === "mix" || ids.includes(e.targetId))
        .filter((e) =>
          e.kind === "range"
            ? rangePortion(p, e, index)
            : markerPortion(p, e, index),
        ).length,
      feel = Object.keys(FEEL_SCALES)
        .map((k) => d.feel[k])
        .filter(Boolean)
        .join(" · "),
      focus =
        d.focusState === "none"
          ? "No clear focus"
          : d.focusIds
              .map((id) => focusName(p, id))
              .filter(Boolean)
              .join(" · ");
    return `<details class="workflow-disclosure"><summary><span class="summary-copy"><strong>${esc(label)}</strong><span class="micro">${s.lengthBars} bars · ${esc(names.join(" · ") || "No active tracks")}</span></span><span class="chev">⌄</span></summary><button class="mini-btn" data-action="summary-jump" data-index="${index}">Edit ${esc(label)}</button><div class="summary-lines"><div class="summary-line"><b>Length</b><span>${s.lengthBars} bars</span></div><div class="summary-line"><b>Tracks</b><span>${d.silence ? "No active tracks" : esc(names.join(" · ") || "Not mapped")}</span></div><div class="summary-line"><b>Changes</b><span>${eventCount ? `${eventCount} mapped` : "None mapped"}</span></div><div class="summary-line"><b>Feel</b><span>${esc(feel || "Not mapped")}</span></div><div class="summary-line"><b>Focus</b><span>${esc(focus || "Not mapped")}</span></div>${d.parking ? `<div class="summary-line"><b>Parking Lot</b><span>${esc(d.parking)}</span></div>` : ""}${d.takeaway ? `<div class="summary-line"><b>Takeaway</b><span>${esc(d.takeaway)}</span></div>` : ""}</div></details>`;
  }

  function renderSkeletonHome() {
    const p = project(),
      done = skeletonCheckpointCount(p),
      checkpoints =
        checkpointRow(
          "Session",
          "Create tracks and section markers.",
          "skeleton-session",
          sessionDone(p),
          mapDone(p),
        ) +
        checkpointRow(
          "Draft",
          "Build every mapped part end to end.",
          "skeleton-draft",
          draftDone(p),
          sessionDone(p),
        ) +
        checkpointRow(
          "Bounce",
          "Export and hear the complete draft.",
          "skeleton-bounce",
          bounceDone(p),
          draftDone(p),
        );
    app.innerHTML = phaseHome(1, done, 3, checkpoints);
  }
  function refreshSkeletonChecks() {
    const p = project();
    app.querySelectorAll('[data-action="toggle-session-track"], [data-action="toggle-session-marker"]').forEach((el) => {
      const on = el.dataset.trackId ? p.skeleton.session.tracks[el.dataset.trackId] : p.skeleton.session.markers[el.dataset.sectionId];
      el.setAttribute("aria-pressed", String(!!on));
      el.querySelector(".round-check").classList.toggle("on", !!on);
    });
    const next = app.querySelector('[data-route="skeleton-draft"]');
    if (next) next.disabled = !sessionDone(p);
    for (const [action, on] of [["toggle-bounce-export", p.skeleton.bounce.exported], ["toggle-bounce-listen", p.skeleton.bounce.listened]]) {
      const el = app.querySelector(`[data-action="${action}"]`);
      if (el) { el.classList.toggle("on", !!on); el.setAttribute("aria-pressed", String(!!on)); el.querySelector(".round-check").classList.toggle("on", !!on); }
    }
    const listen = app.querySelector('[data-action="toggle-bounce-listen"]'), roadmap = app.querySelector('[data-route="roadmap"]');
    if (listen) listen.disabled = !p.skeleton.bounce.exported;
    if (roadmap) roadmap.disabled = !skeletonDone(p);
  }
  function renderSkeletonSession() {
    const p = project(),
      labels = sectionLabels(p);
    app.innerHTML =
      topbar(
        historyBackButton("skeleton", "The Skeleton"),
        phasePill(1),
        savedMark(),
      ) +
      `<div class="work-position">1 of 3</div><h2>Session</h2><p class="sub">Create the tracks and markers from The Map.</p><div class="session-groups"><section><div class="section-kicker">Tracks</div><div class="group-card list">${tracks(
        p,
      )
        .map(
          (t) =>
            `<button class="list-row" data-action="toggle-session-track" data-track-id="${t.id}"><span class="round-check ${p.skeleton.session.tracks[t.id] ? "on" : ""}"></span><div><div class="title">${esc(t.name)}</div><div class="desc">Placeholder track</div></div><span></span></button>`,
        )
        .join(
          "",
        )}</div></section><section><div class="section-kicker">Markers</div><div class="group-card list">${sections(
        p,
      )
        .map(
          (s, i) =>
            `<button class="list-row" data-action="toggle-session-marker" data-section-id="${s.id}"><span class="round-check ${p.skeleton.session.markers[s.id] ? "on" : ""}"></span><div><div class="title">${esc(labels[i])}</div><div class="desc">${s.lengthBars} bars</div></div><span></span></button>`,
        )
        .join(
          "",
        )}</div></section></div><div class="spacer-24"></div><button class="primary full" data-action="go" data-route="skeleton-draft" ${sessionDone(p) ? "" : "disabled"}>Next</button>`;
  }
  function draftSectionHtml(p, s, i) {
    const req = draftRequirements(p, i), state = p.skeleton.draft.parts[s.id] || {},
      count = req.filter((id) => state[id]).length, done = draftSectionDone(p, i);
    return `<details class="workflow-disclosure" data-draft-section="${s.id}" ${ui.draftOpenId === s.id ? "open" : ""}><summary><span class="round-check ${done ? "on" : ""}"></span><span><strong>${esc(sectionLabels(p)[i])}</strong><span class="copy">${req.length ? `${count} of ${req.length} tracks` : "No active tracks · Complete"}</span></span><span class="chev">⌄</span></summary><div class="draft-checks">${req.map((id) => `<button class="list-row" data-action="toggle-draft-part" data-section-id="${s.id}" data-track-id="${id}" aria-pressed="${!!state[id]}"><span class="round-check ${state[id] ? "on" : ""}"></span><div><div class="title">${esc(trackById(p, id)?.name)}</div><div class="desc">${esc(timingSummary(p, id, i))}${relevantTrackEvents(p, id, i).length ? ` · ${esc(relevantTrackEvents(p, id, i).join(" · "))}` : ""}</div></div></button>`).join("")}${!req.length ? '<p class="micro">Intentionally silent in The Map.</p>' : ""}</div></details>`;
  }
  function draftCoverage(p) {
    const total = sections(p).reduce((n, _, i) => n + draftRequirements(p, i).length, 0);
    const done = sections(p).reduce((n, s, i) => n + draftRequirements(p, i).filter((id) => p.skeleton.draft.parts[s.id]?.[id]).length, 0);
    return `${done} of ${total} mapped parts · ${sections(p).filter((_, i) => draftSectionDone(p, i)).length} of ${sections(p).length} sections`;
  }
  function renderSkeletonDraft() {
    const p = project();
    app.innerHTML = topbar(historyBackButton("skeleton", "The Skeleton"), phasePill(1), savedMark()) +
      `<div class="work-position">2 of 3</div><h2>Draft</h2><p class="sub">Build each mapped part.</p><p id="draftCoverage" class="coverage" aria-live="polite">${draftCoverage(p)}</p><div class="section-kicker">Sections</div><div class="draft-sections">${sections(p).map((sec, i) => draftSectionHtml(p, sec, i)).join("")}</div><div class="spacer-24"></div><button class="primary full" data-action="go" data-route="skeleton-bounce" ${draftDone(p) ? "" : "disabled"}>Next</button>`;
  }
  function refreshDraftChecks() {
    const p = project();
    app.querySelectorAll("[data-draft-section]").forEach((details, i) => {
      const sid = details.dataset.draftSection, req = draftRequirements(p, i), state = p.skeleton.draft.parts[sid] || {};
      details.querySelector("summary .round-check").classList.toggle("on", draftSectionDone(p, i));
      details.querySelector("summary .copy").textContent = req.length ? `${req.filter((id) => state[id]).length} of ${req.length} tracks` : "No active tracks · Complete";
      details.querySelectorAll('[data-action="toggle-draft-part"]').forEach((el) => {
        el.setAttribute("aria-pressed", String(!!state[el.dataset.trackId]));
        el.querySelector(".round-check").classList.toggle("on", !!state[el.dataset.trackId]);
      });
    });
    document.getElementById("draftCoverage").textContent = draftCoverage(p);
    app.querySelector('[data-route="skeleton-bounce"]').disabled = !draftDone(p);
  }
  function relevantTrackEvents(p, trackId, index) {
    return visibleEvents(p, "track", trackId, index).map((x) => x.event.label);
  }
  function renderSkeletonBounce() {
    const p = project();
    app.innerHTML =
      topbar(
        historyBackButton("skeleton", "The Skeleton"),
        phasePill(1),
        savedMark(),
      ) +
      `<div class="work-position">3 of 3</div><h2>Bounce</h2><p class="sub">Hear the complete arrangement as one song.</p><div class="section-kicker">Bounce</div>${actionCard("Export draft bounce", "One beginning-to-end bounce.", p.skeleton.bounce.exported, "toggle-bounce-export")}${actionCard("Listen start to finish", "Play the bounce once without stopping.", p.skeleton.bounce.listened, "toggle-bounce-listen", !p.skeleton.bounce.exported)}<div class="spacer-24"></div><button class="primary full" data-action="go" data-route="roadmap" ${skeletonDone(p) ? "" : "disabled"}>View Roadmap</button>`;
  }

  function renderRoadmap() {
    const p = project();
    if (p.type === "original") {
      app.innerHTML =
        topbar(
          backButton("project", "Original Song"),
          phaseTag("Roadmap"),
          "",
        ) +
        `<h2>Original Song</h2><p class="sub">Anything worth keeping → finished record.</p><div class="spacer-18"></div><div class="roadmap-grid">${ORIGINAL_PHASES.map((ph, i) => `<div class="road-phase ${i === 0 ? "current" : "future"}"><div class="road-top"><div class="road-num">${i + 1}</div><div><h3>${esc(ph[0])}</h3><p>${esc(ph[1])}</p></div></div></div>`).join("")}</div>`;
      return;
    }
    app.innerHTML =
      topbar(backButton("project", "Recreation"), phaseTag("Roadmap"), "") +
      `<h2>Roadmap</h2><p class="sub">Seven phases from analysis to finished rebuild.</p><div class="spacer-18"></div><div class="roadmap-grid">${STUDY_PHASES.map(
        (ph, i) => {
          const st = studyPhaseStatus(p, i),
            unlocked = studyPhaseUnlocked(p, i),
            tag = unlocked ? "button" : "div";
          return `<${tag} class="road-phase ${st} ${unlocked ? "clickable" : ""}" ${unlocked ? `data-action="go" data-route="${ph.route}"` : ""}><div class="road-top">${st === "done" ? `<span class="round-check on"></span>` : st === "current" ? `<span class="current-ring"></span>` : `<div class="road-num">${i + 1}</div>`}<div><h3>${esc(ph.title)}</h3><p>${esc(ph.desc)}</p><span class="micro">${st === "unimplemented" ? "Coming later · Not implemented" : st === "done" ? "Completed" : st === "current" ? "Current" : st === "available" ? "Available" : "Locked"}</span></div>${unlocked ? `<span class="chev">›</span>` : ""}</div><div class="road-checks">${ph.checkpoints.map((x) => `<span class="road-check">${esc(x)}</span>`).join("")}</div></${tag}>`;
        },
      ).join("")}</div>`;
  }
  function renderNotes() {
    const p = project();
    if (p.type === "original") {
      app.innerHTML =
        topbar(backButton("project", "Original Song"), phaseTag("Notes"), "") +
        `<h2>Notes</h2><p class="sub">Keep project notes in one place.</p>`;
      return;
    }
    const labels = sectionLabels(p),
      parking = [],
      takeaways = [];
    if (p.map.phaseParking) parking.push(["The Map", p.map.phaseParking]);
    if (p.map.phaseTakeaway) takeaways.push(["The Map", p.map.phaseTakeaway]);
    sections(p).forEach((s, i) => {
      const d = sectionData(p, s.id);
      if (d.parking) parking.push([`The Map · ${labels[i]}`, d.parking]);
      if (d.takeaway) takeaways.push([`The Map · ${labels[i]}`, d.takeaway]);
    });
    app.innerHTML =
      topbar(backButton("project", "Recreation"), phaseTag("Notes"), "") +
      `<h2>Notes</h2><p class="sub">Keep questions and lessons in one place.</p><div class="notes-columns"><section><div class="section-kicker">Parking Lot</div>${parking.length ? parking.map(([ctx, text]) => noteCard(ctx, text)).join("") : '<div class="empty">Nothing parked yet.</div>'}</section><section><div class="section-kicker">Takeaways</div>${takeaways.length ? takeaways.map(([ctx, text]) => noteCard(ctx, text)).join("") : '<div class="empty">No takeaways yet.</div>'}</section></div>`;
  }
  function noteCard(ctx, text) {
    return `<div class="card card-pad" style="margin-bottom:9px"><div class="micro" style="margin-bottom:6px">${esc(ctx)}</div><div style="font-size:14px;line-height:1.5">${esc(text)}</div></div>`;
  }
  function renderOriginalSpark() {
    const p = project(),
      starts = [
        "Lyric",
        "Melody",
        "Beat",
        "Chords",
        "Instrument part",
        "Sound",
        "Concept",
        "Voice memo",
        "Other",
      ],
      reasons = ["Rhythm", "Emotion", "Melody", "Sound", "Words", "Energy"];
    app.innerHTML =
      topbar(
        backButton("project", "Original Song"),
        phaseTag("The Spark"),
        savedMark(),
      ) +
      `<h1>Start with what you have</h1><p class="sub">Capture the thing that made you want to make something.</p><div class="section-kicker">Starting With</div><div class="choice-wrap">${starts.map((x) => `<button class="choice ${p.spark.starts.includes(x) ? "selected" : ""}" data-action="toggle-spark-start" data-name="${x}">${x}</button>`).join("")}</div><div class="section-kicker">The Idea</div><textarea class="textarea" data-input="spark-idea" placeholder="What do you have right now?">${esc(p.spark.idea)}</textarea><div class="section-kicker">What Makes It Worth Keeping?</div><div class="choice-wrap">${reasons.map((x) => `<button class="choice ${p.spark.reasons.includes(x) ? "selected" : ""}" data-action="toggle-spark-reason" data-name="${x}">${x}</button>`).join("")}</div><div class="section-kicker">Anchor</div><textarea class="textarea" data-input="spark-anchor" placeholder="What absolutely should survive as this song grows?">${esc(p.spark.anchor)}</textarea>`;
  }

  function openAddSectionTypeSheet() {
    sectionDraft = {
      name: "",
      bars: null,
      customName: false,
      customBars: false,
      canAdd: true,
      added: 0,
    };
    sheetRoot.replaceChildren();
    renderSectionBuilder();
    openSheet();
  }
  let sectionDraft = null;
  function lengthChoices(value, action) {
    return `<div class="length-segmented" role="group" aria-label="Bar length">${[4, 8, 12, 16].map((n) => `<button class="choice ${Number(value) === n ? "selected" : ""}" data-action="${action}" data-bars="${n}" aria-pressed="${Number(value) === n}">${n}</button>`).join("")}<button class="choice ${value === "custom" ? "selected" : ""}" data-action="${action}" data-bars="custom">Custom</button></div>`;
  }
  function renderSectionBuilder() {
    const d = sectionDraft;
    // Build once per opening. Selection only updates properties on existing nodes.
    if (!sheetRoot.querySelector(".section-builder")) {
      sheetRoot.innerHTML = `<div class="sheet section-builder"><div class="grabber"></div><h3>Add sections</h3><div class="section-kicker">Section</div><div class="choice-wrap">${[...SECTION_TYPES, "Custom"].map((name) => `<button class="choice" data-action="choose-section-type" data-name="${name}">${name}</button>`).join("")}</div><input hidden class="field custom-length" id="newSectionName" aria-label="Section name" placeholder="Section name"><div class="section-kicker">Bars</div>${lengthChoices(null, "set-new-section-bars")}<input hidden class="field custom-length" id="newSectionBars" type="number" inputmode="numeric" min="1" max="256" aria-label="Custom bar length" placeholder="Number of bars"><div class="builder-status" id="builderStatus" role="status" aria-live="polite"></div><div class="sheet-error" id="sheetError"></div><div class="sheet-actions"><button class="primary full" data-action="save-new-section">Add Section</button><button class="sheet-close" data-action="close-sheet">Done</button></div></div>`;
    }
    sheetRoot.querySelectorAll('[data-action="choose-section-type"]').forEach((el) => setSelected(el, el.dataset.name === d.name));
    sheetRoot.querySelectorAll('[data-action="set-new-section-bars"]').forEach((el) => setSelected(el, d.customBars ? el.dataset.bars === "custom" : Number(el.dataset.bars) === d.bars));
    const name = document.getElementById("newSectionName"), bars = document.getElementById("newSectionBars");
    name.hidden = !d.customName;
    bars.hidden = !d.customBars;
    if (document.activeElement !== bars) bars.value = d.bars || "";
    sheetRoot.querySelector('[data-action="save-new-section"]').disabled = !d.canAdd || !d.name || !validBars(d.bars) || (d.customName && !clean(d.typedName));
  }
  function setSelected(el, selected) {
    el.classList.toggle("selected", selected);
    el.setAttribute("aria-pressed", String(selected));
  }
  function refreshStudySelections() {
    const p = project(), d = sectionData(p, sections(p)[ui.sectionIndex].id);
    app.querySelectorAll('[data-action="set-feel"]').forEach((el) => setSelected(el, d.feel[el.dataset.scale] === el.dataset.value));
    app.querySelectorAll('[data-action="toggle-focus"]').forEach((el) => setSelected(el, d.focusIds.includes(el.dataset.trackId)));
    app.querySelectorAll('[data-action="focus-none"]').forEach((el) => setSelected(el, d.focusState === "none"));
    const next = app.querySelector('[data-action="next-section"]');
    if (next) next.disabled = !sectionComplete(p, ui.sectionIndex);
    app.querySelectorAll(".section-tab").forEach((el, i) => {
      el.classList.toggle("done", sectionComplete(p, i));
      el.disabled = sections(p).slice(0, i).some((_, j) => !sectionComplete(p, j));
    });
  }
  function suggestedBarsFor(p, name) {
    const found = [...sections(p)]
      .reverse()
      .find((s) => s.name === name && validBars(s.lengthBars));
    return found ? Number(found.lengthBars) : null;
  }
  function openSectionSheet(id) {
    const s = sections().find((x) => x.id === id);
    if (!s) return;
    sheetRoot.innerHTML = `<div class="sheet"><div class="grabber"></div><h3>Edit section</h3><div class="section-kicker">Name</div><input class="field" id="renameSection" aria-label="Section name" value="${esc(s.name)}"><div class="section-kicker">Bars</div>${lengthChoices([4, 8, 12, 16].includes(Number(s.lengthBars)) ? s.lengthBars : "custom", "set-sheet-bars")}<input id="sectionBars" class="field custom-length" type="number" inputmode="numeric" min="1" max="256" aria-label="Custom bar length" value="${s.lengthBars || ""}" ${[4, 8, 12, 16].includes(Number(s.lengthBars)) ? "hidden" : ""}><div class="sheet-error" id="sheetError"></div><div class="sheet-actions"><button class="primary full" data-action="save-section" data-id="${id}">Done</button><button class="sheet-close" data-action="close-sheet">Cancel</button></div></div>`;
    openSheet();
  }
  function openAddChangeSheet(targetType, targetId) {
    const active = visibleEvents(
        project(),
        targetType,
        targetId,
        ui.sectionIndex,
      ),
      attrs = `data-target-type="${targetType}" ${targetId ? `data-target-id="${targetId}"` : ""}`;
    sheetRoot.innerHTML = `<div class="sheet change-sheet"><div class="grabber"></div><h3>Add change</h3><div class="change-groups">${CHANGE_GROUPS.map(
      (g) =>
        `<div><div class="sheet-group-title">${g.label}</div><div class="change-options">${Object.entries(
          CHANGE_DEFS,
        )
          .filter(([, d]) => d.group === g.key)
          .map(
            ([label, d]) =>
              `<button class="change-option ${active.some((x) => x.event.label === label) ? "active" : ""}" data-action="choose-change" data-label="${label}" ${attrs}><span class="change-swatch tone-${d.tone}"></span>${label}${active.some((x) => x.event.label === label) ? '<span class="active-mark" aria-label="Already mapped">✓</span>' : ""}</button>`,
          )
          .join("")}</div></div>`,
    ).join(
      "",
    )}</div><button class="sheet-close" data-action="close-sheet">Cancel</button></div>`;
    openSheet();
  }
  function defaultEventPosition(p, targetType, targetId, kind) {
    const s = sections(p)[ui.sectionIndex],
      vis =
        targetType === "track"
          ? visiblePresence(p, targetId, ui.sectionIndex)
          : [],
      chosen = vis.find((x) => x.range.id === ui.selectedPresenceId) || vis[0],
      start = chosen
        ? Math.max(
            anchorAbs(p, chosen.range.start),
            sectionStarts(p)[ui.sectionIndex],
          )
        : sectionStarts(p)[ui.sectionIndex];
    return kind === "marker"
      ? { point: anchorAtAbs(p, start) }
      : {
          start: anchorAtAbs(p, start),
          end: chosen?.range.end ? { ...chosen.range.end } : null,
        };
  }
  function openSettings() {
    const p = project();
    sheetRoot.innerHTML = `<div class="sheet"><div class="grabber"></div><h3>Project Settings</h3><div class="sheet-actions"><button class="secondary full" data-action="export-backup">Export Backup</button><button class="secondary full" data-action="import-backup">Import Backup</button><button class="destructive full" data-action="reset-project">Reset This Project</button><button class="sheet-close" data-action="close-sheet">Done</button></div></div>`;
    openSheet();
  }
  function openProjectMenu(id) {
    const p = db.projects.find((x) => x.id === id);
    if (!p) return;
    sheetRoot.innerHTML = `<div class="sheet"><div class="grabber"></div><h3>${esc(p.title)}</h3><div class="sheet-actions"><button class="destructive full" data-action="delete-project" data-id="${p.id}">Delete Project</button><button class="sheet-close" data-action="close-sheet">Cancel</button></div></div>`;
    openSheet();
  }
  let sheetOpener = null;
  function openSheet() {
    if (!sheetRoot.classList.contains("open"))
      sheetOpener = document.activeElement;
    const heading = sheetRoot.querySelector("h3");
    if (heading) {
      heading.id = "sheetTitle";
      sheetRoot.setAttribute("aria-labelledby", "sheetTitle");
    }
    sheetRoot.setAttribute("role", "dialog");
    sheetRoot.setAttribute("aria-modal", "true");
    document.body.classList.add("sheet-open");
    clearTimeout(sheetClearTimer);
    sheetClearTimer = null;
    sheetRoot.classList.add("open");
    sheetRoot.setAttribute("aria-hidden", "false");
    app.inert = true;
    document.getElementById("undoNotice").inert = true;
    if (heading) { heading.tabIndex = -1; heading.focus({ preventScroll: true }); }
  }
  function closeSheet() {
    app.inert = false;
    document.getElementById("undoNotice").inert = false;
    document.body.classList.remove("sheet-open");
    sheetRoot.classList.remove("open");
    const opener = sheetOpener?.isConnected ? sheetOpener : ui.route === "structure" ? app.querySelector('[data-action="open-add-section"]') : null;
    opener?.focus({ preventScroll: true });
    sheetRoot.setAttribute("aria-hidden", "true");
    clearTimeout(sheetClearTimer);
    sheetClearTimer = setTimeout(() => {
      if (!sheetRoot.classList.contains("open")) sheetRoot.innerHTML = "";
      sheetClearTimer = null;
    }, 140);
  }
  function sheetError(msg) {
    const el = document.getElementById("sheetError");
    if (el) el.textContent = msg;
  }

  function addSection(name, bars) {
    name = clean(name);
    bars = Number(bars);
    if (!name || !validBars(bars)) return null;
    const p = project();
    const s = { id: uid(), name, lengthBars: bars };
    p.map.sections.push(s);
    p.map.sectionData[s.id] = makeSectionData();
    p.skeleton.session.markers[s.id] = false;
    p.skeleton.draft.parts[s.id] = {};
    tracks(p).forEach((t) => (p.skeleton.draft.parts[s.id][t.id] = false));
    invalidateStructureVerification(p);
    invalidateBounce(p);
    save();
    return s;
  }
  function removeSection(p, id) {
    const idx = sectionIndexById(p, id);
    if (idx < 0) return;
    const next = sections(p)[idx + 1] || null;
    if (lengthsComplete(p)) splitTimelineAtSections(p);
    p.map.timeline.presence.forEach((r) => {
      if (r.start.sectionId === id && r.end == null && next)
        r.start = { sectionId: next.id, bar: 0 };
    });
    p.map.timeline.events.forEach((e) => {
      if (
        e.kind === "range" &&
        e.start.sectionId === id &&
        e.end == null &&
        next
      )
        e.start = { sectionId: next.id, bar: 0 };
    });
    p.map.sections.splice(idx, 1);
    delete p.map.sectionData[id];
    delete p.skeleton.session.markers[id];
    delete p.skeleton.draft.parts[id];
    p.map.timeline.presence = p.map.timeline.presence.filter(
      (r) =>
        r.start.sectionId !== id && (r.end == null || r.end.sectionId !== id),
    );
    p.map.timeline.events = p.map.timeline.events.filter((e) =>
      e.kind === "marker"
        ? e.point.sectionId !== id
        : e.start.sectionId !== id && (e.end == null || e.end.sectionId !== id),
    );
    reconcileTimelineAfterStructureChange(p);
    invalidateStructureVerification(p);
    invalidateMarkersFrom(p, idx);
    save();
  }
  function addTrack(name) {
    name = clean(name);
    if (
      !name ||
      tracks(project()).some((t) => t.name.toLowerCase() === name.toLowerCase())
    )
      return;
    const p = project(),
      t = { id: uid(), name };
    p.map.tracks.push(t);
    p.skeleton.session.tracks[t.id] = false;
    sections(p).forEach((s) => {
      p.skeleton.draft.parts[s.id] = p.skeleton.draft.parts[s.id] || {};
      p.skeleton.draft.parts[s.id][t.id] = false;
    });
    invalidateMapVerification(p);
    save();
  }
  function removeTrack(p, id) {
    const t = trackById(p, id);
    if (!t) return;
    const used =
      trackUsedAnywhere(p, id) || eventsForTarget(p, "track", id).length;
    if (used && !confirm(`Remove ${t.name} and its mapped timeline data?`))
      return;
    p.map.tracks = p.map.tracks.filter((x) => x.id !== id);
    p.map.timeline.presence = p.map.timeline.presence.filter(
      (r) => r.trackId !== id,
    );
    p.map.timeline.events = p.map.timeline.events.filter(
      (e) => !(e.targetType === "track" && e.targetId === id),
    );
    Object.values(p.map.sectionData).forEach((d) => {
      d.focusIds = (d.focusIds || []).filter((x) => x !== id);
      if (!d.focusIds.length && d.focusState === "selected") d.focusState = "";
    });
    delete p.skeleton.session.tracks[id];
    Object.values(p.skeleton.draft.parts).forEach((x) => {
      if (x) delete x[id];
    });
    invalidateMapVerification(p);
    if (used) invalidateBounce(p);
    save();
  }
  function subtractSectionFromTrack(p, trackId, index) {
    if (!lengthsComplete(p)) return;
    const s = sections(p)[index],
      starts = sectionStarts(p),
      secStart = starts[index],
      secEnd = secStart + Number(s.lengthBars),
      out = [];
    presenceForTrack(p, trackId).forEach((r) => {
      const a = rangeAbs(p, r);
      if (a.end <= secStart + 1e-6 || a.start >= secEnd - 1e-6) {
        out.push(r);
        return;
      }
      if (a.start < secStart - 1e-6)
        out.push({
          id: uid(),
          trackId,
          start: r.start,
          end: anchorAtAbs(p, secStart, true),
        });
      if (a.end > secEnd + 1e-6)
        out.push({
          id: uid(),
          trackId,
          start: anchorAtAbs(p, secEnd, false),
          end: r.end,
        });
    });
    p.map.timeline.presence = p.map.timeline.presence
      .filter((r) => r.trackId !== trackId)
      .concat(out);
    mergePresenceForTrack(p, trackId, false);
    invalidateDraftTrack(p, trackId, [s.id]);
  }
  function eventCoveredByPresence(p, e, startAbs, endAbs) {
    if (e.targetType !== "track") return true;
    return presenceForTrack(p, e.targetId).some((r) => {
      const a = rangeAbs(p, r);
      return startAbs >= a.start - 1e-6 && endAbs <= a.end + 1e-6;
    });
  }
  function reconcileStateProperty(p, event) {
    if (!event || event.kind !== "range") return;
    const list = p.map.timeline.events
      .filter(
        (e) =>
          e.kind === "range" &&
          e.property === event.property &&
          e.targetType === event.targetType &&
          (e.targetType === "mix" || e.targetId === event.targetId),
      )
      .sort(
        (a, b) =>
          anchorAbs(p, a.start) - anchorAbs(p, b.start) ||
          (a === event ? 1 : b === event ? -1 : 0),
      );
    for (let i = 0; i < list.length - 1; i++) {
      const cur = list[i],
        next = list[i + 1],
        cut = anchorAbs(p, next.start);
      if (rangeAbs(p, cur).end > cut) cur.end = { ...next.start };
      if (anchorAbs(p, cur.start) >= cut)
        p.map.timeline.events = p.map.timeline.events.filter(
          (e) => e.id !== cur.id,
        );
    }
  }

  function moveSection(p, id, to) {
    const from = sectionIndexById(p, id);
    to = clamp(to, 0, sections(p).length - 1);
    if (from < 0 || from === to) return;
    if (lengthsComplete(p)) splitTimelineAtSections(p);
    p.map.sections.splice(to, 0, p.map.sections.splice(from, 1)[0]);
    reconcileTimelineAfterStructureChange(p);
    invalidateStructureVerification(p);
    invalidateMarkersFrom(p, Math.min(from, to));
    save();
  }
  function installSorting() {
    const container = document.getElementById("sortList");
    if (!container) return;
    container.querySelectorAll("[data-drag-handle]").forEach((handle) => {
      handle.addEventListener("click", (e) => {
        e.preventDefault();
        e.stopPropagation();
      });
      handle.addEventListener(
        "pointerdown",
        (e) => {
          if (e.button !== undefined && e.button !== 0) return;
          e.preventDefault();
          e.stopPropagation();
          const row = handle.closest(".sort-row"),
            rect = row.getBoundingClientRect(),
            offset = e.clientY - rect.top,
            placeholder = document.createElement("div"),
            ghost = row.cloneNode(true),
            controller = new AbortController(),
            opts = { signal: controller.signal };
          placeholder.className = "sort-placeholder";
          placeholder.style.height = rect.height + "px";
          ghost.classList.add("sort-ghost");
          Object.assign(ghost.style, {
            left: rect.left + "px",
            top: rect.top + "px",
            width: rect.width + "px",
            height: rect.height + "px",
          });
          row.replaceWith(placeholder);
          document.body.appendChild(ghost);
          document.body.classList.add("is-sorting");
          const finish = (cancel) => {
            controller.abort();
            cancelGesture = null;
            const target = [...container.children].indexOf(placeholder);
            ghost.remove();
            placeholder.replaceWith(row);
            document.body.classList.remove("is-sorting");
            if (!cancel) moveSection(project(), row.dataset.sectionId, target);
            renderStructure();
          };
          cancelGesture = () => finish(true);
          window.addEventListener("resize", () => finish(true), opts);
          window.addEventListener(
            "pointermove",
            (ev) => {
              if (ev.pointerId !== e.pointerId) return;
              ev.preventDefault();
              ghost.style.top =
                clamp(ev.clientY - offset, 8, innerHeight - rect.height - 8) +
                "px";
              if (ev.clientY > innerHeight - 70) window.scrollBy(0, 14);
              if (ev.clientY < 70) window.scrollBy(0, -14);
              for (const other of container.querySelectorAll(".sort-row")) {
                const r = other.getBoundingClientRect();
                if (ev.clientY < r.top + r.height / 2) {
                  container.insertBefore(placeholder, other);
                  return;
                }
              }
              container.appendChild(placeholder);
            },
            { ...opts, passive: false },
          );
          window.addEventListener(
            "pointerup",
            (ev) => {
              if (ev.pointerId === e.pointerId) finish(false);
            },
            opts,
          );
          window.addEventListener(
            "pointercancel",
            (ev) => {
              if (ev.pointerId === e.pointerId) finish(true);
            },
            opts,
          );
          window.addEventListener("blur", () => finish(true), opts);
        },
        { passive: false },
      );
    });
  }
  // All movement uses a disposable candidate. Canonical music changes only on commit.
  let boundarySelection = null;
  const lanePositions = new WeakMap();
  function clearBoundarySelection() {
    boundarySelection = null;
    app.querySelectorAll('.boundary-selected').forEach(el=>{el.classList.remove('boundary-selected');el.setAttribute('aria-pressed','false');});
  }
  function boundaryRef(handle) {
    return { type:handle.hasAttribute('data-presence-handle') ? 'presence' : 'event', id:handle.dataset.rangeId || handle.dataset.eventId, edge:handle.dataset.edge || 'point' };
  }
  function selectBoundary(handle) {
    clearBoundarySelection();
    boundarySelection = boundaryRef(handle);
    handle.classList.add('boundary-selected');
    handle.setAttribute('aria-pressed','true');
  }
  function laneBoundary(lane, clientX) {
    const rect=lane.getBoundingClientRect(), len=Number(sections()[ui.sectionIndex].lengthBars);
    return clamp(Math.round((clientX-rect.left)/rect.width*len),0,len);
  }
  function boundaryHandle(ref) {
    return [...app.querySelectorAll('[data-presence-handle],[data-event-handle],[data-event-marker]')].find(h=>{
      const r=boundaryRef(h);return r.id===ref.id && r.type===ref.type && r.edge===ref.edge;
    });
  }
  function moveBoundary(ref,boundary) {
    const obj=selectedObject(ref.type,ref.id);
    if(!obj) return false;
    const candidate=JSON.parse(JSON.stringify(obj));
    if(!applyTiming(candidate,ref.type,ref.edge,boundary)) return false;
    if(JSON.stringify(candidate)===JSON.stringify(obj)) return false;
    const before=copyProject();
    if(ref.type==='event'){ui.selectedEventId=ref.id;ui.selectedPresenceId=null;ui.expandedTrackId=obj.targetType==='mix'?'__mix__':obj.targetId;}
    Object.assign(obj,candidate);
    clearBoundarySelection();
    finishTimelineEdit(before,obj,ref.type,'Timing changed');
    boundaryHandle(ref)?.focus({preventScroll:true});
    return true;
  }
  function installTimelineInteractions() {
    app.querySelectorAll('[data-presence-handle],[data-event-handle],[data-event-marker]').forEach(handle=>{
      handle.onpointerdown=e=>startBoundaryGesture(e,handle);
      handle.onclick=e=>{ e.preventDefault();e.stopPropagation(); if(e.detail===0) {
        const ref=boundaryRef(handle);
        if(ref.edge==='point'){const obj=selectedObject('event',ref.id);ui.selectedEventId=ref.id;ui.selectedPresenceId=null;ui.expandedTrackId=obj.targetType==='mix'?'__mix__':obj.targetId;refreshArrangement();handle=boundaryHandle(ref);}
        selectBoundary(handle);
      } };
      handle.onkeydown=e=>{
        if(e.key==='Escape'){e.preventDefault();cancelGesture?.();clearBoundarySelection();return;}
        if(!['ArrowLeft','ArrowRight'].includes(e.key)) return;
        e.preventDefault();
        const ref=boundaryRef(handle),obj=selectedObject(ref.type,ref.id),p=project(),base=sectionStarts(p)[ui.sectionIndex],len=Number(sections(p)[ui.sectionIndex].lengthBars);
        const pos=ref.edge==='point' ? anchorAbs(p,obj.point)-base : ref.edge==='end' ? rangeAbs(p,obj).end-base : anchorAbs(p,obj[ref.edge])-base;
        moveBoundary(ref,e.key==='ArrowLeft' ? Math.ceil(pos)-1 : Math.floor(pos)+1);
      };
    });
    app.querySelectorAll('[data-presence-surface]').forEach(surface=>{
      surface.onpointerdown=e=>startLaneTap(e,surface);
      surface.onclick=e=>{
        e.preventDefault();e.stopPropagation();
        if(e.detail===0){const value=lanePositions.get(surface)||0; if(boundarySelection) moveBoundary(boundarySelection,value);else commitPresenceTransition(surface.dataset.trackId,value);}
      };
      surface.onkeydown=e=>{
        if(!['ArrowLeft','ArrowRight'].includes(e.key))return;
        e.preventDefault();const len=Number(sections()[ui.sectionIndex].lengthBars),value=clamp((lanePositions.get(surface)||0)+(e.key==='ArrowLeft'?-1:1),0,len);
        lanePositions.set(surface,value);surface.setAttribute('aria-label',`${trackById(project(),surface.dataset.trackId).name}, ${boundaryLabel('start',value)}; Enter to place`);
        const rect=surface.parentElement.getBoundingClientRect();surface.parentElement.closest('.timeline-scroll')?.scrollBy({left: rect.width/len*(e.key==='ArrowLeft'?-1:1),behavior:'instant'});
      };
    });
    // Destination picking uses the same lane, including occupied material.
    app.querySelectorAll('.timeline-lane').forEach(lane=>{
      lane.onpointerdown=e=>{
        if(!boundarySelection || e.target.closest('[data-presence-handle],[data-event-handle],[data-event-marker]'))return;
        const obj=selectedObject(boundarySelection.type,boundarySelection.id),track=lane.closest('[data-track-row]')?.dataset.trackRow;
        if((boundarySelection.type==='presence' && obj?.trackId!==track) || (boundarySelection.type==='event' && obj?.targetType==='track' && obj.targetId!==track)) {clearBoundarySelection();return;}
        e.stopPropagation();startLaneTap(e,lane.querySelector('[data-presence-surface]')||lane,boundarySelection);
      };
    });
  }
  function startLaneTap(e,surface,selected=null) {
    if(e.button!==0 || ui.animating)return;
    // An ancestor owns a selected-edge destination, so do not install two gestures.
    if(boundarySelection && !selected)return;
    e.stopPropagation();
    const lane=surface.closest('.timeline-lane'),origin={x:e.clientX,y:e.clientY},ref=selected && {...selected},value=laneBoundary(lane,e.clientX);
    const controller=new AbortController(),opts={signal:controller.signal};
    let cancelled=false,finished=false;
    const rect=lane.getBoundingClientRect(),scroll=lane.closest('.timeline-scroll'),scrollLeft=scroll?.scrollLeft;
    const finish=(cancel,ev)=>{
      if(finished || ev && ev.pointerId!==e.pointerId)return;
      finished=true;controller.abort();cancelGesture=null;
      const current=lane.getBoundingClientRect();
      if(cancel || cancelled || !lane.isConnected || current.width!==rect.width || current.height!==rect.height || current.left!==rect.left || current.top!==rect.top || scroll?.scrollLeft!==scrollLeft)return;
      if(ref)moveBoundary(ref,value);else commitPresenceTransition(surface.dataset.trackId,value);
    };
    cancelGesture=()=>finish(true);
    window.addEventListener('pointermove',ev=>{if(ev.pointerId===e.pointerId && (Math.abs(ev.clientY-origin.y)>10 || Math.abs(ev.clientX-origin.x)>10))cancelled=true;},opts);
    window.addEventListener('pointerup',ev=>finish(false,ev),opts);
    window.addEventListener('pointercancel',ev=>finish(true,ev),opts);
    surface.addEventListener('lostpointercapture',()=>finish(true),opts);
    window.addEventListener('resize',()=>finish(true),opts);
    window.addEventListener('blur',()=>finish(true),opts);
  }
  function startBoundaryGesture(e,handle) {
    if(e.button!==0 || ui.animating)return;
    e.stopPropagation();
    const band=handle.closest('.event-line') || handle.closest('.timeline-lane');
    const handles=[...band.querySelectorAll(handle.hasAttribute('data-presence-handle')?'[data-presence-handle]':'[data-event-handle],[data-event-marker]')];
    handle=handles.reduce((best,h)=>Math.abs(h.getBoundingClientRect().left+22-e.clientX)<Math.abs(best.getBoundingClientRect().left+22-e.clientX)?h:best,handle);
    const ref=boundaryRef(handle),obj=selectedObject(ref.type,ref.id);
    if(!obj)return;
    const lane=handle.closest('.timeline-lane'),rect=lane.getBoundingClientRect(),scroll=lane.closest('.timeline-scroll'),original=JSON.parse(JSON.stringify(obj));
    const graphic=ref.edge==='point'?handle:lane.querySelector(`[data-graphic="${ref.id}"]`),guide=lane.querySelector('.snap-guide'),output=document.getElementById('dragPosition');
    const originalGraphic=graphic?.getAttribute('style'),originalHandles=[...lane.querySelectorAll('[data-presence-handle],[data-event-handle]')].map(el=>[el,el.getAttribute('style')]);
    const origin={x:e.clientX,y:e.clientY,width:innerWidth,height:innerHeight,scrollLeft:scroll.scrollLeft},controller=new AbortController(),opts={signal:controller.signal};
    let candidate=original,moved=false,finished=false,captured=false;
    try{handle.setPointerCapture(e.pointerId);captured=true;}catch(_){}
    const restore=()=>{if(graphic)graphic.setAttribute('style',originalGraphic);originalHandles.forEach(([h,style])=>h.setAttribute('style',style));};
    const finish=(cancel,ev)=>{
      if(finished || ev && ev.pointerId!==e.pointerId)return;
      finished=true;controller.abort();cancelGesture=null;
      cancel ||= !handle.isConnected || captured&&!handle.hasPointerCapture(e.pointerId) || innerWidth!==origin.width || innerHeight!==origin.height || lane.getBoundingClientRect().width!==rect.width || scroll.scrollLeft!==origin.scrollLeft;
      output.hidden=true;if(guide)guide.hidden=true;document.body.classList.remove('is-dragging');
      if(cancel){restore();clearBoundarySelection();return;}
      if(!moved){
        if(ref.edge==='point') {ui.selectedEventId=ref.id;ui.selectedPresenceId=null;const ev=selectedObject('event',ref.id);ui.expandedTrackId=ev.targetType==='mix'?'__mix__':ev.targetId;refreshArrangement();handle=boundaryHandle(ref);}
        if(handle)selectBoundary(handle);
        return;
      }
      restore();
      if(JSON.stringify(candidate)===JSON.stringify(original))return;
      const before=copyProject();Object.assign(obj,candidate);clearBoundarySelection();
      if(ref.type==='event'){ui.selectedEventId=ref.id;ui.selectedPresenceId=null;ui.expandedTrackId=obj.targetType==='mix'?'__mix__':obj.targetId;}
      finishTimelineEdit(before,obj,ref.type,'Timing changed');
      boundaryHandle(ref)?.focus({preventScroll:true});
    };
    cancelGesture=()=>finish(true);
    handle.addEventListener('lostpointercapture',()=>finish(true),opts);
    window.addEventListener('pointermove',ev=>{
      if(ev.pointerId!==e.pointerId)return;
      const dx=ev.clientX-origin.x,dy=ev.clientY-origin.y;
      if(Math.abs(dy)>12 && (!moved || Math.abs(dy)>Math.abs(dx))){finish(true);return;}
      if(!moved && Math.abs(dx)<4)return;
      moved=true;document.body.classList.add('is-dragging');
      const boundary=laneBoundary(lane,ev.clientX),next=JSON.parse(JSON.stringify(original));
      if(!applyTiming(next,ref.type,ref.edge,boundary))return;
      candidate=next;
      const p=project(),len=Number(sections(p)[ui.sectionIndex].lengthBars),portion=ref.edge==='point'?markerPortion(p,next,ui.sectionIndex):rangePortion(p,next,ui.sectionIndex);
      // Out-of-view endpoints are rejected, so preview and canonical commit agree.
      if(!portion)return;
      if(graphic){graphic.style.left=portion.left+'%';if(ref.edge!=='point')graphic.style.right=portion.right+'%';}
      originalHandles.forEach(([h])=>{const r=boundaryRef(h);if(r.id===ref.id)h.style.left=(r.edge==='start'?portion.left:100-portion.right)+'%';});
      if(guide){guide.hidden=false;guide.style.left=boundary/len*100+'%';}
      output.hidden=false;output.textContent=boundaryLabel(ref.edge,boundary);output.style.left=clamp(ev.clientX,80,innerWidth-80)+'px';output.style.top=Math.max(12,ev.clientY-58)+'px';
    },opts);
    window.addEventListener('pointerup',ev=>finish(false,ev),opts);
    window.addEventListener('pointercancel',ev=>finish(true,ev),opts);
    window.addEventListener('resize',()=>finish(true),opts);
    scroll.addEventListener('scroll',()=>finish(true),opts);
    window.addEventListener('scroll',()=>finish(true),{...opts,capture:true});
    window.addEventListener('blur',()=>finish(true),opts);
    const observer=new ResizeObserver(()=>{if(lane.getBoundingClientRect().width!==rect.width || lane.getBoundingClientRect().height!==rect.height)finish(true);});observer.observe(lane);controller.signal.addEventListener('abort',()=>observer.disconnect(),{once:true});
  }
  document.addEventListener('keydown',e=>{if(e.key==='Escape'){cancelGesture?.();clearBoundarySelection();}});
  document.addEventListener('pointerdown',e=>{
    if(boundarySelection && !e.target.closest('.timeline-lane'))clearBoundarySelection();
  },true);

  app.addEventListener("click", (e) => {
    const b = e.target.closest("[data-action]");
    if (!b || b.disabled || ui.animating) return;
    const action = b.dataset.action,
      p = project();
    if (action === "delete-section") {
      e.stopPropagation();
      const before = copyProject(), label = sectionLabels(p)[sectionIndexById(p, b.dataset.id)];
      removeSection(p, b.dataset.id);
      renderStructure();
      offerUndo(before, `${label} deleted`);
      return;
    }
    if (action === "history-back") {
      if (history.state?.fromRoute) {
        history.back();
        return;
      }
      return go(b.dataset.fallbackRoute || "project");
    }
    if (action === "go") return go(b.dataset.route);
    if (action === "new-project") return go("new-project");
    if (action === "set-new-type") {
      ui.newType = b.dataset.type;
      app.querySelectorAll('[data-action="set-new-type"]').forEach((el) => setSelected(el, el.dataset.type === ui.newType));
      return;
    }
    if (action === "create-project") {
      const titleInput = document.getElementById("newTitle"),
        title = clean(titleInput?.value),
        artist = clean(document.getElementById("newArtist")?.value);
      if (!title) {
        titleInput?.focus({ preventScroll: true });
        return;
      }
      const np =
        ui.newType === "study"
          ? makeStudyProject(title, artist)
          : makeOriginalProject(title, artist);
      db.projects.push(np);
      db.currentProjectId = np.id;
      save();
      return go("project");
    }
    if (action === "open-project") {
      db.currentProjectId = b.dataset.id;
      save();
      return go("project");
    }
    if (action === "project-menu") return openProjectMenu(b.dataset.id);
    if (action === "settings") return openSettings();
        if (action === "toggle-setup") {
      p.map.setup[b.dataset.field] = !p.map.setup[b.dataset.field];
      invalidateMapVerification(p);
      save();
      return renderMapHome();
    }
    if (action === "open-add-section") return openAddSectionTypeSheet();
    if (action === "edit-section") return openSectionSheet(b.dataset.sectionId);
    if (action === "toggle-structure-verified") {
      if (!lengthsComplete(p)) return;
      p.map.structureVerified = !p.map.structureVerified;
      invalidateMapVerification(p);
      save();
      return renderStructure();
    }
    if (action === "toggle-track-choice") {
      const name = b.dataset.name,
        t = tracks(p).find((x) => x.name === name);
      if (t) removeTrack(p, t.id);
      else addTrack(name);
      const names = new Set(tracks(p).map((t) => t.name));
      app.querySelectorAll('[data-action="toggle-track-choice"]').forEach((el) => setSelected(el, names.has(el.dataset.name)));
      app.querySelector('[data-action="start-section-study"]').disabled = !tracksDone(p);
      return;
    }
    if (action === "add-custom-track") {
      const input = document.getElementById("customTrack"),
        v = clean(input?.value);
      if (v) {
        addTrack(v);
        renderTracks();
      }
      return;
    }
    if (action === "start-section-study") {
      ui.sectionIndex = 0;
      ui.expandedTrackId = null;
      return go("section-study");
    }
    if (action === "jump-section")
      return animateSectionTo(Number(b.dataset.index));
    if (action === "prev-section") {
      if (ui.sectionIndex > 0) return animateSectionTo(ui.sectionIndex - 1);
    }
    if (action === "next-section") {
      if (ui.sectionIndex < sections(p).length - 1)
        return animateSectionTo(ui.sectionIndex + 1);
      return go("map-summary");
    }
    if (action === "toggle-timeline-track") {
      ui.expandedTrackId =
        ui.expandedTrackId === b.dataset.trackId ? null : b.dataset.trackId;
      ui.selectedEventId = null;
      ui.selectedPresenceId = visiblePresence(
        p,
        b.dataset.trackId,
        ui.sectionIndex,
      )[0]?.range.id;
      return refreshArrangement();
    }
    if (action === "open-add-change")
      return openAddChangeSheet(
        b.dataset.targetType,
        b.dataset.targetId || null,
      );
    if (action === "toggle-section-silence") {
      const s = sections(p)[ui.sectionIndex],
        d = sectionData(p, s.id);
      if (d.silence) {
        d.silence = false;
        d.focusState = "";
      } else {
        tracks(p).forEach((t) =>
          subtractSectionFromTrack(p, t.id, ui.sectionIndex),
        );
        d.silence = true;
        d.focusIds = [];
        d.focusState = "none";
        invalidateDraftSection(p, s.id);
      }
      invalidateMapVerification(p);
      save();
      return renderSectionStudy();
    }
    if (action === "set-feel") {
      const d = sectionData(p, sections(p)[ui.sectionIndex].id);
      d.feel[b.dataset.scale] = b.dataset.value;
      invalidateMapVerification(p);
      save();
      return refreshStudySelections();
    }
    if (action === "toggle-focus") {
      const d = sectionData(p, sections(p)[ui.sectionIndex].id),
        id = b.dataset.trackId,
        i = d.focusIds.indexOf(id);
      if (i >= 0) d.focusIds.splice(i, 1);
      else d.focusIds.push(id);
      d.focusState = d.focusIds.length ? "selected" : "";
      invalidateMapVerification(p);
      save();
      return refreshStudySelections();
    }
    if (action === "focus-none") {
      const d = sectionData(p, sections(p)[ui.sectionIndex].id);
      d.focusIds = [];
      d.focusState = d.focusState === "none" ? "" : "none";
      invalidateMapVerification(p);
      save();
      return refreshStudySelections();
    }
    if (action === "summary-jump") {
      ui.sectionIndex = Number(b.dataset.index);
      ui.expandedTrackId = null;
      return go("section-study");
    }
    if (action === "toggle-map-verified") {
      if (!sectionStudyDone(p)) return;
      p.map.mapVerified = !p.map.mapVerified;
      if (!p.map.mapVerified) p.map.teachBack = false;
      save();
      return renderMapSummary();
    }
    if (action === "toggle-teach-back") {
      if (!p.map.mapVerified) return;
      p.map.teachBack = !p.map.teachBack;
      save();
      return renderMapSummary();
    }
    if (action === "toggle-session-track") {
      p.skeleton.session.tracks[b.dataset.trackId] =
        !p.skeleton.session.tracks[b.dataset.trackId];
      invalidateBounce(p);
      save();
      return refreshSkeletonChecks();
    }
    if (action === "toggle-session-marker") {
      p.skeleton.session.markers[b.dataset.sectionId] =
        !p.skeleton.session.markers[b.dataset.sectionId];
      invalidateBounce(p);
      save();
      return refreshSkeletonChecks();
    }
    if (action === "toggle-draft-part") {
      const s = sections(p).find((sec) => sec.id === b.dataset.sectionId),
        id = b.dataset.trackId;
      if (!s || !sessionDone(p)) return;
      p.skeleton.draft.parts[s.id] = p.skeleton.draft.parts[s.id] || {};
      p.skeleton.draft.parts[s.id][id] = !p.skeleton.draft.parts[s.id][id];
      invalidateBounce(p);
      save();
      return refreshDraftChecks();
    }
    if (action === "toggle-bounce-export") {
      p.skeleton.bounce.exported = !p.skeleton.bounce.exported;
      if (!p.skeleton.bounce.exported) p.skeleton.bounce.listened = false;
      save();
      return refreshSkeletonChecks();
    }
    if (action === "toggle-bounce-listen") {
      if (!p.skeleton.bounce.exported) return;
      p.skeleton.bounce.listened = !p.skeleton.bounce.listened;
      save();
      return refreshSkeletonChecks();
    }
    if (action === "toggle-spark-start") {
      toggleArray(p.spark.starts, b.dataset.name);
      save();
      return renderOriginalSpark();
    }
    if (action === "toggle-spark-reason") {
      toggleArray(p.spark.reasons, b.dataset.name);
      save();
      return renderOriginalSpark();
    }
  });
  app.addEventListener("input", (e) => {
    const p = project();
    if (e.target.id === "tempoInput") {
      p.map.setup.tempo = e.target.value;
      invalidateMapVerification(p);
      save();
      refreshMapProgress();
    }
    if (e.target.dataset.input === "phase-parking") {
      p.map.phaseParking = e.target.value;
      save();
    }
    if (e.target.dataset.input === "phase-takeaway") {
      p.map.phaseTakeaway = e.target.value;
      save();
    }
    if (e.target.dataset.input === "section-parking") {
      sectionData(p, sections(p)[ui.sectionIndex].id).parking = e.target.value;
      save();
    }
    if (e.target.dataset.input === "section-takeaway") {
      sectionData(p, sections(p)[ui.sectionIndex].id).takeaway = e.target.value;
      save();
    }
    if (e.target.dataset.input === "spark-idea") {
      p.spark.idea = e.target.value;
      save();
    }
    if (e.target.dataset.input === "spark-anchor") {
      p.spark.anchor = e.target.value;
      save();
    }
  });
  app.addEventListener("change", (e) => {
    if (e.target.id === "meterInput") {
      project().map.setup.meter = e.target.value;
      invalidateMapVerification(project());
      save();
      refreshMapProgress();
    }
  });
  app.addEventListener("keydown", (e) => {
    const reorder=e.target.closest('[data-drag-handle]');
    if(reorder && ['ArrowUp','ArrowDown'].includes(e.key)) {
      e.preventDefault();const id=reorder.closest('[data-section-id]').dataset.sectionId;
      moveSection(project(),id,sectionIndexById(project(),id)+(e.key==='ArrowUp'?-1:1));renderStructure();
      app.querySelector(`[data-section-id="${id}"] [data-drag-handle]`)?.focus({preventScroll:true});return;
    }

    if (
      (e.key === "Enter" || e.key === " ") &&
      e.target.matches(".structure-row, [data-drag-handle]")
    ) {
      e.preventDefault();
      return openSectionSheet(e.target.closest("[data-section-id]").dataset.sectionId);
    }
    if (e.key !== "Enter" || e.shiftKey || e.isComposing) return;
    if (e.target.id === "newTitle") {
      e.preventDefault();
      document.getElementById("newArtist")?.focus({ preventScroll: true });
      return;
    }
    if (e.target.id === "newArtist") {
      e.preventDefault();
      app.querySelector('[data-action="create-project"]')?.click();
      return;
    }
    if (e.target.id === "customTrack") {
      e.preventDefault();
      document.querySelector('[data-action="add-custom-track"]')?.click();
    }
  });

  sheetRoot.addEventListener("click", (e) => {
    if (e.target === sheetRoot) return closeSheet();
    const b = e.target.closest("[data-action]");
    if (!b || b.disabled || ui.animating) return;
    const action = b.dataset.action,
      p = project();
    if (action === "close-sheet") return closeSheet();
    if (action === "choose-section-type") {
      const d = sectionDraft;
      d.name = b.dataset.name;
      d.canAdd = true;
      d.customName = d.name === "Custom";
      if (!d.bars) d.bars = suggestedBarsFor(p, d.name);
      renderSectionBuilder();
      return;
    }
    if (action === "set-new-section-bars") {
      sectionDraft.canAdd = true;
      sectionDraft.customBars = b.dataset.bars === "custom";
      sectionDraft.bars = sectionDraft.customBars
        ? null
        : Number(b.dataset.bars);
      renderSectionBuilder();
      return;
    }
    if (action === "save-new-section") {
      const d = sectionDraft, name = d.customName ? clean(d.typedName) : d.name;
      if (!d.canAdd) return;
      if (!name || !validBars(d.bars)) return sheetError("Choose a section and bar length.");
      // A new intentional choice/input re-arms Add; a double click cannot add twice.
      d.canAdd = false;
      const added = addSection(name, d.bars);
      if (!added) { d.canAdd = true; return; }
      d.added++;
      renderStructure();
      renderSectionBuilder();
      document.getElementById("builderStatus").textContent = `Added ${name} · ${d.bars} bars`;
      document.getElementById("sheetError").textContent = "";
      sheetRoot.querySelector('[data-action="choose-section-type"][aria-pressed="true"]')?.focus({ preventScroll: true });
      return;
    }
    if (action === "set-sheet-bars") {
      const input = document.getElementById("sectionBars");
      input.hidden = b.dataset.bars !== "custom";
      if (input.hidden) input.value = b.dataset.bars;
      sheetRoot
        .querySelectorAll('[data-action="set-sheet-bars"]')
        .forEach((x) => setSelected(x, x === b));
      return;
    }
    if (action === "save-section") {
      const s = sections(p).find((x) => x.id === b.dataset.id),
        name = clean(document.getElementById("renameSection")?.value),
        bars = Number(document.getElementById("sectionBars")?.value);
      if (!s || !name || !validBars(bars)) {
        sheetError("Add a name and whole-number bar length.");
        return;
      }
      const sectionIndex = sectionIndexById(p, s.id),
        lengthChanged = Number(s.lengthBars) !== bars,
        nameChanged = s.name !== name;
      s.name = name;
      s.lengthBars = bars;
      if (lengthChanged || nameChanged) invalidateStructureVerification(p);
      if (lengthChanged) {
        p.map.timeline.presence.forEach((r) => {
          if (r.start.sectionId === s.id && r.start.bar !== "end")
            r.start.bar = clamp(Number(r.start.bar) || 0, 0, bars - 1);
          if (r.end && r.end.sectionId === s.id && r.end.bar !== "end")
            r.end.bar = clamp(Number(r.end.bar) || 1, 1, bars);
        });
        p.map.timeline.events.forEach((ev) => {
          if (ev.kind === "marker" && ev.point.sectionId === s.id)
            ev.point.bar = clamp(Number(ev.point.bar) || 0, 0, bars - 1);
          if (ev.kind === "range") {
            if (ev.start.sectionId === s.id && ev.start.bar !== "end")
              ev.start.bar = clamp(Number(ev.start.bar) || 0, 0, bars - 1);
            if (ev.end && ev.end.sectionId === s.id && ev.end.bar !== "end")
              ev.end.bar = clamp(Number(ev.end.bar) || 1, 1, bars);
          }
        });
        tracks(p).forEach((t) => mergePresenceForTrack(p, t.id, false));
        invalidateMarkersFrom(p, sectionIndex);
        invalidateDraftSection(p, s.id);
      }
      save();
      closeSheet();
      return renderStructure();
    }
    if (action === "choose-change") {
      const before = copyProject(),
        targetType = b.dataset.targetType,
        targetId = b.dataset.targetId || null,
        label = b.dataset.label,
        meta = changeMeta(label);
      if (
        targetType === "track" &&
        !visiblePresence(p, targetId, ui.sectionIndex).length
      )
        return;
      const ev = {
        id: uid(),
        targetType,
        targetId,
        label,
        ...meta,
        ...defaultEventPosition(p, targetType, targetId, meta.kind),
      };
      p.map.timeline.events.push(ev);
      reconcileStateProperty(p, ev);
      invalidateMapVerification(p);
      invalidateEventDraft(p, ev, sectionIdsForEvent(p, ev));
      ui.selectedEventId = ev.id;
      ui.selectedPresenceId = null;
      closeSheet();
      save();
      offerUndo(before, "Change added");
      return renderSectionStudy();
    }
    if (action === "export-backup") return exportBackup();
    if (action === "import-backup") {
      document.getElementById("importFile").click();
      return;
    }
    if (action === "reset-project") {
      if (confirm(`Reset ${p.title}? This clears its saved progress.`)) {
        const fresh =
          p.type === "study"
            ? makeStudyProject(p.title, p.artist)
            : makeOriginalProject(p.title);
        fresh.id = p.id;
        db.projects[db.projects.findIndex((x) => x.id === p.id)] = fresh;
        save();
        closeSheet();
        go("project");
      }
      return;
    }
    if (action === "delete-project") {
      if (confirm("Delete this project?")) {
        db.projects = db.projects.filter((x) => x.id !== b.dataset.id);
        if (db.currentProjectId === b.dataset.id)
          db.currentProjectId = db.projects[0]?.id || null;
        save();
        closeSheet();
        go("projects");
      }
      return;
    }
  });

  function toggleArray(arr, val) {
    const i = arr.indexOf(val);
    if (i >= 0) arr.splice(i, 1);
    else arr.push(val);
  }
  function exportBackup() {
    const blob = new Blob([JSON.stringify(db, null, 2)], {
        type: "application/json",
      }),
      url = URL.createObjectURL(blob),
      a = document.createElement("a");
    a.href = url;
    a.download = "babel-fire-backup.json";
    a.click();
    setTimeout(() => URL.revokeObjectURL(url), 1000);
  }
  document
    .getElementById("importFile")
    .addEventListener("change", async (e) => {
      const file = e.target.files?.[0];
      if (!file) return;
      try {
        const parsed = JSON.parse(await file.text());
        if (!parsed || !Array.isArray(parsed.projects)) throw new Error();
        const normalized = normalizeDatabase(parsed);
        db = normalized;
        clearUndo();
        persist();
        closeSheet();
        ui = {
          route: "projects",
          sectionIndex: 0,
          newType: "original",
          expandedTrackId: null,
          animating: false,
        };
        history.replaceState(
          {
            route: "projects",
            projectId: db.currentProjectId,
            fromRoute: null,
            fromLabel: null,
          },
          "",
          location.pathname + location.search,
        );
        render();
      } catch (err) {
        alert("That backup could not be imported.");
      } finally {
        e.target.value = "";
      }
    });

  // Editor state is transient. Only musical anchors and project progress are persisted.
  let undoState = null;
  function copyProject() {
    return JSON.parse(JSON.stringify(project()));
  }
  function clearUndo() {
    undoState = null;
    const notice = document.getElementById("undoNotice");
    if (notice) {
      notice.hidden = true;
      notice.replaceChildren();
    }
  }
  function offerUndo(before, message) {
    undoState = before;
    const notice = document.getElementById("undoNotice");
    notice.innerHTML = `<span>${esc(message)}</span><button id="undoEdit">Undo</button>`;
    notice.hidden = false;
    document.getElementById("undoEdit").onclick = () => {
      const prior = undoState;
      if (!prior) return;
      const i = db.projects.findIndex((p) => p.id === prior.id);
      if (i < 0) return;
      db.projects[i] = prior;
      db.currentProjectId = prior.id;
      clearUndo();
      persist();
      render();
    };
  }
  function selectedObject(type, id) {
    return type === "presence"
      ? project().map.timeline.presence.find((r) => r.id === id)
      : project().map.timeline.events.find((e) => e.id === id);
  }
  function finishTimelineEdit(before, obj, type, message) {
    const p = project(),
      old =
        type === "presence"
          ? before.map.timeline.presence.find((x) => x.id === obj.id)
          : before.map.timeline.events.find((x) => x.id === obj.id);
    if (JSON.stringify(old) === JSON.stringify(obj)) return renderSectionStudy();
    if (type === "presence") {
      const ids = [
        ...sectionIdsForRange(before, old),
        ...sectionIdsForRange(p, obj),
      ];
      mergePresenceForTrack(p, obj.trackId, false);
      if (
        !p.map.timeline.presence.some((r) => r.id === ui.selectedPresenceId)
      ) {
        const position = anchorAbs(p, obj.start);
        ui.selectedPresenceId = visiblePresence(
          p,
          obj.trackId,
          ui.sectionIndex,
        ).find(({ range }) => {
          const a = rangeAbs(p, range);
          return position >= a.start && position < a.end;
        })?.range.id;
      }
      reconcileTrackEvents(p, obj.trackId, before);
      normalizeAllFocus(p);
      invalidateDraftTrack(p, obj.trackId, ids);
    } else {
      const ids = [
        ...sectionIdsForEvent(before, old),
        ...sectionIdsForEvent(p, obj),
      ];
      reconcileStateProperty(p, obj);
      invalidateEventDraft(p, obj, ids);
    }
    invalidateMapVerification(p);
    save();
    offerUndo(before, message);
    const timelineX=app.querySelector(".timeline-scroll")?.scrollLeft || 0;
    const y = scrollY, notesOpen = !!app.querySelector(".note-disclosure")?.open;
    renderSectionStudy();
    if (notesOpen && app.querySelector(".note-disclosure")) app.querySelector(".note-disclosure").open = true;
    window.scrollTo(0, y);
    if(app.querySelector(".timeline-scroll"))app.querySelector(".timeline-scroll").scrollLeft=timelineX;
  }
  // Intersect changes with their parent's actual presence. Retain the original ID on
  // the first surviving piece; only a real new piece needs a new identity.
  function reconcileTrackEvents(p, trackId, before) {
    const spans = presenceForTrack(p, trackId)
      .map((r) => ({ r, ...rangeAbs(p, r) }))
      .sort((a, b) => a.start - b.start);
    const out = [];
    for (const e of p.map.timeline.events) {
      if (e.targetType !== "track" || e.targetId !== trackId) {
        out.push(e);
        continue;
      }
      if (e.kind === "marker") {
        const point = anchorAbs(p, e.point);
        if (spans.some((s) => point >= s.start && point < s.end)) out.push(e);
        continue;
      }
      const previous = before?.map.timeline.events.find(
        (old) => old.id === e.id,
      );
      const a = previous ? rangeAbs(before, previous) : rangeAbs(p, e);
      if (previous?.end == null && previous) {
        const holder = presenceForTrack(before, trackId).find((r) => {
          const span = rangeAbs(before, r);
          return a.start >= span.start && a.start < span.end;
        });
        const retained =
          holder &&
          presenceForTrack(p, trackId).find((r) => r.id === holder.id);
        if (retained) a.end = Math.max(a.end, rangeAbs(p, retained).end);
      }
      let count = 0;
      for (const span of spans) {
        const start = Math.max(a.start, span.start),
          end = Math.min(a.end, span.end);
        if (end <= start) continue;
        out.push({
          ...e,
          id: count++ === 0 ? e.id : uid(),
          start: anchorAtAbs(p, start),
          end:
            e.end == null && span.r.end == null
              ? null
              : anchorAtAbs(p, end, true),
        });
      }
    }
    p.map.timeline.events = out;
  }
  function applyTiming(obj, type, edge, boundary) {
    const p = project(),
      s = sections(p)[ui.sectionIndex],
      len = Number(s.lengthBars),
      old = JSON.parse(JSON.stringify(obj));
    if (edge === "point") {
      obj.point = { sectionId: s.id, bar: clamp(boundary, 0, len - 1) };
      const pos = anchorAbs(p, obj.point);
      if (!eventCoveredByPresence(p, obj, pos, pos + 1e-6)) {
        Object.assign(obj, old);
        return false;
      }
    } else {
      const value = clamp(
        boundary,
        edge === "end" && anchorAbs(p, obj.start) >= sectionStarts(p)[ui.sectionIndex] ? 1 : 0,
        edge === "end" ? len : len - 1,
      );
      obj[edge] = {
        sectionId: s.id,
        bar: edge === "end" && value === len ? "end" : value,
      };
      const a = rangeAbs(p, obj);
      if (type === "presence") {
        const original = selectedObject(type,obj.id), span = rangeAbs(p,original);
        const others = presenceForTrack(p,obj.trackId).filter(r=>r.id!==obj.id).map(r=>rangeAbs(p,r));
        const previous = others.filter(r=>r.end<=span.start).reduce((v,r)=>Math.max(v,r.end),-Infinity);
        const next = others.filter(r=>r.start>=span.end).reduce((v,r)=>Math.min(v,r.start),Infinity);
        if (a.start < previous || a.end > next) { Object.assign(obj,old); return false; }
      }
      if (
        !(a.end > a.start) ||
        (type === "event" && !eventCoveredByPresence(p, obj, a.start, a.end))
      ) {
        Object.assign(obj, old);
        return false;
      }
    }
    return true;
  }
  app.addEventListener("click", (e) => {
    const b = e.target.closest("[data-action]");
    if (!b || b.disabled || ui.animating) return;
    const action = b.dataset.action,
      p = project();
    if (action === "select-presence") {
      clearBoundarySelection();
      ui.expandedTrackId = b.dataset.trackId;
      ui.selectedPresenceId = b.dataset.rangeId;
      ui.selectedEventId = null;
        return refreshArrangement();
    }
    if (action === "select-event") {
      clearBoundarySelection();
      const ev = p.map.timeline.events.find((x) => x.id === b.dataset.eventId);
      if (!ev) return;
      ui.selectedEventId = ev.id;
      ui.selectedPresenceId = null;
        return refreshArrangement();
    }
    if (action === "remove-selected") {
      const type = b.dataset.kind,
        obj = selectedObject(type, b.dataset.id);
      if (!obj) return;
      const before = copyProject();
      if (type === "presence") {
        p.map.timeline.presence = p.map.timeline.presence.filter(
          (x) => x.id !== obj.id,
        );
        reconcileTrackEvents(p, obj.trackId, before);
        normalizeAllFocus(p);
        invalidateDraftTrack(p, obj.trackId, sectionIdsForRange(before, obj));
        ui.selectedPresenceId = null;
      } else {
        p.map.timeline.events = p.map.timeline.events.filter(
          (x) => x.id !== obj.id,
        );
        invalidateEventDraft(p, obj, sectionIdsForEvent(before, obj));
        ui.selectedEventId = null;
      }
      invalidateMapVerification(p);
      save();
      offerUndo(
        before,
        type === "presence" ? "Presence removed" : "Change removed",
      );
      return renderSectionStudy();
    }

  });
  sheetRoot.addEventListener("input", (e) => {
    if (!sectionDraft) return;
    if (e.target.id === "newSectionName") {
      sectionDraft.typedName = e.target.value;
      sectionDraft.canAdd = true;
    }
    if (e.target.id === "newSectionBars") {
      sectionDraft.bars = Number(e.target.value);
      sectionDraft.canAdd = true;
    }
    const d = sectionDraft,
      button = sheetRoot.querySelector('[data-action="save-new-section"]');
    if (button)
      button.disabled =
        !d.canAdd || !d.name || !validBars(d.bars) || (d.customName && !clean(d.typedName));
  });

  sheetRoot.addEventListener("keydown", (e) => {
    if (e.key === "Escape") {
      e.preventDefault();
      closeSheet();
      return;
    }
    if (e.key !== "Tab") return;
    const controls = [
      ...sheetRoot.querySelectorAll(
        "button:not(:disabled),input:not([hidden]),select",
      ),
    ].filter((el) => el.getClientRects().length);
    const first = controls[0],
      last = controls.at(-1);
    if (e.shiftKey && (document.activeElement === first || document.activeElement === sheetRoot.querySelector("h3"))) {
      e.preventDefault();
      last?.focus();
    } else if (!e.shiftKey && (document.activeElement === last || document.activeElement === sheetRoot.querySelector("h3"))) {
      e.preventDefault();
      first?.focus();
    }
  });
  initHistory();
  render();
})();
