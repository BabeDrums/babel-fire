from pathlib import Path

app = Path('app.js')
s = app.read_text()
old = '''      app.querySelectorAll('[data-action="toggle-track-choice"]').forEach((el) => setSelected(el, names.has(el.dataset.name)));
      app.querySelector('[data-action="start-section-study"]').disabled = !tracksDone(p);
      return;'''
new = '''      app.querySelectorAll('[data-action="toggle-track-choice"]').forEach((el) => setSelected(el, names.has(el.dataset.name)));
      const next = app.querySelector('[data-action="start-section-study"]');
      if (tracksDone(p)) {
        if (!next)
          app.querySelector('.inline-add')?.insertAdjacentHTML(
            'afterend',
            '<div class="tracks-next-wrap"><button class="primary" data-action="start-section-study">Next</button></div>',
          );
      } else next?.closest('.tracks-next-wrap')?.remove();
      queueViewportFit();
      return;'''
if old not in s:
    raise SystemExit('track toggle anchor not found')
s = s.replace(old, new, 1)
app.write_text(s)

tests = Path('tests/test_v6.py')
t = tests.read_text()
old = '''            expect(self.page.locator('[data-route="structure"]')).to_be_disabled()
            expect(self.page.locator('.checkpoint-count')).to_have_text('0 of 3')
            self.click('toggle-setup',f'[data-field="{field}"]')
            expect(self.page.locator('[data-route="structure"]')).to_be_enabled()'''
new = '''            self.assertEqual(self.page.locator('[data-route="structure"]').count(),0)
            expect(self.page.locator('.checkpoint-locked-message')).to_have_text('Available after Song Setup')
            expect(self.page.locator('.checkpoint-count')).to_have_text('0 of 3')
            self.click('toggle-setup',f'[data-field="{field}"]')
            expect(self.page.locator('[data-route="structure"]')).to_be_enabled()'''
if old not in t:
    raise SystemExit('setup prerequisite loop anchor not found')
t = t.replace(old, new, 1)
old = '''        expect(self.page.locator('[data-route="structure"]')).to_be_disabled()
        self.page.locator('#meterInput').select_option('3/4')
        expect(self.page.locator('[data-route="structure"]')).to_be_enabled()'''
new = '''        self.assertEqual(self.page.locator('[data-route="structure"]').count(),0)
        expect(self.page.locator('.checkpoint-locked-message')).to_have_text('Available after Song Setup')
        self.page.locator('#meterInput').select_option('3/4')
        expect(self.page.locator('[data-route="structure"]')).to_be_enabled()'''
if old not in t:
    raise SystemExit('meter prerequisite anchor not found')
t = t.replace(old, new, 1)
old = '''        self.canvas_route('structure')
        kicker = self.page.locator('.section-kicker').first
        self.assertEqual(kicker.evaluate('el=>getComputedStyle(el).textTransform'), 'none')
        self.assertEqual(self.page.locator('.structure-list').evaluate('el=>getComputedStyle(el).display'), 'block')'''
new = '''        self.canvas_route('structure')
        self.assertEqual(self.page.locator('.section-kicker:text-is("Structure")').count(), 0)
        self.assertEqual(self.page.locator('h1').evaluate('el=>getComputedStyle(el).textTransform'), 'none')
        self.assertEqual(self.page.locator('.structure-list').evaluate('el=>getComputedStyle(el).display'), 'block')'''
if old not in t:
    raise SystemExit('foundation structure kicker anchor not found')
t = t.replace(old, new, 1)
old = '''                expect(self.page.locator('.structure-ready-label')).to_have_text('Finish structure')
                self.assertEqual(self.page.locator('[data-action="open-add-section"]').evaluate('el=>getComputedStyle(el).borderStyle'),'solid')'''
new = '''                self.assertEqual(self.page.locator('.structure-ready-label').count(),0)
                self.assertEqual(self.page.locator('.section-kicker:text-is("Structure")').count(),0)
                self.assertEqual(self.page.locator('[data-action="open-add-section"]').evaluate('el=>getComputedStyle(el).borderStyle'),'solid')'''
if old not in t:
    raise SystemExit('structure polish label anchor not found')
t = t.replace(old, new, 1)
tests.write_text(t)
