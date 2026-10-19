from pathlib import Path


def replace_once(text, old, new, label):
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"{label}: expected 1 match, found {count}")
    return text.replace(old, new, 1)


app = Path("app.js")
s = app.read_text(encoding="utf-8")

s = replace_once(
    s,
    '''  function renderProjects() {
    app.innerHTML =
      topbar("", phaseTag("FIRE"), "") +
      `<header class="projects-heading"><div><h1>Projects</h1><p class="sub">Original songs and recreations.</p></div><button class="top-icon-btn" data-action="new-project" aria-label="New project"><span aria-hidden="true">+</span></button></header><div class="projects-grid">${''',
    '''  function renderProjects() {
    app.innerHTML =
      `<header class="projects-heading"><div><h1>Projects</h1><p class="sub">Original songs and recreations.</p></div><button class="top-icon-btn" data-action="new-project" aria-label="New project"><span aria-hidden="true">+</span></button></header><div class="projects-grid">${''',
    "remove passive FIRE chrome",
)

s = replace_once(
    s,
    '''  function renderNewProject() {
    app.innerHTML =
      topbar(backButton("projects", "Projects"), phaseTag("New Project"), "") +
      `<h2>New project</h2><p class="sub">Start original or rebuild a reference.</p><div class="spacer-24"></div><div class="new-type"><button class="type-card ${ui.newType === "original" ? "selected" : ""}" data-action="set-new-type" data-type="original" aria-pressed="${ui.newType === "original"}"><strong>Original Song</strong><span>Start with anything worth keeping.</span></button><button class="type-card ${ui.newType === "study" ? "selected" : ""}" data-action="set-new-type" data-type="study" aria-pressed="${ui.newType === "study"}"><strong>Recreation</strong><span>Rebuild an existing song to learn how it works.</span></button></div><div class="section-kicker">Project</div><input class="field" id="newTitle" aria-label="Project title" enterkeyhint="${ui.newType === "study" ? "next" : "done"}" autocomplete="off" placeholder="${ui.newType === "study" ? "Song title" : "Song title or Untitled"}"><input class="field custom-length" id="newArtist" aria-label="Artist" enterkeyhint="done" autocomplete="off" placeholder="Artist" ${ui.newType === "study" ? "" : "hidden"}><div class="spacer-24"></div><button class="primary full" data-action="create-project">Create Project</button>`;
  }''',
    '''  function renderNewProject() {
    const typeCopy =
      ui.newType === "study"
        ? "Rebuild an existing song to learn how it works."
        : "Start with anything worth keeping.";
    app.innerHTML =
      topbar(backButton("projects", "Projects"), "", "") +
      `<h2>New project</h2><p class="sub">Start original or rebuild a reference.</p><div class="spacer-24"></div><div class="project-type-control" role="group" aria-label="Project type"><button class="segment-choice ${ui.newType === "original" ? "selected" : ""}" data-action="set-new-type" data-type="original" aria-pressed="${ui.newType === "original"}">Original</button><button class="segment-choice ${ui.newType === "study" ? "selected" : ""}" data-action="set-new-type" data-type="study" aria-pressed="${ui.newType === "study"}">Recreation</button></div><p class="project-type-copy" id="newTypeDescription">${typeCopy}</p><div class="section-kicker project-field-label">Project</div><input class="field" id="newTitle" aria-label="Project title" enterkeyhint="${ui.newType === "study" ? "next" : "done"}" autocomplete="off" placeholder="${ui.newType === "study" ? "Song title" : "Song title or Untitled"}"><input class="field custom-length" id="newArtist" aria-label="Artist" enterkeyhint="done" autocomplete="off" placeholder="Artist" ${ui.newType === "study" ? "" : "hidden"}><div class="spacer-24"></div><button class="primary full" data-action="create-project">Create Project</button>`;
  }''',
    "native project type selector",
)

s = replace_once(
    s,
    '''      const titleInput = document.getElementById("newTitle");
      titleInput.placeholder = ui.newType === "study" ? "Song title" : "Song title or Untitled";
      titleInput.setAttribute("enterkeyhint", ui.newType === "study" ? "next" : "done");
      return;''',
    '''      const titleInput = document.getElementById("newTitle"),
        typeDescription = document.getElementById("newTypeDescription");
      titleInput.placeholder = ui.newType === "study" ? "Song title" : "Song title or Untitled";
      titleInput.setAttribute("enterkeyhint", ui.newType === "study" ? "next" : "done");
      if (typeDescription)
        typeDescription.textContent =
          ui.newType === "study"
            ? "Rebuild an existing song to learn how it works."
            : "Start with anything worth keeping.";
      return;''',
    "project type description update",
)

app.write_text(s, encoding="utf-8")

css = Path("styles.css")
s = css.read_text(encoding="utf-8")

s = replace_once(
    s,
    ''':is(.list-row, .project-open, .quick-card, .nav-btn, .text-btn, .mini-btn, .sheet-close, .mix-toggle, .top-icon-btn, .project-menu, .type-card):not(:disabled):active {''',
    ''':is(.list-row, .project-open, .quick-card, .nav-btn, .text-btn, .mini-btn, .sheet-close, .mix-toggle, .top-icon-btn, .project-menu, .segment-choice):not(:disabled):active {''',
    "pressed selector",
)

s = replace_once(
    s,
    '''.project-open {
  width: 100%;
  padding: 16px 58px 15px 18px;
  text-align: left;
  cursor: pointer;
  min-width: 0;
  min-height: 106px;
  height: 100%;
  border-radius: inherit;
}''',
    '''.project-open {
  position: relative;
  width: 100%;
  padding: 16px 58px 15px 18px;
  text-align: left;
  cursor: pointer;
  min-width: 0;
  min-height: 106px;
  height: 100%;
  border-radius: inherit;
}''',
    "project row positioning",
)

s = replace_once(
    s,
    '''.project-open .foot {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 12px;
  margin-top: 11px;
  font-size: 12px;
  color: var(--muted);
}''',
    '''.project-open .foot {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-top: 11px;
  padding-right: 22px;
  font-size: 12px;
  color: var(--muted);
}
.project-open .foot > span:last-child {
  position: absolute;
  right: 18px;
  bottom: 16px;
  font-size: 18px;
  line-height: 1;
  color: var(--quiet);
}''',
    "project disclosure placement",
)

old_type = '''.new-type {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px;
}
.type-card {
  min-height: 115px;
  text-align: left;
  padding: 16px;
  border-radius: var(--radius-card);
  background: #111318;
  border: 1px solid var(--line);
  cursor: pointer;
}
.type-card.selected {
  border-color: var(--state-selected-border);
  background: var(--state-selected);
}
.type-card strong {
  display: block;
  font-size: 15px;
}
.type-card span {
  display: block;
  font-size: 12px;
  line-height: 1.4;
  color: var(--muted);
  margin-top: 5px;
}'''
new_type = '''.project-type-control {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 3px;
  padding: 3px;
  min-height: 50px;
  border: 1px solid var(--line);
  border-radius: var(--radius-control);
  background: var(--surface-2);
}
.segment-choice {
  min-height: 44px;
  padding: 0 14px;
  border-radius: 9px;
  color: var(--muted);
  font-size: 15px;
  font-weight: 650;
  text-align: center;
}
.segment-choice.selected {
  color: var(--text);
  background: var(--surface-3);
  box-shadow: inset 0 0 0 1px var(--line-strong);
}
.project-type-copy {
  min-height: 38px;
  margin: 10px 2px 0;
  color: var(--muted);
  font-size: 13px;
  line-height: 1.45;
}
.project-field-label {
  margin-top: 18px;
  margin-bottom: 8px;
  font-size: 12px;
  font-weight: 650;
  letter-spacing: 0;
  text-transform: none;
}'''
s = replace_once(s, old_type, new_type, "replace project type cards")

s = replace_once(
    s,
    '''#app[data-route="projects"] .topbar {
  margin-bottom: 28px;
}
.projects-heading {''',
    '''.projects-heading {''',
    "remove projects topbar spacing",
)

s = replace_once(
    s,
    '''.projects-heading {
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
  gap: var(--space-4);
  margin-bottom: var(--space-5);
}''',
    '''.projects-heading {
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
  gap: var(--space-4);
  width: 100%;
  max-width: 760px;
  margin-bottom: var(--space-5);
}''',
    "align projects heading to list",
)

s = replace_once(
    s,
    '''@media (max-width: 430px) {
  #app[data-route="projects"] .topbar {
    margin-bottom: 22px;
  }
  .projects-heading {''',
    '''@media (max-width: 430px) {
  .projects-heading {''',
    "remove mobile projects topbar spacing",
)

s = replace_once(
    s,
    '''@media (max-width: 390px) {
  .quick-grid, .new-type {
    grid-template-columns: 1fr;
  }''',
    '''@media (max-width: 390px) {
  .quick-grid {
    grid-template-columns: 1fr;
  }''',
    "keep project type segmented on compact widths",
)

s = replace_once(
    s,
    ''':is(.list-row, .project-open, .quick-card, .nav-btn, .text-btn, .mini-btn, .sheet-close, .mix-toggle, .top-icon-btn, .project-menu, .type-card):not(:disabled):hover, summary:hover, .structure-row:hover {''',
    ''':is(.list-row, .project-open, .quick-card, .nav-btn, .text-btn, .mini-btn, .sheet-close, .mix-toggle, .top-icon-btn, .project-menu, .segment-choice):not(:disabled):hover, summary:hover, .structure-row:hover {''',
    "hover selector",
)

s = replace_once(
    s,
    '''  .secondary:not(:disabled):hover,
  .type-card:not(:disabled):hover,
  .top-icon-btn:not(:disabled):hover {''',
    '''  .secondary:not(:disabled):hover,
  .top-icon-btn:not(:disabled):hover {''',
    "remove obsolete type card hover",
)

css.write_text(s, encoding="utf-8")

tests = Path("tests/test_v6.py")
s = tests.read_text(encoding="utf-8")
old = '''    def test_projects_foundation_and_new_project_keyboard_flow(self):
        for width in [320, 390, 430, 820, 1180]:
            with self.subTest(width=width):
                self.open('projects', width=width, pointer=width >= 1180)
                self.assertLessEqual(self.page.evaluate('document.documentElement.scrollWidth'), width)
                add = self.page.locator('[data-action="new-project"]')
                box = add.bounding_box()
                self.assertGreaterEqual(box['width'], 44)
                self.assertGreaterEqual(box['height'], 44)
                card = self.page.locator('.project-card').first.bounding_box()
                self.assertLessEqual(card['height'], 140)
                if width >= 1180:
                    self.assertLessEqual(self.page.locator('#app').bounding_box()['width'], 880)
                self.context.close()

        self.open('projects', width=390)
        self.click('new-project')
        self.click('set-new-type', '[data-type="study"]')
        title = self.page.locator('#newTitle')
        artist = self.page.locator('#newArtist')
        self.assertEqual(title.get_attribute('enterkeyhint'), 'next')
        self.assertEqual(artist.get_attribute('enterkeyhint'), 'done')
        title.fill('Enter Flow')
        title.press('Enter')
        expect(artist).to_be_focused()
        artist.fill('Babel')
        artist.press('Enter')
        expect(self.page.locator('h1')).to_have_text('Enter Flow')
        saved = self.db()
        created = next(p for p in saved['projects'] if p['title'] == 'Enter Flow')
        self.assertEqual(created['artist'], 'Babel')
        self.assertEqual(created['schemaVersion'], 5)
'''
new = '''    def test_projects_foundation_and_new_project_keyboard_flow(self):
        for width in [320, 390, 430, 820, 1180]:
            with self.subTest(width=width):
                self.open('projects', width=width, pointer=width >= 1180)
                self.assertLessEqual(self.page.evaluate('document.documentElement.scrollWidth'), width)
                self.assertEqual(self.page.locator('.topbar').count(), 0)
                self.assertEqual(self.page.locator('.pill-tag').count(), 0)
                add = self.page.locator('[data-action="new-project"]')
                box = add.bounding_box()
                self.assertGreaterEqual(box['width'], 44)
                self.assertGreaterEqual(box['height'], 44)
                card = self.page.locator('.project-card').first.bounding_box()
                heading = self.page.locator('.projects-heading').bounding_box()
                self.assertLessEqual(card['height'], 140)
                self.assertLess(abs((box['x'] + box['width']) - (card['x'] + card['width'])), 1.1)
                self.assertLess(abs((heading['x'] + heading['width']) - (card['x'] + card['width'])), 1.1)
                if width >= 1180:
                    self.assertLessEqual(self.page.locator('#app').bounding_box()['width'], 880)
                self.context.close()

        self.open('projects', width=390)
        self.click('new-project')
        self.assertEqual(self.page.locator('.topbar .center .pill-tag').count(), 0)
        segments = self.page.locator('.project-type-control .segment-choice')
        self.assertEqual(segments.count(), 2)
        for i in range(segments.count()):
            self.assertGreaterEqual(segments.nth(i).bounding_box()['height'], 44)
        expect(self.page.locator('#newTypeDescription')).to_have_text('Start with anything worth keeping.')
        self.click('set-new-type', '[data-type="study"]')
        expect(self.page.locator('#newTypeDescription')).to_have_text('Rebuild an existing song to learn how it works.')
        title = self.page.locator('#newTitle')
        artist = self.page.locator('#newArtist')
        self.assertEqual(title.get_attribute('enterkeyhint'), 'next')
        self.assertEqual(artist.get_attribute('enterkeyhint'), 'done')
        title.fill('Enter Flow')
        title.press('Enter')
        expect(artist).to_be_focused()
        artist.fill('Babel')
        artist.press('Enter')
        expect(self.page.locator('h1')).to_have_text('Enter Flow')
        saved = self.db()
        created = next(p for p in saved['projects'] if p['title'] == 'Enter Flow')
        self.assertEqual(created['artist'], 'Babel')
        self.assertEqual(created['schemaVersion'], 5)
'''
s = replace_once(s, old, new, "chunk 1.1 browser acceptance")
tests.write_text(s, encoding="utf-8")
