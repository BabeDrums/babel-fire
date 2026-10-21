const PREVIEW_KEY = "production-projects-v1-v7-preview";
const app = document.getElementById("app");

const style = document.createElement("style");
style.textContent = `
  .v7-new-project-button{position:absolute;top:calc(18px + env(safe-area-inset-top));right:0;width:44px;height:44px;border:0;background:transparent;color:var(--text,#f5f5f7);font:300 34px/44px -apple-system,BlinkMacSystemFont,"SF Pro Display",sans-serif;cursor:pointer}
  .v7-empty-projects{display:grid;gap:18px;justify-items:center;padding:30px 24px;text-align:center}
  .v7-empty-projects span{color:var(--muted,#9b9ba3);font-size:18px}
  .v7-empty-projects button{min-height:46px;padding:0 22px;border:1px solid #4a4a50;border-radius:14px;background:#2d2d34;color:#fff;font:600 17px -apple-system,BlinkMacSystemFont,"SF Pro Text",sans-serif}
  .v7-create-backdrop{position:fixed;inset:0;z-index:1000;display:flex;align-items:flex-end;justify-content:center;padding:12px;background:rgba(0,0,0,.5)}
  .v7-create-sheet{width:min(100%,520px);margin-bottom:max(8px,env(safe-area-inset-bottom));padding:24px;border:1px solid #34343a;border-radius:24px;background:#171719;box-shadow:0 20px 70px rgba(0,0,0,.45)}
  .v7-create-sheet h2{margin:0 0 6px;font-size:26px;letter-spacing:-.02em}
  .v7-create-sheet .v7-create-kind{margin:0 0 22px;color:#9b9ba3;font-size:15px}
  .v7-create-sheet label{display:block;margin:14px 0 7px;color:#b8b8bf;font-size:14px;font-weight:600}
  .v7-create-sheet input{box-sizing:border-box;width:100%;min-height:50px;padding:0 14px;border:1px solid #3a3a40;border-radius:12px;background:#0f0f11;color:#fff;font:17px -apple-system,BlinkMacSystemFont,"SF Pro Text",sans-serif;outline:none}
  .v7-create-sheet input:focus{border-color:#777780}
  .v7-create-actions{display:flex;gap:10px;margin-top:22px}
  .v7-create-actions button{min-height:48px;border-radius:13px;font:600 16px -apple-system,BlinkMacSystemFont,"SF Pro Text",sans-serif}
  .v7-create-cancel{flex:1;border:1px solid #3a3a40;background:transparent;color:#d0d0d5}
  .v7-create-save{flex:1.5;border:1px solid #55555d;background:#303038;color:#fff}
  @media(min-width:700px){.v7-create-backdrop{align-items:center}.v7-create-sheet{margin-bottom:0}}
`;
document.head.appendChild(style);

function isProjectsScreen() {
  return location.hash === "" || location.hash === "#projects";
}

function enhanceProjects() {
  if (!isProjectsScreen()) return;
  const screen = app.querySelector(".root-screen");
  const header = screen?.querySelector(".projects-header");
  if (!screen || !header) return;

  header.style.position = "relative";
  if (!header.querySelector(".v7-new-project-button")) {
    const add = document.createElement("button");
    add.className = "v7-new-project-button";
    add.type = "button";
    add.setAttribute("aria-label", "New Project");
    add.textContent = "+";
    add.addEventListener("click", openCreateSheet);
    header.appendChild(add);
  }

  const empty = screen.querySelector(".project-list .empty-state");
  if (empty && !empty.classList.contains("v7-empty-projects")) {
    empty.classList.add("v7-empty-projects");
    empty.innerHTML = `<span>No preview projects.</span><button type="button">New Project</button>`;
    empty.querySelector("button").addEventListener("click", openCreateSheet);
  }
}

function openCreateSheet() {
  if (document.querySelector(".v7-create-backdrop")) return;
  const backdrop = document.createElement("div");
  backdrop.className = "v7-create-backdrop";
  backdrop.innerHTML = `
    <form class="v7-create-sheet">
      <h2>New Project</h2>
      <p class="v7-create-kind">Recreation</p>
      <label for="v7ProjectTitle">Song</label>
      <input id="v7ProjectTitle" name="title" autocomplete="off" placeholder="Song title" required>
      <label for="v7ProjectArtist">Artist</label>
      <input id="v7ProjectArtist" name="artist" autocomplete="off" placeholder="Artist" required>
      <div class="v7-create-actions">
        <button class="v7-create-cancel" type="button">Cancel</button>
        <button class="v7-create-save" type="submit">Create Project</button>
      </div>
    </form>`;
  document.body.appendChild(backdrop);
  const form = backdrop.querySelector("form");
  const title = backdrop.querySelector("#v7ProjectTitle");
  backdrop.querySelector(".v7-create-cancel").addEventListener("click", () => backdrop.remove());
  backdrop.addEventListener("click", (event) => { if (event.target === backdrop) backdrop.remove(); });
  form.addEventListener("submit", (event) => {
    event.preventDefault();
    createProject(new FormData(form));
  });
  requestAnimationFrame(() => title.focus());
}

function createProject(formData) {
  const title = String(formData.get("title") || "").trim();
  const artist = String(formData.get("artist") || "").trim();
  if (!title || !artist) return;

  let db;
  try { db = JSON.parse(localStorage.getItem(PREVIEW_KEY)); } catch (_) {}
  if (!db || !Array.isArray(db.projects)) db = { version: 5, currentProjectId: null, projects: [] };

  const id = crypto?.randomUUID?.() || `preview-${Date.now()}-${Math.random().toString(36).slice(2)}`;
  const project = {
    id,
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

  db.version = 5;
  db.projects.push(project);
  db.currentProjectId = id;
  localStorage.setItem(PREVIEW_KEY, JSON.stringify(db));
  location.hash = "#project";
  location.reload();
}

const observer = new MutationObserver(enhanceProjects);
observer.observe(app, { childList: true, subtree: true });
window.addEventListener("hashchange", () => requestAnimationFrame(enhanceProjects));
enhanceProjects();
