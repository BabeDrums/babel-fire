from pathlib import Path

app = Path("app.js")
text = app.read_text()

old = '''  app.addEventListener("beforeinput", (e) => {
    const input = e.target;
    if (input.id !== "newArtist" || input.dataset.capitalizeFirst !== "true")
      return;
    input.dataset.capitalizeFirst = "false";
    if (
      e.isComposing ||
      e.inputType !== "insertText" ||
      typeof e.data !== "string" ||
      input.value ||
      input.selectionStart !== 0 ||
      input.selectionEnd !== 0 ||
      !/^[a-z]$/.test(e.data)
    )
      return;
    e.preventDefault();
    input.setRangeText(e.data.toLocaleUpperCase(), 0, 0, "end");
    input.dispatchEvent(new Event("input", { bubbles: true }));
  });
'''
if text.count(old) != 1:
    raise SystemExit(f"beforeinput block count={text.count(old)}")
text = text.replace(old, "", 1)

old = '''      if (ui.newType === "study" && artist && !artist.hidden) {
        // WebKit controls the software keyboard's Shift state. If iOS keeps the
        // prior field's lowercase state during Next, correct only the first
        // direct keystroke; normal autocapitalize="words" handles the rest.
        artist.dataset.capitalizeFirst = "true";
        artist.focus({ preventScroll: true });
      } else app.querySelector('[data-action="create-project"]')?.click();
'''
new = '''      if (ui.newType === "study" && artist && !artist.hidden) {
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
'''
if text.count(old) != 1:
    raise SystemExit(f"handoff block count={text.count(old)}")
text = text.replace(old, new, 1)
app.write_text(text)

tests = Path("tests/test_v6.py")
text = tests.read_text()
old = '''    def test_new_project_next_handoff_capitalizes_first_artist_keystroke(self):
        self.open('new-project', width=390,
                  data={'version': 5, 'currentProjectId': None, 'projects': []})
        self.click('set-new-type', '[data-type="study"]')
        title = self.page.locator('#newTitle')
        artist = self.page.locator('#newArtist')
        title.fill('Creep')
        title.press('Enter')
        expect(artist).to_be_focused()
        self.page.keyboard.type('r')
        self.assertEqual(artist.input_value(), 'R')
        self.page.keyboard.type('adio head')
        self.assertEqual(artist.input_value(), 'Radio head')

'''
new = '''    def test_new_project_next_handoff_uses_fresh_artist_input_without_rewriting_text(self):
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
if text.count(old) != 1:
    raise SystemExit(f"old regression count={text.count(old)}")
text = text.replace(old, new, 1)
tests.write_text(text)
