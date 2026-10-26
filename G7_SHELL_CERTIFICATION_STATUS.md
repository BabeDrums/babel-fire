# G7 Shell Certification — Status Board

This file is the small mutable status board for `G7_SHELL_CERTIFICATION.md`. The certification contract defines what each category means and how it can be locked.

**Current phase:** adaptive sheet-system candidate after physical iPhone review confirmed the symbol/header cleanup is dramatically improved and the Back chevron now looks great. The remaining active contradiction is temporary UI presentation: compact/iPhone sheets were being forced into centered-card geometry by the shared frame. No category is Locked and FIRE Core remains blocked.

| Category | State | Current note |
| --- | --- | --- |
| 1. Page frame | Candidate | Shared navigation/action row + large title/meta below remain intact. Current sheet candidate does not alter page-header geometry. |
| 2. Typography | Candidate | Representative title/meta/row/supporting roles remain intact. Current sheet candidate removes only synthetic routine sheet headings; explicitly authored confirmation headings remain. |
| 3. Spacing and alignment | Candidate | PR #92 unified generated-art host seating; PR #93 removed the last Back-host transform contradiction. Current candidate changes only temporary-UI spacing/presentation. |
| 4. Surfaces | Candidate | Grouped/selection/field surfaces remain. Sheet surface becomes adaptive again: compact bottom sheet, regular-width centered card. |
| 5. Actions | Candidate | Add/More semantics and circle treatment remain physically strong. Sheet action hierarchy remains secondary to task content. |
| 6. Icons and accessories | Candidate | Symbol architecture remains unchanged. Physical review reports the current Back chevron looks great; do not reopen without new contradictory evidence. |
| 7. Controls and states | Candidate | `state-primitives.css` remains sole state-art owner. No state-art change is part of the sheet candidate. |
| 8. Temporary UI | Candidate | Active candidate restores compact bottom sheets, regular-width centered cards, removes automatic visible aria-label headings, preserves explicit confirmation headings, and keeps Custom disclosures attached/focusable. |
| 9. Responsive behavior | Candidate | Adaptive presentation is now the focus: `<700px` bottom sheet, `>=700px` centered card, same product logic. Must pass 390/440/820 and physical iPhone/iPad review. |
| 10. Accessibility and motion | Candidate | Dialog `aria-label` remains intact even when not duplicated visually. Focused Custom fields must remain reachable inside the internally scrollable sheet. |

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
- Current physical review finding is temporary UI rather than symbol geometry:
  - compact/iPhone sheets are centered instead of bottom-attached
  - `frame-primitives.css` is the direct cause because it overrides `.sheet-backdrop` to center at every width
  - base `styles.css` still contains the intended adaptive contract: bottom sheet by default, centered card at `min-width: 700px`
  - routine titles reappeared because `.sheet::before` displays `aria-label`
  - destructive confirmations already author their own `<h2>` title
  - Custom Section / Custom Bars logic already reveals and focuses the dependent field
- Current candidate on `g7-adaptive-sheet-system`:
  - compact `.sheet-backdrop` uses `align-items: flex-end`
  - compact sheet is edge-attached with top-only radius and no bottom border
  - regular width returns to centered full-radius card geometry
  - `.sheet::before` no longer renders visible content
  - dialog `aria-label` remains present for accessibility
  - sheet remains internally scrollable with focused-field scroll margins
  - Custom fields reveal directly beneath their triggering group
- Liquid Glass remains rejected for the current FIRE shell direction.
- Setup / Structure / Tracks remain disposable product fixtures. Their current behavior does not approve FIRE Core architecture.

## Reliability gate

Do not merge the adaptive sheet candidate unless the exact PR head passes:
- Authority/Handoff
- Static
- Chromium 390 / 440 / 820
- real G7 Project → Structure → Add Section coverage

The browser contract must prove compact bottom anchoring, regular-width centering, no synthetic routine heading, retained accessible label, and Custom field reveal/focus behavior.

After exact deployment, physical review is **iPhone first** across New Project, Project actions, Edit project, Add Track, Add Section/Edit Section Custom flows, destructive confirmations, and keyboard behavior. Then review iPad/regular-width presentation.

Physical review must target the exact deployed revision shown by the G7/Shell Test build indicator.

## Freeze status

**0 / 10 Locked — G7 NOT FROZEN. FIRE Core breadboarding blocked.**

All ten categories are currently **Candidate**, not Locked. Candidate means there is a coherent implementation/evidence surface to review; it does not substitute for physical validation.

Do not change a category to Locked without satisfying `G7_SHELL_CERTIFICATION.md` and recording the physical-validation evidence that justified the change.
