from pathlib import Path


def replace_once(text, old, new, label):
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"{label}: expected exactly 1 match, found {count}")
    return text.replace(old, new, 1)


app_path = Path("app.js")
css_path = Path("styles.css")
test_path = Path("tests/test_v6.py")
start_path = Path("START_HERE.md")
changelog_path = Path("CHANGELOG.md")

app = app_path.read_text()

# Current-page labels do not belong in the toolbar center. Keep parent navigation
# controls (for example The Skeleton on child checkpoints) intact.
app = app.replace('phaseTag("Roadmap")', '""')
app = app.replace('phaseTag("Notes")', '""')

# Remove duplicate page-title labeling and make the final Structure step read as
# a normal section title rather than a shouted status label.
app = replace_once(
    app,
    'const body = `<div class="section-kicker">Tracks</div><div class="choice-wrap">',
    'const body = `<div class="choice-wrap">',
    "tracks duplicate heading",
)
app = replace_once(
    app,
    '<div class="section-kicker structure-ready-label">Ready?</div>',
    '<div class="structure-ready-label">Finish structure</div>',
    "structure finish heading",
)

app_path.write_text(app)

css = css_path.read_text()
marker = "/* FIRE DESIGN SYSTEM FOUNDATION — OCTOBER 2026 */"
if marker in css:
    raise SystemExit("design-system foundation marker already present")

foundation = r'''

/* FIRE DESIGN SYSTEM FOUNDATION — OCTOBER 2026
   Projects/New Project are the visual reference. These rules live in the core
   stylesheet so older routes inherit one typography, surface, selection,
   action, and adaptive-presentation language without a polish overlay. */
:root {
  --fire-group-bg: #111318;
  --fire-control-bg: #171a20;
  --fire-selected-bg: rgba(201, 205, 213, 0.12);
  --fire-selected-line: rgba(201, 205, 213, 0.34);
  --fire-section-text: #d4d4d9;
  --fire-meta-text: #85868e;
  --fire-action-width: 320px;
}

/* Type hierarchy: titles carry hierarchy; section labels stop shouting. */
.section-kicker,
.sheet-group-title {
  margin: 30px 2px 10px;
  color: var(--fire-section-text);
  font-size: 14px;
  font-weight: 680;
  letter-spacing: 0;
  line-height: 1.25;
  text-transform: none;
}
.sheet-group-title {
  margin: 0 0 10px;
}
.work-position,
.coverage,
.checkpoint-count,
.progress-meta,
.micro {
  color: var(--fire-meta-text);
}

/* Toolbar centers are reserved for a real parent-navigation control. */
.topbar .center .phase-pill {
  min-height: 44px;
  padding: 0 8px;
  border: 0;
  border-radius: 9px;
  background: transparent;
  color: var(--muted);
  font-size: 14px;
  font-weight: 620;
}

/* Shared grouped surfaces and rows. */
.group-card,
.setup-panel {
  background: var(--fire-group-bg);
  border-color: var(--line);
}
.group-card .list-row,
.setup-row {
  min-height: 64px;
}
.list-row .title {
  font-size: 16px;
  font-weight: 670;
}
.list-row .desc,
.action-card .copy {
  font-size: 13px;
  line-height: 1.4;
}

/* A selected option is not a completed task. */
.choice[aria-pressed]::before {
  display: none;
  width: 0;
  margin: 0;
  content: "";
}
.choice {
  min-height: 46px;
  background: transparent;
  border-color: var(--line);
  font-weight: 560;
}
.choice.selected,
.choice[aria-pressed="true"] {
  background: var(--fire-selected-bg);
  border-color: var(--fire-selected-line);
  color: var(--text);
  box-shadow: inset 0 0 0 1px rgba(255, 255, 255, 0.025);
}

/* The Map: consistent surface language, quieter controls, clearer hierarchy. */
#app[data-route="map"] .phase-layout {
  align-items: start;
}
#app[data-route="map"] .setup-panel,
#app[data-route="map"] .group-card,
#app[data-route="map"] .action-card {
  border-color: var(--line);
  background: var(--fire-group-bg);
}
#app[data-route="map"] .checkpoint-progress {
  height: 3px;
}
#app[data-route="map"] .setup-value,
#app[data-route="map"] .state-control {
  background: var(--fire-control-bg);
}

/* Structure becomes one editable list rather than a stack of unrelated cards. */
#app[data-route="structure"] .structure-list {
  display: block;
  overflow: hidden;
  gap: 0;
  background: var(--fire-group-bg);
  border: 1px solid var(--line);
  border-radius: var(--radius-card);
}
#app[data-route="structure"] .structure-list:has(.empty) {
  background: transparent;
  border: 0;
  border-radius: 0;
}
#app[data-route="structure"] .structure-row {
  min-height: 62px;
  margin: 0;
  padding: 0 14px;
  border: 0;
  border-bottom: 1px solid var(--line);
  border-radius: 0;
  background: transparent;
}
#app[data-route="structure"] .structure-row:last-child {
  border-bottom: 0;
}
#app[data-route="structure"] .structure-row .index {
  color: var(--fire-meta-text);
  font-size: 12px;
}
#app[data-route="structure"] .structure-row .name {
  font-size: 16px;
  font-weight: 670;
}
#app[data-route="structure"] .bars-badge {
  color: var(--muted);
  font-size: 13px;
}
#app[data-route="structure"] .delete-section,
#app[data-route="structure"] .drag-handle {
  color: var(--quiet);
  opacity: 0.78;
}
#app[data-route="structure"] .add-section-row {
  min-height: 48px;
  margin-top: 10px;
  border: 1px solid var(--line);
  border-radius: var(--radius-control);
  background: transparent;
  color: var(--muted);
  font-size: 15px;
  font-weight: 640;
}
.structure-ready-label {
  margin: 30px 2px 10px;
  color: var(--fire-section-text);
  font-size: 14px;
  font-weight: 680;
}
#app[data-route="structure"] .structure-verify .action-card {
  min-height: 64px;
  background: var(--fire-group-bg);
  border: 1px solid var(--line);
  border-radius: var(--radius-card);
}

/* Workflow actions stay prominent without becoming full-width white slabs. */
#app[data-route="structure"] .structure-next,
#app[data-route="tracks"] .primary.full,
#app[data-route="skeleton-session"] .primary.full,
#app[data-route="skeleton-draft"] .primary.full,
#app[data-route="skeleton-bounce"] .primary.full {
  width: min(100%, var(--fire-action-width));
  margin-left: auto;
  display: flex;
}

/* Tracks: denser multi-select field, no completion-style checkmarks. */
#app[data-route="tracks"] .choice-wrap {
  gap: 8px;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
}
#app[data-route="tracks"] .choice {
  min-height: 46px;
  padding: 10px 12px;
}
#app[data-route="tracks"] .inline-add {
  margin-top: 10px;
  background: var(--fire-group-bg);
  border-color: var(--line);
}
#app[data-route="tracks"] .inline-add .secondary {
  min-width: 72px;
}

/* Roadmap: one progression surface instead of seven independent cards. */
#app[data-route="roadmap"] {
  --canvas-width: 920px;
}
#app[data-route="roadmap"] .roadmap-grid {
  display: block;
  overflow: hidden;
  max-width: 860px;
  background: var(--fire-group-bg);
  border: 1px solid var(--line);
  border-radius: var(--radius-card);
}
#app[data-route="roadmap"] .road-phase,
#app[data-route="roadmap"] .roadmap-grid .road-phase {
  width: 100%;
  height: auto;
  margin: 0;
  padding: 17px 18px;
  border: 0;
  border-bottom: 1px solid var(--line);
  border-radius: 0;
  background: transparent;
}
#app[data-route="roadmap"] .road-phase:last-child {
  border-bottom: 0;
}
#app[data-route="roadmap"] .road-phase.current {
  background: rgba(201, 205, 213, 0.055);
}
#app[data-route="roadmap"] .road-phase.future,
#app[data-route="roadmap"] .road-phase.unimplemented {
  opacity: 0.5;
}
#app[data-route="roadmap"] .road-top {
  grid-template-columns: 30px minmax(0, 1fr) auto;
  gap: 13px;
  align-items: center;
}
#app[data-route="roadmap"] .road-top h3 {
  font-size: 17px;
}
#app[data-route="roadmap"] .road-top p {
  margin-top: 2px;
  color: var(--muted);
  font-size: 13px;
  line-height: 1.4;
}
#app[data-route="roadmap"] .road-checks {
  margin: 8px 0 0 43px;
  gap: 0;
  color: var(--fire-meta-text);
}
#app[data-route="roadmap"] .road-check {
  padding: 0;
  border: 0;
  border-radius: 0;
  background: transparent;
  color: var(--fire-meta-text);
  font-size: 12px;
}
#app[data-route="roadmap"] .road-check + .road-check::before {
  content: " · ";
  white-space: pre;
}

/* Skeleton checkpoint work uses the same grouped-row and action language. */
#app[data-route="skeleton-session"] .session-groups {
  align-items: start;
}
#app[data-route="skeleton-session"] .group-card,
#app[data-route="skeleton"] .group-card {
  background: var(--fire-group-bg);
}
#app[data-route="skeleton-session"] .list-row {
  min-height: 64px;
}

/* iPad / wider touch canvases use compact centered task sheets. */
@media (min-width: 700px) {
  .sheet-backdrop {
    align-items: center;
    padding: 32px;
  }
  .sheet {
    width: min(620px, calc(100vw - 64px));
    max-width: 620px;
    max-height: calc(100dvh - 64px);
    padding: 24px;
    padding-bottom: 24px;
    border: 1px solid var(--line-strong);
    border-radius: 20px;
  }
  .grabber {
    display: none;
  }
}

@media (max-width: 699px) {
  #app[data-route="structure"] .structure-next,
  #app[data-route="tracks"] .primary.full,
  #app[data-route="skeleton-session"] .primary.full,
  #app[data-route="skeleton-draft"] .primary.full,
  #app[data-route="skeleton-bounce"] .primary.full {
    width: 100%;
  }
}
'''
css_path.write_text(css.rstrip() + foundation + "\n")

# Add focused regressions for the new shared visual rules. Automated checks guard
# geometry/semantics; physical iPad/iPhone Safari remains the visual approval gate.
tests = test_path.read_text()
anchor = "    def test_dense_lane_scroll_keyboard_precision_and_touch_scroll_cancellation(self):\n"
if anchor not in tests:
    raise SystemExit("test insertion anchor not found")
new_test = '''    def test_fire_design_system_foundation_across_representative_routes(self):\n        self.open('roadmap', width=820, data=self.complete_fixture())\n        self.assertEqual(self.page.locator('.topbar .center').inner_text().strip(), '')\n        roadmap = self.page.locator('.roadmap-grid')\n        self.assertEqual(roadmap.evaluate('el=>getComputedStyle(el).display'), 'block')\n        self.assertEqual(self.page.locator('.road-phase').first.evaluate('el=>getComputedStyle(el).borderRadius'), '0px')\n\n        self.canvas_route('structure')\n        kicker = self.page.locator('.section-kicker').first\n        self.assertEqual(kicker.evaluate('el=>getComputedStyle(el).textTransform'), 'none')\n        self.assertEqual(self.page.locator('.structure-list').evaluate('el=>getComputedStyle(el).display'), 'block')\n        self.click('open-add-section'); self.settled_sheet()\n        sheet = self.page.locator('.sheet'); box = sheet.bounding_box()\n        self.assertLessEqual(box['width'], 620)\n        self.assertGreater(box['y'], 20)\n        self.assertEqual(sheet.evaluate('el=>getComputedStyle(el).borderRadius'), '20px')\n        self.click('close-sheet')\n\n        self.canvas_route('tracks')\n        selected = self.page.locator('.choice[aria-pressed="true"]').first\n        self.assertEqual(selected.evaluate("el=>getComputedStyle(el,'::before').display"), 'none')\n        self.assertLessEqual(self.page.locator('.primary.full').bounding_box()['width'], 320.5)\n\n        self.canvas_route('skeleton-session')\n        self.assertLessEqual(self.page.locator('.primary.full').bounding_box()['width'], 320.5)\n\n'''
tests = tests.replace(anchor, new_test + anchor, 1)
test_path.write_text(tests)

start = start_path.read_text()
start = start.replace(
    "- The next approved product pass is a **FIRE Design System foundation pass**, not another isolated Structure polish pass.",
    "- The first **FIRE Design System foundation batch** is now implemented across representative workflow screens (The Map, Structure, Tracks, Roadmap, and Skeleton/Session). Physical iPad/iPhone approval is required before broad rollout to the remaining routes.",
)
start_path.write_text(start)

changelog = changelog_path.read_text()
needle = "## V6\n\n"
entry = "- First FIRE Design System foundation batch: calmer type hierarchy, grouped progression/list surfaces, selection separated from completion, compact workflow actions, centered iPad task sheets, and shared styling across representative Map/Structure/Tracks/Roadmap/Skeleton screens.\n"
if entry not in changelog:
    if needle not in changelog:
        raise SystemExit("changelog V6 anchor not found")
    changelog = changelog.replace(needle, needle + entry, 1)
changelog_path.write_text(changelog)
