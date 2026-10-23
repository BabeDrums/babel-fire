import {
  COMMON_TRACKS,
  SECTION_TYPES,
  WORK,
  createPreviewProject,
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
let buildCommitPromise = null;

function save() {
  saveDb(db);
}

function project() {
  return currentProject(db);
}

function topbar(left = "", right = "") {
  return `<header class="topbar"><div>${left}</div><div>${right}</div></header>`;
}

function backButton(route, label = "Back") {
  return `<button class="back icon-back" data-route="${route}" data-nav="replace" aria-label="${esc(label)}"><span class="arrow" aria-hidden="true">‹</span></button>`;
}

function pageHeader(title, copy = "") {
  return `<div class="page-header work-header"><h1>${esc(title)}</h1>${copy ? `<p class="sub">${esc(copy)}</p>` : ""}</div>`;
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

function showBuildInfo() {
  const targets = document.querySelectorAll(".build-info");
  if (!targets.length) return;
  buildCommitPromise ||= fetch("../build-info.json", { cache: "no-store" })
    .then((response) => {
      if (!response.ok) throw new Error("Build metadata unavailable");
      return response.json();
    })
    .then((info) => /^[0-9a-f]{40}$/i.test(info.commit) ? info.commit.slice(0, 7) : "unavailable")
    .catch(() => "unavailable");
  buildCommitPromise.then((commit) => {
    targets.forEach((target) => {
      if (target.isConnected) target.textContent = `G7 · ${commit}`;
    });
  });
}

function renderProjects() {
  const rows = db.projects.map((item) => `
    <div class="project-card">
      <button class="project-open" data-project="${esc(item.id)}">
        <span class="project-copy"><strong>${esc(item.title)}</strong><span>${esc(projectMeta(item))}</span></span>
        <span class="chevron" aria-hidden="true">›</span>
      </button>
      <button class="project-card-actions" data-project-actions="${esc(item.id)}" aria-label="Actions for ${esc(item.title)}">•••</button>
    </div>`).join("");

  app.innerHTML = `
    <main class="screen root-screen scroll-safe">
      <div class="projects-heading">
        <h1>Projects</h1>
        <button class="new-project-button" data-action="new-project" aria-label="New Project">+</button>
      </div>
      <div class="project-list group">${rows || `<div class="empty-state projects-empty">No projects yet.</div>`}</div>
      <div class="build-info root-build-info" aria-label="Preview build">G7 · …</div>
    </main>`;
  showBuildInfo();
}

function journeyRow(item, route) {
  const done = workDone(item, route);
  const stateClass = done ? "done" : "upcoming";
  const mark = done ? "✓" : "○";
  return `
    <button class="row journey-row ${stateClass}" data-route="${route}">
      <span class="journey-mark ${stateClass}" aria-hidden="true">${mark}</span>
      <span class="row-title">${esc(WORK[route].title)}</span>
      <span class="chevron" aria-hidden="true">›</span>
    </button>`;
}

function projectNotesRow(item) {
  const notesCount = item.notes.filter((note) => clean(typeof note === "string" ? note : note?.text)).length;
  if (!notesCount) return "";
  return `
    <button class="row notes-row" data-route="notes">
      <span><span class="row-title">Notes</span><span class="row-sub">${notesCount} saved</span></span>
      <span class="chevron" aria-hidden="true">›</span>
    </button>`;
}

function renderOriginalHome(item) {
  app.innerHTML = `
    <main class="screen scroll-safe">
      ${topbar(backButton("projects", "Projects"), `<button class="top-action" data-action="project-actions" aria-label="Project actions">•••</button>`)}
      <div class="project-identity"><h1>${esc(item.title)}</h1><p class="sub">${esc(projectMeta(item))}</p></div>
      <div class="placeholder-state original-placeholder"><p>Original workflow comes with the FIRE Core spine.</p></div>
      ${projectNotesRow(item) ? `<div class="group utility-group">${projectNotesRow(item)}</div>` : ""}
    </main>`;
}

function renderProjectHome() {
  const item = project();
  if (!item) return navigate("projects", "replace");
  if (item.type !== "study") return renderOriginalHome(item);

  const recommended = recommendedWork(item);
  const rec = WORK[recommended];
  const workRoutes = ["setup", "structure", "tracks", "section-study", "review-map"];
  const workRows = workRoutes
    .filter((route) => route !== recommended)
    .map((route) => journeyRow(item, route)).join("");
  const notesRow = projectNotesRow(item);
  const future = ["The Skeleton", "The Sounds", "The Balance", "The Shape", "The World", "The Finish"]
    .map((name) => `<span>${esc(name)}</span>`).join("");

  app.innerHTML = `
    <main class="screen scroll-safe">
      ${topbar(backButton("projects", "Projects"), `<button class="top-action" data-action="project-actions" aria-label="Project actions">•••</button>`)}
      <div class="project-identity"><h1>${esc(item.title)}</h1><p class="sub">${esc(projectMeta(item))}</p></div>

      <button class="continue-row" data-route="${recommended}">
        <span><span class="continue-title">${esc(rec.title)}</span><span class="continue-copy">${esc(rec.copy)}</span></span>
        <span class="chevron" aria-hidden="true">›</span>
      </button>

      <div class="group journey-group">${workRows}${notesRow}</div>
      <div class="future-phases" aria-label="Later phases">
        <span class="future-label">Later</span>
        <div class="future-phase-list">${future}</div>
      </div>
    </main>`;
}

function completionAccessory(checked) {
  return checked
    ? `<span class="checkmark" aria-label="Done">✓</span>`
    : `<span class="completion-ring" aria-hidden="true"></span>`;
}

function referenceRow(setup) {
  return `
    <button class="form-row reference-row" data-action="toggle-setup" data-field="reference">
      <span><span class="form-label">Reference</span><span class="form-help">Import it into your session.</span></span>
      ${completionAccessory(!!setup.reference)}
    </button>`;
}

function setupRow(label, field, value, help = "") {
  const checked = !!value;
  return `
    <button class="form-row" data-action="toggle-setup" data-field="${field}">
      <span><span class="form-label">${esc(label)}</span>${help ? `<span class="form-help">${esc(help)}</span>` : ""}</span>
      ${completionAccessory(checked)}
    </button>`;
}

function setupContinuationMarkup(item) {
  return setupComplete(item)
    ? `<div class="action-row"><button id="setupContinue" class="primary-action" data-action="continue-structure">Continue</button></div>`
    : "";
}

function syncSetupContinuation(item) {
  const host = document.getElementById("setupContinuation");
  if (host) host.innerHTML = setupContinuationMarkup(item);
}

function renderSetup() {
  const item = project();
  if (!item || item.type !== "study") return navigate("project", "replace");
  const setup = item.map.setup;
  app.innerHTML = `
    <main class="screen scroll-safe">
      ${topbar(backButton("project", item.title), "")}
      ${pageHeader("Song Setup")}
      <div class="form-group">
        ${referenceRow(setup)}
        <div class="form-row"><span class="form-label">Tempo</span><span class="form-value"><input id="tempoInput" class="inline-input" inputmode="decimal" aria-label="Tempo" value="${esc(setup.tempo)}" placeholder="—"><span>BPM</span></span></div>
        <div class="form-row"><span class="form-label">Meter</span><select id="meterInput" class="inline-select" aria-label="Meter"><option ${setup.meter === "4/4" ? "selected" : ""}>4/4</option><option ${setup.meter === "3/4" ? "selected" : ""}>3/4</option><option ${setup.meter === "6/8" ? "selected" : ""}>6/8</option></select></div>
        ${setupRow("Grid", "grid", setup.grid, "Align it to the bar grid.")}
        ${setupRow("First Listen", "firstListen", setup.firstListen, "Play the full song once.")}
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
    ? `<div class="action-row"><button class="primary-action" data-action="continue-tracks">Continue</button></div>`
    : "";

  const verification = sections.length
    ? `<button class="row structure-confirm-row" data-action="toggle-structure-verified"><span class="row-title">Matches the song</span>${completionAccessory(item.map.structureVerified)}</button>`
    : "";

  app.innerHTML = `
    <main class="screen scroll-safe">
      ${topbar(backButton("project", item.title), "")}
      ${pageHeader("Structure")}
      <div class="group arrangement">${rows}<button class="row add-section-row" data-action="open-add-section"><span class="row-title">Add Section</span><span class="plus" aria-hidden="true">＋</span></button>${verification}</div>
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
    ? `<div class="action-row"><button class="primary-action" data-action="continue-section-study">Continue</button></div>`
    : "";

  app.innerHTML = `
    <main class="screen scroll-safe">
      ${topbar(backButton("project", item.title), "")}
      ${pageHeader("Tracks", "Choose everything you hear.")}
      <div class="track-grid">${tiles}</div>
      <button class="custom-track-button" data-action="open-custom-track"><span>Other</span><span class="plus" aria-hidden="true">＋</span></button>
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
      missingStructure ? `<button data-route="structure">Structure <span class="chevron">›</span></button>` : "",
      missingTracks ? `<button data-route="tracks">Tracks <span class="chevron">›</span></button>` : "",
    ].join("");
    body = `<div class="prereq-card"><p>Section Study needs structure and tracks first.</p><div class="prereq-actions">${actions}</div></div>`;
  } else {
    body = `<div class="placeholder-state"><p>Section Study isn\'t built yet.</p></div>`;
  }
  app.innerHTML = `<main class="screen scroll-safe">${topbar(backButton("project", item.title), "")}${pageHeader("Section Study")}${body}</main>`;
}

function renderReviewMap() {
  const item = project();
  if (!item || item.type !== "study") return navigate("project", "replace");
  app.innerHTML = `<main class="screen scroll-safe">${topbar(backButton("project", item.title), "")}${pageHeader("Review Map")}<div class="placeholder-state"><p>Review Map isn\'t built yet.</p></div></main>`;
}

function renderNotes() {
  const item = project();
  if (!item) return navigate("projects", "replace");
  const notes = item.notes.map((note) => {
    const entry = typeof note === "string" ? { type: "General", context: "Project", text: note } : note;
    if (!clean(entry?.text)) return "";
    return `<article class="note-card"><div class="meta">${esc(entry.type || "General")} · ${esc(entry.context || "Project")}</div><p>${esc(entry.text)}</p></article>`;
  }).join("");
  app.innerHTML = `<main class="screen scroll-safe">${topbar(backButton("project", item.title), "")}${pageHeader("Notes")}<div class="notes-list">${notes || `<div class="empty-state">No saved notes.</div>`}</div></main>`;
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

function projectTypeControl(selected = "") {
  return `
    <div class="project-type-control" aria-label="Project type">
      <button class="project-type-option${selected === "original" ? " selected" : ""}" data-action="choose-project-type" data-project-type="original" aria-pressed="${selected === "original"}">Original</button>
      <button class="project-type-option${selected === "study" ? " selected" : ""}" data-action="choose-project-type" data-project-type="study" aria-pressed="${selected === "study"}">Recreation</button>
    </div>`;
}

function newProjectFields(type) {
  if (!type) return "";
  const recreation = type === "study";
  return `
    <div class="stack-fields new-project-fields">
      <label class="field-label" for="newProjectTitle">${recreation ? "Song" : "Title"}</label>
      <input id="newProjectTitle" class="field" autocomplete="off" placeholder="${recreation ? "Song title" : "Project title"}" aria-label="${recreation ? "Song title" : "Project title"}">
      <label class="field-label" for="newProjectArtist">${recreation ? "Artist" : "Artist (optional)"}</label>
      <input id="newProjectArtist" class="field" autocomplete="off" placeholder="Artist" aria-label="Artist">
    </div>
    <div class="sheet-actions">
      <button class="sheet-close" data-action="close-sheet">Cancel</button>
      <button class="sheet-primary" data-action="create-project" disabled>Create</button>
    </div>`;
}

function renderNewProjectSheet(type = "") {
  const previousTitle = clean(document.getElementById("newProjectTitle")?.value);
  const previousArtist = clean(document.getElementById("newProjectArtist")?.value);
  sheetState = { type: "new-project", projectType: type };
  sheetRoot.innerHTML = `<div class="sheet" role="dialog" aria-modal="true">
    <div class="grabber"></div>
    <h2>New Project</h2>
    ${projectTypeControl(type)}
    ${newProjectFields(type)}
  </div>`;
  if (type) {
    const title = document.getElementById("newProjectTitle");
    const artist = document.getElementById("newProjectArtist");
    if (title) title.value = previousTitle;
    if (artist) artist.value = previousArtist;
    requestAnimationFrame(() => title?.focus());
  }
}

function openNewProjectSheet() {
  openSheet(`<div class="grabber"></div><h2>New Project</h2>${projectTypeControl()}`, { type: "new-project", projectType: "" });
}

function syncNewProjectAction() {
  const button = sheetRoot.querySelector('[data-action="create-project"]');
  if (!button) return;
  const title = clean(document.getElementById("newProjectTitle")?.value);
  const artist = clean(document.getElementById("newProjectArtist")?.value);
  button.disabled = !title || (sheetState?.projectType === "study" && !artist);
}

function createProject() {
  const type = sheetState?.projectType;
  const title = clean(document.getElementById("newProjectTitle")?.value);
  const artist = clean(document.getElementById("newProjectArtist")?.value);
  if (!type || !title || (type === "study" && !artist)) return;

  const item = createPreviewProject(type, title, artist);
  db.projects.push(item);
  db.currentProjectId = item.id;
  save();
  closeSheet();
  navigate("project");
}

function openAddSectionSheet() {
  const choices = SECTION_TYPES.map((name) => `<button class="sheet-choice" data-action="quick-add-section" data-name="${esc(name)}">${esc(name)}</button>`).join("");
  openSheet(`<div class="grabber"></div><h2>Add Section</h2><div class="sheet-grid">${choices}<button class="sheet-choice" data-action="show-custom-section">Custom</button></div><div id="customSectionArea"></div><div class="sheet-actions single-action"><button class="sheet-close" data-action="close-sheet">Cancel</button></div>`, { type: "add-section" });
}

function openCustomTrackSheet() {
  openSheet(`<div class="grabber"></div><h2>Add Track</h2><input id="customTrackInput" class="field" placeholder="Track name" aria-label="Track name"><div class="sheet-actions"><button class="sheet-close" data-action="close-sheet">Cancel</button><button class="sheet-primary" data-action="add-custom-track" disabled>Add</button></div>`, { type: "custom-track" });
  requestAnimationFrame(() => document.getElementById("customTrackInput")?.focus());
}

function syncCustomTrackAction() {
  const button = sheetRoot.querySelector('[data-action="add-custom-track"]');
  if (button) button.disabled = !clean(document.getElementById("customTrackInput")?.value);
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
  const reset = item.type === "study" ? `<button class="row" data-action="reset-project-preview"><span><span class="row-title">Reset Progress</span><span class="row-sub">Keeps title, artist, and notes.</span></span><span></span></button>` : "";
  openSheet(`<div class="grabber"></div><h2>${esc(item.title)}</h2><div class="group"><button class="row" data-action="edit-project"><span class="row-title">Edit</span><span class="chevron">›</span></button>${reset}<button class="row sheet-danger" data-action="delete-project-preview"><span class="row-title">Delete Project</span><span></span></button></div><div class="sheet-actions single-action"><button class="sheet-close" data-action="close-sheet">Cancel</button></div>`, { type: "project-actions" });
}

function openEditProjectSheet() {
  const item = project();
  if (!item) return;
  openSheet(`<div class="grabber"></div><h2>Edit Project</h2><div class="stack-fields"><label class="field-label" for="editProjectTitle">Title</label><input id="editProjectTitle" class="field" value="${esc(item.title)}" aria-label="Project title"><label class="field-label" for="editProjectArtist">Artist${item.type === "study" ? "" : " (optional)"}</label><input id="editProjectArtist" class="field" value="${esc(item.artist || "")}" aria-label="Artist"></div><div class="sheet-actions"><button class="sheet-close" data-action="close-sheet">Cancel</button><button class="compact-button" data-action="save-project">Save</button></div>`, { type: "edit-project" });
}

app.addEventListener("click", (event) => {
  const button = event.target.closest("button");
  if (!button) return;
  if (button.dataset.projectActions) {
    db.currentProjectId = button.dataset.projectActions;
    save();
    return openProjectActions();
  }
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
  if (action === "open-custom-track") return openCustomTrackSheet();
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

sheetRoot.addEventListener("input", () => {
  if (sheetState?.type === "new-project") syncNewProjectAction();
  if (sheetState?.type === "custom-track") syncCustomTrackAction();
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
  if (action === "choose-project-type") return renderNewProjectSheet(button.dataset.projectType);
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
  if (action === "add-custom-track") {
    const name = clean(document.getElementById("customTrackInput")?.value);
    if (!name || item.map.tracks.some((track) => track.name.toLowerCase() === name.toLowerCase())) return;
    item.map.tracks.push({ id: uid(), name });
    save();
    closeSheet();
    return renderTracks();
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
    const artist = clean(document.getElementById("editProjectArtist")?.value);
    if (!title || (item.type === "study" && !artist)) return;
    item.title = title;
    item.artist = artist;
    save();
    closeSheet();
    return render();
  }
  if (action === "reset-project-preview") {
    resetPreviewProject(item);
    save();
    closeSheet();
    return render();
  }
  if (action === "delete-project-preview") {
    db.projects = db.projects.filter((entry) => entry.id !== item.id);
    db.currentProjectId = db.projects[0]?.id || null;
    save();
    closeSheet();
    if (currentRoute === "projects") return renderProjects();
    return navigate("projects", "replace");
  }
});

document.addEventListener("keydown", (event) => {
  if (event.key === "Escape" && !sheetRoot.hidden) closeSheet();
});

window.addEventListener("popstate", (event) => {
  const route = event.state?.v7Preview ? event.state.route : (location.hash || "#projects").slice(1);
  currentRoute = route || "projects";
  closeSheet(false);
  render();
  window.scrollTo(0, 0);
});

const hashRoute = (location.hash || "").slice(1);
const validRoutes = new Set(["projects", "project", "setup", "structure", "tracks", "section-study", "review-map", "notes"]);
currentRoute = validRoutes.has(hashRoute) ? hashRoute : "projects";
history.replaceState({ v7Preview: true, route: currentRoute }, "", `#${currentRoute}`);
render();
