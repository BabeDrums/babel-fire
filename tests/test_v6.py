"""V6 browser regressions (including retained V5 musical/data invariants). Run against a static server:
FIRE_URL=http://127.0.0.1:8000 python3 -B -m unittest discover -s tests -v
Requires Python Playwright and Chromium (CHROMIUM_PATH may override its location).
Tests use disposable contexts and never read a user's browser storage.
"""
import json
import os
import unittest
from playwright.sync_api import sync_playwright, expect

KEY = 'production-projects-v1'
URL = os.environ.get('FIRE_URL', 'http://127.0.0.1:8000')


def fixture():
    sections = [{'id': f's{i}', 'name': name, 'lengthBars': 8}
                for i, name in enumerate(['Intro', 'Verse', 'Chorus'])]
    data = {s['id']: {'feel': {'depth': 'Close', 'space': 'Dry', 'width': 'Wide',
                             'density': 'Balanced', 'energy': 'Medium'},
                       'focusIds': ['t1'], 'focusState': 'selected', 'silence': False,
                       'parking': f"Note {s['id']}", 'takeaway': 'Keep this'} for s in sections}
    p = {'id': 'p1', 'type': 'study', 'schemaVersion': 4, 'title': 'Migration song',
         'artist': 'Test artist', 'createdAt': 123, 'notes': ['Retain me'],
         'map': {'setup': {'reference': True, 'tempo': '120', 'meter': '4/4',
                           'grid': True, 'firstListen': True},
                 'sections': sections, 'tracks': [{'id': 't1', 'name': 'Drums'},
                                                  {'id': 't2', 'name': 'Bass'}],
                 'structureVerified': True, 'mapVerified': True, 'teachBack': True,
                 'sectionData': data, 'phaseParking': 'Unresolved', 'phaseTakeaway': 'Listen',
                 'timeline': {'presence': [{'id': 'r1', 'trackId': 't1',
                                            'start': {'sectionId': 's0', 'bar': 0}, 'end': None}],
                              'events': [
                                  {'id': 'e1', 'targetType': 'track', 'targetId': 't1',
                                   'label': 'Widens', 'kind': 'range',
                                   'start': {'sectionId': 's0', 'bar': 0}, 'end': None},
                                  {'id': 'e2', 'targetType': 'track', 'targetId': 't1',
                                   'label': 'Pattern shift', 'kind': 'marker',
                                   'point': {'sectionId': 's0', 'bar': 2.5}},
                                  {'id': 'cue', 'targetType': 'mix', 'targetId': None,
                                   'label': 'Transition cue', 'kind': 'marker',
                                   'point': {'sectionId': 's1', 'bar': 0}}]}},
         'skeleton': {'session': {'tracks': {'t1': True, 't2': True},
                                  'markers': {s['id']: True for s in sections}},
                      'draft': {'parts': {s['id']: {'t1': True, 't2': True} for s in sections}},
                      'bounce': {'exported': True, 'listened': True}}}
    return {'version': 4, 'currentProjectId': 'p1', 'projects': [p, {
        'id': 'original', 'type': 'original', 'schemaVersion': 4, 'title': 'My idea',
        'spark': {'starts': ['Beat'], 'idea': 'Preserve the groove', 'reasons': ['Energy'],
                  'anchor': 'Bass'}, 'notes': []}]}


class V6Browser(unittest.TestCase):
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

    def open(self, route='section-study', width=None, data=None, reduced=False, pointer=False):
        width = width or int(os.environ.get('FIRE_TEST_WIDTH', '390'))
        self.context = self.browser.new_context(viewport={'width': width, 'height': 1000},
                                                has_touch=not pointer, reduced_motion='reduce' if reduced else 'no-preference')
        self.addCleanup(self.context.close)
        data = data if data is not None else fixture()
        # Seed exactly once: reload tests must exercise the migrated saved state.
        self.context.add_init_script('''if(!sessionStorage.getItem('seeded')){
          localStorage.setItem(%s,%s);sessionStorage.setItem('seeded','1');
          history.replaceState({route:%s,projectId:'p1',fromRoute:'tracks',fromLabel:'Tracks'},'');
        }''' % (json.dumps(KEY), json.dumps(json.dumps(data)), json.dumps(route)))
        self.page = self.context.new_page()
        self.page.set_default_timeout(5000)
        self.errors = []
        self.page.on('pageerror', lambda e: self.errors.append(str(e)))
        self.page.on('console', lambda m: self.errors.append(m.text) if m.type == 'error' and
                     '404 (File not found)' not in m.text else None)
        response = self.page.goto(URL)
        self.assertEqual(response.status, 200)
        self.addCleanup(lambda errors=self.errors: self.assertEqual(errors, []))
        return self.page

    def click(self, action, extra=''):
        button=self.page.locator(f'[data-action="{action}"]{extra}')
        button.click()

    def expand_map_setup(self):
        disclosure=self.page.locator('[data-action="toggle-setup-disclosure"]')
        if disclosure.count():
            disclosure.click()
            expect(self.page.locator('#tempoInput')).to_be_visible()

    def db(self):
        return self.page.evaluate('(key)=>JSON.parse(localStorage.getItem(key))', KEY)

    def project(self):
        return self.db()['projects'][0]

    def event(self, id):
        return next(e for e in self.project()['map']['timeline']['events'] if e['id'] == id)

    def select(self, range='r1'):
        hit=self.page.locator(f'.presence-hit[data-range-id="{range}"]')
        row=hit.locator('xpath=ancestor::*[@data-track-row][1]')
        if row.evaluate('el=>el.classList.contains("expanded")'):
            row.locator('.timeline-label').click()
        self.page.locator(f'.presence-hit[data-range-id="{range}"]').click()

    def add_change(self, label, target='track'):
        self.click('open-add-change', f'[data-target-type="{target}"]')
        self.click('choose-change', f'[data-label="{label}"]')

    def touch_drag(self, locator, fraction, cancel=False):
        locator.scroll_into_view_if_needed()
        box = locator.bounding_box()
        lane = locator.locator('xpath=..').bounding_box()
        cdp = self.context.new_cdp_session(self.page)
        x, y = box['x']+box['width']/2, box['y']+box['height']/2
        cdp.send('Input.dispatchTouchEvent', {'type': 'touchStart', 'touchPoints': [{'x': x, 'y': y}]})
        dest = lane['x']+lane['width']*fraction
        for i in range(1, 5):
            cdp.send('Input.dispatchTouchEvent', {'type': 'touchMove',
                                                'touchPoints': [{'x': x+(dest-x)*i/4, 'y': y}]})
        cdp.send('Input.dispatchTouchEvent', {'type': 'touchCancel' if cancel else 'touchEnd', 'touchPoints': []})
        cdp.detach()

    def place(self, edge, value, kind='presence', touch=False):
        handle=self.page.locator(f'[data-{kind}-handle][data-edge="{edge}"]')
        self.tap_handle(handle,touch)
        lane=handle.locator('xpath=ancestor::*[contains(@class,"timeline-lane")][1]')
        box=lane.bounding_box();bars=int(lane.evaluate('el=>getComputedStyle(el).getPropertyValue("--bars")'))
        x=box['x']+max(2,min(box['width']-2,box['width']*value/bars));y=box['y']+58
        self.pointer_tap(x,y,touch)

    def pointer_tap(self,x,y,touch=False,cancel=False):
        if touch:
            cdp=self.context.new_cdp_session(self.page)
            cdp.send('Input.dispatchTouchEvent',{'type':'touchStart','touchPoints':[{'x':x,'y':y}]})
            cdp.send('Input.dispatchTouchEvent',{'type':'touchCancel' if cancel else 'touchEnd','touchPoints':[]});cdp.detach()
        else:
            self.page.mouse.move(x,y);self.page.mouse.down()
            if cancel:self.page.keyboard.press('Escape')
            self.page.mouse.up()

    def tap_handle(self,handle,touch=False):
        handle.scroll_into_view_if_needed();box=handle.bounding_box()
        self.pointer_tap(box['x']+22,box['y']+22,touch)

    def direct_boundary(self, track, boundary, touch=False, cancel=False):
        surface=self.page.locator(f'[data-presence-surface][data-track-id="{track}"]')
        if not surface.count():
            self.click('toggle-timeline-track',f'[data-track-id="{track}"]')
            surface=self.page.locator(f'[data-presence-surface][data-track-id="{track}"]')
        surface.scroll_into_view_if_needed();box=surface.bounding_box()
        bars=int(surface.locator('xpath=..').evaluate('el=>getComputedStyle(el).getPropertyValue("--bars")'))
        x=box['x']+max(4,min(box['width']-4,box['width']*boundary/bars))
        y=box['y']+box['height']*.9
        if touch:
            cdp=self.context.new_cdp_session(self.page)
            cdp.send('Input.dispatchTouchEvent',{'type':'touchStart','touchPoints':[{'x':x,'y':y}]})
            cdp.send('Input.dispatchTouchEvent',{'type':'touchCancel' if cancel else 'touchEnd','touchPoints':[]})
            cdp.detach()
        else:
            self.page.mouse.move(x,y)
            self.page.mouse.down()
            if cancel:
                self.page.keyboard.press('Escape')
            self.page.mouse.up()

    def test_v4_migration_and_reload_preserve_identity_progress_and_fractional_offsets(self):
        original = fixture()
        self.open()
        saved = self.db()
        self.assertEqual(saved['version'], 5)
        p = self.project()
        self.assertEqual(p['schemaVersion'], 5)
        self.assertEqual(p['map']['sections'], original['projects'][0]['map']['sections'])
        self.assertEqual(p['map']['tracks'], original['projects'][0]['map']['tracks'])
        self.assertEqual(p['map']['timeline']['presence'][0]['id'], 'r1')
        self.assertEqual({e['id'] for e in p['map']['timeline']['events']}, {'e1', 'e2', 'cue'})
        self.assertEqual(self.event('e2')['point']['bar'], 2.5)
        self.assertEqual(p['skeleton'], original['projects'][0]['skeleton'])
        self.assertEqual(p['notes'], ['Retain me'])
        self.assertEqual(saved['projects'][1]['spark'], original['projects'][1]['spark'])
        self.page.reload()
        self.assertEqual(self.db(), saved)

    def test_section_builder_custom_repeated_names_edit_and_remove(self):
        self.open('structure')
        self.click('open-add-section')
        expect(self.page.locator('[data-action="save-new-section"]')).to_be_disabled()
        self.click('choose-section-type', '[data-name="Verse"]')
        self.click('set-new-section-bars', '[data-bars="4"]')
        expect(self.page.locator('#newSectionBars')).to_be_hidden()
        self.click('save-new-section');self.click('close-sheet')
        expect(self.page.locator('.structure-row').filter(has_text='Verse 2')).to_be_visible()
        self.click('open-add-section');self.click('choose-section-type', '[data-name="Custom"]')
        self.page.locator('#newSectionName').fill('Breakdown')
        self.click('set-new-section-bars', '[data-bars="custom"]')
        self.page.locator('#newSectionBars').fill('0')
        expect(self.page.locator('[data-action="save-new-section"]')).to_be_disabled()
        self.page.locator('#newSectionBars').fill('7');self.click('save-new-section');self.click('close-sheet')
        sid = self.project()['map']['sections'][-1]['id']
        self.click('edit-section', f'[data-section-id="{sid}"]')
        self.page.locator('#renameSection').fill('Break');self.click('set-sheet-bars', '[data-bars="12"]')
        self.click('save-section')
        self.assertEqual(self.project()['map']['sections'][-1], {'id': sid, 'name': 'Break', 'lengthBars': 12})
        self.click('edit-section', f'[data-section-id="{sid}"]')
        self.click('close-sheet');self.click('delete-section',f'[data-id="{sid}"]')
        self.assertNotIn(sid, [s['id'] for s in self.project()['map']['sections']])
        self.assertNotIn('Bars bars', self.page.locator('body').inner_text())

    def test_add_absent_presence_is_open_and_covers_later_new_sections(self):
        self.open();self.direct_boundary('t2',0)
        ranges = self.project()['map']['timeline']['presence']
        self.assertIsNone(next(r for r in ranges if r['trackId']=='t2')['end'])
        self.assertFalse(self.project()['skeleton']['draft']['parts']['s2']['t2'])
        self.assertFalse(self.project()['map']['sectionData']['s2']['silence'])
        # Route to Structure through the normal phase navigator.
        self.click('go', '[data-route="map"]')
        self.click('go', '[data-route="structure"]')
        self.click('open-add-section');self.click('choose-section-type', '[data-name="Outro"]')
        self.click('set-new-section-bars', '[data-bars="4"]');self.click('save-new-section');self.click('close-sheet')
        self.assertEqual(len(self.project()['map']['sections']), 4)
        r = next(r for r in self.project()['map']['timeline']['presence'] if r['trackId']=='t2')
        self.assertIsNone(r['end'])
        self.click('toggle-structure-verified');self.click('go','[data-route="tracks"]')
        self.click('start-section-study');self.click('jump-section','[data-index="3"]')
        expect(self.page.locator('.section-tab.current')).to_have_text('Outro')
        self.assertEqual(self.page.locator('.presence-segment.continue-in.continue-out').count(),2)

    def test_touch_presence_stop_inside_section_edge_and_open_undo(self):
        self.open();self.select()
        self.assertEqual(self.page.locator('[data-open-tail]').count(), 1)
        self.place('end',4)
        self.assertEqual(self.project()['map']['timeline']['presence'][0]['end'], {'sectionId':'s0','bar':4})
        self.assertEqual(self.event('e1')['end'], {'sectionId':'s0','bar':4})
        self.page.locator('#undoEdit').click()
        self.assertIsNone(self.project()['map']['timeline']['presence'][0]['end'])
        self.place('end',8)
        self.assertEqual(self.project()['map']['timeline']['presence'][0]['end'], {'sectionId':'s0','bar':'end'})
        self.page.locator('#undoEdit').click()
        self.assertIsNone(self.project()['map']['timeline']['presence'][0]['end'])

    def test_touch_cancel_leaves_database_and_listeners_clean(self):
        self.open();self.select();before=self.db()
        self.touch_drag(self.page.locator('[data-presence-handle][data-edge="start"]'), .25, cancel=True)
        self.assertEqual(self.db(), before)
        self.assertFalse(self.page.locator('body').evaluate('(e)=>e.classList.contains("is-dragging")'))
        self.touch_drag(self.page.locator('[data-presence-handle][data-edge="start"]'), .25)
        self.assertEqual(self.project()['map']['timeline']['presence'][0]['start']['bar'], 2)

    def test_one_screen_add_change_and_aligned_selection_removal_undo(self):
        self.open();self.select();self.click('open-add-change')
        for label in ['Widens','Narrows','Louder','Softer','Doubles','Pattern shift','Register shift','Effect shift']:
            expect(self.page.locator(f'[data-action="choose-change"][data-label="{label}"]')).to_be_visible()
        self.assertNotIn('Transition cue', self.page.locator('.change-sheet').inner_text())
        self.click('choose-change','[data-label="Louder"]')
        expect(self.page.locator('#sheetRoot')).not_to_have_class('sheet-backdrop open')
        louder=next(e for e in self.project()['map']['timeline']['events'] if e['label']=='Louder')
        self.assertIsNone(louder['end'])
        self.assertTrue(self.project()['skeleton']['draft']['parts']['s0']['t1'])
        self.click('select-event',f'[data-event-id="{louder["id"]}"]')
        self.assertEqual(self.page.locator('.event-line.selected').count(), 1)
        self.click('remove-selected', '[data-kind="event"]')
        self.assertFalse(any(e['id']==louder['id'] for e in self.project()['map']['timeline']['events']))
        self.page.locator('#undoEdit').click()
        self.assertEqual(self.event(louder['id'])['label'], 'Louder')

    def test_supersession_and_different_categories_overlap(self):
        self.open();self.click('jump-section','[data-index="1"]')
        expect(self.page.locator('.section-tab.current')).to_have_text('Verse')
        self.select();self.add_change('Narrows')
        self.assertEqual(self.event('e1')['end'], {'sectionId':'s1','bar':0})
        self.add_change('Louder')
        ranges=[e for e in self.project()['map']['timeline']['events'] if e['kind']=='range']
        self.assertEqual({e['label'] for e in ranges}, {'Widens','Narrows','Louder'})
        self.add_change('Widens')
        ranges=[e for e in self.project()['map']['timeline']['events'] if e['kind']=='range']
        self.assertNotIn('Narrows', [e['label'] for e in ranges])
        self.assertIn('Louder',[e['label'] for e in ranges])

    def test_touch_change_range_trim_and_marker_move_and_tap_timing(self):
        self.open();self.select();self.click('select-event','[data-event-id="e1"]')
        self.place('end',6,'event')
        self.assertEqual(self.event('e1')['end'], {'sectionId':'s0','bar':6})
        self.place('end',5,'event')
        self.assertEqual(self.event('e1')['end']['bar'], 5)
        self.click('select-event','[data-event-id="e2"]')
        self.touch_drag(self.page.locator('[data-event-marker]'), .5)
        self.assertEqual(self.event('e2')['point']['bar'], 4)
        self.assertFalse(self.project()['skeleton']['draft']['parts']['s0']['t1'])
        self.assertTrue(self.project()['skeleton']['draft']['parts']['s1']['t1'])

    def test_stop_resume_adjacent_merge_and_undo(self):
        self.open();self.select();self.place('end',4)
        self.direct_boundary('t1',6)
        ranges=self.project()['map']['timeline']['presence']
        self.assertEqual(len(ranges),2);self.assertEqual(ranges[0]['id'],'r1')
        self.assertEqual(ranges[0]['end']['bar'],4);self.assertEqual(ranges[1]['start']['bar'],6)
        self.assertIsNone(ranges[1]['end'])
        self.page.locator('#undoEdit').click()
        self.assertEqual(len(self.project()['map']['timeline']['presence']),1)
        self.direct_boundary('t1',4)
        ranges=self.project()['map']['timeline']['presence']
        self.assertEqual(len(ranges),1);self.assertEqual(ranges[0]['id'],'r1');self.assertIsNone(ranges[0]['end'])

    def test_structure_touch_reorder_preserves_section_notes_and_open_ranges(self):
        self.open('structure')
        handle=self.page.locator('[data-section-id="s0"] [data-drag-handle]')
        handle.scroll_into_view_if_needed();a=handle.bounding_box();target=self.page.locator('[data-section-id="s2"]').bounding_box()
        cdp=self.context.new_cdp_session(self.page)
        x=a['x']+22;y=a['y']+22
        cdp.send('Input.dispatchTouchEvent',{'type':'touchStart','touchPoints':[{'x':x,'y':y}]})
        cdp.send('Input.dispatchTouchEvent',{'type':'touchMove','touchPoints':[{'x':x,'y':target['y']+target['height']-2}]})
        cdp.send('Input.dispatchTouchEvent',{'type':'touchEnd','touchPoints':[]})
        ids=[s['id'] for s in self.project()['map']['sections']]
        self.assertEqual(ids,['s1','s2','s0'])
        self.assertEqual(self.project()['map']['sectionData']['s0']['parking'],'Note s0')
        self.assertEqual(self.project()['map']['timeline']['presence'][0]['id'],'r1')
        self.assertIsNone(self.project()['map']['timeline']['presence'][0]['end'])
        self.assertEqual(self.project()['map']['timeline']['presence'][0]['start']['sectionId'],'s1')
        self.assertFalse(self.project()['skeleton']['session']['markers']['s1'])

    def test_sliding_collapsed_cues_fixed_order_history_and_reduced_motion(self):
        for width,reduced in [(390,False),(820,True)]:
            with self.subTest(width=width,reduced=reduced):
                self.open(width=width,reduced=reduced);self.select()
                self.click('toggle-timeline-track','[data-track-id="t1"]')
                self.assertEqual(self.page.locator('.track-detail').count(),0)
                self.assertGreater(self.page.locator('.change-range').count(),0)
                self.assertEqual(self.page.locator('.timeline-row').evaluate_all('(els)=>els.map(e=>e.dataset.trackRow)'),['t1','t2'])
                self.click('next-section');expect(self.page.locator('.section-tab.current')).to_have_text('Verse')
                self.assertEqual(self.page.locator('.timeline-row.expanded').count(),0)
                self.assertEqual(self.page.locator('.presence-segment.continue-in.continue-out').count(),1)
                self.assertEqual(self.page.evaluate('history.state.fromRoute'),'tracks')
                self.assertLessEqual(self.page.evaluate('document.documentElement.scrollWidth'),width)
                self.context.close()

    def test_touch_targets(self):
        self.open();self.select();self.click('select-event','[data-event-id="e1"]')
        for selector in ['.presence-hit','.change-marker','.event-handle','.mini-btn','.mix-toggle']:
            for box in self.page.locator(selector+':visible').all():
                size=box.bounding_box()
                self.assertGreaterEqual(size['height'],44,selector)
                self.assertGreaterEqual(size['width'],44,selector)

    def test_import_v4_backup_uses_same_migration(self):
        self.open('project');self.click('settings')
        self.page.locator('#importFile').set_input_files({'name':'v4.json','mimeType':'application/json',
                                                        'buffer':json.dumps(fixture()).encode()})
        expect(self.page.locator('h1')).to_have_text('Projects')
        self.assertEqual(self.db()['version'],5)
        self.assertEqual(self.event('e2')['point']['bar'],2.5)
        self.assertEqual(self.event('cue')['label'],'Transition cue')


    def test_browser_back_tracks_the_entry_route_after_section_slides(self):
        self.open('map')
        self.click('go','[data-route="structure"]')
        self.click('go','[data-route="tracks"]')
        self.click('start-section-study')
        self.click('next-section');expect(self.page.locator('.section-tab.current')).to_have_text('Verse')
        self.click('history-back');expect(self.page.locator('h1')).to_have_text('Tracks')
        self.click('history-back');expect(self.page.locator('h1')).to_have_text('Structure')
        self.page.go_back();expect(self.page.locator('[data-route="structure"]')).to_be_visible()

    def test_finite_cross_section_reorder_remove_preserves_unaffected_coverage_and_ids(self):
        data=fixture();timeline=data['projects'][0]['map']['timeline']
        timeline['presence'][0]['end']={'sectionId':'s1','bar':'end'}
        timeline['events'][0]['end']={'sectionId':'s1','bar':4}
        self.open('structure',data=data)
        self.page.locator('[data-section-id="s0"] [data-drag-handle]').focus()
        self.page.keyboard.press('ArrowDown');self.page.keyboard.press('ArrowDown')
        p=self.project();ranges=p['map']['timeline']['presence']
        self.assertEqual([x['id'] for x in p['map']['sections']],['s1','s2','s0'])
        self.assertEqual({r['start']['sectionId'] for r in ranges},{'s1','s0'})
        self.assertIn('r1',[r['id'] for r in ranges])
        self.assertNotIn('s2',{r['start']['sectionId'] for r in ranges})
        surviving_id=next(r['id'] for r in ranges if r['start']['sectionId']=='s0')
        self.click('delete-section','[data-id="s1"]')
        p=self.project();ranges=p['map']['timeline']['presence']
        self.assertEqual(len(ranges),1)
        self.assertEqual(ranges[0]['id'],surviving_id)
        self.assertEqual(ranges[0]['start']['sectionId'],'s0')
        self.assertEqual(p['map']['sectionData']['s0']['parking'],'Note s0')
        self.assertFalse(any('_sourceId' in r for r in ranges))

    def test_quiet_mix_creation_and_legacy_cue_removal_with_undo(self):
        self.open();self.click('toggle-timeline-track','[data-track-id="__mix__"]')
        self.add_change('Louder','mix')
        event=next(e for e in self.project()['map']['timeline']['events'] if e['label']=='Louder')
        self.assertEqual(event['targetType'],'mix')
        self.click('next-section');expect(self.page.locator('.section-tab.current')).to_have_text('Verse')
        self.click('toggle-timeline-track','[data-track-id="__mix__"]')
        self.click('select-event','[data-event-id="cue"]')
        self.click('remove-selected','[data-kind="event"]')
        self.assertFalse(any(e['id']=='cue' for e in self.project()['map']['timeline']['events']))
        self.page.locator('#undoEdit').click();self.assertEqual(self.event('cue')['label'],'Transition cue')

    def test_legacy_storage_and_narrow_layout(self):
        self.open('projects',width=320,data=fixture())
        self.page.evaluate("localStorage.removeItem('production-projects-v1');localStorage.setItem('smithereens-map-v6',JSON.stringify({sections:[{id:'legacy-a',name:'Intro',lengthBars:8}],ingredients:['Vocal'],analysis:{'legacy-a':{parts:['Vocal'],parking:'Do not lose'}}}))")
        self.page.reload()
        db=self.db();self.assertEqual(db['version'],5)
        self.assertEqual(db['projects'][0]['map']['sections'][0]['id'],'legacy-a')
        self.assertEqual(db['projects'][0]['map']['sectionData']['legacy-a']['parking'],'Do not lose')
        self.assertEqual(len(db['projects'][0]['map']['timeline']['presence']),1)
        self.assertLessEqual(self.page.evaluate('document.documentElement.scrollWidth'),320)


    def test_empty_projects_remain_empty_and_malformed_import_cannot_replace_data(self):
        self.open('project');self.click('settings');before=self.db()
        self.page.once('dialog',lambda d:d.accept())
        self.page.locator('#importFile').set_input_files({'name':'bad.json','mimeType':'application/json','buffer':b'{"unexpected":true}'})
        self.assertEqual(self.db(),before)
        self.page.evaluate("localStorage.setItem('production-projects-v1',JSON.stringify({version:4,currentProjectId:null,projects:[]}));history.replaceState({route:'projects'},'')")
        self.page.reload();expect(self.page.locator('h1')).to_have_text('Projects')
        self.assertEqual(self.db()['projects'],[])


    def test_short_presence_blocks_select_remove_merge_and_undo(self):
        data=fixture();timeline=data['projects'][0]['map']['timeline']
        timeline['presence']=[{'id':'r1','trackId':'t1','start':{'sectionId':'s0','bar':0},'end':{'sectionId':'s0','bar':1}},
                              {'id':'r2','trackId':'t1','start':{'sectionId':'s0','bar':2},'end':None}]
        self.open(data=data);self.select()
        expect(self.page.locator('.presence-hit')).to_have_count(2)
        target=self.page.locator('.presence-hit[data-range-id="r2"]')
        box=target.bounding_box();self.assertGreaterEqual(box['height'],44)
        target.click()
        self.assertEqual(self.page.locator('[data-presence-handle][data-edge="start"]').get_attribute('data-range-id'),'r2')
        self.click('remove-selected','[data-kind="presence"][data-id="r2"]')
        self.assertEqual([r['id'] for r in self.project()['map']['timeline']['presence']],['r1'])
        self.page.locator('#undoEdit').click()
        self.assertEqual({r['id'] for r in self.project()['map']['timeline']['presence']},{'r1','r2'})
        self.page.locator('.presence-hit[data-range-id="r2"]').click()
        self.place('start',1)
        self.assertEqual([r['id'] for r in self.project()['map']['timeline']['presence']],['r1'])
        self.assertEqual(self.page.locator('[data-presence-handle][data-edge="start"]').get_attribute('data-range-id'),'r1')

    def complete_fixture(self):
        data=fixture()
        data['projects'][0]['map']['timeline']['presence'].append(
            {'id':'bass','trackId':'t2','start':{'sectionId':'s0','bar':0},'end':None})
        return data

    def test_live_bpm_validation_progress_caret_and_route_guards(self):
        self.open('map', data=self.complete_fixture());self.expand_map_setup()
        inp=self.page.locator('#tempoInput'); inp.focus()
        original=self.project()['skeleton']
        for value,valid in [('',False),(' ',False),('abc',False),('Infinity',False),('0',False),('-2',False),('120.5',True),('1.',True),('1..2',False),('120',True)]:
            inp.fill(value)
            expect(inp).to_be_focused()
            self.assertEqual(self.project()['map']['setup']['tempo'],value)
            self.assertEqual(self.page.locator('[data-route="structure"]').is_enabled(),valid)
            expect(self.page.locator('.checkpoint-count')).to_have_text('3 of 3' if valid else '0 of 3')
            self.assertEqual(self.project()['skeleton'],original)
        # Guard history restoration even if stored completion records are true.
        inp.fill('')
        self.page.evaluate("history.pushState({route:'skeleton-bounce',projectId:'p1'},'');dispatchEvent(new PopStateEvent('popstate',{state:history.state}))")
        expect(self.page.locator('h1')).to_have_text('The Map')
        self.assertEqual(self.page.evaluate('history.state.route'),'map')
        self.assertEqual(self.project()['skeleton'],original)
        inp.fill('128.25');self.click('go','[data-route="structure"]')
        expect(self.page.locator('h1')).to_have_text('Structure')

    def test_each_setup_prerequisite_locks_and_restores_without_losing_work(self):
        self.open('map', data=self.complete_fixture()); original=self.project()['skeleton']
        for field in ['reference','grid','firstListen']:
            self.expand_map_setup()
            self.click('toggle-setup',f'[data-field="{field}"]')
            self.assertEqual(self.page.locator('[data-route="structure"]').count(),0)
            expect(self.page.locator('.checkpoint-locked-message')).to_have_text('Available after Song Setup')
            expect(self.page.locator('.checkpoint-count')).to_have_text('0 of 3')
            self.click('toggle-setup',f'[data-field="{field}"]')
            expect(self.page.locator('[data-route="structure"]')).to_be_enabled()
            expect(self.page.locator('.checkpoint-count')).to_have_text('3 of 3')
            self.assertEqual(self.project()['skeleton'],original)
        self.expand_map_setup()
        self.page.locator('#meterInput').evaluate("el=>{el.add(new Option('Choose',''));el.value='';el.dispatchEvent(new Event('change',{bubbles:true}))}")
        self.assertEqual(self.page.locator('[data-route="structure"]').count(),0)
        expect(self.page.locator('.checkpoint-locked-message')).to_have_text('Available after Song Setup')
        self.page.locator('#meterInput').select_option('3/4')
        expect(self.page.locator('[data-route="structure"]')).to_be_enabled()

    def test_sheet_selection_preserves_nodes_geometry_focus_and_edit_keyboard(self):
        self.open('structure');self.click('edit-section','[data-section-id="s0"]')
        self.assertNotEqual(self.page.evaluate('document.activeElement.tagName'),'INPUT')
        expect(self.page.locator('#sheetRoot')).to_have_attribute('role','dialog')
        self.click('close-sheet');self.click('open-add-section')
        self.page.evaluate("window.originalChoice=document.querySelector('[data-name=Verse]');window.originalSheet=document.querySelector('.section-builder')")
        verse=self.page.locator('[data-name="Verse"]')
        self.page.locator('.sheet').evaluate('async el=>{await Promise.all(el.getAnimations().map(a=>a.finished))}')
        before=verse.bounding_box()
        self.click('choose-section-type','[data-name="Verse"]')
        self.click('set-new-section-bars','[data-bars="12"]')
        self.assertTrue(self.page.evaluate("window.originalChoice===document.querySelector('[data-name=Verse]') && window.originalSheet===document.querySelector('.section-builder')"))
        self.assertEqual(verse.bounding_box(),before)
        self.assertNotEqual(self.page.evaluate('document.activeElement.tagName'),'INPUT')
        self.page.keyboard.press('Escape');expect(self.page.locator('#sheetRoot')).to_have_attribute('aria-hidden','true')
        expect(self.page.locator('[data-action="open-add-section"]')).to_be_focused()

    def test_tracks_and_feel_selection_keep_geometry_and_focus(self):
        self.open('tracks');choice=self.page.locator('[data-name="Guitar"]');before=choice.bounding_box()
        choice.click();expect(choice).to_be_focused();self.assertEqual(choice.bounding_box(),before)
        self.click('start-section-study')
        choice=self.page.locator('[data-scale="depth"][data-value="Distant"]');before=choice.bounding_box()
        choice.click();expect(choice).to_be_focused();self.assertEqual(choice.bounding_box(),before)
        expect(choice).to_have_attribute('aria-pressed','true')

    def test_draft_inline_progress_history_and_legacy_route(self):
        self.open('skeleton-draft',data=self.complete_fixture())
        expect(self.page.locator('h2')).to_have_text('Draft')
        self.assertEqual(self.page.locator('[data-draft-section]').count(),3)
        before=self.page.evaluate('history.length')
        for sid in ['s0','s1']:
            self.page.locator(f'[data-draft-section="{sid}"] > summary').click()
        self.click('toggle-draft-part','[data-section-id="s0"][data-track-id="t1"]')
        expect(self.page.locator('#draftCoverage')).to_contain_text('5 of 6 mapped parts')
        self.assertEqual(self.page.evaluate('history.length'),before)
        self.assertTrue(self.page.locator('[data-draft-section="s1"]').evaluate('el=>el.open'))
        expect(self.page.locator('[data-route="skeleton-bounce"]')).to_be_disabled()
        self.click('toggle-draft-part','[data-section-id="s0"][data-track-id="t1"]')
        self.click('go','[data-route="skeleton-bounce"]')
        expect(self.page.locator('h2')).to_have_text('Bounce')
        expect(self.page.locator('[data-route="roadmap"]')).to_have_text('View Roadmap')
        self.click('history-back');expect(self.page.locator('h2')).to_have_text('Draft')
        self.page.evaluate("history.replaceState({route:'draft-section',projectId:'p1',sectionIndex:2},'')")
        self.page.reload()
        expect(self.page.locator('h2')).to_have_text('Draft')
        self.assertTrue(self.page.locator('[data-draft-section="s2"]').evaluate('el=>el.open'))
        self.assertEqual(self.page.evaluate('history.state.route'),'skeleton-draft')

    def test_dependency_completion_and_restored_future_routes(self):
        cases=[('structureVerified',False,'structure'),('mapVerified',False,'section-study'),('teachBack',False,'section-study')]
        for field,value,expected in cases:
            with self.subTest(field=field):
                data=self.complete_fixture();data['projects'][0]['map'][field]=value
                self.open('skeleton-bounce',data=data)
                self.assertEqual(self.page.evaluate('history.state.route'),expected)
                self.assertTrue(self.project()['skeleton']['bounce']['listened'])
                self.context.close()
        data=self.complete_fixture();data['projects'][0]['skeleton']['session']['tracks']['t1']=False
        self.open('skeleton-bounce',data=data)
        expect(self.page.locator('h2')).to_have_text('Session')
        self.click('toggle-session-track','[data-track-id="t1"]')
        self.click('go','[data-route="skeleton-draft"]')
        self.assertTrue(self.project()['skeleton']['draft']['parts']['s0']['t1'])
        self.page.evaluate("history.pushState({route:'sounds',projectId:'p1'},'');dispatchEvent(new PopStateEvent('popstate',{state:history.state}))")
        expect(self.page.locator('h2')).to_have_text('Roadmap')
        self.assertEqual(self.page.locator('.road-phase.unimplemented').count(),5)
        self.assertEqual(self.page.locator('.road-phase.unimplemented[data-action]').count(),0)

    def test_parent_pills_and_back_follow_distinct_destinations(self):
        self.open('map');self.click('go','[data-route="tracks"]');self.click('start-section-study')
        self.click('history-back');expect(self.page.locator('h1')).to_have_text('Tracks')
        self.page.go_forward();expect(self.page.locator('.study-pane')).to_be_visible()
        self.page.locator('.phase-pill').click();expect(self.page.locator('h1')).to_have_text('The Map')
        self.assertEqual(self.page.locator('.phase-pill').count(),0)
        self.canvas_route('project');expect(self.page.locator('h1')).to_have_text('Migration song')
        self.click('go','[data-route="roadmap"]');expect(self.page.locator('h2')).to_have_text('Roadmap')
        self.context.close()
        self.open('skeleton',data=self.complete_fixture());self.click('go','[data-route="skeleton-session"]')
        self.click('history-back');expect(self.page.locator('h2')).to_have_text('The Skeleton')
        self.click('go','[data-route="skeleton-session"]');self.click('go','[data-route="skeleton-draft"]')
        self.click('history-back');expect(self.page.locator('h2')).to_have_text('Session')

    def test_boundary_truth_across_viewports_and_selection_cancel_noop(self):
        self.open();self.select()
        self.assertEqual(self.page.locator('[data-presence-handle]:not([data-open-tail])').count(),1)
        self.assertEqual(self.page.locator('.presence-segment.real-stop').count(),0)
        original=self.db();self.tap_handle(self.page.locator('[data-open-tail]'))
        self.page.keyboard.press('Escape');self.assertEqual(self.db(),original)
        self.place('start',0);self.assertEqual(self.db(),original)
        self.assertTrue(self.page.locator('#undoNotice').is_hidden())
        self.click('next-section');expect(self.page.locator('.section-tab.current')).to_have_text('Verse')
        self.select();self.assertEqual(self.page.locator('[data-presence-handle]:not([data-open-tail])').count(),0)
        self.place('end',4)
        self.assertEqual(self.project()['map']['timeline']['presence'][0]['end'],{'sectionId':'s1','bar':4})
        self.touch_drag(self.page.locator('[data-presence-handle][data-edge="end"]'), .75)
        self.assertEqual(self.project()['map']['timeline']['presence'][0]['end']['bar'],6)

    def test_newer_edits_retire_undo_and_notes_do_not_invalidate(self):
        self.open();self.select();self.place('end',4)
        expect(self.page.locator('#undoNotice')).to_be_visible()
        self.page.locator('.note-disclosure summary').click()
        self.page.locator('[data-input="section-parking"]').fill('Newer note')
        expect(self.page.locator('#undoNotice')).to_be_hidden()
        self.assertEqual(self.project()['map']['timeline']['presence'][0]['end']['bar'],4)
        self.assertEqual(self.project()['map']['sectionData']['s0']['parking'],'Newer note')

    def test_responsive_text_enlargement_and_no_press_scale(self):
        for width,height in [(320,740),(390,844),(820,1180),(1180,820)]:
            with self.subTest(width=width):
                data=self.complete_fixture();data['projects'][0]['map']['tracks'][0]['name']='A very long custom instrument name with harmonies'
                self.open(width=width,data=data,reduced=True)
                self.page.set_viewport_size({'width':width,'height':height})
                self.page.add_style_tag(content='body {font-size:21px}')
                self.assertLessEqual(self.page.evaluate('document.documentElement.scrollWidth'),width)
                self.select();button=self.page.locator('[data-action="remove-selected"][data-kind="presence"]').first
                box=button.bounding_box();button.dispatch_event('pointerdown')
                self.assertEqual(button.bounding_box(),box)
                self.assertEqual(self.page.evaluate("matchMedia('(prefers-reduced-motion: reduce)').matches"),True)
                self.context.close()

    def test_projects_navigation_shell_and_new_project_keyboard_flow(self):
        for width in [320, 390, 430, 820, 1180]:
            with self.subTest(width=width):
                self.open('projects', width=width, pointer=width >= 1180)
                self.assertLessEqual(self.page.evaluate('document.documentElement.scrollWidth'), width)
                self.assertEqual(self.page.locator('.topbar').count(), 1)
                self.assertEqual(self.page.locator('.pill-tag').count(), 0)
                add = self.page.locator('.topbar .right [data-action="new-project"]')
                box = add.bounding_box()
                self.assertGreaterEqual(box['width'], 44)
                self.assertGreaterEqual(box['height'], 44)
                card = self.page.locator('.project-card').first.bounding_box()
                shell = self.page.locator('.project-page').bounding_box()
                toolbar = self.page.locator('.topbar').bounding_box()
                title = self.page.locator('.page-heading h1').bounding_box()
                subtitle = self.page.locator('.page-heading .sub').bounding_box()
                self.assertLessEqual(card['height'], 140)
                self.assertLess(abs((box['x'] + box['width']) - (card['x'] + card['width'])), 1.1)
                self.assertLess(abs(shell['x'] - card['x']), 1.1)
                self.assertLess(abs((shell['x'] + shell['width']) - (card['x'] + card['width'])), 1.1)
                self.assertLess(abs(toolbar['x'] - shell['x']), 1.1)
                self.assertLess(abs(toolbar['width'] - shell['width']), 1.1)
                self.assertEqual(self.page.locator('.project-menu').first.text_content().strip(), '…')
                self.assertEqual(self.page.locator('.project-open .foot > span:last-child').first.text_content().strip(), '›')

                self.click('new-project')
                expect(self.page.locator('.page-heading h1')).to_have_text('New project')
                self.assertEqual(self.page.locator('.topbar .left [data-action="history-back"]').count(), 1)
                self.assertEqual(self.page.locator('.topbar [data-action="new-project"]').count(), 0)
                self.assertEqual(self.page.locator('.project-page.route-forward').count(), 1)
                self.assertTrue(self.page.locator('.project-page.route-forward').evaluate('el=>el.getAnimations().every(a=>a.effect.getKeyframes().every(k=>!k.transform || k.transform==="none"))'))
                self.page.locator('.project-page').evaluate('async el=>{await Promise.all(el.getAnimations().map(a=>a.finished))}')
                new_shell = self.page.locator('.project-page').bounding_box()
                new_toolbar = self.page.locator('.topbar').bounding_box()
                new_title = self.page.locator('.page-heading h1').bounding_box()
                new_subtitle = self.page.locator('.page-heading .sub').bounding_box()
                segmented = self.page.locator('.project-type-control').bounding_box()
                self.assertLess(abs(new_shell['x'] - shell['x']), 1.1)
                self.assertLess(abs(new_shell['width'] - shell['width']), 1.1)
                self.assertLess(abs(new_toolbar['x'] - toolbar['x']), 1.1)
                self.assertLess(abs(new_toolbar['width'] - toolbar['width']), 1.1)
                self.assertLess(abs(new_title['y'] - title['y']), 1.1)
                self.assertLess(abs(new_subtitle['y'] - subtitle['y']), 1.1)
                self.assertLess(abs(segmented['y'] - card['y']), 1.1)
                if width >= 1180:
                    self.assertLessEqual(shell['width'], 760.1)
                    self.assertLessEqual(card['width'], 760.1)

                self.page.locator('[data-action="history-back"]').click()
                expect(self.page.locator('.page-heading h1')).to_have_text('Projects')
                self.assertEqual(self.page.locator('.project-page.route-back').count(), 1)
                self.context.close()

        self.open('projects', width=390, data={'version':5,'currentProjectId':None,'projects':[]})
        self.assertEqual(self.page.locator('.empty').count(), 0)
        self.assertEqual(self.page.get_by_text('No projects yet. Tap + to start one.').count(), 0)
        self.context.close()

        self.open('projects', width=390)
        self.click('new-project')
        self.assertEqual(self.page.locator('.topbar .center .pill-tag').count(), 0)
        segments = self.page.locator('.project-type-control .segment-choice')
        self.assertEqual(segments.count(), 2)
        for i in range(segments.count()):
            self.assertGreaterEqual(segments.nth(i).bounding_box()['height'], 44)
        self.assertEqual(self.page.locator('#newTypeDescription').count(), 0)
        self.assertEqual(self.page.get_by_text('Start with anything worth keeping.').count(), 0)
        self.click('set-new-type', '[data-type="study"]')
        self.assertEqual(self.page.get_by_text('Rebuild an existing song to learn how it works.').count(), 0)
        title = self.page.locator('#newTitle')
        artist = self.page.locator('#newArtist')
        self.assertEqual(title.get_attribute('enterkeyhint'), 'next')
        self.assertEqual(artist.get_attribute('enterkeyhint'), 'done')
        self.assertEqual(title.get_attribute('autocapitalize'), 'words')
        self.assertEqual(artist.get_attribute('autocapitalize'), 'words')
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

    def test_revisioned_assets_and_development_stamp(self):
        self.open('projects')
        stamp=self.page.locator('#buildStamp')
        expect(stamp).to_have_text(__import__('re').compile(r'FIRE V6 DEV · [0-9a-f]{7}'))
        revision=self.page.request.get(URL+'/build-info.json').json()['commit']
        self.assertIn('?v='+revision,self.page.locator('script[src]').get_attribute('src'))
        self.assertIn('?v='+revision,self.page.locator('link[rel="stylesheet"]').get_attribute('href'))

    def test_real_stop_touch_cancel_and_resize_restore_canonical_data(self):
        self.open();self.select();self.place('end',4)
        before=self.db()
        self.touch_drag(self.page.locator('[data-presence-handle][data-edge="end"]'), .75, cancel=True)
        self.assertEqual(self.db(),before)
        handle=self.page.locator('[data-presence-handle][data-edge="end"]');handle.scroll_into_view_if_needed()
        box=handle.bounding_box();self.page.mouse.move(box['x']+22,box['y']+22);self.page.mouse.down()
        self.page.mouse.move(box['x']+42,box['y']+22)
        self.page.set_viewport_size({'width':390 if self.page.viewport_size['width']==820 else 820,'height':1000});self.page.mouse.up()
        self.assertEqual(self.db(),before)
        self.assertFalse(self.page.locator('body').evaluate('el=>el.classList.contains("is-dragging")'))

    def test_each_change_taxonomy_action_is_immediate_and_undoable(self):
        self.open();self.select()
        for label in ['Widens','Narrows','Louder','Softer','Doubles','Pattern shift','Register shift','Effect shift']:
            before=self.db();self.add_change(label)
            self.assertTrue(any(e['label']==label for e in self.project()['map']['timeline']['events']))
            expect(self.page.locator('#sheetRoot')).to_have_attribute('aria-hidden','true')
            self.page.locator('#undoEdit').click();self.assertEqual(self.db(),before)

    def test_draft_silent_section_and_current_requirements(self):
        data=self.complete_fixture();p=data['projects'][0]
        p['map']['timeline']['presence'][0]['end']={'sectionId':'s1','bar':'end'}
        p['map']['timeline']['presence'][1]['end']={'sectionId':'s1','bar':'end'}
        p['map']['sectionData']['s2']['silence']=True
        p['map']['sectionData']['s2']['focusState']='none';p['map']['sectionData']['s2']['focusIds']=[]
        self.open('skeleton-draft',data=data)
        expect(self.page.locator('#draftCoverage')).to_have_text('4 of 4 mapped parts · 3 of 3 sections')
        expect(self.page.locator('[data-draft-section="s2"] summary')).to_contain_text('No active tracks · Complete')
        expect(self.page.locator('[data-route="skeleton-bounce"]')).to_be_enabled()

    def canvas_fixture(self):
        data=self.complete_fixture();p=data['projects'][0]
        for i in range(3,8):
            sid=f's{i}'
            p['map']['sections'].append({'id':sid,'name':f'Chorus variation {i}','lengthBars':8})
            p['map']['sectionData'][sid]=json.loads(json.dumps(p['map']['sectionData']['s0']))
            p['skeleton']['session']['markers'][sid]=True
            p['skeleton']['draft']['parts'][sid]={'t1':True,'t2':True}
        return data

    def canvas_route(self, route):
        self.page.evaluate("route=>{history.pushState({route,projectId:'p1'},'');dispatchEvent(new PopStateEvent('popstate',{state:history.state}))}",route)

    def settled_sheet(self):
        self.page.locator('.sheet').evaluate('async el=>{await Promise.all(el.getAnimations().map(a=>a.finished))}')

    def test_new_project_fields_persist_and_original_stores_artist(self):
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

    def test_cross_platform_screen_canvases_and_fluid_widths(self):
        routes=['projects','new-project','project','roadmap','map','structure','tracks','section-study',
                'map-summary','skeleton','skeleton-session','skeleton-draft','skeleton-bounce','notes']
        for width in [320,390,820,1180,1440,1728,1920]:
            with self.subTest(width=width):
                self.open('projects',width=width,data=self.canvas_fixture(),pointer=width>=1180)
                for route in routes:
                    with self.subTest(route=route):
                        self.canvas_route(route)
                        self.assertEqual(self.page.evaluate('history.state.route'),route)
                        self.assertLessEqual(self.page.evaluate('document.documentElement.scrollWidth'),width)
                        self.assertGreater(self.page.locator('#app').bounding_box()['width'],width*.8 if width<1000 else 600)
                        if route in ['skeleton-bounce','skeleton']:
                            self.assertLessEqual(self.page.locator('#app').bounding_box()['width'],760)
                        if route=='new-project':
                            self.assertLessEqual(self.page.locator('#app').bounding_box()['width'],880)
                        if route=='section-study':
                            self.select()
                            self.assertEqual(self.page.locator('.presence-segment.real-stop').count(),0)
                            lane=self.page.locator('.timeline-lane').first.bounding_box()
                            self.assertGreater(lane['width'],width*.5 if width>=1440 else 100)
                            arrangement=self.page.locator('.arrangement-region').bounding_box()
                            observations=self.page.locator('.study-observations').bounding_box()
                            self.assertEqual(observations['x']>arrangement['x']+arrangement['width'],width>=1100)
                        if route=='skeleton-draft':
                            a=self.page.locator('[data-draft-section="s0"]').bounding_box()
                            b=self.page.locator('[data-draft-section="s1"]').bounding_box()
                            self.assertEqual(b['x']>a['x'],width>=900)
                # All editing panels remain contained/reachable at the same widths.
                self.canvas_route('structure')
                for action,extra in [('open-add-section',''),('edit-section','[data-section-id="s0"]')]:
                    self.click(action,extra);self.settled_sheet()
                    box=self.page.locator('.sheet').bounding_box()
                    self.assertGreaterEqual(box['x'],0);self.assertLessEqual(box['x']+box['width'],width)
                    self.assertGreaterEqual(box['y'],0)
                    self.assertNotEqual(self.page.evaluate('document.activeElement.tagName'),'INPUT')
                    if width>=1100:
                        self.assertGreater(box['y'],20)
                        self.assertLess(abs(box['x']+box['width']/2-width/2),1)
                    self.page.keyboard.press('Escape')
                self.canvas_route('section-study');self.select();self.click('open-add-change')
                self.settled_sheet();self.assertEqual(self.page.locator('[data-action="choose-change"]').count(),8)
                self.page.keyboard.press('Escape');self.context.close()
        # Intermediate widths use the same fluid canvas rather than device-specific widths.
        self.open(width=1000,data=self.canvas_fixture(),pointer=True)
        previous=0
        for width in [1000,1099,1100,1280,1600,1800]:
            self.page.set_viewport_size({'width':width,'height':1000})
            current=self.page.locator('#app').bounding_box()['width']
            self.assertGreater(current,previous);previous=current
            self.assertLessEqual(self.page.evaluate('document.documentElement.scrollWidth'),width)

    def assert_hover_stable(self, locator):
        locator.scroll_into_view_if_needed();before=locator.bounding_box()
        locator.hover()
        self.assertEqual(locator.bounding_box(),before)
        self.assertNotEqual(locator.evaluate('el=>getComputedStyle(el).cursor'),'default')

    def test_mouse_hover_click_and_sheet_keyboard_focus(self):
        for width in [1180,1440,1728]:
            with self.subTest(width=width):
                self.open('projects',width=width,data=self.canvas_fixture(),pointer=True)
                self.assertTrue(self.page.evaluate("matchMedia('(hover:hover) and (pointer:fine)').matches"))
                self.assert_hover_stable(self.page.locator('.project-open').first)
                self.assert_hover_stable(self.page.locator('.project-menu').first)
                self.click('project-menu','[data-id="p1"]');self.settled_sheet()
                self.page.keyboard.press('Tab');expect(self.page.locator('[data-action="delete-project"]')).to_be_focused()
                self.page.keyboard.press('Shift+Tab');expect(self.page.locator('[data-action="close-sheet"]')).to_be_focused()
                self.page.keyboard.press('Escape');expect(self.page.locator('.project-menu').first).to_be_focused()
                self.click('open-project','[data-id="p1"]');self.page.locator('.quick-card[data-route="roadmap"]').click();self.click('go','[data-route="map"]');self.expand_map_setup()
                self.page.locator('#tempoInput').fill('128.5');expect(self.page.locator('#tempoInput')).to_be_focused()
                self.click('go','[data-route="structure"]');self.click('open-add-section');self.settled_sheet()
                self.assert_hover_stable(self.page.locator('[data-name="Verse"]'))
                self.click('choose-section-type','[data-name="Verse"]')
                self.assert_hover_stable(self.page.locator('[data-bars="8"]'))
                self.click('set-new-section-bars','[data-bars="8"]')
                self.page.keyboard.press('Escape')
                self.assertEqual(self.project()['map']['setup']['tempo'],'128.5')
                self.context.close()

    def test_mouse_arrangement_placement_boundary_drag_cancel_and_undo(self):
        for width in [1180,1440,1728]:
            with self.subTest(width=width):
                self.open(width=width,data=self.canvas_fixture(),pointer=True);self.select()
                self.assert_hover_stable(self.page.locator('[data-presence-handle][data-edge="start"]'))
                self.place('end',4)
                self.assertEqual(next(r for r in self.project()['map']['timeline']['presence'] if r['id']=='r1')['end']['bar'],4)
                handle=self.page.locator('[data-presence-handle][data-edge="end"]')
                handle.scroll_into_view_if_needed();box=handle.bounding_box();lane=handle.locator('xpath=..').bounding_box()
                self.page.mouse.move(box['x']+22,box['y']+22);self.page.mouse.down()
                self.page.mouse.move(lane['x']+lane['width']*.75,box['y']+22,steps=8);self.page.mouse.up()
                self.assertEqual(next(r for r in self.project()['map']['timeline']['presence'] if r['id']=='r1')['end']['bar'],6)
                before=self.db()
                handle=self.page.locator('[data-presence-handle][data-edge="end"]');box=handle.bounding_box()
                self.page.mouse.move(box['x']+22,box['y']+22);self.page.mouse.down()
                self.page.mouse.move(lane['x']+lane['width']*.5,box['y']+22,steps=4)
                # Native capture loss represents OS/browser interruption of the mouse gesture.
                handle.evaluate('el=>el.releasePointerCapture(1)')
                self.page.mouse.move(lane['x']+lane['width']*.4,box['y']+22);self.page.mouse.up()
                self.assertEqual(self.db(),before)
                self.assertFalse(self.page.locator('body').evaluate('el=>el.classList.contains("is-dragging")'))
                self.page.locator('#undoEdit').click()
                self.assertEqual(next(r for r in self.project()['map']['timeline']['presence'] if r['id']=='r1')['end']['bar'],4)
                self.context.close()

    def test_desktop_disclosure_click_activation_and_wheel_scrolling(self):
        self.open('skeleton-draft',width=1440,data=self.canvas_fixture(),pointer=True)
        summary=self.page.locator('[data-draft-section="s0"] summary');self.assert_hover_stable(summary)
        history_length=self.page.evaluate('history.length');summary.click()
        self.click('toggle-draft-part','[data-section-id="s0"][data-track-id="t1"]')
        expect(self.page.locator('#draftCoverage')).to_contain_text('15 of 16 mapped parts')
        self.assertEqual(self.page.evaluate('history.length'),history_length)
        summary.focus();self.page.keyboard.press('Space')
        self.assertNotEqual(summary.evaluate('el=>getComputedStyle(el).outlineStyle'),'none')
        self.assertFalse(self.page.locator('[data-draft-section="s0"]').evaluate('el=>el.open'))
        self.page.keyboard.press('Enter')
        self.assertTrue(self.page.locator('[data-draft-section="s0"]').evaluate('el=>el.open'))
        self.canvas_route('notes');self.page.set_viewport_size({'width':1440,'height':520})
        self.page.mouse.move(700,350);self.page.mouse.wheel(0,700)
        self.page.wait_for_function('scrollY>0')
        self.canvas_route('structure');self.click('open-add-section');self.settled_sheet()
        sheet=self.page.locator('.sheet');box=sheet.bounding_box();page_scroll=self.page.evaluate('scrollY')
        self.page.mouse.move(box['x']+box['width']/2,box['y']+box['height']/2)
        self.page.mouse.wheel(0,500)
        self.page.wait_for_function('document.querySelector(".sheet").scrollTop>0')
        self.assertEqual(self.page.evaluate('scrollY'),page_scroll)
        self.page.keyboard.press('Escape')
        self.page.set_viewport_size({'width':768,'height':700})
        self.canvas_route('section-study')
        nav=self.page.locator('.horizontal-nav');box=nav.bounding_box()
        self.page.mouse.move(box['x']+box['width']/2,box['y']+box['height']/2)
        self.page.mouse.wheel(600,0)
        self.page.wait_for_function('document.querySelector(".horizontal-nav").scrollLeft>0')

    def test_repeated_builder_commits_keeps_geometry_and_blocks_double_submit(self):
        for width in [320,390,820,1180,1440,1728,1920]:
            with self.subTest(width=width):
                self.open('structure',width=width,pointer=width>=1180)
                old=self.project();initial=len(old['map']['sections'])
                self.click('open-add-section');self.settled_sheet()
                self.assertNotEqual(self.page.evaluate('document.activeElement.tagName'),'INPUT')
                self.page.evaluate('window.builderNode=document.querySelector(".section-builder")')
                for count,(name,bars) in enumerate([('Intro',4),('Verse',8),('Chorus',8),('Outro',4)],1):
                    self.click('choose-section-type',f'[data-name="{name}"]')
                    self.click('set-new-section-bars',f'[data-bars="{bars}"]')
                    button=self.page.locator('[data-action="save-new-section"]');box=button.bounding_box()
                    button.dblclick()
                    self.assertEqual(len(self.project()['map']['sections']),initial+count)
                    self.assertEqual(button.bounding_box(),box)
                    expect(button).to_be_disabled()
                    expect(self.page.locator('#builderStatus')).to_have_text(f'Added {name} · {bars} bars')
                    expect(self.page.locator(f'[data-bars="{bars}"]')).to_have_attribute('aria-pressed','true')
                    self.assertTrue(self.page.evaluate('window.builderNode===document.querySelector(".section-builder")'))
                    expect(self.page.locator('#sheetRoot')).to_have_attribute('aria-hidden','false')
                self.assertEqual(self.project()['map']['sections'][:initial],old['map']['sections'])
                self.assertEqual(self.project()['map']['sectionData']['s0'],old['map']['sectionData']['s0'])
                self.assertEqual(self.project()['notes'],old['notes'])
                self.assertEqual(len({x['id'] for x in self.project()['map']['sections']}),initial+4)
                expect(self.page.locator('[data-action="close-sheet"]')).to_have_text('Done')
                self.click('close-sheet');expect(self.page.locator('[data-action="open-add-section"]')).to_be_focused()
                self.page.reload();self.assertEqual(len(self.project()['map']['sections']),initial+4)
                self.context.close()

    def test_direct_presence_start_stop_resume_mouse_and_touch_all_canvases(self):
        for width in [320,390,820,1180,1440,1728,1920]:
            for touch in [False,True]:
                with self.subTest(width=width,touch=touch):
                    self.open(width=width,pointer=not touch);self.select()
                    old=self.project();original_id=old['map']['timeline']['presence'][0]['id']
                    self.place('end',2,touch=touch)
                    p=self.project();first=next(r for r in p['map']['timeline']['presence'] if r['id']==original_id)
                    self.assertEqual(first['end'],{'sectionId':'s0','bar':2})
                    expect(self.page.locator('#sheetRoot')).to_have_attribute('aria-hidden','true')
                    self.assertEqual(self.page.locator('[data-presence-handle][data-edge="end"]').count(),1)
                    self.direct_boundary('t1',6,touch=touch)
                    ranges=sorted(self.project()['map']['timeline']['presence'],key=lambda r:r['start']['bar'])
                    self.assertEqual(len(ranges),2);self.assertEqual(ranges[0]['id'],original_id)
                    self.assertEqual(ranges[0]['end']['bar'],2);self.assertEqual(ranges[1]['start']['bar'],6)
                    self.assertIsNone(ranges[1]['end'])
                    self.assertEqual(self.page.locator('.presence-segment.continue-out').count(),1)
                    self.page.locator('#undoEdit').click()
                    self.assertEqual(len(self.project()['map']['timeline']['presence']),1)
                    self.assertEqual(self.project()['map']['timeline']['presence'][0]['end']['bar'],2)
                    self.direct_boundary('t2',3,touch=touch)
                    bass=next(r for r in self.project()['map']['timeline']['presence'] if r['trackId']=='t2')
                    self.assertEqual(bass['start'],{'sectionId':'s0','bar':3});self.assertIsNone(bass['end'])
                    self.assertEqual(self.project()['map']['sectionData']['s0']['parking'],old['map']['sectionData']['s0']['parking'])
                    self.context.close()

    def test_direct_resume_preserves_later_gaps_boundaries_and_surviving_ids(self):
        data=fixture();timeline=data['projects'][0]['map']['timeline']
        timeline['presence']=[{'id':'r1','trackId':'t1','start':{'sectionId':'s0','bar':0},'end':{'sectionId':'s0','bar':2}},
                              {'id':'r2','trackId':'t1','start':{'sectionId':'s0','bar':4},'end':{'sectionId':'s0','bar':5}},
                              {'id':'r3','trackId':'t1','start':{'sectionId':'s0','bar':6},'end':None}]
        self.open(data=data);self.select();before=self.db()
        self.direct_boundary('t1',3)
        ranges={r['id']:r for r in self.project()['map']['timeline']['presence']}
        self.assertEqual(ranges['r1'],before['projects'][0]['map']['timeline']['presence'][0])
        self.assertEqual(ranges['r2']['start']['bar'],3);self.assertEqual(ranges['r2']['end']['bar'],5)
        self.assertEqual(ranges['r3'],before['projects'][0]['map']['timeline']['presence'][2])
        self.page.locator('#undoEdit').click();self.assertEqual(self.db(),before)
        self.direct_boundary('t1',2)
        ranges={r['id']:r for r in self.project()['map']['timeline']['presence']}
        self.assertEqual(set(ranges),{'r1','r3'});self.assertEqual(ranges['r1']['end']['bar'],5)
        self.assertIsNone(ranges['r3']['end'])
        self.page.locator('#undoEdit').click();self.assertEqual(self.db(),before)

    def test_block_body_never_splits_and_cancel_does_not_consume_undo(self):
        for touch in [False,True]:
            self.open(pointer=not touch);self.select();before=self.db()
            self.direct_boundary('t1',2,touch=touch)
            self.assertEqual(self.db(),before)
            self.direct_boundary('t2',4,touch=touch,cancel=True)
            self.assertEqual(self.db(),before)
            expect(self.page.locator('#undoNotice')).to_be_hidden()
            self.place('end',4,touch=touch)
            before=self.db();self.direct_boundary('t2',2,touch=touch,cancel=True)
            self.assertEqual(self.db(),before)
            self.page.locator('#undoEdit').click()
            self.assertIsNone(self.project()['map']['timeline']['presence'][0]['end'])
            self.context.close()

    def test_aligned_changes_and_fractional_data_until_intentional_edit(self):
        self.open(width=1440,pointer=True);self.select()
        self.assertEqual(self.event('e2')['point']['bar'],2.5)
        self.click('select-event','[data-event-id="e1"]');self.place('end',4,'event')
        self.assertEqual(self.event('e1')['end'],{'sectionId':'s0','bar':4})
        self.assertEqual(self.event('e2')['point']['bar'],2.5)
        self.assertEqual(self.page.locator('.change-editor,.change-lane,.timing-options').count(),0)
        lane=self.page.locator('[data-track-row="t1"] .timeline-lane').bounding_box()
        for line in self.page.locator('[data-track-row="t1"] .event-line').all():
            box=line.bounding_box();self.assertAlmostEqual(box['x'],lane['x']);self.assertAlmostEqual(box['width'],lane['width'])
        self.page.locator('#undoEdit').click();self.assertIsNone(self.event('e1')['end'])
        self.touch_drag(self.page.locator('[data-event-marker]'),.5)
        self.assertEqual(self.event('e2')['point']['bar'],4)
        self.page.locator('#undoEdit').click();self.assertEqual(self.event('e2')['point']['bar'],2.5)

    def test_component_shapes_stay_fixed_across_hover_focus_selected_and_disabled(self):
        self.open('projects',width=1440,data=self.complete_fixture(),pointer=True)
        samples=[('projects','.project-open'),('projects','.project-menu'),('project','.quick-card'),
                 ('map','.nav-btn'),('map','.state-control'),('map','.action-card'),('map','.list-row'),
                 ('structure','.structure-row'),('tracks','.choice'),('section-study','.segment'),
                 ('skeleton-draft','.workflow-disclosure summary'),('skeleton-bounce','.primary')]
        for route,selector in samples:
            with self.subTest(route=route,selector=selector):
                self.canvas_route(route)
                if route == 'map' and selector in ('.state-control','.action-card'):
                    self.expand_map_setup()
                node=self.page.locator(selector).first
                node.scroll_into_view_if_needed();before=node.bounding_box()
                radius=node.evaluate('el=>getComputedStyle(el).borderRadius')
                self.assertEqual(float(node.evaluate('el=>getComputedStyle(el).opacity')),1)
                node.hover();self.assertEqual(node.bounding_box(),before)
                self.assertEqual(node.evaluate('el=>getComputedStyle(el).borderRadius'),radius)
                node.focus();self.assertEqual(node.bounding_box(),before)
                self.assertEqual(node.evaluate('el=>getComputedStyle(el).borderRadius'),radius)
                box=node.bounding_box();self.page.mouse.move(box['x']+box['width']/2,box['y']+box['height']/2);self.page.mouse.down()
                self.assertEqual(node.bounding_box(),before)
                self.assertEqual(node.evaluate('el=>getComputedStyle(el).borderRadius'),radius)
                self.page.mouse.move(0,0);self.page.mouse.up()
                node.evaluate('el=>el.classList.add("selected")')
                self.assertEqual(node.bounding_box(),before)
                self.assertEqual(node.evaluate('el=>getComputedStyle(el).borderRadius'),radius)
                if node.evaluate('el=>el.tagName')=='BUTTON':
                    node.evaluate('el=>el.disabled=true');self.assertEqual(node.bounding_box(),before)
                    self.assertEqual(node.evaluate('el=>getComputedStyle(el).borderRadius'),radius)
                    self.assertGreaterEqual(float(node.evaluate('el=>getComputedStyle(el).opacity')),.5)
        self.canvas_route('structure');self.click('edit-section','[data-section-id="s0"]');self.settled_sheet()
        expect(self.page.locator('.sheet')).to_have_css('border-radius','20px')
        self.assertNotEqual(self.page.evaluate('document.activeElement.tagName'),'INPUT')

    def test_fire_design_system_foundation_across_representative_routes(self):
        self.open('roadmap', width=820, data=self.complete_fixture())
        self.assertEqual(self.page.locator('.topbar .center').inner_text().strip(), '')
        roadmap = self.page.locator('.roadmap-grid')
        self.assertEqual(roadmap.evaluate('el=>getComputedStyle(el).display'), 'block')
        self.assertEqual(self.page.locator('.road-phase').first.evaluate('el=>getComputedStyle(el).borderRadius'), '0px')

        self.canvas_route('structure')
        self.assertEqual(self.page.locator('.section-kicker:text-is("Structure")').count(), 0)
        self.assertEqual(self.page.locator('h1').evaluate('el=>getComputedStyle(el).textTransform'), 'none')
        self.assertEqual(self.page.locator('.structure-list').evaluate('el=>getComputedStyle(el).display'), 'block')
        self.click('open-add-section'); self.settled_sheet()
        sheet = self.page.locator('.sheet'); box = sheet.bounding_box()
        self.assertLessEqual(box['width'], 620)
        self.assertGreater(box['y'], 20)
        self.assertEqual(sheet.evaluate('el=>getComputedStyle(el).borderRadius'), '20px')
        self.click('close-sheet')

        self.canvas_route('tracks')
        selected = self.page.locator('.choice[aria-pressed="true"]').first
        self.assertEqual(selected.evaluate("el=>getComputedStyle(el,'::before').display"), 'none')
        self.assertLessEqual(self.page.locator('[data-action="start-section-study"]').bounding_box()['width'], 320.5)

        self.canvas_route('skeleton-session')
        self.assertLessEqual(self.page.locator('[data-route="skeleton-draft"]').bounding_box()['width'], 320.5)

    def test_dense_lane_scroll_keyboard_precision_and_touch_scroll_cancellation(self):
        data=fixture();data['projects'][0]['map']['sections'][0]['lengthBars']=256
        self.open(width=320,data=data);self.select();before=self.db()
        scroll=self.page.locator('.timeline-scroll')
        self.assertGreater(scroll.evaluate('el=>el.scrollWidth'),scroll.evaluate('el=>el.clientWidth'))
        self.assertGreaterEqual(self.page.locator('.timeline-lane').first.bounding_box()['width']/256,44)
        handle=self.page.locator('[data-presence-handle][data-edge="start"]');handle.focus();self.page.keyboard.press('ArrowRight')
        self.assertEqual(self.project()['map']['timeline']['presence'][0]['start']['bar'],1)
        self.assertEqual(self.event('e2')['point']['bar'],2.5)
        self.page.locator('#undoEdit').click();self.assertEqual(self.db(),before)
        label=self.page.locator('[data-track-row="t1"] .timeline-label');label_x=label.bounding_box()['x']
        scroll.evaluate('el=>el.scrollLeft=2000');self.assertGreater(scroll.evaluate('el=>el.scrollLeft'),1000)
        self.assertAlmostEqual(label.bounding_box()['x'],label_x,delta=1)
        add=self.page.locator('[data-action="open-add-change"][data-target-type="track"]')
        self.assertLessEqual(add.bounding_box()['x']+add.bounding_box()['width'],320)
        self.page.set_viewport_size({'width':820,'height':1000})
        self.assertLessEqual(self.page.evaluate('document.documentElement.scrollWidth'),820)
        scroll.evaluate('el=>el.scrollLeft=0')
        surface=self.page.locator('[data-presence-surface][data-track-id="t2"]');box=surface.bounding_box()
        x=box['x']+30;y=box['y']+58;before=self.db();cdp=self.context.new_cdp_session(self.page)
        cdp.send('Input.dispatchTouchEvent',{'type':'touchStart','touchPoints':[{'x':x,'y':y}]})
        cdp.send('Input.dispatchTouchEvent',{'type':'touchMove','touchPoints':[{'x':x,'y':y+35}]})
        cdp.send('Input.dispatchTouchEvent',{'type':'touchEnd','touchPoints':[]});cdp.detach()
        self.assertEqual(self.db(),before)

    def test_builder_keeps_keyboard_focus_inside_after_committing(self):
        self.open('structure',width=1440,pointer=True);initial=len(self.project()['map']['sections'])
        self.click('open-add-section');self.click('choose-section-type','[data-name="Intro"]')
        self.click('set-new-section-bars','[data-bars="4"]')
        self.page.locator('[data-action="save-new-section"]').focus();self.page.keyboard.press('Enter')
        expect(self.page.locator('[data-action="choose-section-type"][data-name="Intro"]')).to_be_focused()
        self.assertNotEqual(self.page.evaluate('document.activeElement.tagName'),'INPUT')
        self.page.keyboard.press('Escape')
        expect(self.page.locator('#sheetRoot')).to_have_attribute('aria-hidden','true')
        self.assertEqual(len(self.project()['map']['sections']),initial+1)

    def test_structure_delete_undo_and_edit_responsibilities(self):
        self.open('structure');before=self.db();dialogs=[]
        self.page.on('dialog',lambda d:(dialogs.append(d.message),d.dismiss()))
        delete=self.page.get_by_role('button',name='Delete Intro',exact=True)
        box=delete.bounding_box();self.assertGreaterEqual(box['width'],44);self.assertGreaterEqual(box['height'],44)
        delete.click();self.assertEqual(dialogs,[])
        self.assertNotIn('s0',[x['id'] for x in self.project()['map']['sections']])
        self.page.locator('#undoEdit').click();self.assertEqual(self.db(),before)
        self.click('edit-section','[data-section-id="s0"]')
        self.assertEqual(self.page.locator('.sheet [data-action*="delete"],.sheet [data-action*="remove"],.sheet [data-action="move-section"]').count(),0)
        self.assertNotEqual(self.page.evaluate('document.activeElement.tagName'),'INPUT')
        self.click('set-sheet-bars','[data-bars="12"]');self.page.locator('#renameSection').fill('Bridge');self.click('save-section')
        self.assertEqual(self.project()['map']['sections'][0],{'id':'s0','name':'Bridge','lengthBars':12})
        self.assertEqual(self.project()['map']['sectionData']['s0']['parking'],'Note s0')

    def test_structure_polish_hierarchy_and_responsive_next(self):
        for width in [390,820]:
            with self.subTest(width=width):
                self.open('structure',width=width,pointer=width>=820)
                self.assertEqual(self.page.locator('.structure-ready-label').count(),0)
                self.assertEqual(self.page.locator('.section-kicker:text-is("Structure")').count(),0)
                self.assertEqual(self.page.locator('[data-action="open-add-section"]').evaluate('el=>getComputedStyle(el).borderStyle'),'solid')
                row=self.page.locator('.structure-row').first
                self.assertGreaterEqual(row.bounding_box()['height'],62)
                self.assertEqual(self.page.locator('.bars-badge').first.evaluate('el=>getComputedStyle(el).backgroundColor'),'rgba(0, 0, 0, 0)')
                nxt=self.page.locator('[data-route="tracks"]');page=self.page.locator('.workflow-page')
                if width>=640:
                    self.assertLessEqual(nxt.bounding_box()['width'],280.5)
                    self.assertAlmostEqual(nxt.bounding_box()['x']+nxt.bounding_box()['width'],page.bounding_box()['x']+page.bounding_box()['width'],delta=1)
                else:
                    self.assertAlmostEqual(nxt.bounding_box()['width'],page.bounding_box()['width'],delta=1)
                self.click('open-add-section');self.click('choose-section-type','[data-name="Intro"]')
                selected=self.page.locator('[data-action="choose-section-type"][data-name="Intro"]')
                self.assertEqual(selected.evaluate("el=>getComputedStyle(el,'::before').display"),'none')
                self.click('set-new-section-bars','[data-bars="8"]');self.click('save-new-section')
                expect(self.page.locator('#builderStatus')).to_have_text('Added Intro · 8 bars')
                expect(self.page.locator('[data-bars="8"]')).to_have_attribute('aria-pressed','true')
                expect(self.page.locator('#sheetRoot')).to_have_attribute('aria-hidden','false')
                self.context.close()

    def test_segment_selected_and_keyboard_focus_are_distinct_without_geometry_changes(self):
        self.open('structure',width=390,pointer=True);self.click('open-add-section')
        self.click('choose-section-type','[data-name="Intro"]');self.settled_sheet()
        group=self.page.locator('.length-segmented');buttons=group.locator('button')
        widths=[b.bounding_box()['width'] for b in buttons.all()]
        self.assertLess(max(widths)-min(widths),1)
        target=buttons.nth(1);before=target.bounding_box();target.click()
        self.assertEqual(target.bounding_box(),before)
        self.assertEqual(target.evaluate('el=>getComputedStyle(el).outlineStyle'),'none')
        self.assertEqual(target.evaluate('el=>getComputedStyle(el).boxShadow'),'none')
        self.page.keyboard.press('Tab');self.page.keyboard.press('Shift+Tab')
        self.assertEqual(target.evaluate('el=>getComputedStyle(el).outlineStyle'),'solid')
        self.assertEqual(target.bounding_box(),before)

    def test_drag_keeps_nodes_and_canonical_state_until_one_commit_without_snapback(self):
        self.open(width=1180,pointer=True);self.select();before=self.db()
        handle=self.page.locator('[data-presence-handle][data-edge="start"]');handle.scroll_into_view_if_needed()
        handle.evaluate('''el=>{window.dragNode=el;window.laneNode=el.closest('.timeline-lane');window.laneMutations=0;
          window.laneObserver=new MutationObserver(ms=>window.laneMutations+=ms.filter(m=>m.type==='childList').length);
          window.laneObserver.observe(window.laneNode,{childList:true,subtree:true});
          window.savedWrites=0;const old=Storage.prototype.setItem;Storage.prototype.setItem=function(k,v){if(k==='production-projects-v1')window.savedWrites++;return old.call(this,k,v)};}''')
        box=handle.bounding_box();lane=handle.locator('xpath=..').bounding_box();y=box['y']+22
        self.page.mouse.move(box['x']+22,y);self.page.mouse.down()
        self.page.mouse.move(lane['x']+lane['width']*.25,y,steps=8)
        self.assertEqual(self.db(),before)
        self.assertTrue(handle.evaluate('el=>el===window.dragNode && el.closest(".timeline-lane")===window.laneNode'))
        self.assertEqual(self.page.evaluate('window.laneMutations'),0)
        self.assertEqual(self.page.evaluate('window.savedWrites'),0)
        self.assertAlmostEqual(handle.bounding_box()['x']+22,lane['x']+lane['width']*.25,delta=1)
        expect(self.page.locator('.snap-guide:visible')).to_have_count(1)
        self.page.mouse.up()
        self.assertEqual(self.page.evaluate('window.savedWrites'),1)
        self.assertEqual(self.project()['map']['timeline']['presence'][0]['start']['bar'],2)
        handle=self.page.locator('[data-presence-handle][data-edge="start"]')
        self.assertAlmostEqual(handle.bounding_box()['x']+22,lane['x']+lane['width']*.25,delta=1)
        expect(self.page.locator('#dragPosition')).to_be_hidden()
        self.assertEqual(self.page.locator('.snap-guide:visible').count(),0)
        self.page.locator('#undoEdit').click();self.assertEqual(self.db(),before)

    def test_boundary_crossing_is_rejected_without_id_churn_or_unrelated_gap_mutation(self):
        data=fixture();tl=data['projects'][0]['map']['timeline']
        tl['presence']=[{'id':'r1','trackId':'t1','start':{'sectionId':'s0','bar':1},'end':{'sectionId':'s0','bar':3}},
                        {'id':'r2','trackId':'t1','start':{'sectionId':'s0','bar':5},'end':{'sectionId':'s0','bar':7}}]
        self.open(data=data,width=1180,pointer=True);self.select();before=self.db()
        self.place('end',6);self.assertEqual(self.db(),before)
        self.select();self.place('start',4);self.assertEqual(self.db(),before)
        self.select('r2');self.place('start',0);self.assertEqual(self.db(),before)
        self.select('r2');self.place('end',4);self.assertEqual(self.db(),before)
        self.select('r1');self.place('end',4)
        ranges=self.project()['map']['timeline']['presence']
        self.assertEqual([r['id'] for r in ranges],['r1','r2'])
        self.assertEqual(ranges[1],before['projects'][0]['map']['timeline']['presence'][1])
        self.assertEqual(ranges[0]['end']['bar'],4)

    def test_keyboard_real_boundaries_and_point_share_bar_semantics(self):
        self.open(width=820);self.select();before=self.db()
        handle=self.page.locator('[data-presence-handle][data-edge="start"]');handle.focus()
        self.assertIn('Start at bar 1',handle.get_attribute('aria-label'))
        self.page.keyboard.press('ArrowRight')
        self.assertEqual(self.project()['map']['timeline']['presence'][0]['start']['bar'],1)
        expect(self.page.locator('[data-presence-handle][data-edge="start"]')).to_be_focused()
        self.page.keyboard.press('ArrowLeft');self.assertEqual(self.project()['map']['timeline']['presence'][0]['start']['bar'],0)
        self.place('end',2)
        self.assertIn('Stop after bar 2',self.page.locator('[data-presence-handle][data-edge="end"]').get_attribute('aria-label'))
        self.page.locator('#undoEdit').click()
        marker=self.page.locator('[data-event-marker]');marker.focus();self.page.keyboard.press('Enter')
        expect(self.page.locator('[data-action="remove-selected"][data-kind="event"]')).to_be_visible()
        self.page.keyboard.press('Escape');marker=self.page.locator('[data-event-marker]');marker.focus();self.page.keyboard.press('ArrowRight')
        self.assertEqual(self.event('e2')['point']['bar'],3)
        self.page.locator('#undoEdit').click();self.assertEqual(self.event('e2')['point']['bar'],2.5)

    def test_drag_cancel_escape_vertical_capture_resize_route_and_layout(self):
        for mode in ['escape','vertical','capture','resize','route','layout']:
            with self.subTest(mode=mode):
                self.open(width=1180,pointer=True);self.select();before=self.db()
                handle=self.page.locator('[data-presence-handle][data-edge="start"]');handle.scroll_into_view_if_needed()
                box=handle.bounding_box();lane=handle.locator('xpath=..').bounding_box();y=box['y']+22
                self.page.mouse.move(box['x']+22,y);self.page.mouse.down();self.page.mouse.move(lane['x']+lane['width']*.25,y,steps=4)
                if mode=='escape':self.page.keyboard.press('Escape')
                if mode=='vertical':self.page.mouse.move(box['x']+24,y+45,steps=3)
                if mode=='capture':handle.evaluate('el=>el.releasePointerCapture(1)');self.page.mouse.move(lane['x']+lane['width']*.3,y)
                if mode=='resize':self.page.set_viewport_size({'width':820,'height':1000})
                if mode=='route':self.page.locator('.phase-pill').evaluate('el=>el.click()')
                if mode=='layout':
                    handle.locator('xpath=..').evaluate('el=>el.style.width="75%"')
                    self.page.wait_for_timeout(40)
                self.page.mouse.up();self.assertEqual(self.db(),before)
                expect(self.page.locator('#dragPosition')).to_be_hidden()
                self.assertFalse(self.page.locator('body').evaluate('el=>el.classList.contains("is-dragging")'))
                self.context.close()

    def test_no_hover_tooltip_or_retired_timing_architecture(self):
        self.open(width=1440,pointer=True);self.select()
        forbidden='.timing-options,.placement-sheet,.change-editor,.change-lane,.lane-feedback,.presence-selectors,input[type="range"]'
        self.assertEqual(self.page.locator(forbidden).count(),0)
        for node in [self.page.locator('.presence-hit').first,self.page.locator('[data-presence-handle]').first,self.page.locator('[data-event-marker]').first]:
            node.hover();expect(self.page.locator('#dragPosition')).to_be_hidden()
        text=self.page.locator('.timeline-card').inner_text()
        for copy in ['Timing options','Earlier','Later','Move start','Move stop','Continue','Tap a boundary']:
            self.assertNotIn(copy,text)

    def test_review_map_reuses_chip_disclosure_and_verify_geometry(self):
        for width in [320,820,1440]:
            self.open('map-summary',width=width,data=self.complete_fixture())
            chips=self.page.locator('.chip');heights=[x.bounding_box()['height'] for x in chips.all()]
            self.assertLess(max(heights)-min(heights),1)
            summaries=self.page.locator('.review-sections summary');boxes=[x.bounding_box() for x in summaries.all()]
            self.assertLess(max(x['height'] for x in boxes)-min(x['height'] for x in boxes),1)
            summaries.first.click();card=self.page.locator('.review-sections .workflow-disclosure').first.bounding_box()
            body=self.page.locator('.review-sections .summary-lines').first.bounding_box()
            self.assertGreaterEqual(body['x'],card['x']);self.assertLessEqual(body['x']+body['width'],card['x']+card['width'])
            verify=self.page.locator('.action-card');self.assertEqual(verify.count(),2)
            self.assertEqual(verify.nth(0).bounding_box()['height'],verify.nth(1).bounding_box()['height'])
            self.context.close()


    def test_dense_native_horizontal_navigation_and_touch_vertical_boundary_cancel(self):
        data=fixture();data['projects'][0]['map']['sections'][0]['lengthBars']=64
        self.open(width=820,data=data);before=self.db()
        scroll=self.page.locator('.timeline-scroll');box=scroll.bounding_box()
        self.page.mouse.move(box['x']+box['width']*.7,box['y']+45)
        self.page.mouse.wheel(350,0)
        expect(scroll).to_have_js_property('scrollLeft',350)
        self.assertEqual(self.db(),before)
        scroll.evaluate('el=>el.scrollLeft=0')
        surface=self.page.locator('[data-presence-surface][data-track-id="t2"]');box=surface.bounding_box()
        x=min(650,box['x']+250);y=box['y']+58
        cdp=self.context.new_cdp_session(self.page)
        cdp.send('Input.dispatchTouchEvent',{'type':'touchStart','touchPoints':[{'x':x,'y':y}]})
        for i in range(1,6):
            cdp.send('Input.dispatchTouchEvent',{'type':'touchMove','touchPoints':[{'x':x-i*25,'y':y}]})
            self.page.wait_for_timeout(20)
        cdp.send('Input.dispatchTouchEvent',{'type':'touchEnd','touchPoints':[]});cdp.detach()
        self.assertGreater(scroll.evaluate('el=>el.scrollLeft'),50)
        self.assertEqual(self.db(),before)
        # On a normal fitted section, vertical handle contact yields to page scroll.
        self.open(width=390);self.select();self.place('end',4);before=self.db()
        handle=self.page.locator('[data-presence-handle][data-edge="end"]');handle.scroll_into_view_if_needed();box=handle.bounding_box()
        x=box['x']+22;y=box['y']+22;cdp=self.context.new_cdp_session(self.page)
        cdp.send('Input.dispatchTouchEvent',{'type':'touchStart','touchPoints':[{'x':x,'y':y}]})
        cdp.send('Input.dispatchTouchEvent',{'type':'touchMove','touchPoints':[{'x':x+2,'y':y+50}]})
        cdp.send('Input.dispatchTouchEvent',{'type':'touchEnd','touchPoints':[]});cdp.detach()
        self.assertEqual(self.db(),before);expect(self.page.locator('#dragPosition')).to_be_hidden()


    def test_change_uses_effective_parent_stop_instead_of_false_open_grip(self):
        data=fixture();data['projects'][0]['map']['timeline']['presence'][0]['end']={'sectionId':'s0','bar':4}
        self.open(width=820,data=data);self.select();self.click('select-event','[data-event-id="e1"]')
        end=self.page.locator('[data-event-handle][data-edge="end"]')
        self.assertIsNone(self.event('e1')['end'])
        self.assertIsNone(end.get_attribute('data-open-tail'))
        self.assertIn('Stop after bar 4',end.get_attribute('aria-label'))
        end.focus();self.page.keyboard.press('ArrowLeft')
        self.assertEqual(self.event('e1')['end']['bar'],3)
        self.page.locator('#undoEdit').click();self.assertIsNone(self.event('e1')['end'])
        # A finite parent stop outside this section must not invent a local handle.
        data=fixture();data['projects'][0]['map']['timeline']['presence'][0]['end']={'sectionId':'s1','bar':4}
        self.open(width=820,data=data);self.select();self.click('select-event','[data-event-id="e1"]')
        self.assertEqual(self.page.locator('[data-event-handle][data-edge="end"]').count(),0)


    def test_workflow_shell_continuity_project_map_structure_tracks(self):
        self.open('project',width=820)
        cases=[
            ('project','Migration song','Test artist · Recreation','projects',''),
            ('map','The Map','Understand the song before rebuilding it.','project',''),
            ('structure','Structure','Build the song one section at a time.','map','1 of 3'),
            ('tracks','Tracks','Select everything that appears somewhere in the song.','structure','2 of 3'),
        ]
        anchor=None
        for route,title,subtitle,back,status in cases:
            with self.subTest(route=route):
                self.canvas_route(route)
                self.assertEqual(self.page.locator('.workflow-page').count(),1)
                self.assertEqual(self.page.locator('.topbar .center').inner_text(),'')
                self.assertEqual(self.page.locator('.phase-pill').count(),0)
                expect(self.page.locator('.workflow-page .page-heading h1')).to_have_text(title)
                expect(self.page.locator('.workflow-page .page-heading .sub')).to_have_text(subtitle)
                back_button=self.page.locator('.topbar > .left > .nav-btn')
                self.assertEqual(back_button.count(),1)
                self.assertEqual(back_button.get_attribute('data-fallback-route'),back)
                if status:
                    expect(self.page.locator('.workflow-position')).to_have_text(status)
                else:
                    self.assertEqual(self.page.locator('.workflow-position').count(),0)
                box=self.page.locator('.workflow-page .page-heading h1').bounding_box()
                if anchor is None:
                    anchor=(box['x'],box['y'])
                else:
                    self.assertLessEqual(abs(box['x']-anchor[0]),1)
                    self.assertLessEqual(abs(box['y']-anchor[1]),1)



if __name__ == '__main__':
    unittest.main()
