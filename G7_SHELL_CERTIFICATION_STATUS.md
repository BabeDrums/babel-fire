# G7 Shell Certification — Status Board

This file is the small mutable status board for `G7_SHELL_CERTIFICATION.md`. The certification contract defines what each category means and how it can be locked.

**Current phase:** final generic shell-polish candidate after physical iPhone/iPad review of exact G7 `5d6ab57` found two remaining interaction defects: routine text fields suppress normal iOS predictive/correction assistance, and split-action rows highlight only the pressed child region instead of the full parent row. No category is Locked and FIRE Core remains blocked.

| Category | State | Current note |
| --- | --- | --- |
| 1. Page frame | Candidate | Shared navigation/action row + large title/meta below remain intact. Current candidate does not alter page-header geometry. |
| 2. Typography | Candidate | Representative title/meta/row/supporting roles remain intact. Routine sheet headings stay hidden unless explicitly authored. |
| 3. Spacing and alignment | Candidate | PR #95 unified sheet rhythm to 12px related and 24px major/footer gaps. Current candidate only changes pressed-surface ownership, not spacing. |
| 4. Surfaces | Candidate | Adaptive compact bottom-sheet / regular centered-card surfaces remain intact. Split-action rows now use one parent-owned pressed surface rather than child-only patches. |
| 5. Actions | Candidate | Add/More semantics and circle treatment remain physically strong. Project and Structure split-action rows preserve separate actions while sharing one visual press state. |
| 6. Icons and accessories | Candidate | Symbol architecture remains unchanged. Physical review reports the current Back chevron looks great; do not reopen without new contradictory evidence. |
| 7. Controls and states | Candidate | Normal text assistance is restored for ordinary `.field` text inputs while specialized `inputmode` controls remain specialized. `state-primitives.css` remains sole progress-state art owner. |
| 8. Temporary UI | Candidate | PR #94/#95 adaptive sheet presentation and rhythm remain intact. Current candidate changes only generic text-entry assistance and split-row pressed feedback. |
| 9. Responsive behavior | Candidate | Same product logic must hold across iPhone and iPad/regular width; final physical sanity pass is required after exact deployment. |
| 10. Accessibility and motion | Candidate | Dialog labels/focus behavior remain intact. Text fields keep explicit capitalization and Next/Done progression while normal correction/spelling assistance returns. |

## Current evidence

- Developer Shell Test: `v7-preview/shell-test.html`.
- Shared symbol/accessory infrastructure: `v7-preview/shell-primitives.css`.
- Progress-state visual authority: `v7-preview/state-primitives.css`.
- Shared structural frame authority: `v7-preview/frame-primitives.css`, loaded by both real G7 and Shell Test after symbol/state layers.
- Shared routine text-entry normalization candidate: `v7-preview/input-primitives.js`, loaded only by real G7.
- Shell Test-only comparison styling remains isolated in `v7-preview/shell-test-experiments.css`.
- PR #88 merged the symbol architecture into real G7 at `109590e66038845849c832d3f4e3ea93ba5193c1`.
- PR #89 repaired header/action rows, 44px target vs 36px material, state visual ownership, Tempo/Meter lane, and modal framing at `d93729ff7a734035f25a6835323d19706f15186d`.
- PR #92 fixed generated-art host seating and merged at `8d26e015da05aa4836d31bde0cb5405f50e448c1`; exact Pages deployment and post-merge Static + Chromium 390/440/820 passed.
- PR #93 neutralized the final nested Back-host transform contradiction and merged at `c444d9b2a26d8e9196a901155586763c78af2f86`. Physical review says the chevron now looks great.
- PR #94 restored adaptive sheets and merged at `c4c69f7927a6c34221e3044d2660b5d50fc75726`.
- PR #95 unified sheet vertical rhythm and merged at `5d6ab57a6cd2109c873689c758d0e32b437cace1`:
  - related disclosure gap = 12px
  - major section gap = 24px
  - footer gap = 24px
  - single- and multi-action footers share one separation
  - Custom Section / Custom Bars use one related disclosure gap
  - Custom Bars no longer stacks a second field margin
  - exact pre/post merge Chromium 390/440/820 passed
- Physical iPhone/iPad review after PR #95 found the shell broadly solid and exposed only two new generic interaction issues:
  - normal iOS predictive/correction behavior is suppressed by legacy text-field attributes
  - Project/Structure split-action rows highlight only one child region during press
- Current candidate on `g7-final-shell-interaction-polish`:
  - ordinary `.field` text inputs remove restrictive autocomplete suppression and normalize `autocorrect="on"` + `spellcheck="true"`
  - `autocapitalize="words"` and explicit Enter-key progression remain owned by existing fixture markup/app behavior
  - specialized fields with `inputmode` (for example numeric Custom Bars) are not normalized as ordinary text fields
  - Project and Structure parent rows own the edge-to-edge pressed surface through shared frame CSS
  - project-open / project-actions / section-edit / reorder children no longer paint separate pressed backgrounds
  - symbol geometry, modal geometry/rhythm, product fixture content, V6, and FIRE Core remain untouched
- Fixture-specific wording/content decisions such as `Accurate` → `Confirmed` and Tracks/FX are outside this shell candidate.
- Liquid Glass remains rejected for the current FIRE shell direction.
- Setup / Structure / Tracks remain disposable product fixtures. Their current behavior does not approve FIRE Core architecture.

## Reliability gate

Do not merge the final shell-polish candidate unless the exact PR head passes:
- Authority/Handoff
- Static
- Chromium 390 / 440 / 820
- real G7 fixture coverage

The browser contract must prove:
- New Project ordinary text fields receive correction/spelling assistance instead of explicit suppression
- word capitalization and Title → Artist Enter progression remain intact
- specialized numeric/input-mode fields are not generalized
- pressing either side of Project split rows paints one parent-owned surface
- pressing edit or reorder in Structure paints one parent-owned surface
- child controls remain visually transparent during the parent press state
- PR #94/#95 adaptive sheet presentation/rhythm remain intact

After exact deployment, physical review is **iPhone first**, then iPad/regular width. If these final two shell defects are resolved and no new systemic contradiction appears, proceed to explicit shell approval/freeze instead of reopening fixture-specific product content.

Physical review must target the exact deployed revision shown by the G7/Shell Test build indicator.

## Freeze status

**0 / 10 Locked — G7 NOT FROZEN. FIRE Core breadboarding blocked.**

All ten categories are currently **Candidate**, not Locked. Candidate means there is a coherent implementation/evidence surface to review; it does not substitute for physical validation.

Do not change a category to Locked without satisfying `G7_SHELL_CERTIFICATION.md` and recording the physical-validation evidence that justified the change.
