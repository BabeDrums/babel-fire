from pathlib import Path
import re

path = Path(__file__).resolve().parents[1] / "tests" / "test_v6.py"
text = path.read_text(encoding="utf-8")


def sub_once(pattern, repl, label):
    global text
    text, count = re.subn(pattern, repl, text, count=1, flags=re.S)
    if count != 1:
        raise RuntimeError(f"{label}: expected one match, found {count}")


sub_once(
    r"    def test_live_bpm_validation_progress_caret_and_route_guards\(self\):.*?\n    def test_each_setup_prerequisite_locks_and_restores_without_losing_work",
    '''    def test_live_bpm_validation_progress_caret_and_route_guards(self):
        self.open('map', data=self.complete_fixture());self.expand_map_setup()
        inp=self.page.locator('#tempoInput'); inp.focus()
        original=self.project()['skeleton']
        for value,valid in [('',False),(' ',False),('abc',False),('Infinity',False),('0',False),('-2',False),('120.5',True),('1.',True),('1..2',False),('120',True)]:
            inp.fill(value)
            expect(inp).to_be_focused()
            self.assertEqual(self.project()['map']['setup']['tempo'],value)
            structure=self.page.locator('.step-row[data-route="structure"]')
            if valid:
                expect(structure).to_be_enabled()
                expect(structure.locator('.step-state')).to_have_text('Done')
            else:
                expect(structure).to_be_disabled()
                expect(structure.locator('.step-state')).to_have_text('Locked')
            expect(self.page.locator('.step-count')).to_have_text('3 of 3 complete' if valid else '0 of 3 complete')
            self.assertEqual(self.project()['skeleton'],original)
        # Guard history restoration even if stored completion records are true.
        inp.fill('')
        self.page.evaluate("history.pushState({route:'skeleton-bounce',projectId:'p1'},'');dispatchEvent(new PopStateEvent('popstate',{state:history.state}))")
        expect(self.page.locator('h1')).to_have_text('The Map')
        self.assertEqual(self.page.evaluate('history.state.route'),'map')
        self.assertEqual(self.project()['skeleton'],original)
        inp.fill('128.25');self.click('go','[data-route="structure"]')
        expect(self.page.locator('h1')).to_have_text('Structure')

    def test_each_setup_prerequisite_locks_and_restores_without_losing_work''',
    "live BPM Step states",
)

sub_once(
    r"    def test_each_setup_prerequisite_locks_and_restores_without_losing_work\(self\):.*?\n    def test_sheet_selection_preserves_nodes_geometry_focus_and_edit_keyboard",
    '''    def test_each_setup_prerequisite_locks_and_restores_without_losing_work(self):
        self.open('map', data=self.complete_fixture()); original=self.project()['skeleton']
        for field in ['reference','grid','firstListen']:
            self.expand_map_setup()
            self.click('toggle-setup',f'[data-field="{field}"]')
            expect(self.page.locator('.step-row[data-route="structure"]')).to_be_disabled()
            expect(self.page.locator('.step-count')).to_have_text('0 of 3 complete')
            self.click('toggle-setup',f'[data-field="{field}"]')
            expect(self.page.locator('.step-row[data-route="structure"]')).to_be_enabled()
            expect(self.page.locator('.step-count')).to_have_text('3 of 3 complete')
            self.assertEqual(self.project()['skeleton'],original)
        self.expand_map_setup()
        self.page.locator('#meterInput').evaluate("el=>{el.add(new Option('Choose',''));el.value='';el.dispatchEvent(new Event('change',{bubbles:true}))}")
        expect(self.page.locator('.step-row[data-route="structure"]')).to_be_disabled()
        self.page.locator('#meterInput').select_option('3/4')
        expect(self.page.locator('.step-row[data-route="structure"]')).to_be_enabled()

    def test_sheet_selection_preserves_nodes_geometry_focus_and_edit_keyboard''',
    "setup prerequisites Step states",
)

sub_once(
    r"    def test_parent_pills_and_back_follow_distinct_destinations\(self\):.*?\n    def test_boundary_truth_across_viewports_and_selection_cancel_noop",
    '''    def test_context_navigation_and_back_follow_distinct_destinations(self):
        self.open('map');self.click('go','[data-route="tracks"]');self.click('start-section-study')
        self.click('history-back');expect(self.page.locator('h1')).to_have_text('Tracks')
        self.page.go_forward();expect(self.page.locator('.study-pane')).to_be_visible()
        expect(self.page.locator('.context-nav-button')).to_have_text('The Map⌄')
        self.page.locator('.context-nav-button').click()
        expect(self.page.locator('.context-nav-sheet')).to_be_visible()
        expect(self.page.locator('.context-nav-row[data-route="project"]')).to_be_visible()
        expect(self.page.locator('.context-nav-row[data-route="roadmap"]')).to_be_visible()
        expect(self.page.locator('.context-nav-row[data-route="notes"]')).to_be_visible()
        self.page.locator('.context-nav-row[data-route="map"]').click()
        expect(self.page.locator('h1')).to_have_text('The Map')
        expect(self.page.locator('.context-nav-button')).to_contain_text('Migration song')
        self.canvas_route('project');expect(self.page.locator('h1')).to_have_text('Migration song')
        self.click('go','[data-route="roadmap"]');expect(self.page.locator('h2')).to_have_text('Roadmap')
        self.context.close()
        self.open('skeleton',data=self.complete_fixture());self.click('go','[data-route="skeleton-session"]')
        self.click('history-back');expect(self.page.locator('h2')).to_have_text('The Skeleton')
        self.click('go','[data-route="skeleton-session"]');self.click('go','[data-route="skeleton-draft"]')
        self.click('history-back');expect(self.page.locator('h2')).to_have_text('Session')

    def test_boundary_truth_across_viewports_and_selection_cancel_noop''',
    "context navigation history",
)

text = text.replace("('map','.state-control'),('map','.setup-listen-row'),('map','.list-row'),", "('map','.state-control'),('map','.setup-listen-row'),('map','.step-row'),", 1)
text = text.replace("if mode=='route':self.page.locator('.phase-pill').evaluate('el=>el.click()')", "if mode=='route':self.page.locator('[data-action=\"history-back\"]').evaluate('el=>el.click()')", 1)

text = text.replace("self.assertEqual(self.page.locator('.topbar .center').inner_text().strip(), '')\n        roadmap", "expect(self.page.locator('.topbar .center .context-nav-button')).to_contain_text('Migration song')\n        roadmap", 1)

sub_once(
    r"    def test_workflow_shell_continuity_project_map_structure_tracks\(self\):.*?\n\n\n\n    def test_project_actions_edit_reset_preserve_metadata_and_notes",
    '''    def test_workflow_shell_continuity_project_map_structure_tracks(self):
        self.open('project',width=820)
        cases=[
            ('project','Migration song','Test artist · Recreation','projects','',''),
            ('map','The Map','Understand the song before rebuilding it.','project','','Migration song'),
            ('structure','Structure','Build the song one section at a time.','map','Step 1 of 3','The Map'),
            ('tracks','Tracks','Select everything that appears somewhere in the song.','structure','Step 2 of 3','The Map'),
        ]
        anchor=None
        for route,title,subtitle,back,status,center in cases:
            with self.subTest(route=route):
                self.canvas_route(route)
                self.assertEqual(self.page.locator('.workflow-page').count(),1)
                self.assertEqual(self.page.locator('.phase-pill').count(),0)
                if center:
                    expect(self.page.locator('.topbar .center .context-nav-button')).to_contain_text(center)
                else:
                    self.assertEqual(self.page.locator('.topbar .center').inner_text(),'')
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



    def test_project_actions_edit_reset_preserve_metadata_and_notes''',
    "workflow shell context navigation",
)

text = text.replace("expect(card.locator('.foot')).to_contain_text('The Map · 2 of 3')", "expect(card.locator('.foot')).to_contain_text('The Map · Section Study')", 1)

path.write_text(text, encoding="utf-8")
