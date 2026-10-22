import {
  COMMON_TRACKS,
  SECTION_TYPES,
  WORK,
  currentProject,
  helpers,
  loadDb,
  projectMeta,
  recommendedWork,
  resetPreviewProject,
  saveDb,
  setupComplete,
  structureComplete,
  tracksComplete,
  workDone,
} from "./model.js";

const { clean, deepCopy, uid } = helpers;
const app = document.getElementById("app");
const sheetRoot = document.getElementById("sheetRoot");
const esc = (value) => String(value ?? "").replace(/[&<>"']/g, (char) => ({
  "&": "&amp;",
  "<": "&lt;",
  ">": "&gt;",
  '"': "&quot;",
  "'": "&#39;",
})[char]);

let db = loadDb();
let currentRoute = "projects";
let sheetState = null;
let viewportFitFrame = 0;
let buildCommitPromise = null;

function applyViewportFit() {
  const screen = app.querySelector(".screen");
  const phone = window.matchMedia("(max-width: 699px)").matches;
  app.dataset.scrollable = "false";
  document.documentElement.dataset.v7Fit = "false";
  if (!screen || !phone) return;

  const viewport = window.visualViewport;
  const viewportTop = viewport?.offsetTop || 0;
  const viewportHeight = viewport?.height || window.innerHeight;
  const viewportBottom = viewportTop + viewportHeight;
  const contentBottom = screen.getBoundingClientRect().bottom;
  const needsScroll = contentBottom > viewportBottom - 12;

  app.dataset.scrollable = needsScroll ? "true" : "false";
  document.documentElement.dataset.v7Fit = needsScroll ? "false" : "true";
}

function queueViewportFit() {
  cancelAnimationFrame(viewportFitFrame);
  viewportFitFrame = requestAnimationFrame(applyViewportFit);
}

function save() {
  saveDb(db);
}

function project() {
  return currentProject(db);
}

function topbar(left = "", right = "") {
  return `<header class="topbar"><div>${left}</div><div>${right}</div></header>`;
}

function backButton(label, route) {
  return `<button class="back" data-route="${route}" data-nav="replace"><span class="arrow" aria-hidden="true">‹</span><span>${esc(label)}</span></button>`;
}

function pageHeader(title, copy = "") {
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
  queueViewportFit();
}

function continueTo(route) {
  navigate(route, "replace");
}

function showBuildStamp() {
  const stamp = app.querySelector(".build-stamp");
  if (!stamp) return;
  buildCommitPromise ||= fetch("../build-info.json", { cache: "no-store" })
    .then((response) => {
      if (!response.ok) throw new Error("Build metadata unavailable");
      return response.json();
    })
    .then((info) => /^[0-9a-f]{40}$/i.test(info.commit) ? info.commit.slice(0, 7) : "unavailable")
    .catch(() => "unavailable");
  buildCommitPromise.then((commit) => {
    if (stamp.isConnected) stamp.textContent = `FIRE V7 PREVIEW · ${commit}`;
  });
}

function renderProjects() {
  const rows = db.projects.map((item) => `
    <button class="project-row" data-project="${esc(item.id)}">
      <span class="project-copy"><strong>${esc(item.title)}</strong><span>${esc(projectMeta(item))}</span></span>
      <span class="chevron" aria-hidden="true">›</span>
    </button>`).join("");

  app.innerHTML = `
    <main class="screen root-screen scroll-safe">
      <div class="projects-heading">
        <h1>Projects</h1>
        <button class="new-project-button" data-action="new-project" aria-label="New Project">+</button>
      </div>
      <div class="project-list group">${rows || `<div class="empty-state projects-empty">No projects yet.</div>`}</div>
      <footer class="build-stamp">FIRE V7 PREVIEW · …</footer>
    </main>`;
  showBuildStamp();
}

function journeyRow(item, route) {
  const done = workDone(item, route);
  const current = route === recommendedWork(item);
  const stateClass = done ? "done" : current ? "current" : "upcoming";
  const mark = done ? "✓" : current ? "●" : "○";
  return `
    <button class="row journey-row ${stateClass}" data-route="${route}" ${current ? `aria-current="step"` : ""}>
      <span class="journey-mark ${stateClass}" aria-hidden="true">${mark}</span>
      <span class="row-title">${esc(WORK[route].title)}</span>
      <span class="chevron" aria-hidden="true">›</span>
    </button>`;
}

function renderProjectHome() {
  const item = project();
  if (!item) return navigate("projects", "replace");
  if (item.type !== "study") {
    app.innerHTML = `<main class="screen">${topbar(backButton("Projects", "projects"), "")}${pageHeader(item.title, "Original workflow is not part of this shell prototype yet.")}<div class="prereq-card"><p class="prototype-end">This preview is intentionally proving the Recreation shell first.</p></div></main>`;
    return;
  }

  const recommended = recommendedWork(item);
  const rec = WORK[recommended];
  const workRows = ["setup", "structure", "tracks", "section-study", "review-map"]
    .map((route) => journeyRow(item, route)).join("");
  const notesCount = item.notes.filter((note) => clean(typeof note === "string" ? note : note?.text)).length;
  const future = ["The Skeleton", "The Sounds", "The Balance", "The Shape", "The World", "The Finish"]
    .map((name) => `<div class="future-row"><span>${esc(name)}</span></div>`).join("");

  app.innerHTML = `
    <main class="screen scroll-safe">
      ${topbar(backButton("Projects", "projects"), `<button class="top-action" data-action="project-actions" aria-label="Project actions">•••</button>`)}
      <div class="project-identity"><h1>${esc(item.title)}</h1><p class="sub">${esc(projectMeta(item))}</p></div>

      <div class="section-title"><span>Continue</span></div>
      <button class="continue-row" data-route="${recommended}">
        <span><span class="continue-title">${esc(rec.title)}</span><span class="continue-copy">${esc(rec.copy)}</span></span>
        <span class="chevron" aria-hidden="true">›</span>
      </button>

      <div class="section-title"><span>Journey</span></div>
      <section class="journey">
        <div class="phase-label">The Map</div>
        <div class="group journey-group">${workRows}</div>
        <div class="future-phases" aria-label="Future phases">${future}</div>
      </section>

      <div class="section-title"><span>Notes</span></div>
      <div class="group">
        <button class="row" data-route="notes">
          <span><span class="row-title">Project Notes</span><span class="row-sub">${notesCount ? `${notesCount} saved note${notesCount === 1 ? "" : "s"}` : "Questions, takeaways, and ideas."}</span></span>
          <span class="chevron" aria-hidden="true">›</span>
        </button>
      </div>
    </main>`;
}

function completionAccessory(checked) {
  return checked
    ? `<span class="checkmark" aria-label="Done">✓</span>`
    : `<span class="completion-ring" aria-hidden="true"></span>`;
}

function setupRow(label, field, value, help = "") {
  const checked = !!value;
  const accessory = field === "reference"
    ? (checked
      ? `<span class="form-value"><span>Imported</span><span class="checkmark" aria-label="Done">✓</span></span>`
      : `<span class="form-value">Import</span>`)
    : completionAccessory(checked);
  return `
    <button class="form-row" data-action="toggle-setup" data-field="${field}">
      <span><span class="form-label">${esc(label)}</span>${help ? `<span class="form-help">${esc(help)}</span>` : ""}</span>
      ${accessory}
    </button>`;
}

function setupContinuationMarkup(item) {
  return setupComplete(item)
    ? `<div class="action-row"><button id="setupContinue" class="primary-action" data-action="continue-structure">Continue to Structure</button></div>`
    : "";
}

function syncSetupContinuation(item) {
  const host = document.getElementById("setupContinuation");
  if (host) host.innerHTML = setupContinuationMarkup(item);
  queueViewportFit();
}

function renderSetup() {
  const item = project();
  if (!item || item.type !== "study") return navigate("project", "replace");
  const setup = item.map.setup;
  app.innerHTML = `
    <main class="screen scroll-safe">
      ${topbar(backButton(item.title, "project"), "")}
      ${pageHeader("Song Setup", "Prepare the reference before studying it.")}
      <div class="form-group">
        ${setupRow("Reference", "reference", setup.reference)}
        <div class="form-row"><span class="form-label">Tempo</span><span class="form-value"><input id="tempoInput" class="inline-input" inputmode="decimal" aria-label="Tempo" value="${esc(setup.tempo)}" placeholder="—"><span>BPM</span></span></div>
        <div class="form-row"><span class="form-label">Meter</span><select id="meterInput" class="inline-select" aria-label="Meter"><option ${setup.meter === "4/4" ? "selected" : ""}>4/4</option><option ${setup.meter === "3/4" ? "selected" : ""}>3/4</option><option ${setup.meter === "6/8" ? "selected" : ""}>6/8</option></select></div>
        ${setupRow("Grid", "grid", setup.grid, "Align the reference to the bar grid.")}
        ${setupRow("First Listen", "firstListen", setup.firstListen, "Play the full song once without stopping.")}
      </div>
      <div id="setupContinuation">${setupContinuationMarkup(item)}</div>
    </main>`;
}

function renderStructure() {
  const item = project();
  if (!item || item.type !== "study") return navigate("project", "replace");
  const sections = item.map.sections;
  const rows = sections.map((section, index) => `
    <button class="arrangement-row" data-action="edit-section" data-section-id="${esc(section.id)}">
      <span class="arrangement-index">${index + 1}</span>
      <span class="arrangement-name">${esc(section.name)}</span>
      <span class="arrangement-bars">${Number(section.lengthBars) || 8} bars</span>
      <span class="chevron" aria-hidden="true">›</span>
    </button>`).join("");

  const continuation = structureComplete(item)
    ? `<div class="action-row"><button class="primary-action" data-action="continue-tracks">Continue to Tracks</button></div>`
    : "";

  app.innerHTML = `
    <main class="screen scroll-safe">
      ${topbar(backButton(item.title, "project"), "")}
      ${pageHeader("Structure", "Build the song one section at a time.")}
      ${sections.length
        ? `<div class="group arrangement">${rows}<button class="row add-section-row" data-action="open-add-section"><span class="row-title">Add Section</span><span class="plus" aria-hidden="true">＋</span></button></div>`
        : `<div class="structure-empty"><p>Add the first section you hear.</p><button class="primary-action compact-primary" data-action="open-add-section">Add Section</button></div>`}
      ${sections.length ? `<button class="confirm-row" data-action="toggle-structure-verified"><span class="row-title">Structure matches the song</span>${item.map.structureVerified ? `<span class="checkmark" aria-label="Done">✓</span>` : `<span class="trailing">Confirm</span>`}</button>` : ""}
      ${continuation}
    </main>`;
}

function renderTracks() {
  const item = project();
  if (!item || item.type !== "study") return navigate("project", "replace");
  const selectedNames = new Set(item.map.tracks.map((track) => track.name));
  const extra = item.map.tracks.map((track) => track.name).filter((name) => !COMMON_TRACKS.includes(name));
  const names = [...COMMON_TRACKS, ...extra];
  const tiles = names.map((name) => `<button class="track-tile${selectedNames.has(name) ? " selected" : ""}" data-action="toggle-track" data-name="${esc(name)}" aria-pressed="${selectedNames.has(name)}">${esc(name)}</button>`).join("");
  const continuation = tracksComplete(item)
    ? `<div class="action-row action-separated"><button class="primary-action" data-action="continue-section-study">Continue to Section Study</button></div>`
    : "";

  app.innerHTML = `
    <main class="screen scroll-safe">
      ${topbar(backButton(item.title, "project"), "")}
      ${pageHeader("Tracks", "Choose everything you hear in the song.")}
      <div class="track-grid">${tiles}</div>
      <div class="custom-track"><input id="customTrackInput" class="field" placeholder="Other…" aria-label="Other track"><button class="compact-button" data-action="add-custom-track">Add</button></div>
      ${continuation}
    </main>`;
}

function renderSectionStudy() {
  const item = project();
  if (!item || item.type !== "study") return navigate("project", "replace");
  const missingStructure = item.map.sections.length === 0;
  const missingTracks = item.map.tracks.length === 0;
  let body = "";
  if (missingStructure || missingTracks) {
    const actions = [
      missingStructure ? `<button data-route="structure">Add the song structure <span class="chevron">›</span></button>` : "",
      missingTracks ? `<button data-route="tracks">Choose the tracks <span class="chevron">›</span></button>` : "",
    ].join("");
    body = `<div class="prereq-card"><h3>Finish the missing context first.</h3><p>Section Study needs a structure and at least one track.</p><div class="prereq-actions">${actions}</div></div>`;
  } else {
    body = `<div class="prereq-card"><h3>Ready for Section Study.</h3><p class="prototype-end">The full timeline editor stays in V6 until this lighter shell is approved.</p></div>`;
  }
  app.innerHTML = `<main class="screen">${topbar(backButton(item.title, "project"), "")}${pageHeader("Section Study", "Study what changes from section to section.")}${body}</main>`;
}

function renderReviewMap() {
  const item = project();
  if (!item || item.type !== "study") return navigate("project", "replace");
  app.innerHTML = `<main class="screen">${topbar(backButton(item.title, "project"), "")}${pageHeader("Review Map", "Review the song map before rebuilding it.")}<div class="prereq-card"><p class="prototype-end">The full Review Map workspace still uses V6 while this lighter shell is being evaluated.</p></div></main>`;
}

function renderNotes() {
  const item = project();
  if (!item) return navigate("projects", "replace");
  const notes = item.notes.map((note) => {
    const entry = typeof note === "string" ? { type: "General", context: "Project", text: note } : note;
    if (!clean(entry?.text)) return "";
    return `<article class="note-card"><div class="meta">${esc(entry.type || "General")} · ${esc(entry.context || "Project")}</div><p>${esc(entry.text)}</p></article>`;
  }).join("");
  app.innerHTML = `<main class="screen scroll-safe">${topbar(backButton(item.title, "project"), "")}${pageHeader("Notes", "Your project notes, in one place.")}<div class="notes-list">${notes || `<div class="empty-state">No saved notes yet.</div>`}</div></main>`;
}

function render() {
  if (currentRoute === "projects") return renderProjects();
  if (currentRoute === "project") return renderProjectHome();
  if (currentRoute === "setup") return renderSetup();
  if (currentRoute === "structure") return renderStructure();
  if (currentRoute === "tracks") return renderTracks();
  if (currentRoute === "section-study") return renderSectionStudy();
  if (currentRoute === "review-map") return renderReviewMap();
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

function openNewProjectSheet() {
  openSheet(`
    <div class="grabber"></div>
    <h2>New Project</h2>
    <p class="sheet-kicker">Recreation</p>
    <div class="stack-fields">
      <label class="field-label" for="newProjectTitle">Song</label>
      <input id="newProjectTitle" class="field" autocomplete="off" placeholder="Song title" aria-label="Song title">
      <label class="field-label" for="newProjectArtist">Artist</label>
      <input id="newProjectArtist" class="field" autocomplete="off" placeholder="Artist" aria-label="Artist">
    </div>
    <div class="sheet-actions">
      <button class="sheet-close" data-action="close-sheet">Cancel</button>
      <button class="compact-button" data-action="create-project">Create Project</button>
    </div>`, { type: "new-project" });
  requestAnimationFrame(() => document.getElementById("newProjectTitle")?.focus());
}

function createProject() {
  const title = clean(document.getElementById("newProjectTitle")?.value);
  const artist = clean(document.getElementById("newProjectArtist")?.value);
  if (!title || !artist) return;

  const item = {
    id: uid(),
    type: "study",
    schemaVersion: 5,
    title,
    artist,
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
  db.projects.push(item);
  db.currentProjectId = item.id;
  save();
  closeSheet();
  navigate("project");
}

function openAddSectionSheet() {
  const choices = SECTION_TYPES.map((name) => `<button class="sheet-choice" data-action="quick-add-section" data-name="${esc(name)}">${esc(name)}</button>`).join("");
  openSheet(`<div class="grabber"></div><h2>Add Section</h2><div class="sheet-grid">${choices}<button class="sheet-choice" data-action="show-custom-section">Custom</button></div><div id="customSectionArea"></div><div class="sheet-actions"><button class="sheet-close" data-action="close-sheet">Cancel</button></div>`, { type: "add-section" });
}

function openEditSectionSheet(sectionId) {
  const item = project();
  const section = item?.map?.sections?.find((entry) => entry.id === sectionId);
  if (!section) return;
  const selectedBars = Number(section.lengthBars) || 8;
  const bars = [4, 8, 12, 16].map((value) => `<button class="${selectedBars === value ? "selected" : ""}" data-action="edit-section-bars" data-bars="${value}">${value}</button>`).join("");
  const index = item.map.sections.findIndex((entry) => entry.id === sectionId);
  openSheet(`<div class="grabber"></div><h2>Edit Section</h2><input id="editSectionName" class="field" value="${esc(section.name)}" aria-label="Section name"><div class="bars-grid">${bars}</div><div class="move-row"><button data-action="move-section" data-direction="up" ${index === 0 ? "disabled" : ""}>Move Up</button><button data-action="move-section" data-direction="down" ${index === item.map.sections.length - 1 ? "disabled" : ""}>Move Down</button></div><div class="sheet-actions"><button class="compact-button" data-action="save-section">Save</button><button class="sheet-close" data-action="duplicate-section">Duplicate</button><button class="sheet-close sheet-danger" data-action="delete-section">Delete</button></div>`, { type: "edit-section", sectionId, bars: selectedBars });
}

function openProjectActions() {
  const item = project();
  if (!item) return;
  openSheet(`<div class="grabber"></div><h2>${esc(item.title)}</h2><div class="group"><button class="row" data-action="edit-project"><span class="row-title">Edit Project</span><span class="chevron">›</span></button><button class="row" data-action="reset-project-preview"><span><span class="row-title">Reset Progress</span><span class="row-sub">Keeps title, artist, and notes.</span></span><span></span></button><button class="row sheet-danger" data-action="delete-project-preview"><span class="row-title">Delete Project</span><span></span></button></div><div class="sheet-actions"><button class="sheet-close" data-action="close-sheet">Cancel</button></div>`, { type: "project-actions" });
}

function openEditProjectSheet() {
  const item = project();
  if (!item) return;
  openSheet(`<div class="grabber"></div><h2>Edit Project</h2><div class="stack-fields"><input id="editProjectTitle" class="field" value="${esc(item.title)}" aria-label="Song title"><input id="editProjectArtist" class="field" value="${esc(item.artist || "")}" aria-label="Artist"></div><div class="sheet-actions"><button class="compact-button" data-action="save-project">Save</button><button class="sheet-close" data-action="close-sheet">Cancel</button></div>`, { type: "edit-project" });
}

app.addEventListener("click", (event) => {
  const button = event.target.closest("button");
  if (!button) return;
  if (button.dataset.project) {
    db.currentProjectId = button.dataset.project;
    save();
    return navigate("project");
  }
  if (button.dataset.route) return navigate(button.dataset.route, button.dataset.nav === "replace" ? "replace" : "push");

  const action = button.dataset.action;
  if (!action) return;
  const item = project();

  if (action === "new-project") return openNewProjectSheet();
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
    syncSetupContinuation(item);
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
  if (action === "create-project") return createProject();
  if (action === "quick-add-section") {
    item.map.sections.push({ id: uid(), name: button.dataset.name, lengthBars: 8 });
    item.map.structureVerified = false;
    save();
    closeSheet();
    return renderStructure();
  }
  if (action === "show-custom-section") {
    const area = document.getElementById("customSectionArea");
    area.innerHTML = `<div class="custom-section-entry"><input id="customSectionName" class="field" placeholder="Section name" aria-label="Custom section name"><button class="compact-button" data-action="add-custom-section">Add</button></div>`;
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

document.addEventListener("keydown", (event) => {
  if (event.key === "Escape" && !sheetRoot.hidden) closeSheet();
});

app.addEventListener("click", () => requestAnimationFrame(queueViewportFit));
app.addEventListener("input", queueViewportFit);
app.addEventListener("change", queueViewportFit);
window.addEventListener("resize", queueViewportFit);
window.visualViewport?.addEventListener("resize", queueViewportFit);

window.addEventListener("popstate", (event) => {
  const route = event.state?.v7Preview ? event.state.route : (location.hash || "#projects").slice(1);
  currentRoute = route || "projects";
  closeSheet(false);
  render();
  window.scrollTo(0, 0);
  queueViewportFit();
});

const hashRoute = (location.hash || "").slice(1);
const validRoutes = new Set(["projects", "project", "setup", "structure", "tracks", "section-study", "review-map", "notes"]);
currentRoute = validRoutes.has(hashRoute) ? hashRoute : "projects";
history.replaceState({ v7Preview: true, route: currentRoute }, "", `#${currentRoute}`);
render();
queueViewportFit();