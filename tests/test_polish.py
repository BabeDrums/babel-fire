"""Focused regressions for the V6 Apple-minimal polish pass."""
import json
import os
import unittest
from playwright.sync_api import sync_playwright
from test_v6 import fixture, KEY

URL = os.environ.get('FIRE_URL', 'http://127.0.0.1:8000')


class PolishBrowser(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pw = sync_playwright().start()
        cls.browser = cls.pw.chromium.launch(
            executable_path=os.environ.get('CHROMIUM_PATH', '/usr/bin/chromium'),
            args=['--no-sandbox'])

    @classmethod
    def tearDownClass(cls):
        cls.browser.close()
        cls.pw.stop()

    def open(self, route='section-study', width=None, data=None):
        width = width or int(os.environ.get('FIRE_TEST_WIDTH', '390'))
        self.context = self.browser.new_context(viewport={'width': width, 'height': 1000})
        self.addCleanup(self.context.close)
        data = data if data is not None else fixture()
        self.context.add_init_script('''
          localStorage.setItem(%s,%s);
          history.replaceState({route:%s,projectId:'p1',fromRoute:'tracks',fromLabel:'Tracks',sectionIndex:0},'');
        ''' % (json.dumps(KEY), json.dumps(json.dumps(data)), json.dumps(route)))
        self.page = self.context.new_page()
        self.page.set_default_timeout(5000)
        errors = []
        self.page.on('pageerror', lambda e: errors.append(str(e)))
        self.addCleanup(lambda: self.assertEqual(errors, []))
        response = self.page.goto(URL)
        self.assertEqual(response.status, 200)
        return self.page

    def test_new_project_enter_advances_and_submits(self):
        page = self.open('projects')
        page.locator('[data-action="new-project"]').click()
        page.locator('[data-action="set-new-type"][data-type="study"]').click()
        title = page.locator('#newTitle')
        artist = page.locator('#newArtist')
        title.fill('Enter Flow')
        title.press('Enter')
        self.assertTrue(artist.evaluate('el=>document.activeElement===el'))
        artist.fill('Babel')
        artist.press('Enter')
        page.wait_for_selector('h1:text("Enter Flow")')

    def test_review_map_chips_are_navigation(self):
        page = self.open('map-summary')
        structure = page.locator('.summary-nav-chip').first
        self.assertIn('Intro', structure.inner_text())
        structure.click()
        page.wait_for_selector('[data-route="section-study"], .study-pane')
        self.assertEqual(page.locator('.work-position').inner_text().split('·')[0].strip(), 'Section Study')

    def test_draft_parent_uses_derived_progress(self):
        data = fixture()
        project = data['projects'][0]
        project['skeleton']['draft']['parts']['s0']['t1'] = False
        page = self.open('skeleton-draft', data=data)
        parent = page.locator('[data-draft-section="s0"] summary .round-check')
        self.assertTrue(parent.evaluate('el=>el.classList.contains("derived-status")'))
        self.assertEqual(page.locator('[data-draft-section="s0"] .draft-child-label').inner_text(), 'Complete tracks below')
        self.assertEqual(page.locator('[data-draft-section="s0"] .draft-progress').count(), 1)

    def test_open_presence_has_ghost_continuation_marker(self):
        page = self.open('section-study')
        self.assertEqual(page.locator('.timeline-ruler .timeline-continuation-marker').inner_text(), '9')
        segment = page.locator('.presence-segment.continue-out').first
        self.assertEqual(segment.count(), 1)
        right = segment.evaluate('el=>getComputedStyle(el).right')
        self.assertTrue(right.startswith('-'))


if __name__ == '__main__':
    unittest.main()
