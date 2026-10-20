from pathlib import Path

app = Path("app.js")
text = app.read_text()

old = '''  function makeOriginalProject(title = "Untitled") {
    return {
      id: uid(),
      type: "original",
      title: title || "Untitled",
      createdAt: Date.now(),
      schemaVersion: SCHEMA_VERSION,
      spark: { starts: [], idea: "", reasons: [], anchor: "" },
      notes: [],
    };
  }
'''
new = '''  function makeOriginalProject(title = "", artist = "") {
    return {
      id: uid(),
      type: "original",
      title,
      artist,
      createdAt: Date.now(),
      schemaVersion: SCHEMA_VERSION,
      spark: { starts: [], idea: "", reasons: [], anchor: "" },
      notes: [],
    };
  }
'''
if text.count(old) != 1:
    raise SystemExit(f"makeOriginalProject count={text.count(old)}")
text = text.replace(old, new, 1)

old = '''      if (p.type === "original") {
        p.spark = p.spark || { starts: [], idea: "", reasons: [], anchor: "" };
'''
new = '''      if (p.type === "original") {
        p.artist = p.artist || "";
        p.spark = p.spark || { starts: [], idea: "", reasons: [], anchor: "" };
'''
if text.count(old) != 1:
    raise SystemExit(f"original normalize count={text.count(old)}")
text = text.replace(old, new, 1)

old = '''  function renderNewProject() {
    app.innerHTML =
      topbar(backButton("projects", "Projects"), "", "") +
      `<h2>New project</h2><p class="sub">Start original or rebuild a reference.</p><div class="spacer-24"></div><div class="project-type-control" role="group" aria-label="Project type"><button class="segment-choice ${ui.newType === "original" ? "selected" : ""}" data-action="set-new-type" data-type="original" aria-pressed="${ui.newType === "original"}">Original</button><button class="segment-choice ${ui.newType === "study" ? "selected" : ""}" data-action="set-new-type" data-type="study" aria-pressed="${ui.newType === "study"}">Recreation</button></div><div class="section-kicker project-field-label">Project</div><input class="field" id="newTitle" aria-label="Project title" enterkeyhint="${ui.newType === "study" ? "next" : "done"}" autocomplete="off" autocapitalize="words" placeholder="${ui.newType === "study" ? "Song title" : "Song title or Untitled"}"><input class="field custom-length" id="newArtist" aria-label="Artist" enterkeyhint="done" autocomplete="off" autocapitalize="words" placeholder="Artist" ${ui.newType === "study" ? "" : "hidden"}><div class="spacer-24"></div><button class="primary full" data-action="create-project">Create Project</button>`;
  }
'''
new = '''  function renderNewProject() {
    app.innerHTML =
      topbar(backButton("projects", "Projects"), "", "") +
      `<h2>New project</h2><p class="sub">Start original or rebuild a reference.</p><div class="spacer-24"></div><div class="project-type-control" role="group" aria-label="Project type"><button class="segment-choice ${ui.newType === "original" ? "selected" : ""}" data-action="set-new-type" data-type="original" aria-pressed="${ui.newType === "original"}">Original</button><button class="segment-choice ${ui.newType === "study" ? "selected" : ""}" data-action="set-new-type" data-type="study" aria-pressed="${ui.newType === "study"}">Recreation</button></div><div class="section-kicker project-field-label">Project</div><input class="field" id="newTitle" aria-label="Song title" enterkeyhint="next" autocomplete="off" autocapitalize="words" placeholder="Song title"><input class="field custom-length" id="newArtist" aria-label="Artist" enterkeyhint="done" autocomplete="off" autocapitalize="words" placeholder="Artist"><div class="spacer-24"></div><button class="primary full" data-action="create-project">Create Project</button>`;
  }
'''
if text.count(old) != 1:
    raise SystemExit(f"renderNewProject count={text.count(old)}")
text = text.replace(old, new, 1)

old = '''    if (action === "set-new-type") {
      ui.newType = b.dataset.type;
      app.querySelectorAll('[data-action="set-new-type"]').forEach((el) => setSelected(el, el.dataset.type === ui.newType));
      document.getElementById("newArtist").hidden = ui.newType !== "study";
      const titleInput = document.getElementById("newTitle");
      titleInput.placeholder = ui.newType === "study" ? "Song title" : "Song title or Untitled";
      titleInput.setAttribute("enterkeyhint", ui.newType === "study" ? "next" : "done");
      return;
    }
'''
new = '''    if (action === "set-new-type") {
      ui.newType = b.dataset.type;
      app.querySelectorAll('[data-action="set-new-type"]').forEach((el) => setSelected(el, el.dataset.type === ui.newType));
      return;
    }
'''
if text.count(old) != 1:
    raise SystemExit(f"set-new-type count={text.count(old)}")
text = text.replace(old, new, 1)

old = '''    if (action === "create-project") {
      const title =
          clean(document.getElementById("newTitle")?.value) || "Untitled",
        np =
          ui.newType === "study"
            ? makeStudyProject(
                title,
                clean(document.getElementById("newArtist")?.value),
              )
            : makeOriginalProject(title);
      db.projects.push(np);
      db.currentProjectId = np.id;
      save();
      return go("project");
    }
'''
new = '''    if (action === "create-project") {
      const titleInput = document.getElementById("newTitle"),
        title = clean(titleInput?.value),
        artist = clean(document.getElementById("newArtist")?.value);
      if (!title) {
        titleInput?.focus({ preventScroll: true });
        return;
      }
      const np =
        ui.newType === "study"
          ? makeStudyProject(title, artist)
          : makeOriginalProject(title, artist);
      db.projects.push(np);
      db.currentProjectId = np.id;
      save();
      return go("project");
    }
'''
if text.count(old) != 1:
    raise SystemExit(f"create-project count={text.count(old)}")
text = text.replace(old, new, 1)

old = '''    if (e.target.id === "newTitle") {
      e.preventDefault();
      const artist = document.getElementById("newArtist");
      if (ui.newType === "study" && artist && !artist.hidden) {
        // Treat Artist as a genuinely fresh editing host. iOS/WebKit can carry
        // the prior field's keyboard state across a scripted focus handoff;
        // replacing the input gives the new field its own editor session while
        // preserving the user's text exactly as entered.
        const freshArtist = artist.cloneNode(true);
        freshArtist.value = artist.value;
        artist.replaceWith(freshArtist);
        freshArtist.focus({ preventScroll: true });
        const end = freshArtist.value.length;
        freshArtist.setSelectionRange(end, end);
      } else app.querySelector('[data-action="create-project"]')?.click();
      return;
    }
'''
new = '''    if (e.target.id === "newTitle") {
      e.preventDefault();
      document.getElementById("newArtist")?.focus({ preventScroll: true });
      return;
    }
'''
if text.count(old) != 1:
    raise SystemExit(f"newTitle handoff count={text.count(old)}")
text = text.replace(old, new, 1)

app.write_text(text)

tests = Path("tests/test_v6.py")
text = tests.read_text()
old = '''    def test_new_project_next_handoff_uses_fresh_artist_input_without_rewriting_text(self):
        self.open('new-project', width=390,
                  data={'version': 5, 'currentProjectId': None, 'projects': []})
        self.click('set-new-type', '[data-type="study"]')
        title = self.page.locator('#newTitle')
        self.page.evaluate('window.previousArtist=document.getElementById("newArtist")')
        title.fill('Creep')
        title.press('Enter')
        artist = self.page.locator('#newArtist')
        expect(artist).to_be_focused()
        self.assertFalse(self.page.evaluate('window.previousArtist.isConnected'))
        self.page.keyboard.type('r')
        self.assertEqual(artist.input_value(), 'r')
        self.assertEqual(artist.get_attribute('autocapitalize'), 'words')
        self.assertEqual(title.get_attribute('enterkeyhint'), 'next')

'''
new = '''    def test_new_project_fields_persist_and_original_stores_artist(self):
        self.open('new-project', width=390,
                  data={'version': 5, 'currentProjectId': None, 'projects': []})
        title = self.page.locator('#newTitle')
        artist = self.page.locator('#newArtist')
        expect(artist).to_be_visible()
        self.assertEqual(title.get_attribute('placeholder'), 'Song title')
        self.assertEqual(title.get_attribute('enterkeyhint'), 'next')
        self.page.evaluate('window.originalArtist=document.getElementById("newArtist")')
        title.fill('My Song')
        title.press('Enter')
        expect(artist).to_be_focused()
        self.assertTrue(self.page.evaluate('window.originalArtist===document.getElementById("newArtist")'))
        artist.fill('Babel')
        self.click('set-new-type', '[data-type="study"]')
        expect(artist).to_be_visible()
        self.assertEqual(title.input_value(), 'My Song')
        self.assertEqual(artist.input_value(), 'Babel')
        self.click('set-new-type', '[data-type="original"]')
        self.click('create-project')
        saved = self.db()['projects'][0]
        self.assertEqual(saved['type'], 'original')
        self.assertEqual(saved['title'], 'My Song')
        self.assertEqual(saved['artist'], 'Babel')

    def test_new_project_requires_song_title_instead_of_creating_untitled(self):
        self.open('new-project', width=390,
                  data={'version': 5, 'currentProjectId': None, 'projects': []})
        self.page.locator('#newArtist').fill('Babel')
        self.click('create-project')
        self.assertEqual(len(self.db()['projects']), 0)
        expect(self.page.locator('#newTitle')).to_be_focused()

'''
if text.count(old) != 1:
    raise SystemExit(f"new project regression count={text.count(old)}")
text = text.replace(old, new, 1)
tests.write_text(text)
