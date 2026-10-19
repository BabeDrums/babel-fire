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

    def open(self, route='section-study', width=None, data=None, reduced=False):
        width = width or int(os.environ.get('FIRE_TEST_WIDTH', '390'))
        self.context = self.browser.new_context(viewport={'width': width, 'height': 1000},
                                                has_touch=True, reduced_motion='reduce' if reduced else 'no-preference')
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
        self.addCleanup(lambda: self.assertEqual(self.errors, []))
        return self.page

    def click(self, action, extra=''):
        self.page.locator(f'[data-action="{action}"]{extra}').click()

    def db(self):
        return self.page.evaluate('(key)=>JSON.parse(localStorage.getItem(key))', KEY)

    def project(self):
        return self.db()['projects'][0]

    def event(self, id):
        return next(e for e in self.project()['map']['timeline']['events'] if e['id'] == id)

    def select(self, range='r1'):
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

    def place(self, edge, value, kind='presence'):
        self.click('place-boundary', f'[data-kind="{kind}"][data-edge="{edge}"]')
        self.page.locator('#placementPosition').fill(str(value))
        self.click('commit-placement')

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
        self.click('save-new-section')
        expect(self.page.locator('.structure-row').filter(has_text='Verse 2')).to_be_visible()
        self.click('open-add-section');self.click('choose-section-type', '[data-name="Custom"]')
        self.page.locator('#newSectionName').fill('Breakdown')
        self.click('set-new-section-bars', '[data-bars="custom"]')
        self.page.locator('#newSectionBars').fill('0')
        expect(self.page.locator('[data-action="save-new-section"]')).to_be_disabled()
        self.page.locator('#newSectionBars').fill('7');self.click('save-new-section')
        sid = self.project()['map']['sections'][-1]['id']
        self.click('edit-section', f'[data-section-id="{sid}"]')
        self.page.locator('#renameSection').fill('Break');self.click('set-sheet-bars', '[data-bars="12"]')
        self.click('save-section')
        self.assertEqual(self.project()['map']['sections'][-1], {'id': sid, 'name': 'Break', 'lengthBars': 12})
        self.click('edit-section', f'[data-section-id="{sid}"]')
        self.page.once('dialog', lambda d: d.accept());self.click('remove-section')
        self.assertNotIn(sid, [s['id'] for s in self.project()['map']['sections']])
        self.assertNotIn('Bars bars', self.page.locator('body').inner_text())

    def test_add_absent_presence_is_open_and_covers_later_new_sections(self):
        self.open();self.click('add-presence-section', '[data-track-id="t2"]')
        ranges = self.project()['map']['timeline']['presence']
        self.assertIsNone(next(r for r in ranges if r['trackId']=='t2')['end'])
        self.assertFalse(self.project()['skeleton']['draft']['parts']['s2']['t2'])
        self.assertFalse(self.project()['map']['sectionData']['s2']['silence'])
        # Route to Structure through the normal phase navigator.
        self.click('go', '[data-route="map"]')
        self.click('go', '[data-route="structure"]')
        self.click('open-add-section');self.click('choose-section-type', '[data-name="Outro"]')
        self.click('set-new-section-bars', '[data-bars="4"]');self.click('save-new-section')
        self.assertEqual(len(self.project()['map']['sections']), 4)
        r = next(r for r in self.project()['map']['timeline']['presence'] if r['trackId']=='t2')
        self.assertIsNone(r['end'])
        self.click('toggle-structure-verified');self.click('go','[data-route="tracks"]')
        self.click('start-section-study');self.click('jump-section','[data-index="3"]')
        expect(self.page.locator('.section-tab.current')).to_have_text('Outro')
        self.assertEqual(self.page.locator('.presence-segment.continue-in.continue-out').count(),2)

    def test_touch_presence_end_inside_and_boundary_and_continue_undo(self):
        self.open();self.select()
        self.assertEqual(self.page.locator('[data-presence-handle][data-edge="end"]').count(), 0)
        self.place('end',4)
        self.assertEqual(self.project()['map']['timeline']['presence'][0]['end'], {'sectionId':'s0','bar':4})
        self.assertEqual(self.event('e1')['end'], {'sectionId':'s0','bar':4})
        self.page.locator('#undoEdit').click()
        self.assertIsNone(self.project()['map']['timeline']['presence'][0]['end'])
        self.place('end',8)
        self.assertEqual(self.project()['map']['timeline']['presence'][0]['end'], {'sectionId':'s0','bar':'end'})
        self.click('continue-range', '[data-kind="presence"]')
        self.assertIsNone(self.project()['map']['timeline']['presence'][0]['end'])
        self.assertFalse(self.project()['skeleton']['bounce']['exported'])

    def test_touch_cancel_leaves_database_and_listeners_clean(self):
        self.open();self.select();before=self.db()
        self.touch_drag(self.page.locator('[data-presence-handle][data-edge="start"]'), .25, cancel=True)
        self.assertEqual(self.db(), before)
        self.assertFalse(self.page.locator('body').evaluate('(e)=>e.classList.contains("is-dragging")'))
        self.touch_drag(self.page.locator('[data-presence-handle][data-edge="start"]'), .25)
        self.assertEqual(self.project()['map']['timeline']['presence'][0]['start']['bar'], 2)

    def test_one_screen_add_change_and_direct_chip_selection_removal_undo(self):
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
        self.assertEqual(self.page.locator('.change-editor').count(), 1)
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
        self.click('start-track','[data-track-id="t1"]')
        self.page.locator('#placementPosition').fill('6');self.click('commit-placement')
        ranges=self.project()['map']['timeline']['presence']
        self.assertEqual(len(ranges),2);self.assertEqual(ranges[0]['id'],'r1')
        self.assertEqual(ranges[0]['end']['bar'],4);self.assertEqual(ranges[1]['start']['bar'],6)
        self.assertIsNone(ranges[1]['end'])
        self.page.locator('#undoEdit').click()
        self.assertEqual(len(self.project()['map']['timeline']['presence']),1)
        self.click('start-track','[data-track-id="t1"]')
        self.page.locator('#placementPosition').fill('4');self.click('commit-placement')
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
                self.assertGreater(self.page.locator('.event-summary-range').count(),0)
                self.assertEqual(self.page.locator('.timeline-row').evaluate_all('(els)=>els.map(e=>e.dataset.trackRow)'),['t1','t2'])
                self.click('next-section');expect(self.page.locator('.section-tab.current')).to_have_text('Verse')
                self.assertEqual(self.page.locator('.timeline-row.expanded').count(),0)
                self.assertEqual(self.page.locator('.presence-segment.continue-in.continue-out').count(),1)
                self.assertEqual(self.page.evaluate('history.state.fromRoute'),'tracks')
                self.assertLessEqual(self.page.evaluate('document.documentElement.scrollWidth'),width)
                self.context.close()

    def test_touch_targets(self):
        self.open();self.select();self.click('select-event','[data-event-id="e1"]')
        for selector in ['.presence-hit','.change-chip','.event-handle','.mini-btn','.mix-toggle']:
            for box in self.page.locator(selector).all():
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
        self.click('history-back');expect(self.page.locator('h2')).to_have_text('Tracks')
        self.click('history-back');expect(self.page.locator('h2')).to_have_text('Structure')
        self.page.go_back();expect(self.page.locator('[data-route="structure"]')).to_be_visible()

    def test_finite_cross_section_reorder_remove_preserves_unaffected_coverage_and_ids(self):
        data=fixture();timeline=data['projects'][0]['map']['timeline']
        timeline['presence'][0]['end']={'sectionId':'s1','bar':'end'}
        timeline['events'][0]['end']={'sectionId':'s1','bar':4}
        self.open('structure',data=data)
        self.click('edit-section','[data-section-id="s0"]')
        self.click('move-section','[data-delta="1"]')
        self.click('move-section','[data-delta="1"]')
        self.click('close-sheet')
        p=self.project();ranges=p['map']['timeline']['presence']
        self.assertEqual([x['id'] for x in p['map']['sections']],['s1','s2','s0'])
        self.assertEqual({r['start']['sectionId'] for r in ranges},{'s1','s0'})
        self.assertIn('r1',[r['id'] for r in ranges])
        self.assertNotIn('s2',{r['start']['sectionId'] for r in ranges})
        surviving_id=next(r['id'] for r in ranges if r['start']['sectionId']=='s0')
        self.click('edit-section','[data-section-id="s1"]')
        self.page.once('dialog',lambda d:d.accept());self.click('remove-section')
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


    def test_short_presence_pieces_have_large_explicit_selectors(self):
        data=fixture();timeline=data['projects'][0]['map']['timeline']
        timeline['presence']=[{'id':'r1','trackId':'t1','start':{'sectionId':'s0','bar':0},'end':{'sectionId':'s0','bar':1}},
                              {'id':'r2','trackId':'t1','start':{'sectionId':'s0','bar':2},'end':None}]
        self.open(data=data);self.select()
        expect(self.page.locator('.presence-choice')).to_have_count(2)
        target=self.page.locator('.presence-choice[data-range-id="r2"]')
        box=target.bounding_box();self.assertGreaterEqual(box['height'],44);self.assertGreaterEqual(box['width'],44)
        target.click()
        self.assertEqual(self.page.locator('[data-presence-handle][data-edge="start"]').get_attribute('data-range-id'),'r2')
        self.click('remove-selected','[data-kind="presence"][data-id="r2"]')
        self.assertEqual([r['id'] for r in self.project()['map']['timeline']['presence']],['r1'])
        self.page.locator('#undoEdit').click()
        self.assertEqual({r['id'] for r in self.project()['map']['timeline']['presence']},{'r1','r2'})
        self.page.locator('.presence-choice[data-range-id="r2"]').click()
        self.place('start',1)
        self.assertEqual([r['id'] for r in self.project()['map']['timeline']['presence']],['r1'])
        self.assertEqual(self.page.locator('[data-presence-handle][data-edge="start"]').get_attribute('data-range-id'),'r1')

    def complete_fixture(self):
        data=fixture()
        data['projects'][0]['map']['timeline']['presence'].append(
            {'id':'bass','trackId':'t2','start':{'sectionId':'s0','bar':0},'end':None})
        return data

    def test_live_bpm_validation_progress_caret_and_route_guards(self):
        self.open('map', data=self.complete_fixture())
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
        expect(self.page.locator('h2')).to_have_text('The Map')
        self.assertEqual(self.page.evaluate('history.state.route'),'map')
        self.assertEqual(self.project()['skeleton'],original)
        inp.fill('128.25');self.click('go','[data-route="structure"]')
        expect(self.page.locator('h2')).to_have_text('Structure')

    def test_each_setup_prerequisite_locks_and_restores_without_losing_work(self):
        self.open('map', data=self.complete_fixture()); original=self.project()['skeleton']
        for field in ['reference','grid','firstListen']:
            self.click('toggle-setup',f'[data-field="{field}"]')
            expect(self.page.locator('[data-route="structure"]')).to_be_disabled()
            expect(self.page.locator('.checkpoint-count')).to_have_text('0 of 3')
            self.click('toggle-setup',f'[data-field="{field}"]')
            expect(self.page.locator('[data-route="structure"]')).to_be_enabled()
            expect(self.page.locator('.checkpoint-count')).to_have_text('3 of 3')
            self.assertEqual(self.project()['skeleton'],original)
        self.page.locator('#meterInput').evaluate("el=>{el.add(new Option('Choose',''));el.value='';el.dispatchEvent(new Event('change',{bubbles:true}))}")
        expect(self.page.locator('[data-route="structure"]')).to_be_disabled()
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
        self.click('history-back');expect(self.page.locator('h2')).to_have_text('Tracks')
        self.page.go_forward();expect(self.page.locator('.study-pane')).to_be_visible()
        self.page.locator('.phase-pill').click();expect(self.page.locator('h2')).to_have_text('The Map')
        self.page.locator('.phase-pill').click();expect(self.page.locator('h1')).to_have_text('Migration song')
        self.click('go','[data-route="roadmap"]');expect(self.page.locator('h2')).to_have_text('Roadmap')
        self.context.close()
        self.open('skeleton',data=self.complete_fixture());self.click('go','[data-route="skeleton-session"]')
        self.click('history-back');expect(self.page.locator('h2')).to_have_text('The Skeleton')
        self.click('go','[data-route="skeleton-session"]');self.click('go','[data-route="skeleton-draft"]')
        self.click('history-back');expect(self.page.locator('h2')).to_have_text('Session')

    def test_boundary_truth_across_viewports_and_placement_cancel_noop(self):
        self.open();self.select()
        self.assertEqual(self.page.locator('[data-presence-handle]').count(),1)
        self.assertEqual(self.page.locator('.presence-segment.real-stop').count(),0)
        original=self.db();self.click('place-boundary','[data-edge="end"]')
        self.page.locator('#placementPosition').fill('4');self.click('close-sheet')
        self.assertEqual(self.db(),original)
        self.place('start',0);self.assertEqual(self.db(),original)
        self.assertTrue(self.page.locator('#undoNotice').is_hidden())
        self.click('next-section');expect(self.page.locator('.section-tab.current')).to_have_text('Verse')
        self.select();self.assertEqual(self.page.locator('[data-presence-handle]').count(),0)
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
                self.select();button=self.page.locator('[data-action="place-boundary"]').first
                box=button.bounding_box();button.dispatch_event('pointerdown')
                self.assertEqual(button.bounding_box(),box)
                self.assertEqual(self.page.evaluate("matchMedia('(prefers-reduced-motion: reduce)').matches"),True)
                self.context.close()

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


if __name__ == '__main__':
    unittest.main()
