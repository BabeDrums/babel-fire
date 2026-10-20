from pathlib import Path


def replace_once(text, old, new, label):
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"{label}: expected 1 match, found {count}")
    return text.replace(old, new, 1)

app_path = Path("app.js")
app = app_path.read_text(encoding="utf-8")

app = replace_once(
    app,
    '''  function renderNewProject() {\n    const typeCopy =\n      ui.newType === "study"\n        ? "Rebuild an existing song to learn how it works."\n        : "Start with anything worth keeping.";\n    app.innerHTML =''',
    '''  function renderNewProject() {\n    app.innerHTML =''',
    "new project helper copy constant",
)

app = replace_once(
    app,
    '''</div><p class="project-type-copy" id="newTypeDescription">${typeCopy}</p><div class="section-kicker project-field-label">Project</div>''',
    '''</div><div class="section-kicker project-field-label">Project</div>''',
    "new project helper copy markup",
)

app = replace_once(
    app,
    '''      const titleInput = document.getElementById("newTitle"),\n        typeDescription = document.getElementById("newTypeDescription");\n      titleInput.placeholder = ui.newType === "study" ? "Song title" : "Song title or Untitled";\n      titleInput.setAttribute("enterkeyhint", ui.newType === "study" ? "next" : "done");\n      if (typeDescription)\n        typeDescription.textContent =\n          ui.newType === "study"\n            ? "Rebuild an existing song to learn how it works."\n            : "Start with anything worth keeping.";\n      return;''',
    '''      const titleInput = document.getElementById("newTitle");\n      titleInput.placeholder = ui.newType === "study" ? "Song title" : "Song title or Untitled";\n      titleInput.setAttribute("enterkeyhint", ui.newType === "study" ? "next" : "done");\n      return;''',
    "new project helper copy interaction",
)

app = replace_once(
    app,
    '''      const artist = document.getElementById("newArtist");\n      if (ui.newType === "study" && artist && !artist.hidden) artist.focus();\n      else app.querySelector('[data-action="create-project"]')?.click();''',
    '''      const artist = document.getElementById("newArtist");\n      if (ui.newType === "study" && artist && !artist.hidden) {\n        // Give iOS a fresh text-input handoff so the Artist field can reapply\n        // its own keyboard traits (including autocapitalize="words").\n        e.target.blur();\n        artist.focus({ preventScroll: true });\n      } else app.querySelector('[data-action="create-project"]')?.click();''',
    "fresh artist input handoff",
)

app_path.write_text(app, encoding="utf-8")

# Remove the now-unused helper style so the core stylesheet stays honest.
styles_path = Path("styles.css")
styles = styles_path.read_text(encoding="utf-8")
styles = replace_once(
    styles,
    '''.project-type-copy {\n  min-height: 38px;\n  margin: 10px 2px 0;\n  color: var(--muted);\n  font-size: 13px;\n  line-height: 1.45;\n}\n''',
    '',
    "unused project helper style",
)
styles_path.write_text(styles, encoding="utf-8")

# Keep the acceptance test focused on the approved UI and keyboard semantics.
test_path = Path("tests/test_v6.py")
tests = test_path.read_text(encoding="utf-8")
tests = replace_once(
    tests,
    '''        expect(self.page.locator('#newTypeDescription')).to_have_text('Start with anything worth keeping.')\n        self.click('set-new-type', '[data-type="study"]')\n        expect(self.page.locator('#newTypeDescription')).to_have_text('Rebuild an existing song to learn how it works.')\n''',
    '''        self.assertEqual(self.page.locator('#newTypeDescription').count(), 0)\n        self.assertEqual(self.page.get_by_text('Start with anything worth keeping.').count(), 0)\n        self.click('set-new-type', '[data-type="study"]')\n        self.assertEqual(self.page.get_by_text('Rebuild an existing song to learn how it works.').count(), 0)\n''',
    "helper copy acceptance assertions",
)
test_path.write_text(tests, encoding="utf-8")
