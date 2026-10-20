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
    'aria-label="Project options">•••</button>',
    'aria-label="Project options">…</button>',
    "project menu glyph",
)
app = replace_once(
    app,
    ': `<div class="empty">No projects yet. Tap + to start one.</div>`',
    ': ""',
    "projects empty-state helper",
)
app = replace_once(
    app,
    'id="newTitle" aria-label="Project title" enterkeyhint="${ui.newType === "study" ? "next" : "done"}" autocomplete="off"',
    'id="newTitle" aria-label="Project title" enterkeyhint="${ui.newType === "study" ? "next" : "done"}" autocomplete="off" autocapitalize="words"',
    "title autocapitalize",
)
app = replace_once(
    app,
    'id="newArtist" aria-label="Artist" enterkeyhint="done" autocomplete="off"',
    'id="newArtist" aria-label="Artist" enterkeyhint="done" autocomplete="off" autocapitalize="words"',
    "artist autocapitalize",
)
app_path.write_text(app, encoding="utf-8")

styles_path = Path("styles.css")
styles = styles_path.read_text(encoding="utf-8")
styles = replace_once(
    styles,
    '''.project-menu {
  position: absolute;
  right: 7px;
  top: 7px;
  width: 44px;
  height: 44px;
  display: grid;
  place-items: center;
  color: var(--muted);
  cursor: pointer;
  border-radius: var(--radius-control);
}''',
    '''.project-menu {
  position: absolute;
  right: 7px;
  top: 7px;
  width: 44px;
  height: 44px;
  display: grid;
  place-items: center;
  color: var(--quiet);
  font-size: 20px;
  line-height: 1;
  cursor: pointer;
  border-radius: var(--radius-control);
}''',
    "project menu visual priority",
)
styles_path.write_text(styles, encoding="utf-8")

test_path = Path("tests/test_v6.py")
tests = test_path.read_text(encoding="utf-8")
tests = replace_once(
    tests,
    '''                self.assertLessEqual(card['height'], 140)
                self.assertLess(abs((box['x'] + box['width']) - (card['x'] + card['width'])), 1.1)
                self.assertLess(abs((heading['x'] + heading['width']) - (card['x'] + card['width'])), 1.1)
''',
    '''                self.assertLessEqual(card['height'], 140)
                self.assertLess(abs((box['x'] + box['width']) - (card['x'] + card['width'])), 1.1)
                self.assertLess(abs((heading['x'] + heading['width']) - (card['x'] + card['width'])), 1.1)
                self.assertEqual(self.page.locator('.project-menu').first.text_content().strip(), '…')
                self.assertEqual(self.page.locator('.project-open .foot > span:last-child').first.text_content().strip(), '›')
''',
    "project card affordance assertions",
)
tests = replace_once(
    tests,
    '''                self.context.close()

        self.open('projects', width=390)
''',
    '''                self.context.close()

        self.open('projects', width=390, data={'version':5,'currentProjectId':None,'projects':[]})
        self.assertEqual(self.page.locator('.empty').count(), 0)
        self.assertEqual(self.page.get_by_text('No projects yet. Tap + to start one.').count(), 0)
        self.context.close()

        self.open('projects', width=390)
''',
    "empty project acceptance assertion",
)
tests = replace_once(
    tests,
    '''        self.assertEqual(title.get_attribute('enterkeyhint'), 'next')
        self.assertEqual(artist.get_attribute('enterkeyhint'), 'done')
''',
    '''        self.assertEqual(title.get_attribute('enterkeyhint'), 'next')
        self.assertEqual(artist.get_attribute('enterkeyhint'), 'done')
        self.assertEqual(title.get_attribute('autocapitalize'), 'words')
        self.assertEqual(artist.get_attribute('autocapitalize'), 'words')
''',
    "autocapitalize acceptance assertions",
)
test_path.write_text(tests, encoding="utf-8")
