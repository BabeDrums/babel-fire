# G7 Shell Certification — Status Board

This file is the small mutable status board for `G7_SHELL_CERTIFICATION.md`. The certification contract defines what each category means and how it can be locked.

**Current phase:** sheet-rhythm candidate after physical iPhone review of PR #94 confirmed adaptive bottom-sheet presentation is much better but exposed inconsistent vertical spacing between sheet content, progressive disclosures, and footer actions. No category is Locked and FIRE Core remains blocked.

| Category | State | Current note |
| --- | --- | --- |
| 1. Page frame | Candidate | Shared navigation/action row + large title/meta below remain intact. Current sheet-rhythm candidate does not alter page-header geometry. |
| 2. Typography | Candidate | Representative title/meta/row/supporting roles remain intact. Routine sheet headings stay hidden unless explicitly authored. |
| 3. Spacing and alignment | Candidate | Active candidate unifies temporary-UI rhythm into 12px related disclosure gaps and 24px major/footer gaps instead of local per-sheet margins. |
| 4. Surfaces | Candidate | PR #94 restored adaptive sheet surfaces: compact bottom sheet, regular-width centered card. Current candidate changes only internal rhythm. |
| 5. Actions | Candidate | Add/More semantics and circle treatment remain physically strong. Sheet footers now share one 24px content-to-actions separation, including single-action menus. |
| 6. Icons and accessories | Candidate | Symbol architecture remains unchanged. Physical review reports the current Back chevron looks great; do not reopen without new contradictory evidence. |
| 7. Controls and states | Candidate | `state-primitives.css` remains sole state-art owner. No state-art change is part of the sheet-rhythm candidate. |
| 8. Temporary UI | Candidate | PR #94 restored adaptive presentation. Current candidate unifies vertical spacing and removes the Custom Bars accidental double gap. |
| 9. Responsive behavior | Candidate | Same sheet rhythm must hold across `<700px` bottom sheets and `>=700px` centered cards, with keyboard/focus movement preserving internal relationships. |
| 10. Accessibility and motion | Candidate | Dialog labels remain semantic; focused Custom fields remain reachable inside the internally scrollable sheet. No accessibility behavior is removed. |

## Current evidence

- Developer Shell Test: `v7-preview/shell-test.html`.
- Shared symbol/accessory infrastructure: `v7-preview/shell-primitives.css`.
- Progress-state visual authority: `v7-preview/state-primitives.css`.
- Shared structural frame authority: `v7-preview/frame-primitives.css`, loaded by both real G7 and Shell Test after symbol/state layers.
- Shell Test-only comparison styling remains isolated in `v7-preview/shell-test-experiments.css`.
- PR #87 deployed the refined outward chevron optical-anchor candidate; physical review reported the symbol family looked strong enough to promote.
- PR #88 merged the symbol architecture into real G7 at `109590e66038845849c832d3f4e3ea93ba5193c1`.
- PR #89 repaired header/action rows, 44px target vs 36px material, state visual ownership, Tempo/Meter lane, and modal framing at `d93729ff7a734035f25a6835323d19706f15186d`.
- PR #92 fixed generated-art host seating and merged at `8d26e015da05aa4836d31bde0cb5405f50e448c1`; exact Pages deployment and post-merge Static + Chromium 390/440/820 passed.
- PR #93 neutralized the final nested Back-host transform contradiction and merged at `c444d9b2a26d8e9196a901155586763c78af2f86`. Exact Pages deploy succeeded; physical review says the chevron now looks great.
- PR #94 restored adaptive sheets and merged at `c4c69f7927a6c34221e3044d2660b5d50fc75726`:
  - compact `<700px` presentation is bottom-attached
  - regular `>=700px` presentation is centered
  - routine `aria-label` headings are not visually duplicated
  - explicit destructive headings remain
  - Custom disclosure/focus behavior remains intact
  - pre-merge Authority/Handoff + Static + Chromium 390/440/820 passed and exact Pages deployment succeeded
- Physical iPhone review of PR #94 found the adaptive direction much better but exposed inconsistent rhythm:
  - project-type → fields, content-group → content-group, and content → footer do not all share one system
  - `.sheet-actions.single-action` currently differs from normal footers
  - Custom Bars stacks its wrapper gap with `.numeric-field` top margin
- Current candidate on `g7-sheet-rhythm-system`:
  - related disclosure gap = 12px
  - major section gap = 24px
  - footer gap = 24px
  - normal and single-action footers share the same separation
  - project type and major content groups use the same major rhythm
  - Custom Section / Custom Bars attach with the same related gap
  - Custom Bars removes the nested field margin so one relationship has one spacing owner
- Liquid Glass remains rejected for the current FIRE shell direction.
- Setup / Structure / Tracks remain disposable product fixtures. Their current behavior does not approve FIRE Core architecture.

## Reliability gate

Do not merge the sheet-rhythm candidate unless the exact PR head passes:
- Authority/Handoff
- Static
- Chromium 390 / 440 / 820
- real G7 fixture coverage

The browser contract must prove:
- New Project uses 24px project-type → fields → footer rhythm
- Project actions uses the same 24px content → single-action footer rhythm
- Add Section uses 24px major section/footer gaps
- Custom Section / Custom Bars use 12px related gaps
- Custom Bars does not retain a second local top margin
- PR #94 compact/regular presentation remains intact

After exact deployment, physical review is **iPhone first** across New Project, Project actions, Edit project, Add Track, Add Section/Edit Section Custom flows, and keyboard behavior. Then review iPad/regular width.

Physical review must target the exact deployed revision shown by the G7/Shell Test build indicator.

## Freeze status

**0 / 10 Locked — G7 NOT FROZEN. FIRE Core breadboarding blocked.**

All ten categories are currently **Candidate**, not Locked. Candidate means there is a coherent implementation/evidence surface to review; it does not substitute for physical validation.

Do not change a category to Locked without satisfying `G7_SHELL_CERTIFICATION.md` and recording the physical-validation evidence that justified the change.
