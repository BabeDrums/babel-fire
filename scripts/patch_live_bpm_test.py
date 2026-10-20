from pathlib import Path

path = Path('tests/test_v6.py')
s = path.read_text()
old = '''            self.assertEqual(self.project()['map']['setup']['tempo'],value)
            self.assertEqual(self.page.locator('[data-route="structure"]').is_enabled(),valid)
            expect(self.page.locator('.checkpoint-count')).to_have_text('3 of 3' if valid else '0 of 3')
            self.assertEqual(self.project()['skeleton'],original)'''
new = '''            self.assertEqual(self.project()['map']['setup']['tempo'],value)
            structure=self.page.locator('[data-route="structure"]')
            if valid:
                expect(structure).to_be_enabled()
            else:
                self.assertEqual(structure.count(),0)
                expect(self.page.locator('.checkpoint-locked-message')).to_have_text('Available after Song Setup')
            expect(self.page.locator('.checkpoint-count')).to_have_text('3 of 3' if valid else '0 of 3')
            self.assertEqual(self.project()['skeleton'],original)'''
if old not in s:
    raise SystemExit('live BPM validation assertion anchor not found')
path.write_text(s.replace(old,new,1))
