from pathlib import Path

app = Path("app.js")
text = app.read_text()

old = '  app.addEventListener("keydown", (e) => {\n'
new = '''  app.addEventListener("beforeinput", (e) => {
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
  app.addEventListener("keydown", (e) => {
'''
if text.count(old) != 1:
    raise SystemExit(f"keydown insertion anchor count={text.count(old)}")
text = text.replace(old, new, 1)

old = '''      if (ui.newType === "study" && artist && !artist.hidden) {
        // Give iOS a fresh text-input handoff so the Artist field can reapply
        // its own keyboard traits (including autocapitalize="words").
        e.target.blur();
        artist.focus({ preventScroll: true });
      } else app.querySelector('[data-action="create-project"]')?.click();
'''
new = '''      if (ui.newType === "study" && artist && !artist.hidden) {
        // WebKit controls the software keyboard's Shift state. If iOS keeps the
        // prior field's lowercase state during Next, correct only the first
        // direct keystroke; normal autocapitalize="words" handles the rest.
        artist.dataset.capitalizeFirst = "true";
        artist.focus({ preventScroll: true });
      } else app.querySelector('[data-action="create-project"]')?.click();
'''
if text.count(old) != 1:
    raise SystemExit(f"handoff anchor count={text.count(old)}")
text = text.replace(old, new, 1)
app.write_text(text)

tests = Path("tests/test_v6.py")
text = tests.read_text()
anchor = '    def test_cross_platform_screen_canvases_and_fluid_widths(self):\n'
addition = '''    def test_new_project_next_handoff_capitalizes_first_artist_keystroke(self):
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
if text.count(anchor) != 1:
    raise SystemExit(f"test anchor count={text.count(anchor)}")
text = text.replace(anchor, addition + anchor, 1)
tests.write_text(text)
