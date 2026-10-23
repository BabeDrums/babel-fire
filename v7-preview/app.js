import {
  COMMON_TRACKS,
  SECTION_TYPES,
  WORK,
  createPreviewProject,
  currentProject,
  helpers,
  loadDb,
  noteActivity,
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
let reorderState = null;

function save() {
  saveDb(db);
}

function project() {
  return currentProject(db);
}

function backButton(route, label = "Back") {
  return `<button class="toolbar-button icon-back" data-route="${route}" data-nav="replace" aria-label="${esc(label)}"><span class="back-glyph" aria-hidden="true">‹</span></button>`;
}

function moreButton(action = "project-actions", label = "Project actions") {
  return `<button class="toolbar-button more-button" data-action="${action}" aria-label="${esc(label)}">•••</button>`;
}

function screenHeader(title, { backRoute = "", backLabel = "Back", right = "", meta = "" } = {}) {
  const left = backRoute ? backButton(backRoute, backLabel) : `<span class="toolbar-spacer" aria-hidden="true"></span>`;
  const rightSlot = right || `<span class="toolbar-spacer" aria-hidden="true"></span>`;
  return `
    <header class="screen-header">
      <div class="toolbar"><div>${left}</div><div>${rightSlot}</div></div>
      <div class="title-block"><h1>${esc(title)}</h1>${meta ? `<p class="screen-meta">${esc(meta)}</p>` : ""}</div>
    </header>`;
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

function sortedProjects() {
  return [...db.projects].sort((a, b) => {
    const activity = Number(b.lastActivityAt || b.createdAt || 0) - Number(a.lastActivityAt || a.createdAt || 0);
    if (activity) return activity;
    return Number(b.createdAt || 0) - Number(a.createdAt || 0);
  });
}

function renderProjects() {
  const rows = sortedProjects().map((item) => `
    <div class="project-card" data-project-card="${esc(item.id)}">
      <button class="project-open" data-project="${esc(item.id)}">
        <span class="project-copy"><strong>${esc(item.title)}</strong><span>${esc(projectMeta(item))}</span></span>
        <span class="chevron" aria-hidden="true">›</span>
      </button>
      <button class="project-card-actions more-button" data-project-actions="${esc(item.id)}" aria-label="Actions for ${esc(item.title)}">•••</button>
    </div>`).join("");

  app.innerHTML = `
    <main class="screen root-screen scroll-safe">
      ${screenHeader("Projects", { right: `<button class="toolbar-button new-project-button" data-action="new-project" aria-label="New Project">＋</button>` })}
      <div class="project-list group">${rows || `<div class="empty-state projects-empty">No projects yet.</div>`}</div>
      <div class="build-info root-build-info" aria-label="Preview build">G7 · …</div>
    </main>`;
  showBuildInfo();
}

function journeyRow(item, route) {
  const done = workDone(item, route);
  return `
    <button class="row journey-row ${done ? "done" : "upcoming"}" data-route="${route}">
      <span class="journey-mark ${done ? "done" : "upcoming"}" aria-hidden="true">${done ? "✓" : "○"}</span>
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
  const notesRow = projectNotesRow(item);
  app.innerHTML = `
    <main class="screen scroll-safe">
      ${screenHeader(item.title, { backRoute: "projects", backLabel: "Projects", right: moreButton(), meta: projectMeta(item) })}
      <div class="placeholder-state original-placeholder"><p>Original workflow isn't built yet.</p></div>
      ${notesRow ? `<div class="group utility-group">${notesRow}</div>` : ""}
    </main>`;
}

function renderProjectHome() {
  const item = project();
  if (!item) return navigate("projects", "replace");
  if (item.type !== "study") return renderOriginalHome(item);

  const recommended = recommendedWork(item);
  const routes = ["setup", "structure", "tracks"];
  const rows = routes.filter((route) => route !== recommended).map((route) => journeyRow(item, route)).join("");
  const notesRow = projectNotesRow(item);
  const current = recommended
    ? `<button class="continue-row" data-route="${recommended}"><span class="continue-title">${esc(WORK[recommended].title)}</span><span class="chevron" aria-hidden="true">›</span></button>`
    : `<div class="map-complete" role="status">Song map complete.</div>`;

  app.innerHTML = `
    <main class="screen scroll-safe">
      ${screenHeader(item.title, { backRoute: "projects", backLabel: "Projects", right: moreButton(), meta: projectMeta(item) })}
      ${current}
      <div class="group journey-group">${rows}${notesRow}</div>
    </main>`;
}

function completionAccessory(checked) {
  return checked
    ? `<span class="checkmark" aria-label="Done">✓</span>`
    : `<span class="completion-ring" aria-hidden="true"></span>`;
}

function setupToggleRow(label, field, value) {
  return `
    <button class="form-row" data-action="toggle-setup" data-field="${field}">
      <span class="form-label">${esc(label)}</span>
      ${completionAccessory(!!value)}
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
      ${screenHeader("Song Setup", { backRoute: "project", backLabel: item.title })}
      <div class="form-group">
        ${setupToggleRow("Reference", "reference", setup.reference)}
        <div class="form-row"><span class="form-label">Tempo</span><span class="form-value"><input id="tempoInput" class="inline-input" inputmode="decimal" aria-label="Tempo" value="${esc(setup.tempo)}" placeholder="—"><span>BPM</span></span></div>
        <div class="form-row"><span class="form-label">Meter</span><select id="meterInput" class="inline-select" aria-label="Meter"><option ${setup.meter === "4/4" ? "selected" : ""}>4/4</option><option ${setup.meter === "3/4" ? "selected" : ""}>3/4</option><option ${setup.meter === "6/8" ? "selected" : ""}>6/8</option></select></div>
        ${setupToggleRow("Grid", "grid", setup.grid)}
        ${setupToggleRow("First Listen", "firstListen", setup.firstListen)}
      </div>
      <div id="setupContinuation">${setupContinuationMarkup(item)}</div>
    </main>`;
}

function renderStructure() {
  const item = project();
  if (!item || item.type !== "study") return navigate("project", "replace");
  const sections = item.map.sections;
  const rows = sections.map((section, index) => `
    <div class="arrangement-row" data-section-row="${esc(section.id)}">
      <span class="arrangement-index">${index + 1}</span>
      <button class="section-edit-target" data-action="edit-section" data-section-id="${esc(section.id)}" aria-label="Edit ${esc(section.name)}">
        <span class="arrangement-name">${esc(section.name)}</span>
        <span class="arrangement-bars">${Number(section.lengthBars) || 8} bars</span>
      </button>
      <button class="reorder-handle" data-section-reorder="${esc(section.id)}" aria-label="Reorder ${esc(section.name)}" title="Drag to reorder">≡</button>
    </div>`).join("");

  const verification = sections.length
    ? `<button class="row structure-confirm-row" data-action="toggle-structure-verified"><span class="row-title">Matches the song</span>${completionAccessory(item.map.structureVerified)}</button>`
    : "";
  const continuation = structureComplete(item)
    ? `<div class="action-row"><button class="primary-action" data-action="continue-tracks">Continue</button></div>`
    : "";

  app.innerHTML = `
    <main class="screen scroll-safe">
      ${screenHeader("Structure", { backRoute: "project", backLabel: item.title })}
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
    ? `<div class="action-row"><button class="primary-action" data-action="finish-map">Done</button></div>`
    : "";

  app.innerHTML = `
    <main class="screen scroll-safe">
      ${screenHeader("Tracks", { backRoute: "project", backLabel: item.title })}
      <div class="track-grid">${tiles}</div>
      <button class="custom-track-button" data-action="open-custom-track"><span>Other</span><span class="plus" aria-hidden="true">＋</span></button>
      ${continuation}
    </main>`;
}

function renderNotes() {
  const item = project();
  if (!item) return navigate("projects", "replace");
  const notes = item.notes.map((note) => {
    const entry = typeof note === "string" ? { type: "General", context: "Project", text: note } : note;
    if (!clean(entry?.text)) return "";
    return `<article class="note-card"><div class="meta">${esc(entry.type || "General")} · ${esc(entry.context || "Project")}</div><p>${esc(entry.text)}</p></article>`;
  }).join("");
  app.innerHTML = `<main class="screen scroll-safe">${screenHeader("Notes", { backRoute: "project", backLabel: item.title })}<div class="notes-list">${notes || `<div class="empty-state">No saved notes.</div>`}</div></main>`;
}

function render() {
  if (currentRoute === "projects") return renderProjects();
  if (currentRoute === "project") return renderProjectHome();
  if (currentRoute === "setup") return renderSetup();
  if (currentRoute === "structure") return renderStructure();
  if (currentRoute === "tracks") return renderTracks();
  if (currentRoute === "notes") return renderNotes();
  navigate("project", "replace");
}

function openSheet(html, state = null, label = "Dialog") {
  sheetState = state;
  sheetRoot.innerHTML = `<div class="sheet" role="dialog" aria-modal="true" aria-label="${esc(label)}">${html}</div>`;
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

function textField(id, label, value = "", placeholder = "") {
  return `<label class="field-label" for="${id}">${esc(label)}</label><input id="${id}" class="field" value="${esc(value)}" placeholder="${esc(placeholder)}" aria-label="${esc(label)}" autocomplete="off" autocapitalize="words" autocorrect="off" spellcheck="false">`;
}

function projectTypeControl(selected = "original") {
  return `
    <div class="project-type-control" aria-label="Project type">
      <button class="project-type-option${selected === "original" ? " selected" : ""}" data-action="choose-project-type" data-project-type="original" aria-pressed="${selected === "original"}">Original</button>
      <button class="project-type-option${selected === "study" ? " selected" : ""}" data-action="choose-project-type" data-project-type="study" aria-pressed="${selected === "study"}">Cover</button>
    </div>`;
}

function newProjectFields() {
  return `
    <div class="stack-fields new-project-fields">
      ${textField("newProjectTitle", "Title", "", "Title")}
      ${textField("newProjectArtist", "Artist", "", "Artist")}
    </div>
    <div class="sheet-actions">
      <button class="sheet-close" data-action="close-sheet">Cancel</button>
      <button class="sheet-primary" data-action="create-project" disabled>Create</button>
    </div>`;
}

function openNewProjectSheet() {
  openSheet(`<div class="grabber"></div><h2>New Project</h2>${projectTypeControl("original")}${newProjectFields()}`, { type: "new-project", projectType: "original" }, "New Project");
}

function chooseProjectType(type) {
  if (!sheetState || sheetState.type !== "new-project") return;
  sheetState.projectType = type;
  sheetRoot.querySelectorAll(".project-type-option").forEach((button) => {
    const selected = button.dataset.projectType === type;
    button.classList.toggle("selected", selected);
    button.setAttribute("aria-pressed", String(selected));
  });
  syncNewProjectAction();
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

function sectionBarsControls(selectedBars) {
  const standard = [4, 8, 12, 16];
  const isCustom = !standard.includes(Number(selectedBars));
  return `<div class="bars-grid" aria-label="Bars">${standard.map((value) => `<button class="bar-choice${Number(selectedBars) === value ? " selected" : ""}" data-action="choose-section-bars" data-bars="${value}" aria-pressed="${Number(selectedBars) === value}">${value}</button>`).join("")}<button class="bar-choice${isCustom ? " selected" : ""}" data-action="choose-section-bars" data-bars="custom" aria-pressed="${isCustom}">Custom</button></div>`;
}

function openAddSectionSheet() {
  const choices = [...SECTION_TYPES, "Custom"].map((name) => `<button class="sheet-choice" data-action="choose-section-type" data-name="${esc(name)}" aria-pressed="false">${esc(name)}</button>`).join("");
  openSheet(`
    <div class="grabber"></div>
    <h2>Add Section</h2>
    <div class="sheet-grid section-types">${choices}</div>
    <div id="customSectionArea" hidden>${textField("customSectionName", "Section name", "", "Section name")}</div>
    ${sectionBarsControls(8)}
    <div id="customBarsArea" hidden><label class="field-label" for="customBarsInput">Bars</label><input id="customBarsInput" class="field numeric-field" inputmode="numeric" aria-label="Custom bars" placeholder="Bars"></div>
    <div id="sectionAddedNotice" class="inline-notice" aria-live="polite"></div>
    <div class="sheet-actions"><button class="sheet-close" data-action="close-sheet">Done</button><button class="sheet-primary" data-action="add-section" disabled>Add</button></div>`,
  { type: "add-section", sectionName: "", bars: 8, customBars: "" }, "Add Section");
}

function syncAddSectionSheet() {
  if (sheetState?.type !== "add-section") return;
  const customType = sheetState.sectionName === "Custom";
  const customBars = sheetState.bars === "custom";
  const customTypeArea = document.getElementById("customSectionArea");
  const customBarsArea = document.getElementById("customBarsArea");
  if (customTypeArea) customTypeArea.hidden = !customType;
  if (customBarsArea) customBarsArea.hidden = !customBars;
  const name = customType ? clean(document.getElementById("customSectionName")?.value) : clean(sheetState.sectionName);
  const bars = customBars ? Number(document.getElementById("customBarsInput")?.value) : Number(sheetState.bars);
  const add = sheetRoot.querySelector('[data-action="add-section"]');
  if (add) add.disabled = !name || !Number.isFinite(bars) || bars <= 0 || !Number.isInteger(bars);
}

function chooseSectionType(button) {
  if (sheetState?.type !== "add-section") return;
  sheetState.sectionName = button.dataset.name;
  sheetRoot.querySelectorAll('[data-action="choose-section-type"]').forEach((entry) => {
    const selected = entry === button;
    entry.classList.toggle("selected", selected);
    entry.setAttribute("aria-pressed", String(selected));
  });
  syncAddSectionSheet();
  if (sheetState.sectionName === "Custom") requestAnimationFrame(() => document.getElementById("customSectionName")?.focus());
}

function chooseSectionBars(button) {
  if (!sheetState || !["add-section", "edit-section"].includes(sheetState.type)) return;
  const raw = button.dataset.bars;
  sheetState.bars = raw === "custom" ? "custom" : Number(raw);
  sheetRoot.querySelectorAll('[data-action="choose-section-bars"]').forEach((entry) => {
    const selected = entry === button;
    entry.classList.toggle("selected", selected);
    entry.setAttribute("aria-pressed", String(selected));
  });
  const customBarsArea = document.getElementById("customBarsArea");
  if (customBarsArea) customBarsArea.hidden = sheetState.bars !== "custom";
  if (sheetState.type === "add-section") syncAddSectionSheet();
}

function addSectionFromSheet() {
  const item = project();
  if (!item || sheetState?.type !== "add-section") return;
  const customType = sheetState.sectionName === "Custom";
  const customBars = sheetState.bars === "custom";
  const name = customType ? clean(document.getElementById("customSectionName")?.value) : clean(sheetState.sectionName);
  const bars = customBars ? Number(document.getElementById("customBarsInput")?.value) : Number(sheetState.bars);
  if (!name || !Number.isInteger(bars) || bars <= 0) return;
  item.map.sections.push({ id: uid(), name, lengthBars: bars });
  item.map.structureVerified = false;
  noteActivity(item);
  save();
  renderStructure();
  const notice = document.getElementById("sectionAddedNotice");
  if (notice) notice.textContent = `Added ${name} · ${bars} bars`;
  sheetState.sectionName = "";
  sheetRoot.querySelectorAll('[data-action="choose-section-type"]').forEach((entry) => {
    entry.classList.remove("selected");
    entry.setAttribute("aria-pressed", "false");
  });
  const customName = document.getElementById("customSectionName");
  if (customName) customName.value = "";
  syncAddSectionSheet();
}

function openCustomTrackSheet() {
  openSheet(`<div class="grabber"></div><h2>Add Track</h2>${textField("customTrackInput", "Track name", "", "Track name")}<div class="sheet-actions"><button class="sheet-close" data-action="close-sheet">Cancel</button><button class="sheet-primary" data-action="add-custom-track" disabled>Add</button></div>`, { type: "custom-track" }, "Add Track");
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
  const standard = [4, 8, 12, 16];
  const custom = !standard.includes(selectedBars);
  openSheet(`
    <div class="grabber"></div><h2>Edit Section</h2>
    <div class="stack-fields">${textField("editSectionName", "Name", section.name, "Section name")}</div>
    ${sectionBarsControls(selectedBars)}
    <div id="customBarsArea" ${custom ? "" : "hidden"}><label class="field-label" for="customBarsInput">Bars</label><input id="customBarsInput" class="field numeric-field" inputmode="numeric" aria-label="Custom bars" value="${custom ? selectedBars : ""}"></div>
    <div class="sheet-actions"><button class="sheet-primary" data-action="save-section">Save</button><button class="sheet-close" data-action="duplicate-section">Duplicate</button><button class="sheet-close sheet-danger" data-action="delete-section">Delete</button></div>`,
  { type: "edit-section", sectionId, bars: custom ? "custom" : selectedBars }, "Edit Section");
}

function openProjectActions() {
  const item = project();
  if (!item) return;
  const reset = item.type === "study" ? `<button class="row" data-action="reset-project-preview"><span class="row-title">Reset Progress</span><span></span></button>` : "";
  openSheet(`<div class="grabber"></div><div class="group"><button class="row" data-action="edit-project"><span class="row-title">Edit Details</span><span class="chevron">›</span></button>${reset}<button class="row sheet-danger" data-action="delete-project-preview"><span class="row-title">Delete Project</span><span></span></button></div><div class="sheet-actions single-action"><button class="sheet-close" data-action="close-sheet">Cancel</button></div>`, { type: "project-actions" }, "Project actions");
}

function openEditProjectSheet() {
  const item = project();
  if (!item) return;
  openSheet(`<div class="grabber"></div><h2>Edit Details</h2><div class="stack-fields">${textField("editProjectTitle", "Title", item.title, "Title")}${textField("editProjectArtist", "Artist", item.artist || "", "Artist")}</div><div class="sheet-actions"><button class="sheet-close" data-action="close-sheet">Cancel</button><button class="sheet-primary" data-action="save-project">Save</button></div>`, { type: "edit-project" }, "Edit Details");
}

function moveSection(sectionId, direction) {
  const item = project();
  if (!item) return;
  const index = item.map.sections.findIndex((entry) => entry.id === sectionId);
  const target = index + direction;
  if (index < 0 || target < 0 || target >= item.map.sections.length) return;
  const [section] = item.map.sections.splice(index, 1);
  item.map.sections.splice(target, 0, section);
  item.map.structureVerified = false;
  noteActivity(item);
  save();
  renderStructure();
  requestAnimationFrame(() => document.querySelector(`[data-section-reorder="${CSS.escape(sectionId)}"]`)?.focus());
}

function startReorder(event, handle) {
  if (event.pointerType === "mouse" && event.button !== 0) return;
  const item = project();
  if (!item) return;
  const sectionId = handle.dataset.sectionReorder;
  const index = item.map.sections.findIndex((entry) => entry.id === sectionId);
  if (index < 0) return;
  reorderState = { pointerId: event.pointerId, sectionId, startIndex: index, targetIndex: index, handle };
  handle.setPointerCapture?.(event.pointerId);
  handle.closest(".arrangement-row")?.classList.add("dragging");
  event.preventDefault();
}

function updateReorder(event) {
  if (!reorderState || event.pointerId !== reorderState.pointerId) return;
  const row = document.elementFromPoint(event.clientX, event.clientY)?.closest(".arrangement-row[data-section-row]");
  document.querySelectorAll(".arrangement-row.drop-target").forEach((entry) => entry.classList.remove("drop-target"));
  if (!row) return;
  const item = project();
  const targetIndex = item?.map?.sections?.findIndex((entry) => entry.id === row.dataset.sectionRow) ?? -1;
  if (targetIndex < 0) return;
  reorderState.targetIndex = targetIndex;
  if (targetIndex !== reorderState.startIndex) row.classList.add("drop-target");
  event.preventDefault();
}

function finishReorder(event, cancelled = false) {
  if (!reorderState || event.pointerId !== reorderState.pointerId) return;
  const state = reorderState;
  reorderState = null;
  document.querySelectorAll(".arrangement-row.dragging,.arrangement-row.drop-target").forEach((entry) => entry.classList.remove("dragging", "drop-target"));
  try { state.handle.releasePointerCapture?.(event.pointerId); } catch (error) {}
  if (cancelled || state.targetIndex === state.startIndex) return;
  const item = project();
  const index = item?.map?.sections?.findIndex((entry) => entry.id === state.sectionId) ?? -1;
  if (index < 0) return;
  const [section] = item.map.sections.splice(index, 1);
  item.map.sections.splice(state.targetIndex, 0, section);
  item.map.structureVerified = false;
  noteActivity(item);
  save();
  renderStructure();
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
    noteActivity(item); save(); return renderSetup();
  }
  if (action === "continue-structure") return continueTo("structure");
  if (action === "open-add-section") return openAddSectionSheet();
  if (action === "edit-section") return openEditSectionSheet(button.dataset.sectionId);
  if (action === "toggle-structure-verified") {
    item.map.structureVerified = !item.map.structureVerified;
    noteActivity(item); save(); return renderStructure();
  }
  if (action === "continue-tracks") return continueTo("tracks");
  if (action === "toggle-track") {
    const name = button.dataset.name;
    const index = item.map.tracks.findIndex((track) => track.name === name);
    if (index >= 0) item.map.tracks.splice(index, 1);
    else item.map.tracks.push({ id: uid(), name });
    noteActivity(item); save(); return renderTracks();
  }
  if (action === "open-custom-track") return openCustomTrackSheet();
  if (action === "finish-map") return navigate("project", "replace");
});

app.addEventListener("input", (event) => {
  const item = project();
  if (!item || currentRoute !== "setup") return;
  if (event.target.id === "tempoInput") {
    item.map.setup.tempo = event.target.value;
    noteActivity(item); save(); syncSetupContinuation(item);
  }
});

app.addEventListener("change", (event) => {
  const item = project();
  if (!item || currentRoute !== "setup") return;
  if (event.target.id === "meterInput") {
    item.map.setup.meter = event.target.value;
    noteActivity(item); save(); syncSetupContinuation(item);
  }
});

app.addEventListener("pointerdown", (event) => {
  const handle = event.target.closest("[data-section-reorder]");
  if (handle) startReorder(event, handle);
});
app.addEventListener("pointermove", updateReorder);
app.addEventListener("pointerup", (event) => finishReorder(event, false));
app.addEventListener("pointercancel", (event) => finishReorder(event, true));
app.addEventListener("lostpointercapture", (event) => finishReorder(event, true), true);

app.addEventListener("keydown", (event) => {
  const handle = event.target.closest("[data-section-reorder]");
  if (!handle) return;
  if (event.key === "ArrowUp" || event.key === "ArrowDown") {
    event.preventDefault();
    moveSection(handle.dataset.sectionReorder, event.key === "ArrowUp" ? -1 : 1);
  }
});

sheetRoot.addEventListener("input", () => {
  if (sheetState?.type === "new-project") syncNewProjectAction();
  if (sheetState?.type === "custom-track") syncCustomTrackAction();
  if (sheetState?.type === "add-section") syncAddSectionSheet();
});

sheetRoot.addEventListener("click", (event) => {
  if (event.target === sheetRoot) return closeSheet();
  const button = event.target.closest("button");
  if (!button) return;
  const action = button.dataset.action;
  const item = project();
  if (action === "close-sheet") return closeSheet();
  if (action === "choose-project-type") return chooseProjectType(button.dataset.projectType);
  if (action === "create-project") return createProject();
  if (action === "choose-section-type") return chooseSectionType(button);
  if (action === "choose-section-bars") return chooseSectionBars(button);
  if (action === "add-section") return addSectionFromSheet();
  if (action === "add-custom-track") {
    const name = clean(document.getElementById("customTrackInput")?.value);
    if (!name || item.map.tracks.some((track) => track.name.toLowerCase() === name.toLowerCase())) return;
    item.map.tracks.push({ id: uid(), name });
    noteActivity(item); save(); closeSheet(); return renderTracks();
  }
  if (action === "save-section") {
    const section = item.map.sections.find((entry) => entry.id === sheetState.sectionId);
    if (!section) return;
    const name = clean(document.getElementById("editSectionName")?.value) || section.name;
    const bars = sheetState.bars === "custom" ? Number(document.getElementById("customBarsInput")?.value) : Number(sheetState.bars);
    if (!Number.isInteger(bars) || bars <= 0) return;
    section.name = name;
    section.lengthBars = bars;
    item.map.structureVerified = false;
    noteActivity(item); save(); closeSheet(); return renderStructure();
  }
  if (action === "duplicate-section") {
    const index = item.map.sections.findIndex((entry) => entry.id === sheetState.sectionId);
    if (index < 0) return;
    const copy = { ...deepCopy(item.map.sections[index]), id: uid() };
    item.map.sections.splice(index + 1, 0, copy);
    item.map.structureVerified = false;
    noteActivity(item); save(); closeSheet(); return renderStructure();
  }
  if (action === "delete-section") {
    item.map.sections = item.map.sections.filter((entry) => entry.id !== sheetState.sectionId);
    item.map.structureVerified = false;
    noteActivity(item); save(); closeSheet(); return renderStructure();
  }
  if (action === "edit-project") return openEditProjectSheet();
  if (action === "save-project") {
    const title = clean(document.getElementById("editProjectTitle")?.value);
    const artist = clean(document.getElementById("editProjectArtist")?.value);
    if (!title || (item.type === "study" && !artist)) return;
    item.title = title;
    item.artist = artist;
    noteActivity(item); save(); closeSheet(); return render();
  }
  if (action === "reset-project-preview") {
    resetPreviewProject(item); save(); closeSheet(); return render();
  }
  if (action === "delete-project-preview") {
    db.projects = db.projects.filter((entry) => entry.id !== item.id);
    db.currentProjectId = sortedProjects().find((entry) => entry.id !== item.id)?.id || db.projects[0]?.id || null;
    save(); closeSheet();
    if (currentRoute === "projects") return renderProjects();
    return navigate("projects", "replace");
  }
});

document.addEventListener("keydown", (event) => {
  if (event.key === "Escape" && !sheetRoot.hidden) closeSheet();
});

window.addEventListener("popstate", (event) => {
  const route = event.state?.v7Preview ? event.state.route : (location.hash || "#projects").slice(1);
  const validRoutes = new Set(["projects", "project", "setup", "structure", "tracks", "notes"]);
  currentRoute = validRoutes.has(route) ? route : "project";
  closeSheet(false);
  render();
  window.scrollTo(0, 0);
});

const hashRoute = (location.hash || "").slice(1);
const validRoutes = new Set(["projects", "project", "setup", "structure", "tracks", "notes"]);
currentRoute = validRoutes.has(hashRoute) ? hashRoute : (hashRoute ? "project" : "projects");
history.replaceState({ v7Preview: true, route: currentRoute }, "", `#${currentRoute}`);
render();
