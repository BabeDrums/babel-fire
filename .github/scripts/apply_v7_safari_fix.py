from pathlib import Path
import re


def sub(path, pattern, repl, *, flags=0, count=1):
    p = Path(path)
    text = p.read_text()
    new, n = re.subn(pattern, repl, text, count=count, flags=flags)
    if n != count:
        raise SystemExit(f"{path}: expected {count} replacement(s), got {n}: {pattern[:80]}")
    p.write_text(new)


def replace(path, old, new, *, count=1):
    p = Path(path)
    text = p.read_text()
    n = text.count(old)
    if n != count:
        raise SystemExit(f"{path}: expected {count} exact occurrence(s), got {n}: {old[:80]!r}")
    p.write_text(text.replace(old, new))

app = "v7-preview/app.js"
replace(app, 'let viewportFitFrame = 0;\n', '')
sub(app, r'function applyViewportFit\(\) \{.*?\n\}\n\nfunction queueViewportFit\(\) \{.*?\n\}\n\n', '', flags=re.S)
replace(app, '  queueViewportFit();\n', '', count=3)
replace(app, '\nqueueViewportFit();', '')
sub(app, r'function referenceRow\(setup\) \{.*?\n\}\n\nfunction setupRow', '''function referenceRow(setup) {
  return `
    <button class="form-row reference-row" data-action="toggle-setup" data-field="reference">
      <span><span class="form-label">Reference</span><span class="form-help">Import the reference into your session.</span></span>
      ${completionAccessory(!!setup.reference)}
    </button>`;
}

function setupRow''', flags=re.S)
replace(app, '    body = `<div class="prereq-card"><h3>Ready for Section Study.</h3><p class="prototype-end">The full timeline editor stays in V6 until this lighter shell is approved.</p></div>`;', '    body = `<div class="prereq-card"><h3>Ready for Section Study.</h3><p class="prototype-end">Section Study isn\\\'t available in this preview yet.</p></div>`;')
replace(app, '  app.innerHTML = `<main class="screen">${topbar(backButton(item.title, "project"), "")}${pageHeader("Review Map", "Review the song map before rebuilding it.")}<div class="prereq-card"><p class="prototype-end">The full Review Map workspace still uses V6 while this lighter shell is being evaluated.</p></div></main>`;', '  app.innerHTML = `<main class="screen">${topbar(backButton(item.title, "project"), "")}${pageHeader("Review Map", "Review the song map before rebuilding it.")}<div class="prereq-card"><p class="prototype-end">Review Map isn\\\'t available in this preview yet.</p></div></main>`;')
sub(app, r'function openReferenceSheet\(\) \{.*?\n\}\n\nfunction createProject', 'function createProject', flags=re.S)
replace(app, '      setup: { reference: false, referenceName: "", tempo: "", meter: "4/4", grid: false, firstListen: false },', '      setup: { reference: false, tempo: "", meter: "4/4", grid: false, firstListen: false },')
replace(app, '''  if (action === "import-reference") {
    document.getElementById("referenceFileInput")?.click();
    return;
  }
  if (action === "reference-actions") return openReferenceSheet();
''', '')
replace(app, '''  if (event.target.id === "referenceFileInput") {
    const file = event.target.files?.[0];
    if (!file) return;
    item.map.setup.reference = true;
    item.map.setup.referenceName = file.name;
    save();
    renderSetup();
    return;
  }
''', '')
replace(app, '''  if (action === "replace-reference") {
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
''', '')
replace(app, '''app.addEventListener("click", () => requestAnimationFrame(queueViewportFit));
app.addEventListener("input", queueViewportFit);
app.addEventListener("change", queueViewportFit);
window.addEventListener("resize", queueViewportFit);
window.visualViewport?.addEventListener("resize", queueViewportFit);

''', '')

css = "v7-preview/styles.css"
sub(css, r'@media \(max-width: 699px\) \{\n  html\[data-v7-fit="true"\],.*?\n\}\n\n', '', flags=re.S)
replace(css, '.root-screen { padding-top: 18px; }\n', '.root-screen { padding-top: 18px; }\n.scroll-safe { padding-bottom: 64px; }\n')
replace(css, '.journey-row.upcoming .row-title { color: #8d8e96; }', '.journey-row.upcoming .row-title { color: #a1a2aa; }')
replace(css, '''.journey-row.done .chevron,
.journey-row.upcoming .chevron { opacity: .72; }''', '''.journey-row.done .chevron { opacity: .72; }
.journey-row.upcoming .chevron { opacity: .9; }''')
replace(css, '.reference-detail { max-width: 430px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }\n.visually-hidden { position: absolute !important; width: 1px !important; height: 1px !important; padding: 0 !important; margin: -1px !important; overflow: hidden !important; clip: rect(0 0 0 0) !important; white-space: nowrap !important; border: 0 !important; }\n', '')

tests = "tests/test_v7_preview.py"
replace(tests, 'import os\nimport unittest\n', 'import os\nimport unittest\nfrom pathlib import Path\n')
sub(tests, r'    def assert_short_page_locked\(self, page\):.*?(?=    def test_projects_is_one_job_open_or_create)', '', flags=re.S)
replace(tests, '        self.assert_short_page_locked(page)\n', '', count=3)
sub(tests, r'    def test_short_work_pages_do_not_fake_scroll\(self\):.*?(?=    def test_project_home_is_continue_journey_notes_without_v6_chrome)', '''    def test_phone_pages_use_natural_document_scrolling(self):
        page = self.open("project", study_db(setup=True, structure=True, tracks=True), height=720)
        self.assertNotEqual(page.evaluate("getComputedStyle(document.documentElement).overflowY"), "hidden")
        self.assertNotEqual(page.evaluate("getComputedStyle(document.body).overflowY"), "hidden")
        self.assertFalse(page.evaluate("'v7Fit' in document.documentElement.dataset"))
        self.assertFalse(page.evaluate("'scrollable' in document.querySelector('#app').dataset"))
        source = Path("v7-preview/app.js").read_text()
        styles = Path("v7-preview/styles.css").read_text()
        self.assertNotIn("visualViewport", source)
        self.assertNotIn("dataset.scrollable", source)
        self.assertNotIn("data-v7-fit", styles)

''', flags=re.S)
replace(tests, '''        reference = page.locator(".reference-row")
        expect(reference.locator(".reference-detail")).to_have_text("Imported reference")
        expect(reference.locator(".checkmark")).to_be_visible()
''', '''        reference = page.locator(".reference-row")
        expect(reference.locator(".form-help")).to_have_text("Import the reference into your session.")
        expect(reference.locator(".checkmark")).to_be_visible()
''')
sub(tests, r'    def test_reference_import_has_identity_feedback_and_replace_remove_actions\(self\):.*?(?=    def test_song_setup_continuation_reacts_to_tempo_without_rerendering_input)', '''    def test_reference_is_a_setup_requirement_not_a_file_picker(self):
        page = self.open("setup")
        reference = page.locator(".reference-row")
        expect(reference.locator(".form-help")).to_have_text("Import the reference into your session.")
        expect(reference.locator(".completion-ring")).to_be_visible()
        self.assertEqual(page.locator('input[type="file"]').count(), 0)
        reference.click()
        reference = page.locator(".reference-row")
        expect(reference.locator(".checkmark")).to_be_visible()
        self.assertEqual(page.locator(".sheet").count(), 0)
        preview = page.evaluate("(key) => JSON.parse(localStorage.getItem(key))", PREVIEW_KEY)
        setup = preview["projects"][0]["map"]["setup"]
        self.assertTrue(setup["reference"])
        self.assertNotIn("referenceName", setup)
        reference.click()
        expect(page.locator(".reference-row .completion-ring")).to_be_visible()
        preview = page.evaluate("(key) => JSON.parse(localStorage.getItem(key))", PREVIEW_KEY)
        self.assertFalse(preview["projects"][0]["map"]["setup"]["reference"])

    def test_preview_placeholders_do_not_leak_internal_v6_language(self):
        complete = study_db(setup=True, structure=True, tracks=True)
        page = self.open("section-study", complete)
        expect(page.get_by_text("Section Study isn't available in this preview yet.")).to_be_visible()
        self.assertEqual(page.get_by_text("V6", exact=False).count(), 0)
        self.assertEqual(page.get_by_text("approved", exact=False).count(), 0)
        page = self.open("review-map", complete)
        expect(page.get_by_text("Review Map isn't available in this preview yet.")).to_be_visible()
        self.assertEqual(page.get_by_text("V6", exact=False).count(), 0)

''', flags=re.S)

draft = "V7_DRAFT.md"
replace(draft, '''Reference is a special case: the filename/identity answers **what** is loaded, while a completion mark answers whether the setup requirement is satisfied. The preview should use a real file picker, persist the selected filename as metadata, and offer Replace / Remove rather than treating Reference like a silent boolean toggle.''', '''Reference is a setup requirement, not media FIRE needs to own. The user confirms that the reference has been imported into their production/session environment; FIRE stores only the completion state. Use the same ring/check completion language as other setup requirements. Do not request, upload, retain, or identify the reference file unless a future musical feature genuinely needs the media itself.''')
replace(draft, '''- **Content-aware scrolling:** short phone pages that fit the real visual viewport do not create root scrolling or rubber-band drift. Only genuinely tall pages receive Safari scroll-end clearance.''', '''- **Natural scrolling:** document height determines whether a page scrolls. Never switch root overflow in response to `VisualViewport` changes while the user is scrolling; mobile browser chrome must not cause content to lock, jump, disappear, or reappear. Short pages simply remain shorter than the viewport, while tall pages get modest CSS-only end clearance.''')
replace(draft, '- Respect the real visual viewport for scrolling/end clearance.', '- Use stable CSS viewport sizing and natural document overflow; do not make product scrollability depend on live visual-viewport measurements.')
replace(draft, '''The isolated preview may show prerequisite/placeholder states, but the full specialized editors remain V6 until the shell is approved physically.''', '''The isolated preview may show prerequisite/placeholder states, but preview-facing copy should describe availability plainly rather than expose internal V6 migration or approval language.''')

handoff = "START_HERE.md"
replace(handoff, '## Current verified continuity — October 21, 2026', '## Current verified continuity — October 22, 2026')
replace(handoff, '''PR #37, **Refine V7 visual semantics and composition**, is merged and deployed at `ae00659…`; its PR and post-merge regression matrices passed at 390px, 440px, and 820px, and Pages deployment #62 succeeded. PR #36 is the preceding shell-consolidation milestone; PRs #34–#35 remain the preceding Projects/continuity milestones.''', '''PR #38, **Refine V7 grayscale interaction fidelity**, is merged and deployed at `c7aa0c4…`; its PR and post-merge regression matrices passed at 390px, 440px, and 820px, and Pages deployment #63 succeeded. Physical iPhone Safari review then exposed two conceptual/runtime defects that the current corrective pass addresses: Reference should be a setup attestation rather than a file picker, and VisualViewport-driven root scroll locking can glitch as Safari browser chrome changes height. PR #37 remains the preceding visual-semantics milestone.''')
replace(handoff, '''The current refinement direction is **grayscale interaction fidelity**: make controls feel finished without relying on accent color, replace prototype boolean-style interactions with truthful state behavior, preserve distinct selection/completion/navigation/progression semantics, and let compact/regular layouts adapt presentation without changing product logic.''', '''The current corrective direction is **Safari stability + setup semantics**: preserve the grayscale interaction foundation, treat Reference as a setup completion requirement rather than file ownership, use natural document scrolling instead of runtime root-scroll locking, keep upcoming Journey destinations visibly tappable, and remove internal V6/approval language from preview placeholders.''')
replace(handoff, '''- **status/value** uses text when text is the information itself; Reference uses filename/identity plus completion feedback rather than a bare `Import` / `Imported` toggle''', '''- **status/value** uses text when text is the information itself; Reference is a completion requirement (“Import the reference into your session”) and uses ring/check feedback without asking FIRE to own the media''')
replace(handoff, '''- short phone pages that fit the actual visual viewport should not create fake root scrolling
- genuinely tall pages scroll naturally and receive enough Safari end clearance
- do not globally disable scrolling or globally reserve a giant bottom tail''', '''- document height determines whether a page scrolls naturally
- never toggle root `overflow` from `VisualViewport` measurements while Safari chrome is moving
- short pages remain naturally short; tall pages receive modest CSS-only Safari end clearance
- modal sheets may temporarily lock body scrolling while open, but page scrollability itself is never runtime-switched''')
replace(handoff, '- content-aware viewport behavior', '- natural CSS document scrolling with no VisualViewport-driven root lock')
replace(handoff, '''- grayscale interaction-fidelity refinements: material contrast, primary-action weight, field focus, Reference import/replace/remove, and compact-vs-regular composition''', '''- grayscale interaction-fidelity refinements: material contrast, primary-action weight, field focus, Reference completion semantics, and compact-vs-regular composition''')
replace(handoff, '''3. Song Setup — real Reference file-selection feedback with filename + completion, Replace/Remove behavior, and no fake boolean toggle semantics''', '''3. Song Setup — Reference as a clear ring/check setup requirement with no file picker, filename, Replace/Remove sheet, or media ownership implication''')

app_text = Path(app).read_text()
css_text = Path(css).read_text()
assert "referenceFileInput" not in app_text
assert "openReferenceSheet" not in app_text
assert "visualViewport" not in app_text
assert "queueViewportFit" not in app_text
assert "dataset.scrollable" not in app_text
assert "data-v7-fit" not in css_text
assert "Reference file-selection" not in Path(handoff).read_text()
print("V7 Safari stability + setup semantics patch applied")
