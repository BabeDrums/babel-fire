from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
styles_path = root / "styles.css"
test_path = root / "tests" / "test_v6.py"
nav_test_path = root / "tests" / "test_navigation_progression.py"
styles = styles_path.read_text(encoding="utf-8")
test = test_path.read_text(encoding="utf-8")
nav_test = nav_test_path.read_text(encoding="utf-8")


def replace_once(text, old, new, label):
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected one match, found {count}")
    return text.replace(old, new, 1)


def sub_once(text, pattern, repl, label):
    text, count = re.subn(pattern, repl, text, count=1, flags=re.S)
    if count != 1:
        raise RuntimeError(f"{label}: expected one match, found {count}")
    return text

# Preserve the old inline-style stacking contract in the canonical stylesheet.
styles = replace_once(
    styles,
    "  touch-action: pan-y;\n  z-index: 4;\n  cursor: ew-resize;",
    "  touch-action: pan-y;\n  z-index: 7;\n  cursor: ew-resize;",
    "timeline handle stacking",
)

# Section Study no longer has a direct phase-home link in its body; use the real context navigator.
test = replace_once(
    test,
    '''        # Route to Structure through the normal phase navigator.\n        self.click('go', '[data-route="map"]')\n        self.click('go', '[data-route="structure"]')''',
    '''        # Route to Structure through the real project context navigator.\n        self.click('open-context-nav')\n        self.click('context-go', '[data-route="map"]')\n        self.click('go', '[data-route="structure"]')''',
    "context navigation in section test",
)

# Backup/Restore was deliberately removed from the product; storage migration remains covered separately.
test = sub_once(
    test,
    r"\n    def test_import_v4_backup_uses_same_migration\(self\):.*?\n\n\n    def test_browser_back_tracks_the_entry_route_after_section_slides",
    "\n    def test_browser_back_tracks_the_entry_route_after_section_slides",
    "remove retired backup import regression",
)
test = sub_once(
    test,
    r"    def test_empty_projects_remain_empty_and_malformed_import_cannot_replace_data\(self\):.*?\n\n\n    def test_short_presence_blocks_select_remove_merge_and_undo",
    '''    def test_empty_projects_remain_empty_without_backup_ui(self):
        self.open('projects')
        self.assertEqual(self.page.locator('#importFile').count(), 0)
        self.assertEqual(self.page.locator('[data-action="export-backup"],[data-action="import-backup"]').count(), 0)
        self.page.evaluate("localStorage.setItem('production-projects-v1',JSON.stringify({version:4,currentProjectId:null,projects:[]}));history.replaceState({route:'projects'},'')")
        self.page.reload();expect(self.page.locator('h1')).to_have_text('Projects')
        self.assertEqual(self.db()['projects'],[])


    def test_short_presence_blocks_select_remove_merge_and_undo''',
    "replace malformed backup regression",
)

# This test is about desktop hover/focus, not the Step route itself; route directly to Structure.
test = replace_once(
    test,
    '''                self.page.locator('#tempoInput').fill('128.5');expect(self.page.locator('#tempoInput')).to_be_focused()
                self.click('go','[data-route="structure"]');self.click('open-add-section');self.settled_sheet()''',
    '''                self.page.locator('#tempoInput').fill('128.5');expect(self.page.locator('#tempoInput')).to_be_focused()
                self.canvas_route('structure');self.click('open-add-section');self.settled_sheet()''',
    "desktop hover Structure route",
)

# Cancel a live drag through an in-app route transition without asking browser history to leave the document.
test = replace_once(
    test,
    "                if mode=='route':self.page.locator('[data-action=\"history-back\"]').evaluate('el=>el.click()')",
    "                if mode=='route':self.canvas_route('tracks')",
    "drag route cancellation",
)

# Skeleton Phase Home uses the shared workflow h1 shell.
test = replace_once(
    test,
    "        self.click('history-back');expect(self.page.locator('h2')).to_have_text('The Skeleton')",
    "        self.click('history-back');expect(self.page.locator('h1')).to_have_text('The Skeleton')",
    "Skeleton shared Phase Home heading",
)

# After safety-normalizing the synthetic invalid route, resolve the newly mounted Step row before navigation.
test = replace_once(
    test,
    "        inp.fill('128.25');self.click('go','[data-route=\"structure\"]')\n        expect(self.page.locator('h1')).to_have_text('Structure')",
    "        self.page.locator('#tempoInput').fill('128.25')\n        structure=self.page.locator('.step-row[data-route=\"structure\"]');expect(structure).to_be_enabled();structure.click()\n        expect(self.page.locator('h1')).to_have_text('Structure')",
    "live BPM final Step navigation",
)

# The helper injects a synthetic previous route for every screen. Verify New Project's hierarchy fallback explicitly.
nav_test = replace_once(
    nav_test,
    '''    def test_new_project_back_label_resolves_to_projects(self):
        page = self.open("new-project")
        expect(page.locator('[data-action="history-back"]')).to_contain_text("Projects")''',
    '''    def test_new_project_back_fallback_resolves_to_projects(self):
        page = self.open("new-project")
        expect(page.locator('[data-action="history-back"]')).to_have_attribute("data-fallback-route", "projects")''',
    "New Project Back fallback",
)

styles_path.write_text(styles, encoding="utf-8")
test_path.write_text(test, encoding="utf-8")
nav_test_path.write_text(nav_test, encoding="utf-8")
