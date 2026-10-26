import {
  applyEvaluation,
  currentProject,
  deriveActiveFocus,
  loadDb,
  projectMeta,
  resetCoreProject,
  saveDb,
  stateLabel,
} from "./core-model.js";

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
let buildCommitPromise = null;
let sheetState = null;

function save() {
  saveDb(db);
}

function project() {
  return currentProject(db);
}

function backButton() {
  return `<button class="toolbar-button icon-back" data-action="back-projects" aria-label="Projects"><span class="back-glyph" aria-hidden="true">‹</span></button>`;
}

function moreButton() {
  return `<button class="toolbar-button more-button" data-action="project-actions" aria-label="Project actions">•••</button>`;
}

function screenHeader(title, { back = false, right = "", meta = "" } = {}) {
  const left = back ? backButton() : `<span class="toolbar-spacer" aria-hidden="true"></span>`;
  const rightSlot = right || `<span class="toolbar-spacer" aria-hidden="true"></span>`;
  return `
    <header class="screen-header">
      <div class="toolbar"><div class="toolbar-slot toolbar-leading">${left}</div><div class="toolbar-slot toolbar-trailing">${rightSlot}</div></div>
      <div class="title-block"><h1>${esc(title)}</h1>${meta ? `<p class="screen-meta">${esc(meta)}</p>` : ""}</div>
    </header>`;
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
      if (target.isConnected) target.textContent = `Core proof · G7 · ${commit}`;
    });
  });
}

function routeFromHash() {
  const hash = location.hash.replace(/^#/, "");
  if (hash.startsWith("project/")) return { route: "project", id: decodeURIComponent(hash.slice(8)) };
  return { route: "projects", id: "" };
}

function navigateProjects(mode = "push") {
  closeSheet();
  const url = `${location.pathname}${location.search}#projects`;
  if (mode === "replace") history.replaceState({ coreProof: true, route: "projects" }, "", url);
  else history.pushState({ coreProof: true, route: "projects" }, "", url);
  render();
  window.scrollTo(0, 0);
}

function navigateProject(id, mode = "push") {
  const item = db.projects.find((candidate) => candidate.id === id);
  if (!item) return navigateProjects("replace");
  closeSheet();
  db.currentProjectId = item.id;
  save();
  const url = `${location.pathname}${location.search}#project/${encodeURIComponent(item.id)}`;
  if (mode === "replace") history.replaceState({ coreProof: true, route: "project", id: item.id }, "", url);
  else history.pushState({ coreProof: true, route: "project", id: item.id }, "", url);
  render();
  window.scrollTo(0, 0);
}

function renderProjects() {
  const rows = [...db.projects]
    .sort((a, b) => Number(b.lastActivityAt || 0) - Number(a.lastActivityAt || 0))
    .map((item) => `
      <div class="project-card">
        <button class="project-open" data-project="${esc(item.id)}">
          <span class="project-copy"><strong>${esc(item.title)}</strong><span>${esc(projectMeta(item))}</span></span>
        </button>
      </div>`).join("");

  app.innerHTML = `
    <main class="screen root-screen scroll-safe">
      ${screenHeader("Projects")}
      <div class="project-list group">${rows}</div>
      <div class="build-info root-build-info" aria-label="Core proof build">Core proof · G7 · …</div>
    </main>`;
  showBuildInfo();
}

function latestResultMarkup(item) {
  const last = item.core.history[item.core.history.length - 1];
  if (!last) return "";
  const outcome = last.outcome === "helped" ? "Helped" : last.outcome === "didnt-help" ? "Didn't help" : "Revealed something else";
  return `
    <div class="group utility-group">
      <div class="row">
        <span><span class="row-title">Last result</span><span class="row-sub">${esc(last.domain)} · ${esc(outcome)}</span></span>
      </div>
    </div>`;
}

function targetMarkup(item) {
  if (!item.core.target) return "";
  return `
    <div class="note-card">
      <div class="meta">Target</div>
      <p>${esc(item.core.target)}</p>
    </div>`;
}

function focusMarkup(item) {
  const focus = deriveActiveFocus(item);
  return `
    <section class="work-content">
      <div class="note-card">
        <div class="meta">${esc(focus.domain)} · ${esc(stateLabel(focus.state))}</div>
        <p><strong>${esc(focus.title)}</strong></p>
        <p>${esc(focus.why)}</p>
      </div>
      <div class="note-card">
        <div class="meta">Try in Logic</div>
        <p>${esc(focus.experiment)}</p>
      </div>
    </section>`;
}

function renderProject() {
  const item = project();
  if (!item) return navigateProjects("replace");
  app.innerHTML = `
    <main class="screen work-screen scroll-safe">
      ${screenHeader(item.title, { back: true, right: moreButton(), meta: projectMeta(item) })}
      ${targetMarkup(item)}
      ${focusMarkup(item)}
      ${latestResultMarkup(item)}
      <div class="work-action-host"><div class="page-action-footer"><button class="primary-action" data-action="tried-focus">I tried this</button></div></div>
    </main>`;
}

function render() {
  const route = routeFromHash();
  if (route.route === "project") {
    if (db.projects.some((item) => item.id === route.id)) db.currentProjectId = route.id;
    save();
    return renderProject();
  }
  renderProjects();
}

function openSheet(html, state = null, label = "Dialog") {
  sheetState = state;
  sheetRoot.innerHTML = `<div class="sheet" role="dialog" aria-modal="true" aria-label="${esc(label)}">${html}</div>`;
  sheetRoot.hidden = false;
  requestAnimationFrame(() => {
    const first = sheetRoot.querySelector("button, textarea, input, select");
    if (first) first.focus({ preventScroll: true });
  });
}

function closeSheet() {
  sheetRoot.hidden = true;
  sheetRoot.innerHTML = "";
  sheetState = null;
}

function openEvaluationSheet() {
  openSheet(`
    <div class="sheet-actions sheet-actions-stack">
      <button class="secondary-action" data-action="evaluate-helped">Helped</button>
      <button class="secondary-action" data-action="evaluate-didnt-help">Didn't help</button>
      <button class="secondary-action" data-action="evaluate-revealed">Revealed something else</button>
      <button class="secondary-action" data-action="close-sheet">Cancel</button>
    </div>`, { type: "evaluation" }, "How did the experiment go?");
}

function openRevealedSheet() {
  openSheet(`
    <div class="field-stack">
      <textarea id="revealedNote" class="field-input" rows="4" placeholder="What did it reveal?" aria-label="What did it reveal?"></textarea>
    </div>
    <div class="sheet-actions">
      <button class="secondary-action" data-action="close-sheet">Cancel</button>
      <button class="primary-action" data-action="save-revealed">Save</button>
    </div>`, { type: "revealed" }, "What did it reveal?");
}

function openProjectActions() {
  openSheet(`
    <div class="sheet-actions sheet-actions-stack">
      <button class="secondary-action" data-action="reset-core">Reset proof</button>
      <button class="secondary-action" data-action="close-sheet">Cancel</button>
    </div>`, { type: "project-actions" }, "Project actions");
}

function commitEvaluation(outcome, note = "") {
  const item = project();
  if (!item) return;
  applyEvaluation(item, outcome, note);
  save();
  closeSheet();
  renderProject();
  window.scrollTo(0, 0);
}

app.addEventListener("click", (event) => {
  const projectButton = event.target.closest("[data-project]");
  if (projectButton) return navigateProject(projectButton.dataset.project);

  const actionButton = event.target.closest("[data-action]");
  if (!actionButton) return;
  const action = actionButton.dataset.action;
  if (action === "back-projects") {
    if (history.state?.coreProof && history.length > 1) history.back();
    else navigateProjects("replace");
    return;
  }
  if (action === "project-actions") return openProjectActions();
  if (action === "tried-focus") return openEvaluationSheet();
});

sheetRoot.addEventListener("click", (event) => {
  if (event.target === sheetRoot) return closeSheet();
  const button = event.target.closest("[data-action]");
  if (!button) return;
  const action = button.dataset.action;
  if (action === "close-sheet") return closeSheet();
  if (action === "evaluate-helped") return commitEvaluation("helped");
  if (action === "evaluate-didnt-help") return commitEvaluation("didnt-help");
  if (action === "evaluate-revealed") return openRevealedSheet();
  if (action === "save-revealed") {
    const note = document.getElementById("revealedNote")?.value.trim() || "";
    if (!note) {
      document.getElementById("revealedNote")?.focus();
      return;
    }
    return commitEvaluation("revealed", note);
  }
  if (action === "reset-core") {
    const item = project();
    if (!item) return;
    resetCoreProject(item);
    save();
    closeSheet();
    renderProject();
  }
});

window.addEventListener("popstate", render);

if (!location.hash) history.replaceState({ coreProof: true, route: "projects" }, "", `${location.pathname}${location.search}#projects`);
render();
