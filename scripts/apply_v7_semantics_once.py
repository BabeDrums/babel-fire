from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def replace_once(path: str, old: str, new: str) -> None:
    file = ROOT / path
    text = file.read_text(encoding="utf-8")
    if old not in text:
        raise SystemExit(f"expected text not found in {path}: {old[:80]!r}")
    file.write_text(text.replace(old, new, 1), encoding="utf-8")


def replace_all(path: str, old: str, new: str) -> None:
    file = ROOT / path
    text = file.read_text(encoding="utf-8")
    if old not in text:
        raise SystemExit(f"expected text not found in {path}: {old[:80]!r}")
    file.write_text(text.replace(old, new), encoding="utf-8")


# V7 runtime: semantic state language + composition.
replace_once(
    "v7-preview/app.js",
    '''  const future = ["The Skeleton", "The Sounds", "The Balance", "The Shape", "The World", "The Finish"]
    .map((name) => `<div class="future-row"><span>${esc(name)}</span></div>`).join("");''',
    '''  const future = ["The Skeleton", "The Sounds", "The Balance", "The Shape", "The World", "The Finish"]
    .map((name) => `<span>${esc(name)}</span>`).join("");''',
)
replace_once(
    "v7-preview/app.js",
    '''        <div class="future-phases" aria-label="Future phases">${future}</div>''',
    '''        <div class="future-phases" aria-label="Later phases">
          <span class="future-label">Later</span>
          <div class="future-phase-list">${future}</div>
        </div>''',
)
replace_once(
    "v7-preview/app.js",
    '''  const accessory = field === "reference"
    ? (checked
      ? `<span class="form-value"><span>Imported</span><span class="checkmark" aria-label="Done">✓</span></span>`
      : `<span class="form-value">Import</span>`)
    : completionAccessory(checked);''',
    '''  const accessory = field === "reference"
    ? `<span class="form-value status-value">${checked ? "Imported" : "Import"}</span>`
    : completionAccessory(checked);''',
)
replace_once(
    "v7-preview/app.js",
    '''      ${sections.length ? `<button class="confirm-row" data-action="toggle-structure-verified"><span class="row-title">Structure matches the song</span>${item.map.structureVerified ? `<span class="checkmark" aria-label="Done">✓</span>` : `<span class="trailing">Confirm</span>`}</button>` : ""}''',
    '''      ${sections.length ? `<button class="confirm-row" data-action="toggle-structure-verified"><span class="row-title">Structure matches the song</span>${completionAccessory(item.map.structureVerified)}</button>` : ""}''',
)
replace_once(
    "v7-preview/app.js",
    '''      <div class="custom-track"><input id="customTrackInput" class="field" placeholder="Other…" aria-label="Other track"><button class="compact-button" data-action="add-custom-track">Add</button></div>''',
    '''      <div class="custom-track-control"><input id="customTrackInput" class="field" placeholder="Other…" aria-label="Other track"><button class="inline-add-button" data-action="add-custom-track" aria-label="Add custom track">＋</button></div>''',
)
replace_once(
    "v7-preview/app.js",
    '''document.addEventListener("keydown", (event) => {
  if (event.key === "Escape" && !sheetRoot.hidden) closeSheet();
});''',
    '''app.addEventListener("keydown", (event) => {
  if (currentRoute !== "tracks" || event.target.id !== "customTrackInput" || event.key !== "Enter") return;
  event.preventDefault();
  app.querySelector('[data-action="add-custom-track"]')?.click();
});

document.addEventListener("keydown", (event) => {
  if (event.key === "Escape" && !sheetRoot.hidden) closeSheet();
});''',
)

replace_once(
    "v7-preview/styles.css",
    '''.journey-row.current {
  background: rgba(255,255,255,.035);
}
.journey-row.current .row-title { font-weight: 735; color: var(--text); }
.journey-row.done .row-title { color: #d1d1d7; }''',
    '''.journey-row.current {
  background: rgba(255,255,255,.055);
}
.journey-row.current .row-title { font-weight: 735; color: var(--text); }
.journey-row.done .row-title { color: #b8b8c0; }
.journey-row.upcoming .row-title { color: #8d8e96; }
.journey-row.done .chevron,
.journey-row.upcoming .chevron { opacity: .72; }''',
)
replace_once(
    "v7-preview/styles.css",
    '''.future-phases {
  margin: 10px 2px 0;
  border-top: 1px solid rgba(255,255,255,.055);
}
.future-row {
  min-height: 38px;
  display: flex;
  align-items: center;
  border-bottom: 1px solid rgba(255,255,255,.045);
}
.future-row:last-child { border-bottom: 0; }
.future-row span { font-size: 14px; font-weight: 560; color: #8d8e96; }''',
    '''.future-phases {
  margin: 13px 3px 0;
  display: grid;
  gap: 7px;
}
.future-label {
  color: var(--quiet);
  font-size: 12px;
  font-weight: 700;
}
.future-phase-list {
  display: flex;
  flex-wrap: wrap;
  gap: 5px 13px;
  color: #85868e;
  font-size: 13px;
  line-height: 1.5;
}
.future-phase-list span { white-space: nowrap; }''',
)
replace_once(
    "v7-preview/styles.css",
    '.form-value { color: #dddde2; display: inline-flex; gap: 8px; align-items: center; }',
    '.form-value { color: #dddde2; display: inline-flex; gap: 8px; align-items: center; }\n.status-value { color: #b8b8c0; }',
)
replace_once(
    "v7-preview/styles.css",
    '''.primary-action {
  min-height: 48px;
  min-width: min(100%, 220px);
  padding: 0 18px;
  border-radius: 13px;
  background: #2b2b30;
  border: 1px solid var(--line-strong);
  color: var(--text);
  font-weight: 720;
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.primary-action:not(:disabled):active { background: #35353b; }''',
    '''.primary-action {
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
.primary-action:not(:disabled):active { background: #d9d9de; }''',
)
replace_once(
    "v7-preview/styles.css",
    '''.track-tile.selected { background: #26262b; border-color: var(--line-strong); }
.track-tile:active { background: #222226; }
.custom-track, .custom-section-entry {
  margin-top: 11px;
  display: grid;
  grid-template-columns: minmax(0,1fr) auto;
  gap: 9px;
}''',
    '''.track-tile.selected { background: #25252a; border-color: #4a4a52; }
.track-tile:active { background: #222226; }
.custom-track-control {
  margin-top: 11px;
  position: relative;
}
.custom-track-control .field { padding-right: 54px; }
.inline-add-button {
  position: absolute;
  top: 2px;
  right: 2px;
  width: 44px;
  height: 44px;
  border-radius: 10px;
  color: #c9c9cf;
  font-size: 24px;
  font-weight: 400;
  display: inline-grid;
  place-items: center;
}
.inline-add-button:active { background: rgba(255,255,255,.07); }
.custom-section-entry {
  margin-top: 11px;
  display: grid;
  grid-template-columns: minmax(0,1fr) auto;
  gap: 9px;
}''',
)
replace_once("v7-preview/styles.css", "  .future-row { min-height: 36px; }\n", "")

# Browser regressions for the new semantics.
replace_once(
    "tests/test_v7_preview.py",
    '        self.assertEqual(page.get_by_text("Later", exact=True).count(), 0)',
    '''        expect(page.locator(".future-label")).to_have_text("Later")
        expect(page.locator(".future-phase-list span")).to_have_count(6)
        self.assertEqual(page.locator(".future-row").count(), 0)''',
)
replace_once(
    "tests/test_v7_preview.py",
    '''        page = self.open("setup", study_db(setup=True))
        self.assertEqual(page.get_by_text("Done", exact=True).count(), 0)
        expect(page.get_by_role("button", name="Continue to Structure")).to_be_visible()''',
    '''        page = self.open("setup", study_db(setup=True))
        self.assertEqual(page.get_by_text("Done", exact=True).count(), 0)
        reference = page.locator('.form-row[data-field="reference"]')
        expect(reference).to_contain_text("Imported")
        self.assertEqual(reference.locator(".checkmark").count(), 0)
        expect(page.get_by_role("button", name="Continue to Structure")).to_be_visible()''',
)
replace_once(
    "tests/test_v7_preview.py",
    '''        page.get_by_role("button", name="Structure matches the song").click()
        expect(page.get_by_role("button", name="Continue to Tracks")).to_be_visible()''',
    '''        confirm = page.get_by_role("button", name="Structure matches the song")
        expect(confirm.locator(".completion-ring")).to_be_visible()
        confirm.click()
        expect(page.get_by_role("button", name="Continue to Tracks")).to_be_visible()
        expect(page.get_by_role("button", name="Structure matches the song").locator(".checkmark")).to_be_visible()''',
)
replace_once(
    "tests/test_v7_preview.py",
    '''        tile = page.locator('.track-tile[data-name="Drums"]')
        tile.click()
        expect(tile).to_have_attribute("aria-pressed", "true")
        expect(page.get_by_role("button", name="Continue to Section Study")).to_be_visible()
        expect(page.locator(".action-row.action-separated")).to_be_visible()''',
    '''        expect(page.get_by_role("button", name="Add custom track")).to_be_visible()
        self.assertEqual(page.get_by_role("button", name="Add", exact=True).count(), 0)
        tile = page.locator('.track-tile[data-name="Drums"]')
        tile.click()
        expect(tile).to_have_attribute("aria-pressed", "true")
        expect(page.get_by_role("button", name="Continue to Section Study")).to_be_visible()
        expect(page.locator(".action-row.action-separated")).to_be_visible()''',
)
replace_once(
    "tests/test_v7_preview.py",
    '''    def test_section_study_explains_only_real_missing_context(self):''',
    '''    def test_custom_track_is_one_control_and_enter_adds_it(self):
        page = self.open("tracks", study_db(setup=True, structure=True))
        field = page.get_by_role("textbox", name="Other track")
        field.fill("Strings")
        field.press("Enter")
        expect(page.locator('.track-tile[data-name="Strings"]')).to_be_visible()
        expect(page.get_by_role("button", name="Continue to Section Study")).to_be_visible()

    def test_section_study_explains_only_real_missing_context(self):''',
)

# Durable documentation: make V6 production rules stop masquerading as V7 rules.
replace_once(
    "AGENTS.md",
    '''## Progression and navigation model — October 2026

- User-facing workflow hierarchy is **Project → Phase → Step → Musical content**.
- **Checkpoint** is historical/internal terminology only. Do not present phase navigation as manual checklist controls; completion is automatically derived from canonical project state.
- Phase homes show ordered **Steps** with clear done/current/locked state. Completed Steps remain navigable for editing; locked Steps remain visible when they help orientation.
- **Back = browser/history navigation.** It should truthfully reflect where the user came from rather than pretending to be a hierarchy jump.
- **Center context title = fast in-project navigation.** A quiet interactive context title may occupy the center toolbar when it opens real navigation to useful destinations such as Project Overview, Roadmap, Notes, the current Phase, and available Steps.
- **Roadmap = whole journey.** Do not turn the context navigator into a duplicate seven-phase Roadmap.
- Passive center labels/pills are prohibited. If a center element looks interactive, it must perform navigation.
- A future Projects/Notes tab bar or iPad sidebar is allowed only when Notes becomes a genuine app-level destination; do not add persistent app-level chrome before the product earns it.
''',
    '''## Progression and navigation model — production V6 vs experimental V7

Keep the production and redesign models distinct.

**V6 production behavior** remains governed by `V6.md`. Its Phase/Step homes, center context navigator, and Roadmap are production-generation behavior only; do not treat them as universal FIRE rules or reintroduce them into V7 merely because V6 still ships at `/`.

**V7 redesign direction** is governed by `V7_DRAFT.md` and the latest verified `START_HERE.md`:

- **Projects → Project Home → direct musical work.**
- Project Home owns **Continue + Journey + Notes**.
- A Phase such as The Map is a grouping in Journey, not necessarily another intermediary screen.
- Continue recommends one useful next action; Journey provides orientation and direct revisiting.
- Completed work stays navigable. Upcoming work stays visible when it improves orientation. Hard-block only when a task literally cannot function without missing data.
- No center context navigator and no separate Roadmap destination in V7.
- Back/navigation should remain shallow and truthful to the current V7 route model.
- A future Projects/Notes top-level navigation surface is allowed only when Notes becomes a genuine app-level destination.
''',
)
replace_once(
    "AGENTS.md",
    '- Leading toolbar = navigation; trailing toolbar = contextual action. The center toolbar is normally quiet but may host the approved interactive context navigator described above.',
    '- Leading toolbar = navigation; trailing toolbar = contextual action. Keep the V7 center toolbar quiet; the V6 center context navigator is production-generation behavior and does not carry into V7.',
)
replace_once(
    "AGENTS.md",
    '- iPad task sheets should prefer compact centered form/page-style presentation when appropriate; narrow phone layouts may use bottom-oriented sheets.',
    '- The same task sheet behavior applies across device classes; presentation may adapt to available space (for example, centered on wider canvases and bottom-oriented on compact canvases) without changing product logic.',
)
replace_once(
    "AGENTS.md",
    '- Visual work is not complete merely because CI is green. Physical iPhone/iPad Safari approval is required before locking a visual chunk.',
    '- Visual work is not complete merely because CI is green. Verify the same adaptive interface in physical iOS/iPadOS Safari at representative compact and wide sizes; device class must not change FIRE’s product logic, hierarchy, or interaction model.',
)

replace_once(
    "CONTEXT.md",
    '''Earlier versions described three checkpoints per phase / 21 checkpoints total. The current user-facing progression model calls ordered work inside a Phase **Steps**; completion is derived automatically and Phase homes must not look like manual checklists.


### Current progression and navigation vocabulary — LOCKED

FIRE's user-facing hierarchy is **Project → Phase → Step → Musical content**. `Checkpoint` is historical/internal wording only and must not return as the phase-home checklist metaphor.

- **Back** follows actual browser/history navigation.
- A quiet **interactive center context title** provides fast in-project navigation without becoming another passive pill. Phase homes use the project context; Step/review screens use their parent Phase context.
- The context navigator may expose Project Overview, Roadmap, Notes, the current Phase, and relevant Steps. It does not duplicate the full seven-phase Roadmap.
- **Roadmap** remains the whole-journey view.
- Persistent app-level Projects/Notes navigation is deferred until the global Notes hub is a real top-level destination.
''',
    '''Earlier versions described three checkpoints per phase / 21 checkpoints total. V6 later exposed ordered work as Steps. That vocabulary and its Phase-home shell are **production-generation behavior, not universal FIRE architecture**.

### Current redesign progression and navigation direction — LOCKED FOR V7 SHELL

The V7 shell uses **Projects → Project Home → direct musical work**.

- Project Home owns **Continue + Journey + Notes**.
- Continue recommends one next destination.
- Journey shows the project path, supports direct revisiting, and groups work by Phase without requiring a Phase intermediary screen.
- The Map remains the first Recreation phase, but its work (Song Setup, Structure, Tracks, Section Study, Review Map) is directly reachable from Journey.
- Completed work remains revisitable. Upcoming work remains visible when useful for orientation. Hard gates exist only when a destination cannot function without required context.
- V7 has no center context navigator and no separate Roadmap destination.
- The future Projects/Notes top-level navigation surface remains deferred until Notes is a genuine app-level destination.

The shipped V6 Phase/Step/Roadmap/center-navigator model remains documented in `V6.md` and later V6-specific sections of this file for production maintenance only.
''',
)
replace_once(
    "CONTEXT.md",
    '''**LOCKED home-screen behavior:** The Map is an intentional exception to the otherwise minimal phase-home template because it has genuine setup work that must happen before analysis. Keep the full **Song Setup** controls directly on The Map home: Reference, Tempo, Meter, Grid, followed by the First Listen action card. Then show the three ordered Steps below. Structure / Tracks / Section Study remain visible for orientation even when locked; do not replace them with one generic prerequisite card. Do not hide setup behind a separate page, disclosure, compact row, or pill strip.''',
    '''**V6 production behavior (superseded by V7 shell direction):** V6 keeps Song Setup controls on The Map phase home. In V7, **Song Setup is a dedicated focused work page** reached directly from Project Home/Journey; do not recreate the V6 Map-home shell in the redesign.''',
)
replace_once("CONTEXT.md", "# 17. Phase homes — universal template", "# 17. Phase homes — V6 production pattern (not V7 architecture)")
replace_once(
    "CONTEXT.md",
    '''## LOCKED phase-home rule
A phase home is an **overview**, not a workspace.''',
    '''## V6-only phase-home rule
A V6 phase home is an **overview**, not a workspace. This section exists to maintain production V6 and must not override the V7 Project Home + Journey architecture.''',
)
replace_once(
    "CONTEXT.md",
    '''On narrow iPhone layouts, a route that already fits the visual viewport should not gain fake root scroll or rubber-band drift; keeping the page shell stationary preserves alignment when moving between screens. When a phone route is genuinely dense, first remove redundant supporting copy or compact non-current states before shrinking touch targets. Roadmap should emphasize the current phase and compress future/completed phase detail; Map checkpoint descriptions may collapse when the titles and state already communicate the task.''',
    '''On compact layouts, a route that already fits the visual viewport should not gain fake root scroll or rubber-band drift; keeping the page shell stationary preserves alignment when moving between screens. When a route is genuinely dense, first remove redundant supporting copy or compact non-current states before shrinking touch targets. The same FIRE product logic, hierarchy, and interaction model must survive across phone and tablet; only presentation may adapt to available space. In production V6, Roadmap may compress future/completed phase detail.''',
)

replace_once(
    "START_HERE.md",
    'PR #34, **Simplify V7 Projects empty state**, is merged and deployed. PR #35, **Finalize FIRE handoff continuity**, is also merged. The post-merge `main` regression and Pages deployment completed successfully.',
    'PR #36, **Consolidate V7 shell and Journey**, is merged and deployed at `a151376…`; its PR and post-merge regression matrices passed at 390px, 440px, and 820px, and Pages deployment #61 succeeded. PRs #34–#35 remain the preceding Projects/continuity milestones.',
)
replace_once(
    "START_HERE.md",
    'The current V7 shell-consolidation direction removes the temporary Projects enhancer architecture: New Project, the persistent `+`, quiet zero state, build stamp, and creation sheet belong directly in the V7 renderer/styles. `new-project.js`, MutationObserver visual patching, and runtime CSS injection are superseded.',
    '''The V7 shell is now consolidated: New Project, the persistent `+`, quiet zero state, build stamp, and creation sheet live directly in the V7 renderer/styles. `new-project.js`, MutationObserver visual patching, and runtime CSS injection are gone.

The current refinement direction is **visual semantics + composition**: selection, completion, status, navigation, and primary progression must use distinct visual languages; future phases should orient without looking like dead controls; and the same adaptive FIRE interface must preserve identical product logic across phone/tablet sizes.''',
)
replace_once(
    "START_HERE.md",
    '''Work pages:

- default heuristic is **title → minimum useful instruction → actual musical task → continuation when it becomes useful**
- do not show premature disabled continuation controls just to explain the workflow
- Song Setup is dedicated
- Structure edits the arrangement directly
- Tracks keeps direct multi-select
- Section Study and Review Map specialized editors remain deferred
''',
    '''Work pages:

- default heuristic is **title → minimum useful instruction → actual musical task → continuation when it becomes useful**
- do not show premature disabled continuation controls just to explain the workflow
- Song Setup is dedicated
- Structure edits the arrangement directly
- Tracks keeps direct multi-select
- Section Study and Review Map specialized editors remain deferred

Visual semantics:

- **selection** uses restrained selected surfaces, not completion marks
- **completion** uses ring/check language
- **status/value** uses text where text is clearer (for example, `Imported`)
- **navigation** uses rows/chevrons
- **primary progression** gets the strongest compact button treatment
- do not stack two indicators for one state
''',
)
replace_once(
    "START_HERE.md",
    '''- exact Journey visual treatment
- exact Continue emphasis
- exact future-phase weight/placement
- shell spacing/density refinements
- how much explanatory copy individual work pages need''',
    '''- exact Journey signature treatment beyond the restrained semantic hierarchy
- exact future FIRE/signal-path personality treatment
- shell spacing/density refinements after physical review
- how much explanatory copy dense migrated editors will need''',
)
replace_once(
    "START_HERE.md",
    'Specifically test short-page scrolling, tall-page Safari clearance, spacing/density, direct revisiting, Back behavior, and core action discoverability.',
    'Specifically test short-page scrolling, tall-page Safari clearance, spacing/density, direct revisiting, Back behavior, core action discoverability, and that one adaptive interface preserves identical product logic across compact and wide layouts.',
)

replace_once(
    "V7_DRAFT.md",
    '''## Song Setup''',
    '''## Visual semantics

Use one meaning per visual state:

- **Selection** — restrained selected surface/border; no completion checkmark.
- **Completion** — ring/check language.
- **Status/value** — concise text when a word communicates the state better than an icon.
- **Navigation** — list row + chevron where the row opens another destination.
- **Primary progression** — the strongest compact button treatment on the work page.

Do not show two indicators for the same state. A primary action must read differently from a selected option.

Inactive future phases should orient without masquerading as disabled controls. Keep them visible in a compact quiet summary; expand the active phase’s work in Journey.

## Song Setup''',
)
replace_once(
    "V7_DRAFT.md",
    '''### iPhone

- Project Home is a vertically scrolling hub.
- Work screens are focused single-column pages.
- Native-feeling Back + contextual trailing action only.
- Avoid custom center navigation controls.
- Respect Safari's real visual viewport for scrolling/end clearance.

### iPad

- Prefer sidebar/split composition when it materially reduces navigation.
- Do not simply enlarge the phone layout.''',
    '''### Universal adaptive interface

FIRE has one product logic, hierarchy, and interaction model across device classes.

- Project Home remains the hub.
- Work screens remain focused.
- Back/navigation semantics do not change by device.
- Completion, selection, Journey, and Continue behavior do not change by device.
- Presentation may adapt to available space: column count, content width, spacing, and sheet placement can change when useful.
- Respect the real visual viewport for scrolling/end clearance.
- Do not create “iPhone FIRE” and “iPad FIRE” as separate product experiences.''',
)

# Remove one-shot helper/workflow before the generated commit so the PR stays clean.
for temp in [ROOT / "scripts/apply_v7_semantics_once.py", ROOT / ".github/workflows/apply-v7-semantics-once.yml"]:
    if temp.exists():
        temp.unlink()

print("V7 semantics/composition patch applied")
