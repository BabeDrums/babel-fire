(() => {
  "use strict";

  const SOURCE_KEY = "production-projects-v1";
  const PREVIEW_KEY = "production-projects-v1-v7-preview";
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
  const SECTION_TYPES = [
    "Intro",
    "Verse",
    "Pre-Chorus",
    "Chorus",
    "Bridge",
    "Instrumental",
    "Outro",
  ];

  const app = document.getElementById("app");
  const sheetRoot = document.getElementById("sheetRoot");
  const esc = (value) =>
    String(value ?? "").replace(/[&<>"']/g, (char) => ({
      "&": "&amp;",
      "<": "&lt;",
      ">": "&gt;",
      '"': "&quot;",
      "'": "&#39;",
    })[char]);
  const clean = (value) => String(value ?? "").trim();
  const uid = () => crypto?.randomUUID?.() || `preview-${Date.now()}-${Math.random().toString(36).slice(2)}`;
  const deepCopy = (value) => JSON.parse(JSON.stringify(value));

  function seedDb() {
    const project = {
      id: "preview-creep",
      type: "study",
      schemaVersion: 5,
      title: "Creep",
      artist: "Radiohead",
      createdAt: Date.now(),
      notes: [],
      map: {
        setup: { reference: false, tempo: "", meter: "4/4", grid: false, firstListen: false },
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
    };
    return { version: 5, currentProjectId: project.id, projects: [project] };
  }

  function normalizeProject(project) {
    project.title = clean(project.title) || "Untitled";
    project.artist = clean(project.artist || "");
    project.notes = Array.isArray(project.notes) ? project.notes : [];
    if (project.type !== "study") return project;
    project.map = project.map || {};
    project.map.setup = {
      reference: !!project.map.setup?.reference,
      tempo: String(project.map.setup?.tempo || ""),
      meter: project.map.setup?.meter || "4/4",
      grid: !!project.map.setup?.grid,
      firstListen: !!project.map.setup?.firstListen,
    };
    project.map.sections = Array.isArray(project.map.sections) ? project.map.sections : [];
    project.map.sections = project.map.sections.map((section) => ({
      id: section?.id || uid(),
      name: clean(section?.name) || "Section",
      lengthBars: Number(section?.lengthBars) || 8,
    }));
    project.map.structureVerified = !!project.map.structureVerified;
    project.map.tracks = Array.isArray(project.map.tracks) ? project.map.tracks : [];
    project.map.tracks = project.map.tracks
      .map((track) => typeof track === "string" ? { id: uid(), name: track } : { id: track?.id || uid(), name: clean(track?.name) })
      .filter((track) => track.name);
    project.map.timeline = project.map.timeline || { presence: [], events: [] };
    project.map.sectionData = project.map.sectionData || {};
    project.skeleton = project.skeleton || {
      session: { tracks: {}, markers: {} },
      draft: { parts: {} },
      bounce: { exported: false, listened: false },
    };
    return project;
  }

  function normalizeDb(candidate) {
    const db = candidate && Array.isArray(candidate.projects) ? candidate : seedDb();
    db.version = 5;
    db.projects = db.projects.map(normalizeProject);
    if (!db.projects.some((project) => project.id === db.currentProjectId)) {
      db.currentProjectId = db.projects[0]?.id || null;
    }
    return db;
  }

  function cloneProductionDb() {
    try {
      const source = JSON.parse(localStorage.getItem(SOURCE_KEY));
      if (source && Array.isArray(source.projects) && source.projects.length) return normalizeDb(deepCopy(source));
    } catch (error) {}
    return seedDb();
  }

  function loadDb() {
    if (new URLSearchParams(location.search).get("reset") === "1") {
      const fresh = cloneProductionDb();
      localStorage.setItem(PREVIEW_KEY, JSON.stringify(fresh));
      return fresh;
    }
    try {
      const saved = JSON.parse(localStorage.getItem(PREVIEW_KEY));
      if (saved && Array.isArray(saved.projects)) return normalizeDb(saved);
    } catch (error) {}
    const fresh = cloneProductionDb();
    localStorage.setItem(PREVIEW_KEY, JSON.stringify(fresh));
    return fresh;
  }

  let db = loadDb();
  let currentRoute = "projects";
  let sheetState = null;

  function save() {
    localStorage.setItem(PREVIEW_KEY, JSON.stringify(db));
  }

  function project() {
    return db.projects.find((item) => item.id === db.currentProjectId) || null;
  }

  function setupComplete(project) {
    if (project?.type !== "study") return false;
    const setup = project.map.setup;
    return !!setup.reference && Number(setup.tempo) > 0 && !!setup.meter && !!setup.grid && !!setup.firstListen;
  }

  function structureComplete(project) {
    return !!project?.map?.structureVerified && (project?.map?.sections?.length || 0) > 0;
  }

  function tracksComplete(project) {
    return (project?.map?.tracks?.length || 0) > 0;
  }

  function recommendedWork(project) {
    if (!setupComplete(project)) return "setup";
    if (!structureComplete(project)) return "structure";
    if (!tracksComplete(project)) return "tracks";
    return "section-study";
  }

  const WORK = {
    setup: { title: "Song Setup", copy: "Prepare the reference before studying it." },
    structure: { title: "Structure", copy: "Build the song one section at a time." },
    tracks: { title: "Tracks", copy: "Choose everything that appears somewhere in the song." },
    "section-study": { title: "Section Study", copy: "Study what changes from section to section." },
  };

  function workDone(project, route) {
    if (route === "setup") return setupComplete(project);
    if (route === "structure") return structureComplete(project);
    if (route === "tracks") return tracksComplete(project);
    return false;
  }

  function topbar(left = "", right = "") {
    return `<header class="topbar"><div>${left}</div><div>${right}</div></header>`;
  }

  function backButton(label, route) {
    return `<button class="back" data-route="${route}" data-nav="replace"><span class="arrow" aria-hidden="true">‹</span><span>${esc(label)}</span></button>`;
  }

  function pageHeader(title, copy) {
    return `<div class="page-header"><h1>${esc(title)}</h1>${copy ? `<p class="sub">${esc(copy)}</p>` : ""}</div>`;
  }

  function setHistory(route, mode = "push") {
    const state = { v7Preview: true, route };
    const hash = `#${route}`;
    if (mode === "replace") history.replaceState(state, "", hash);
    else history.pushState(state, "", hash);
  }

  function navigate(route, mode = "push") {
    closeSheet(false);
    currentRoute = route;
    setHistory(route, mode);
    render();
    window.scrollTo(0, 0);
  }

  function continueTo(route) {
    navigate(route, "replace");
  }

  function renderProjects() {
    const rows = db.projects.map((item) => {
      const meta = item.type === "study" ? `${item.artist || "Unknown artist"} · Recreation` : `${item.artist || "Original"} · Original`;
      return `<button class="project-row" data-project="${esc(item.id)}"><span><strong>${esc(item.title)}</strong><span>${esc(meta)}</span></span><span class="chevron" aria-hidden="true">›</span></button>`;
    }).join("");
    app.innerHTML = `<main class="screen scroll-safe">${topbar("", "")}<div class="projects-header">${pageHeader("Projects", "Your songs.")}</div><div class="project-list">${rows || `<div class="empty-state">No preview projects.</div>`}</div><p class="preview-note">V7 Preview · This uses a sandbox copy of your FIRE data, so testing here won’t change the live app. <button data-action="refresh-preview">Refresh copy</button></p></main>`;
  }

  function renderProjectHome() {
    const item = project();
    if (!item) return navigate("projects", "replace");
    if (item.type !== "study") {
      app.innerHTML = `<main class="screen">${topbar(backButton("Projects", "projects"), "")} ${pageHeader(item.title, "Original workflow is not part of this shell prototype yet.")}<div class="prereq-card"><p class="prototype-end">This preview is intentionally proving the Recreation shell first.</p></div></main>`;
      return;
    }
    const recommended = recommendedWork(item);
    const rec = WORK[recommended];
    const workRows = ["setup", "structure", "tracks", "section-study"].map((route) => {
      const done = workDone(item, route);
      const isRecommended = route === recommended;
      let trailing = `<span class="chevron" aria-hidden="true">›</span>`;
      if (done) trailing = `<span class="checkmark" aria-label="Done">✓</span>`;
      else if (isRecommended) trailing = `<span class="trailing">Continue <span class="chevron" aria-hidden="true">›</span></span>`;
      return `<button class="row journey-row${done ? " done" : ""}${isRecommended ? " recommended" : ""}" data-route="${route}"><span class="row-title">${esc(WORK[route].title)}</span>${trailing}</button>`;
    }).join("");
    const notesCount = Array.isArray(item.notes) ? item.notes.filter((note) => clean(typeof note === "string" ? note : note?.text)).length : 0;
    const future = ["The Skeleton", "The Sounds", "The Balance", "The Shape", "The World", "The Finish"].map((name) => `<div class="future-row"><strong>${esc(name)}</strong><span>Later</span></div>`).join("");
    app.innerHTML = `<main class="screen scroll-safe">${topbar(backButton("Projects", "projects"), `<button class="top-action" data-action="project-actions" aria-label="Project actions">•••</button>`)}<div class="project-identity"><h1>${esc(item.title)}</h1><p class="sub">${esc(item.artist || "Unknown artist")} · Recreation</p></div><div class="section-title"><span>Continue</span></div><button class="continue-card" data-route="${recommended}"><span><span class="continue-eyebrow">Recommended</span><span class="continue-title">${esc(rec.title)}</span><span class="continue-copy">${esc(rec.copy)}</span></span><span class="continue-arrow" aria-hidden="true">›</span></button><div class="section-title"><span>Journey</span></div><section class="journey"><div class="phase-block"><div class="phase-head"><strong>The Map</strong><span>In progress</span></div>${workRows}<div class="row journey-row" aria-disabled="true"><span class="row-title">Review Map</span><span class="trailing">Later</span></div></div><div class="future-phases">${future}</div></section><div class="project-notes-row"><button class="row" data-route="notes"><span><span class="row-title">Notes</span><span class="row-sub">${notesCount ? `${notesCount} saved note${notesCount === 1 ? "" : "s"}` : "Questions, takeaways, and ideas."}</span></span><span class="chevron" aria-hidden="true">›</span></button></div></main>`;
  }

  function setupRow(label, field, value, help = "") {
    const checked = !!value;
    return `<button class="form-row" data-action="toggle-setup" data-field="${field}"><span><span class="form-label">${esc(label)}</span>${help ? `<span class="form-help">${esc(help)}</span>` : ""}</span><span class="form-value">${checked ? `<span>${field === "reference" ? "Imported" : "Done"}</span><span class="checkmark" aria-hidden="true">✓</span>` : `<span>${field === "reference" ? "Import" : "Mark done"}</span>`}</span></button>`;
  }

  function renderSetup() {
    const item = project();
    if (!item || item.type !== "study") return navigate("project", "replace");
    const setup = item.map.setup;
    app.innerHTML = `<main class="screen">${topbar(backButton(item.title, "project"), "")} ${pageHeader("Song Setup", "Prepare the reference before studying it.")}<div class="form-group">${setupRow("Reference", "reference", setup.reference)}<div class="form-row"><span class="form-label">Tempo</span><span class="form-value"><input id="tempoInput" class="inline-input" inputmode="decimal" aria-label="Tempo" value="${esc(setup.tempo)}" placeholder="—"><span>BPM</span></span></div><div class="form-row"><span class="form-label">Meter</span><select id="meterInput" class="inline-select" aria-label="Meter"><option ${setup.meter === "4/4" ? "selected" : ""}>4/4</option><option ${setup.meter === "3/4" ? "selected" : ""}>3/4</option><option ${setup.meter === "6/8" ? "selected" : ""}>6/8</option></select></div>${setupRow("Grid", "grid", setup.grid, "Align the reference to the bar grid.")}${setupRow("First Listen", "firstListen", setup.firstListen, "Play the full song once without stopping.")}</div><div class="action-row"><button id="setupContinue" class="primary-action" data-action="continue-structure" ${setupComplete(item) ? "" : "disabled"}>Continue to Structure</button></div></main>`;
  }

  function renderStructure() {
    const item = project();
    if (!item || item.type !== "study") return navigate("project", "replace");
    const sections = item.map.sections;
    const rows = sections.map((section, index) => `<button class="arrangement-row" data-action="edit-section" data-section-id="${esc(section.id)}"><span class="arrangement-index">${index + 1}</span><span class="arrangement-name">${esc(section.name)}</span><span class="arrangement-bars">${Number(section.lengthBars) || 8} bars ›</span></button>`).join("");
    app.innerHTML = `<main class="screen scroll-safe">${topbar(backButton(item.title, "project"), "")} ${pageHeader("Structure", "Build the song one section at a time.")}<div class="arrangement">${rows || `<div class="empty-state">No sections yet.<br>Add the first part you hear.</div>`}</div><button class="add-row" data-action="open-add-section"><span aria-hidden="true">＋</span> Add Section</button>${sections.length ? `<button class="confirm-row" data-action="toggle-structure-verified"><span><span class="row-title">Structure matches the song</span><span class="row-sub">Confirm after the order and lengths feel right.</span></span>${item.map.structureVerified ? `<span class="checkmark" aria-hidden="true">✓</span>` : `<span class="trailing">Confirm</span>`}</button>` : ""}<div class="action-row"><button class="primary-action" data-action="continue-tracks" ${structureComplete(item) ? "" : "disabled"}>Continue to Tracks</button></div></main>`;
  }

  function renderTracks() {
    const item = project();
    if (!item || item.type !== "study") return navigate("project", "replace");
    const selectedNames = new Set(item.map.tracks.map((track) => track.name));
    const extra = item.map.tracks.map((track) => track.name).filter((name) => !COMMON_TRACKS.includes(name));
    const names = [...COMMON_TRACKS, ...extra];
    const tiles = names.map((name) => `<button class="track-tile${selectedNames.has(name) ? " selected" : ""}" data-action="toggle-track" data-name="${esc(name)}" aria-pressed="${selectedNames.has(name)}">${esc(name)}</button>`).join("");
    app.innerHTML = `<main class="screen scroll-safe">${topbar(backButton(item.title, "project"), "")} ${pageHeader("Tracks", "Select everything that appears somewhere in the song.")}<div class="track-grid">${tiles}</div><div class="custom-track"><input id="customTrackInput" class="field" placeholder="Other…" aria-label="Other track"><button class="compact-button" data-action="add-custom-track">Add</button></div><div class="action-row"><button class="primary-action" data-action="continue-section-study" ${tracksComplete(item) ? "" : "disabled"}>Continue to Section Study</button></div></main>`;
  }

  function renderSectionStudy() {
    const item = project();
    if (!item || item.type !== "study") return navigate("project", "replace");
    const missingStructure = item.map.sections.length === 0;
    const missingTracks = item.map.tracks.length === 0;
    let body = "";
    if (missingStructure || missingTracks) {
      const actions = [missingStructure ? `<button data-route="structure">Add the song structure <span class="chevron">›</span></button>` : "", missingTracks ? `<button data-route="tracks">Choose the tracks <span class="chevron">›</span></button>` : ""].join("");
      body = `<div class="prereq-card"><h3>A little more context will make this useful.</h3><p>Section Study needs a song structure and at least one track. Nothing is locked — FIRE is just pointing you to what’s missing.</p><div class="prereq-actions">${actions}</div></div>`;
    } else {
      body = `<div class="prereq-card"><h3>The shell prototype stops here.</h3><p class="prototype-end">Your structure and tracks are ready. We’re proving that Project Home → focused work feels better before migrating the full Section Study timeline editor.</p></div>`;
    }
    app.innerHTML = `<main class="screen">${topbar(backButton(item.title, "project"), "")} ${pageHeader("Section Study", "Study what changes from section to section.")}${body}<div class="action-row"><button class="primary-action" data-route="project" data-nav="replace">Back to Project</button></div></main>`;
  }

  function renderNotes() {
    const item = project();
    if (!item) return navigate("projects", "replace");
    const notes = (Array.isArray(item.notes) ? item.notes : []).map((note, index) => {
      const entry = typeof note === "string" ? { type: "General", context: "Project", text: note } : note;
      if (!clean(entry?.text)) return "";
      return `<article class="note-card"><div class="meta">${esc(entry.type || "General")} · ${esc(entry.context || "Project")}</div><p>${esc(entry.text)}</p></article>`;
    }).join("");
    app.innerHTML = `<main class="screen scroll-safe">${topbar(backButton(item.title, "project"), "")} ${pageHeader("Notes", "Your project notes, in one place.")}<div class="notes-list">${notes || `<div class="empty-state">No saved notes yet.</div>`}</div><p class="preview-note">The cross-project Notes hub comes after this shell is approved.</p></main>`;
  }

  function render() {
    if (currentRoute === "projects") return renderProjects();
    if (currentRoute === "project") return renderProjectHome();
    if (currentRoute === "setup") return renderSetup();
    if (currentRoute === "structure") return renderStructure();
    if (currentRoute === "tracks") return renderTracks();
    if (currentRoute === "section-study") return renderSectionStudy();
    if (currentRoute === "notes") return renderNotes();
    navigate("projects", "replace");
  }

  function openSheet(html, state = null) {
    sheetState = state;
    sheetRoot.innerHTML = `<div class="sheet" role="dialog" aria-modal="true">${html}</div>`;
    sheetRoot.hidden = false;
    document.body.style.overflow = "hidden";
  }

  function closeSheet(clear = true) {
    if (sheetRoot.hidden) return;
    sheetRoot.hidden = true;
    sheetRoot.innerHTML = "";
    document.body.style.overflow = "";
    if (clear) sheetState = null;
  }

  function openAddSectionSheet() {
    const choices = SECTION_TYPES.map((name) => `<button class="sheet-choice" data-action="quick-add-section" data-name="${esc(name)}">${esc(name)}</button>`).join("");
    openSheet(`<div class="grabber"></div><h2>Add section</h2><p class="sheet-sub">Pick the section you hear. FIRE adds it at 8 bars; tap it afterward if you want to change the length.</p><div class="sheet-grid">${choices}<button class="sheet-choice" data-action="show-custom-section">Custom</button></div><div id="customSectionArea"></div><div class="sheet-actions"><button class="sheet-close" data-action="close-sheet">Cancel</button></div>`, { type: "add-section" });
  }

  function openEditSectionSheet(sectionId) {
    const item = project();
    const section = item?.map?.sections?.find((entry) => entry.id === sectionId);
    if (!section) return;
    const selectedBars = Number(section.lengthBars) || 8;
    const bars = [4, 8, 12, 16].map((value) => `<button class="${selectedBars === value ? "selected" : ""}" data-action="edit-section-bars" data-bars="${value}">${value}</button>`).join("");
    const index = item.map.sections.findIndex((entry) => entry.id === sectionId);
    openSheet(`<div class="grabber"></div><h2>Edit section</h2><p class="sheet-sub">Adjust the label or length without leaving Structure.</p><input id="editSectionName" class="field" value="${esc(section.name)}" aria-label="Section name"><div class="bars-grid">${bars}</div><div class="move-row"><button data-action="move-section" data-direction="up" ${index === 0 ? "disabled" : ""}>Move Up</button><button data-action="move-section" data-direction="down" ${index === item.map.sections.length - 1 ? "disabled" : ""}>Move Down</button></div><div class="sheet-actions"><button class="compact-button" data-action="save-section">Save</button><button class="sheet-close" data-action="duplicate-section">Duplicate</button><button class="sheet-close sheet-danger" data-action="delete-section">Delete</button></div>`, { type: "edit-section", sectionId, bars: selectedBars });
  }

  function openProjectActions() {
    const item = project();
    if (!item) return;
    openSheet(`<div class="grabber"></div><h2>${esc(item.title)}</h2><p class="sheet-sub">Preview actions only affect the sandbox copy.</p><div class="group"><button class="row" data-action="edit-project"><span class="row-title">Edit Project</span><span class="chevron">›</span></button><button class="row" data-action="reset-project-preview"><span><span class="row-title">Reset Preview Progress</span><span class="row-sub">Keeps title, artist, and notes.</span></span><span></span></button><button class="row sheet-danger" data-action="delete-project-preview"><span class="row-title">Remove from Preview</span><span></span></button></div><div class="sheet-actions"><button class="sheet-close" data-action="close-sheet">Cancel</button></div>`, { type: "project-actions" });
  }

  function openEditProjectSheet() {
    const item = project();
    if (!item) return;
    openSheet(`<div class="grabber"></div><h2>Edit project</h2><p class="sheet-sub">Title and artist only.</p><input id="editProjectTitle" class="field" value="${esc(item.title)}" aria-label="Song title"><div style="height:10px"></div><input id="editProjectArtist" class="field" value="${esc(item.artist || "")}" aria-label="Artist"><div class="sheet-actions"><button class="compact-button" data-action="save-project">Save</button><button class="sheet-close" data-action="close-sheet">Cancel</button></div>`, { type: "edit-project" });
  }

  function resetPreviewProject(item) {
    if (item.type !== "study") return;
    const notes = deepCopy(item.notes || []);
    item.map = {
      setup: { reference: false, tempo: "", meter: "4/4", grid: false, firstListen: false },
      sections: [],
      structureVerified: false,
      tracks: [],
      timeline: { presence: [], events: [] },
      sectionData: {},
      mapVerified: false,
      teachBack: false,
      phaseParking: "",
      phaseTakeaway: "",
    };
    item.skeleton = {
      session: { tracks: {}, markers: {} },
      draft: { parts: {} },
      bounce: { exported: false, listened: false },
    };
    item.notes = notes;
  }

  app.addEventListener("click", (event) => {
    const button = event.target.closest("button");
    if (!button) return;
    if (button.dataset.project) {
      db.currentProjectId = button.dataset.project;
      save();
      return navigate("project");
    }
    if (button.dataset.route) return button.dataset.action?.startsWith("continue-") ? undefined : navigate(button.dataset.route, button.dataset.nav === "replace" ? "replace" : "push");
    const action = button.dataset.action;
    if (!action) return;
    const item = project();
    if (action === "refresh-preview") {
      db = cloneProductionDb();
      save();
      return render();
    }
    if (action === "project-actions") return openProjectActions();
    if (action === "toggle-setup") {
      item.map.setup[button.dataset.field] = !item.map.setup[button.dataset.field];
      save();
      return renderSetup();
    }
    if (action === "continue-structure") return continueTo("structure");
    if (action === "open-add-section") return openAddSectionSheet();
    if (action === "edit-section") return openEditSectionSheet(button.dataset.sectionId);
    if (action === "toggle-structure-verified") {
      item.map.structureVerified = !item.map.structureVerified;
      save();
      return renderStructure();
    }
    if (action === "continue-tracks") return continueTo("tracks");
    if (action === "toggle-track") {
      const name = button.dataset.name;
      const index = item.map.tracks.findIndex((track) => track.name === name);
      if (index >= 0) item.map.tracks.splice(index, 1);
      else item.map.tracks.push({ id: uid(), name });
      save();
      return renderTracks();
    }
    if (action === "add-custom-track") {
      const input = document.getElementById("customTrackInput");
      const name = clean(input?.value);
      if (!name || item.map.tracks.some((track) => track.name.toLowerCase() === name.toLowerCase())) return;
      item.map.tracks.push({ id: uid(), name });
      save();
      return renderTracks();
    }
    if (action === "continue-section-study") return continueTo("section-study");
  });

  app.addEventListener("input", (event) => {
    const item = project();
    if (!item || currentRoute !== "setup") return;
    if (event.target.id === "tempoInput") {
      item.map.setup.tempo = event.target.value;
      save();
      const continueButton = document.getElementById("setupContinue");
      if (continueButton) continueButton.disabled = !setupComplete(item);
    }
  });

  app.addEventListener("change", (event) => {
    const item = project();
    if (!item || currentRoute !== "setup") return;
    if (event.target.id === "meterInput") {
      item.map.setup.meter = event.target.value;
      save();
    }
  });

  sheetRoot.addEventListener("click", (event) => {
    if (event.target === sheetRoot) return closeSheet();
    const button = event.target.closest("button");
    if (!button) return;
    const action = button.dataset.action;
    const item = project();
    if (action === "close-sheet") return closeSheet();
    if (action === "quick-add-section") {
      item.map.sections.push({ id: uid(), name: button.dataset.name, lengthBars: 8 });
      item.map.structureVerified = false;
      save();
      closeSheet();
      return renderStructure();
    }
    if (action === "show-custom-section") {
      const area = document.getElementById("customSectionArea");
      area.innerHTML = `<div style="height:12px"></div><div class="custom-track"><input id="customSectionName" class="field" placeholder="Section name" aria-label="Custom section name"><button class="compact-button" data-action="add-custom-section">Add</button></div>`;
      area.querySelector("input")?.focus();
      return;
    }
    if (action === "add-custom-section") {
      const name = clean(document.getElementById("customSectionName")?.value);
      if (!name) return;
      item.map.sections.push({ id: uid(), name, lengthBars: 8 });
      item.map.structureVerified = false;
      save();
      closeSheet();
      return renderStructure();
    }
    if (action === "edit-section-bars") {
      sheetState.bars = Number(button.dataset.bars);
      sheetRoot.querySelectorAll('[data-action="edit-section-bars"]').forEach((entry) => entry.classList.toggle("selected", entry === button));
      return;
    }
    if (action === "move-section") {
      const index = item.map.sections.findIndex((entry) => entry.id === sheetState.sectionId);
      const target = button.dataset.direction === "up" ? index - 1 : index + 1;
      if (index < 0 || target < 0 || target >= item.map.sections.length) return;
      const [section] = item.map.sections.splice(index, 1);
      item.map.sections.splice(target, 0, section);
      item.map.structureVerified = false;
      save();
      closeSheet();
      renderStructure();
      return openEditSectionSheet(section.id);
    }
    if (action === "save-section") {
      const section = item.map.sections.find((entry) => entry.id === sheetState.sectionId);
      if (!section) return;
      section.name = clean(document.getElementById("editSectionName")?.value) || section.name;
      section.lengthBars = Number(sheetState.bars) || section.lengthBars || 8;
      item.map.structureVerified = false;
      save();
      closeSheet();
      return renderStructure();
    }
    if (action === "duplicate-section") {
      const index = item.map.sections.findIndex((entry) => entry.id === sheetState.sectionId);
      if (index < 0) return;
      const copy = { ...deepCopy(item.map.sections[index]), id: uid() };
      item.map.sections.splice(index + 1, 0, copy);
      item.map.structureVerified = false;
      save();
      closeSheet();
      return renderStructure();
    }
    if (action === "delete-section") {
      item.map.sections = item.map.sections.filter((entry) => entry.id !== sheetState.sectionId);
      item.map.structureVerified = false;
      save();
      closeSheet();
      return renderStructure();
    }
    if (action === "edit-project") return openEditProjectSheet();
    if (action === "save-project") {
      const title = clean(document.getElementById("editProjectTitle")?.value);
      if (!title) return;
      item.title = title;
      item.artist = clean(document.getElementById("editProjectArtist")?.value);
      save();
      closeSheet();
      return renderProjectHome();
    }
    if (action === "reset-project-preview") {
      resetPreviewProject(item);
      save();
      closeSheet();
      return renderProjectHome();
    }
    if (action === "delete-project-preview") {
      db.projects = db.projects.filter((entry) => entry.id !== item.id);
      db.currentProjectId = db.projects[0]?.id || null;
      save();
      closeSheet();
      return navigate("projects", "replace");
    }
  });

  window.addEventListener("popstate", (event) => {
    const route = event.state?.v7Preview ? event.state.route : (location.hash || "#projects").slice(1);
    currentRoute = route || "projects";
    closeSheet(false);
    render();
    window.scrollTo(0, 0);
  });

  const hashRoute = (location.hash || "").slice(1);
  const validRoutes = new Set(["projects", "project", "setup", "structure", "tracks", "section-study", "notes"]);
  currentRoute = validRoutes.has(hashRoute) ? hashRoute : "projects";
  history.replaceState({ v7Preview: true, route: currentRoute }, "", `#${currentRoute}`);
  render();
})();
