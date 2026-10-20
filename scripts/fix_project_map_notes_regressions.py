from pathlib import Path
import re


def replace_once(text, old, new, label):
    if old not in text:
        raise SystemExit(f"{label}: expected text not found")
    return text.replace(old, new, 1)


def sub_once(text, pattern, replacement, label):
    out, count = re.subn(pattern, replacement, text, count=1, flags=re.S)
    if count != 1:
        raise SystemExit(f"{label}: expected one replacement, got {count}")
    return out

# Preserve checkpoint DOM while Song Setup remains in the same locked/unlocked state.
# This prevents a blur/change event from replacing the navigation target underneath a tap.
app_path = Path("app.js")
app = app_path.read_text()
app = sub_once(
    app,
    r'''  function refreshMapProgress\(\) \{.*?\n  \}\n(?=  app\.addEventListener\("input")''',
    r'''  function refreshMapProgress() {
    const p = project(),
      holder = app.querySelector(".phase-checkpoints .group-card"),
      count = app.querySelector(".checkpoint-count"),
      setupDone = mapSetupComplete(p),
      done = mapCheckpointCount(p);
    if (count) count.textContent = `${done} of 3`;
    if (!holder) return queueViewportFit();
    const currentlyLocked = !!holder.querySelector(".checkpoint-locked-message");
    if (!setupDone && !currentlyLocked) {
      holder.innerHTML = `<div class="list-row static no-status checkpoint-locked-message"><div><div class="title">Available after Song Setup</div></div></div>`;
    } else if (setupDone && currentlyLocked) {
      const studyRoute = sectionStudyCoreDone(p) ? "map-summary" : "section-study";
      holder.innerHTML =
        checkpointRow("Structure", "Map the form.", "structure", structureDone(p), true) +
        checkpointRow("Tracks", "Identify what plays.", "tracks", tracksDone(p), structureDone(p)) +
        checkpointRow("Section Study", "Map each section in time.", studyRoute, sectionStudyDone(p), tracksDone(p));
    }
    queueViewportFit();
  }
''',
    "stable Map progress refresh",
)
app_path.write_text(app)

adaptive = Path("tests/test_adaptive_composition.py")
text = adaptive.read_text()
text = sub_once(
    text,
    r'''    def test_completed_song_setup_collapses_and_can_be_edited\(self\):.*?\n    def test_project_current_phase_is_the_action_without_progress_slab''',
    r'''    def test_completed_song_setup_stays_visible_and_editable(self):
        page = self.open("map")
        expect(page.locator(".phase-setup .section-kicker")).to_have_text("Song Setup")
        tempo = page.locator("#tempoInput")
        expect(tempo).to_be_visible()
        self.assertEqual(page.locator('[data-action="toggle-setup-disclosure"]').count(), 0)
        self.assertEqual(page.locator(".checkpoint-progress").count(), 0)

        tempo.fill("112")
        tempo.blur()
        expect(tempo).to_be_visible()
        expect(tempo).to_have_value("112")

        page.locator('[data-action="go"][data-route="structure"]').click()
        expect(page.locator("h1")).to_have_text("Structure")
        page.go_back()
        expect(page.locator(".phase-setup .section-kicker")).to_have_text("Song Setup")
        expect(page.locator("#tempoInput")).to_have_value("112")

    def test_project_current_phase_is_the_action_without_progress_slab''',
    "adaptive setup test",
)
text = replace_once(
    text,
    '        current = page.locator(\'.project-current .hero-card[data-action="go"]\')\n',
    '        current = page.locator(\'.project-current-card[data-action="go"]\')\n',
    "adaptive project current selector",
)
adaptive.write_text(text)

declutter = Path("tests/test_declutter.py")
text = declutter.read_text()
text = replace_once(
    text,
    '        page.locator(\'[data-action="toggle-setup-disclosure"]\').click()\n        meter = page.locator("#meterInput")\n',
    '        meter = page.locator("#meterInput")\n        expect(meter).to_be_visible()\n',
    "declutter setup disclosure",
)
declutter.write_text(text)

design = Path("tests/test_design_system.py")
text = design.read_text()
text = sub_once(
    text,
    r'''    def test_phone_map_uses_one_quieter_setup_surface\(self\):.*?\n\n\nif __name__ == "__main__":''',
    r'''    def test_phone_map_uses_one_quieter_setup_surface(self):
        self.assertIn('#app[data-route="map"] .setup-value,', self.css)
        self.assertIn('#app[data-route="map"] .state-control {', self.css)
        self.assertIn('#app[data-route="map"] .phase-setup .setup-panel {', self.css)
        self.assertIn('border-radius: var(--radius-card);', self.css)
        self.assertIn('border-bottom: 1px solid var(--line);', self.css)
        self.assertIn('#app[data-route="map"] .phase-setup .setup-listen-row {', self.css)


if __name__ == "__main__":''',
    "design system setup assertion",
)
design.write_text(text)

v6 = Path("tests/test_v6.py")
text = v6.read_text()
text = replace_once(
    text,
    "                 ('map','.nav-btn'),('map','.state-control'),('map','.action-card'),('map','.list-row'),\n",
    "                 ('map','.nav-btn'),('map','.state-control'),('map','.setup-listen-row'),('map','.list-row'),\n",
    "component shape Map sample",
)
text = replace_once(
    text,
    "                if route == 'map' and selector in ('.state-control','.action-card'):\n",
    "                if route == 'map' and selector in ('.state-control','.setup-listen-row'):\n",
    "component shape setup condition",
)
text = sub_once(
    text,
    r'''                nxt=self\.page\.locator\('\[data-route="tracks"\]'\);page=self\.page\.locator\('\.workflow-page'\)\n                if width>=640:\n                    self\.assertLessEqual\(nxt\.bounding_box\(\)\['width'\],280\.5\)\n                    self\.assertAlmostEqual\(nxt\.bounding_box\(\)\['x'\]\+nxt\.bounding_box\(\)\['width'\],page\.bounding_box\(\)\['x'\]\+page\.bounding_box\(\)\['width'\],delta=1\)\n                else:\n                    self\.assertAlmostEqual\(nxt\.bounding_box\(\)\['width'\],page\.bounding_box\(\)\['width'\],delta=1\)''',
    r'''                nxt=self.page.locator('[data-route="tracks"]');page=self.page.locator('.workflow-page')
                self.assertLessEqual(nxt.bounding_box()['width'],220.5)
                self.assertLess(nxt.bounding_box()['width'],page.bounding_box()['width'])
                self.assertAlmostEqual(nxt.bounding_box()['x']+nxt.bounding_box()['width'],page.bounding_box()['x']+page.bounding_box()['width'],delta=1)''',
    "compact Structure Next assertion",
)
text = replace_once(
    text,
    "        expect(card.locator('.foot')).to_contain_text('The Map · 3 of 3')\n",
    "        expect(card.locator('.foot')).to_contain_text('The Map · 2 of 3')\n",
    "project card progress expectation",
)
v6.write_text(text)
