from pathlib import Path

path = Path("tests/test_v6.py")
text = path.read_text(encoding="utf-8")


def replace_once(old, new, label):
    global text
    if old not in text:
        raise SystemExit(f"missing source block: {label}")
    text = text.replace(old, new, 1)

replace_once(
'''    def click(self, action, extra=''):
        button=self.page.locator(f'[data-action="{action}"]{extra}')
        button.click()

    def db(self):
''',
'''    def click(self, action, extra=''):
        button=self.page.locator(f'[data-action="{action}"]{extra}')
        button.click()

    def expand_map_setup(self):
        disclosure=self.page.locator('[data-action="toggle-setup-disclosure"]')
        if disclosure.count():
            disclosure.click()
            expect(self.page.locator('#tempoInput')).to_be_visible()

    def db(self):
''',
"map setup test helper",
)

replace_once(
'''    def test_live_bpm_validation_progress_caret_and_route_guards(self):
        self.open('map', data=self.complete_fixture())
        inp=self.page.locator('#tempoInput'); inp.focus()
''',
'''    def test_live_bpm_validation_progress_caret_and_route_guards(self):
        self.open('map', data=self.complete_fixture());self.expand_map_setup()
        inp=self.page.locator('#tempoInput'); inp.focus()
''',
"live bpm opens disclosure",
)

replace_once(
'''        self.open('map', data=self.complete_fixture()); original=self.project()['skeleton']
        for field in ['reference','grid','firstListen']:
            self.click('toggle-setup',f'[data-field="{field}"]')
''',
'''        self.open('map', data=self.complete_fixture()); original=self.project()['skeleton']
        for field in ['reference','grid','firstListen']:
            self.expand_map_setup()
            self.click('toggle-setup',f'[data-field="{field}"]')
''',
"prerequisite loop opens disclosure",
)

replace_once(
'''            expect(self.page.locator('.checkpoint-count')).to_have_text('3 of 3')
            self.assertEqual(self.project()['skeleton'],original)
        self.page.locator('#meterInput').evaluate("el=>{el.add(new Option('Choose',''));el.value='';el.dispatchEvent(new Event('change',{bubbles:true}))}")
''',
'''            expect(self.page.locator('.checkpoint-count')).to_have_text('3 of 3')
            self.assertEqual(self.project()['skeleton'],original)
        self.expand_map_setup()
        self.page.locator('#meterInput').evaluate("el=>{el.add(new Option('Choose',''));el.value='';el.dispatchEvent(new Event('change',{bubbles:true}))}")
''',
"meter test opens disclosure",
)

replace_once(
'''                self.click('open-project','[data-id="p1"]');self.page.locator('.quick-card[data-route="roadmap"]').click();self.click('go','[data-route="map"]')
                self.page.locator('#tempoInput').fill('128.5');expect(self.page.locator('#tempoInput')).to_be_focused()
''',
'''                self.click('open-project','[data-id="p1"]');self.page.locator('.quick-card[data-route="roadmap"]').click();self.click('go','[data-route="map"]');self.expand_map_setup()
                self.page.locator('#tempoInput').fill('128.5');expect(self.page.locator('#tempoInput')).to_be_focused()
''',
"mouse map edit opens disclosure",
)

replace_once(
'''            with self.subTest(route=route,selector=selector):
                self.canvas_route(route);node=self.page.locator(selector).first
                node.scroll_into_view_if_needed();before=node.bounding_box()
''',
'''            with self.subTest(route=route,selector=selector):
                self.canvas_route(route)
                if route == 'map' and selector in ('.state-control','.action-card'):
                    self.expand_map_setup()
                node=self.page.locator(selector).first
                node.scroll_into_view_if_needed();before=node.bounding_box()
''',
"shape tests open map disclosure when testing setup controls",
)

path.write_text(text, encoding="utf-8")
print("updated V6 regressions for adaptive Map disclosure")
