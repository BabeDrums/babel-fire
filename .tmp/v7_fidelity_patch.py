from pathlib import Path


def replace_once(path, old, new):
    p = Path(path)
    text = p.read_text()
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"{path}: expected one match, found {count}\n--- needle ---\n{old[:500]}")
    p.write_text(text.replace(old, new, 1))


# v7-preview/app.js
path = "v7-preview/app.js"
replace_once(path, '''function showBuildStamp() {
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
''', '''function showBuildInfo() {
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
      if (target.isConnected) target.textContent = `V7 Preview · ${commit}`;
    });
  });
}
''')
replace_once(path, '''      <div class="project-list group">${rows || `<div class="empty-state projects-empty">No projects yet.</div>`}</div>
      <footer class="build-stamp">FIRE V7 PREVIEW · …</footer>
    </main>`;
  showBuildStamp();
}
''', '''      <div class="project-list group">${rows || `<div class="empty-state projects-empty">No projects yet.</div>`}</div>
    </main>`;
}
''')
replace_once(path, '''  const future = ["The Skeleton", "The Sounds", "The Balance", "The Shape", "The World", "The Finish"]
    .map((name) => `<span>${esc(name)}</span>`).join("");
''', '''  const future = ["The Skeleton", "The Sounds", "The Balance", "The Shape", "The World", "The Finish"]
    .map((name) => esc(name)).join(" · ");
''')
replace_once(path, '''function setupRow(label, field, value, help = "") {
  const checked = !!value;
  const accessory = field === "reference"
    ? `<span class="form-value status-value">${checked ? "Imported" : "Import"}</span>`
    : completionAccessory(checked);
  return `
    <button class="form-row" data-action="toggle-setup" data-field="${field}">
      <span><span class="form-label">${esc(label)}</span>${help ? `<span class="form-help">${esc(help)}</span>` : ""}</span>
      ${accessory}
    </button>`;
}
''', '''function referenceRow(setup) {
  const imported = !!setup.reference;
  const detail = clean(setup.referenceName) || (imported ? "Imported reference" : "Choose audio from Files");
  return `
    <button class="form-row reference-row" data-action="${imported ? "reference-actions" : "import-reference"}">
      <span><span class="form-label">Reference</span><span class="form-help reference-detail">${esc(detail)}</span></span>
      ${imported ? completionAccessory(true) : `<span class="form-action">Import…</span>`}
    </button>
    <input id="referenceFileInput" class="visually-hidden" type="file" accept="audio/*" aria-label="Reference audio file">`;
}

function setupRow(label, field, value, help = "") {
  const checked = !!value;
  return `
    <button class="form-row" data-action="toggle-setup" data-field="${field}">
      <span><span class="form-label">${esc(label)}</span>${help ? `<span class="form-help">${esc(help)}</span>` : ""}</span>
      ${completionAccessory(checked)}
    </button>`;
}
''')
replace_once(path, '''        ${setupRow("Reference", "reference", setup.reference)}
''', '''        ${referenceRow(setup)}
''')
replace_once(path, '''function openNewProjectSheet() {
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
''', '''function openNewProjectSheet() {
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
      <button class="sheet-primary" data-action="create-project" disabled>Create Project</button>
    </div>`, { type: "new-project" });
  requestAnimationFrame(() => document.getElementById("newProjectTitle")?.focus());
}

function syncNewProjectAction() {
  const button = sheetRoot.querySelector('[data-action="create-project"]');
  if (!button) return;
  const title = clean(document.getElementById("newProjectTitle")?.value);
  const artist = clean(document.getElementById("newProjectArtist")?.value);
  button.disabled = !(title && artist);
}

function openReferenceSheet() {
  const setup = project()?.map?.setup;
  if (!setup?.reference) return;
  const detail = clean(setup.referenceName) || "Imported reference";
  openSheet(`
    <div class="grabber"></div>
    <h2>Reference</h2>
    <p class="sheet-kicker reference-sheet-name">${esc(detail)}</p>
    <div class="group">
      <button class="row" data-action="replace-reference"><span class="row-title">Replace Reference</span><span></span></button>
      <button class="row sheet-danger" data-action="remove-reference"><span class="row-title">Remove Reference</span><span></span></button>
    </div>
    <div class="sheet-actions"><button class="sheet-close" data-action="close-sheet">Cancel</button></div>`, { type: "reference" });
}
''')
replace_once(path, '''      setup: { reference: false, tempo: "", meter: "4/4", grid: false, firstListen: false },
''', '''      setup: { reference: false, referenceName: "", tempo: "", meter: "4/4", grid: false, firstListen: false },
''')
replace_once(path, '''function openProjectActions() {
  const item = project();
  if (!item) return;
  openSheet(`<div class="grabber"></div><h2>${esc(item.title)}</h2><div class="group"><button class="row" data-action="edit-project"><span class="row-title">Edit Project</span><span class="chevron">›</span></button><button class="row" data-action="reset-project-preview"><span><span class="row-title">Reset Progress</span><span class="row-sub">Keeps title, artist, and notes.</span></span><span></span></button><button class="row sheet-danger" data-action="delete-project-preview"><span class="row-title">Delete Project</span><span></span></button></div><div class="sheet-actions"><button class="sheet-close" data-action="close-sheet">Cancel</button></div>`, { type: "project-actions" });
}
''', '''function openProjectActions() {
  const item = project();
  if (!item) return;
  openSheet(`<div class="grabber"></div><h2>${esc(item.title)}</h2><div class="group"><button class="row" data-action="edit-project"><span class="row-title">Edit Project</span><span class="chevron">›</span></button><button class="row" data-action="reset-project-preview"><span><span class="row-title">Reset Progress</span><span class="row-sub">Keeps title, artist, and notes.</span></span><span></span></button><button class="row sheet-danger" data-action="delete-project-preview"><span class="row-title">Delete Project</span><span></span></button></div><div class="sheet-actions"><button class="sheet-close" data-action="close-sheet">Cancel</button></div><div class="sheet-meta build-info">V7 Preview · …</div>`, { type: "project-actions" });
  showBuildInfo();
}
''')
replace_once(path, '''  if (action === "new-project") return openNewProjectSheet();
  if (action === "project-actions") return openProjectActions();
  if (action === "toggle-setup") {
''', '''  if (action === "new-project") return openNewProjectSheet();
  if (action === "project-actions") return openProjectActions();
  if (action === "import-reference") {
    document.getElementById("referenceFileInput")?.click();
    return;
  }
  if (action === "reference-actions") return openReferenceSheet();
  if (action === "toggle-setup") {
''')
replace_once(path, '''app.addEventListener("input", (event) => {
  const item = project();
  if (!item || currentRoute !== "setup") return;
  if (event.target.id === "tempoInput") {
    item.map.setup.tempo = event.target.value;
    save();
    syncSetupContinuation(item);
  }
});
''', '''app.addEventListener("input", (event) => {
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
});
''')
replace_once(path, '''app.addEventListener("change", (event) => {
  const item = project();
  if (!item || currentRoute !== "setup") return;
  if (event.target.id === "meterInput") {
    item.map.setup.meter = event.target.value;
    save();
  }
});
''', '''app.addEventListener("change", (event) => {
  const item = project();
  if (!item || currentRoute !== "setup") return;
  if (event.target.id === "referenceFileInput") {
    const file = event.target.files?.[0];
    if (!file) return;
    item.map.setup.reference = true;
    item.map.setup.referenceName = file.name;
    save();
    renderSetup();
    return;
  }
  if (event.target.id === "meterInput") {
    item.map.setup.meter = event.target.value;
    save();
  }
});
''')
replace_once(path, '''  if (action === "close-sheet") return closeSheet();
  if (action === "create-project") return createProject();
''', '''  if (action === "close-sheet") return closeSheet();
  if (action === "create-project") return createProject();
  if (action === "replace-reference") {
    closeSheet();
    requestAnimationFrame(() => document.getElementById("referenceFileInput")?.click());
    return;
  }
  if (action === "remove-reference") {
    item.map.setup.reference = false;
    item.map.setup.referenceName = "";
    save();
    closeSheet();
    return renderSetup();
  }
''')

# v7-preview/styles.css
path = "v7-preview/styles.css"
replace_once(path, '''.app-shell {
  width: min(100%, 720px);
''', '''.app-shell {
  width: min(100%, 760px);
''')
replace_once(path, '''.build-stamp {
  position: fixed;
  left: 50%;
  bottom: calc(8px + env(safe-area-inset-bottom));
  transform: translateX(-50%);
  color: var(--quiet);
  font-size: 10px;
  line-height: 14px;
  letter-spacing: .03em;
  white-space: nowrap;
  opacity: .42;
  pointer-events: none;
}
''', '''.sheet-meta {
  margin-top: 12px;
  color: var(--quiet);
  font-size: 10px;
  line-height: 14px;
  letter-spacing: .03em;
  text-align: center;
  opacity: .72;
}
''')
replace_once(path, '''.future-phase-list {
  display: flex;
  flex-wrap: wrap;
  gap: 5px 13px;
  color: #85868e;
  font-size: 13px;
  line-height: 1.5;
}
.future-phase-list span { white-space: nowrap; }
''', '''.future-phase-list {
  color: #85868e;
  font-size: 13px;
  line-height: 1.55;
}
''')
replace_once(path, '''.form-value { color: #dddde2; display: inline-flex; gap: 8px; align-items: center; }
.status-value { color: #b8b8c0; }
''', '''.form-value { color: #dddde2; display: inline-flex; gap: 8px; align-items: center; }
.form-action { color: #d1d1d7; font-size: 14px; font-weight: 620; }
.reference-detail { max-width: 430px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
.visually-hidden { position: absolute !important; width: 1px !important; height: 1px !important; padding: 0 !important; margin: -1px !important; overflow: hidden !important; clip: rect(0 0 0 0) !important; white-space: nowrap !important; border: 0 !important; }
''')
replace_once(path, '''.primary-action {
  min-height: 48px;
  min-width: min(100%, 220px);
  padding: 0 18px;
  border-radius: 13px;
  background: #ececef;
  border: 1px solid rgba(255,255,255,.16);
  color: #111114;
  font-weight: 740;
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.primary-action:not(:disabled):active { background: #d9d9de; }
''', '''.primary-action {
  min-height: 48px;
  min-width: min(100%, 220px);
  padding: 0 18px;
  border-radius: 13px;
  background: #36363c;
  border: 1px solid #5f6069;
  color: var(--text);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.06), 0 1px 2px rgba(0,0,0,.28);
  font-weight: 730;
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.primary-action:not(:disabled):active { background: #414148; }
''')
replace_once(path, '''.track-tile.selected { background: #25252a; border-color: #4a4a52; }
''', '''.track-tile.selected {
  background: #2b2b31;
  border-color: #5b5c65;
  box-shadow: inset 0 0 0 1px rgba(255,255,255,.045);
}
''')
replace_once(path, '''.field {
  min-height: 48px;
  width: 100%;
  border-radius: 12px;
  border: 1px solid var(--line);
  background: #101012;
  color: var(--text);
  padding: 0 13px;
  outline: none;
}
.field::placeholder { color: var(--quiet); }
''', '''.field {
  min-height: 48px;
  width: 100%;
  border-radius: 12px;
  border: 1px solid var(--line);
  background: #101012;
  color: var(--text);
  padding: 0 13px;
  outline: none;
}
.field:focus-visible {
  outline: none;
  border-color: rgba(255,255,255,.34);
  box-shadow: 0 0 0 3px rgba(255,255,255,.07);
}
.field::placeholder { color: var(--quiet); }
''')
replace_once(path, '''.compact-button {
  min-height: 48px;
  padding: 0 16px;
  border: 1px solid var(--line-strong);
  border-radius: 12px;
  background: #29292e;
  font-weight: 680;
}
''', '''.compact-button {
  min-height: 48px;
  padding: 0 16px;
  border: 1px solid var(--line-strong);
  border-radius: 12px;
  background: #29292e;
  font-weight: 680;
}
.sheet-primary {
  min-height: 48px;
  padding: 0 16px;
  border: 1px solid #55565f;
  border-radius: 12px;
  background: #333338;
  color: var(--text);
  font-weight: 700;
}
.sheet-primary:not(:disabled):active { background: #404047; }
.sheet-primary:disabled {
  opacity: 1;
  background: #202023;
  border-color: var(--line);
  color: #666770;
}
''')
replace_once(path, '''@media (max-width: 430px) {
  h1 { font-size: 40px; }
''', '''@media (max-width: 430px) {
  h1 { font-size: 40px; }
  .action-row { justify-content: stretch; }
  .primary-action { width: 100%; min-width: 100%; }
''')
replace_once(path, '''@media (min-width: 700px) {
  .app-shell { padding-inline: 34px; padding-bottom: 54px; }
''', '''@media (min-width: 700px) {
  .app-shell { width: min(100%, 760px); padding-inline: 34px; padding-bottom: 54px; }
  .page-header h1, .project-identity h1 { font-size: 44px; }
  .projects-heading h1 { font-size: 46px; }
''')

# tests/test_v7_preview.py
path = "tests/test_v7_preview.py"
replace_once(path, '''        expect(page.locator(".build-stamp")).to_contain_text("FIRE V7 PREVIEW")
''', '''        self.assertEqual(page.locator(".build-stamp").count(), 0)
''')
replace_once(path, '''        page.get_by_role("button", name="New Project").click()
        expect(page.locator(".sheet")).to_be_visible()
        page.get_by_role("textbox", name="Song title").fill("Still")
        page.get_by_role("textbox", name="Artist").fill("Babel")
        page.get_by_role("button", name="Create Project").click()
''', '''        page.get_by_role("button", name="New Project").click()
        expect(page.locator(".sheet")).to_be_visible()
        create = page.get_by_role("button", name="Create Project")
        expect(create).to_be_disabled()
        page.get_by_role("textbox", name="Song title").fill("Still")
        expect(create).to_be_disabled()
        page.get_by_role("textbox", name="Artist").fill("Babel")
        expect(create).to_be_enabled()
        create.click()
''')
replace_once(path, '''        expect(page.locator(".future-label")).to_have_text("Later")
        expect(page.locator(".future-phase-list span")).to_have_count(6)
''', '''        expect(page.locator(".future-label")).to_have_text("Later")
        expect(page.locator(".future-phase-list")).to_contain_text("The Skeleton · The Sounds · The Balance")
''')
replace_once(path, '''        reference = page.locator('.form-row[data-field="reference"]')
        expect(reference).to_contain_text("Imported")
        self.assertEqual(reference.locator(".checkmark").count(), 0)
        expect(page.get_by_role("button", name="Continue to Structure")).to_be_visible()
''', '''        reference = page.locator(".reference-row")
        expect(reference.locator(".reference-detail")).to_have_text("Imported reference")
        expect(reference.locator(".checkmark")).to_be_visible()
        expect(page.get_by_role("button", name="Continue to Structure")).to_be_visible()
''')
insert_after = '''    def test_song_setup_continuation_reacts_to_tempo_without_rerendering_input(self):
'''
new_test = '''    def test_reference_import_has_identity_feedback_and_replace_remove_actions(self):
        page = self.open("setup")
        reference = page.locator(".reference-row")
        expect(reference).to_contain_text("Import…")
        expect(reference.locator(".reference-detail")).to_have_text("Choose audio from Files")
        self.assertEqual(reference.locator(".checkmark").count(), 0)

        page.locator("#referenceFileInput").set_input_files({
            "name": "still-reference.wav",
            "mimeType": "audio/wav",
            "buffer": b"RIFFfake",
        })
        reference = page.locator(".reference-row")
        expect(reference.locator(".reference-detail")).to_have_text("still-reference.wav")
        expect(reference.locator(".checkmark")).to_be_visible()
        self.assertEqual(reference.get_by_text("Import…", exact=True).count(), 0)

        reference.click()
        expect(page.get_by_role("button", name="Replace Reference")).to_be_visible()
        expect(page.get_by_role("button", name="Remove Reference")).to_be_visible()
        page.get_by_role("button", name="Remove Reference").click()
        reference = page.locator(".reference-row")
        expect(reference.locator(".reference-detail")).to_have_text("Choose audio from Files")
        expect(reference).to_contain_text("Import…")
        self.assertEqual(reference.locator(".checkmark").count(), 0)

        preview = page.evaluate("(key) => JSON.parse(localStorage.getItem(key))", PREVIEW_KEY)
        setup = preview["projects"][0]["map"]["setup"]
        self.assertFalse(setup["reference"])
        self.assertEqual(setup.get("referenceName", ""), "")

'''
text = Path(path).read_text()
if insert_after not in text:
    raise SystemExit("test_v7_preview.py: insertion point not found")
Path(path).write_text(text.replace(insert_after, new_test + insert_after, 1))
replace_once(path, '''        tile = page.locator('.track-tile[data-name="Drums"]')
        tile.click()
        expect(tile).to_have_attribute("aria-pressed", "true")
        expect(page.get_by_role("button", name="Continue to Section Study")).to_be_visible()
''', '''        tile = page.locator('.track-tile[data-name="Drums"]')
        unselected = page.locator('.track-tile[data-name="Bass"]')
        unselected_color = unselected.evaluate("el => getComputedStyle(el).backgroundColor")
        tile.click()
        expect(tile).to_have_attribute("aria-pressed", "true")
        selected_color = tile.evaluate("el => getComputedStyle(el).backgroundColor")
        self.assertNotEqual(selected_color, unselected_color)
        expect(page.get_by_role("button", name="Continue to Section Study")).to_be_visible()
''')
replace_once(path, '''        expect(page.get_by_role("button", name="Delete Project")).to_be_visible()
''', '''        expect(page.get_by_role("button", name="Delete Project")).to_be_visible()
        expect(page.locator(".build-info")).to_contain_text("V7 Preview")
''')

# V7_DRAFT.md
path = "V7_DRAFT.md"
replace_once(path, '''- **Status/value** — concise text when a word communicates the state better than an icon.
''', '''- **Status/value** — concise text when text is the information itself; do not use a bare word as the only feedback for an action that needs stronger confirmation.
''')
replace_once(path, '''Do not show two indicators for the same state. A primary action must read differently from a selected option.
''', '''Do not show two indicators for the same state. A primary action must read differently from a selected option. During the fundamentals gate, prove hierarchy in grayscale through luminance, material, border, typography, spacing, and state before introducing a functional accent color.

Reference is a special case: the filename/identity answers **what** is loaded, while a completion mark answers whether the setup requirement is satisfied. The preview should use a real file picker, persist the selected filename as metadata, and offer Replace / Remove rather than treating Reference like a silent boolean toggle.
''')
replace_once(path, '''- Preview-only sandbox information stays visually subordinate.
''', '''- Preview-only sandbox information stays out of the main Projects canvas; build/version traceability belongs in a subordinate project-actions/debug location during review.
''')
replace_once(path, '''## iPhone / iPad adaptation
''', '''## Interaction fidelity + grayscale foundation

Before signature personality arrives, ordinary controls should feel finished without relying on color:

- selected options must be obvious through grayscale surface/border contrast
- primary continuation must be distinct from selection without becoming a stark white web-style button
- required sheet actions should be visibly disabled until valid
- fields should use restrained focus treatment instead of oversized browser-like rings
- compact widths may use full-width primary actions while regular widths can use trailing compact actions; product logic stays identical
- future customizable atmosphere, animation, and expressive modes are intentionally deferred until the neutral control system is trustworthy

## iPhone / iPad adaptation
''')

# START_HERE.md
path = "START_HERE.md"
replace_once(path, '''PR #36, **Consolidate V7 shell and Journey**, is merged and deployed at `a151376…`; its PR and post-merge regression matrices passed at 390px, 440px, and 820px, and Pages deployment #61 succeeded. PRs #34–#35 remain the preceding Projects/continuity milestones.
''', '''PR #37, **Refine V7 visual semantics and composition**, is merged and deployed at `ae00659…`; its PR and post-merge regression matrices passed at 390px, 440px, and 820px, and Pages deployment #62 succeeded. PR #36 is the preceding shell-consolidation milestone; PRs #34–#35 remain the preceding Projects/continuity milestones.
''')
replace_once(path, '''The current refinement direction is **visual semantics + composition**: selection, completion, status, navigation, and primary progression must use distinct visual languages; future phases should orient without looking like dead controls; and the same adaptive FIRE interface must preserve identical product logic across phone/tablet sizes.
''', '''The current refinement direction is **grayscale interaction fidelity**: make controls feel finished without relying on accent color, replace prototype boolean-style interactions with truthful state behavior, preserve distinct selection/completion/navigation/progression semantics, and let compact/regular layouts adapt presentation without changing product logic.
''')
replace_once(path, '''- temporary subtle `FIRE V7 PREVIEW · <commit>` stamp remains for physical-review traceability
''', '''- preview build/commit traceability stays available in subordinate project actions/debug UI rather than occupying the main Projects canvas
''')
replace_once(path, '''- **status/value** uses text where text is clearer (for example, `Imported`)
''', '''- **status/value** uses text when text is the information itself; Reference uses filename/identity plus completion feedback rather than a bare `Import` / `Imported` toggle
''')
replace_once(path, '''### Testing

- exact Journey signature treatment beyond the restrained semantic hierarchy
''', '''### Testing

- grayscale interaction-fidelity refinements: material contrast, primary-action weight, field focus, Reference import/replace/remove, and compact-vs-regular composition
- exact Journey signature treatment beyond the restrained semantic hierarchy
''')
replace_once(path, '''1. Projects — `+`, one create path, quiet empty state, build stamp, no needless subtitle
''', '''1. Projects — `+`, one create path, quiet empty state, no visible prototype stamp, no needless subtitle
''')
replace_once(path, '''3. Song Setup — focused task, no duplicated status copy
''', '''3. Song Setup — real Reference file-selection feedback with filename + completion, Replace/Remove behavior, and no fake boolean toggle semantics
''')
