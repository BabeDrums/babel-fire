# G7 Shell Certification — Status Board

This file is the small mutable status board for `G7_SHELL_CERTIFICATION.md`. The certification contract defines what each category means and how it can be locked.

**Current phase:** host-centering candidate after iPad physical review of deployed `G7 · f512b90`. The symbol artwork itself remains the preferred direction, but generated symbol/state artwork is not yet physically consistent across every host. No category is Locked and FIRE Core remains blocked.

| Category | State | Current note |
| --- | --- | --- |
| 1. Page frame | Candidate | PR #89 restored one shared navigation/action row with large title/meta below it. The current candidate preserves that frame and removes a dead shell-level header offset rule so structural placement has one owner. Exact candidate physical review still required. |
| 2. Typography | Candidate | Representative title/meta/row/supporting roles remain intact. No new type role is introduced; sparse Shell Test copy now receives intentional internal inset instead of touching its group edge. |
| 3. Spacing and alignment | Candidate | iPad review exposed a remaining host-centering inconsistency: identical generated artwork can sit high in toolbar/action/row/state contexts even while the comparison specimen looks correct. Candidate makes host centering explicit while preserving accepted x-lanes and row/text geometry. |
| 4. Surfaces | Candidate | Existing grouped/selection/field/modal surfaces remain exercised. Toolbar material remains separated from its 44px interaction frame; no surface redesign is part of this candidate. |
| 5. Actions | Candidate | Add/More semantics and circle treatment remain. Candidate changes only how generated artwork is seated inside the existing host; 44px targets and 36px visible material remain fixed. |
| 6. Icons and accessories | Candidate | Intrinsic symbol architecture remains: Plus/More/Reorder geometric, Check with intrinsic vertical metric, Back/Forward with mirrored outward side bearings. New candidate adds one host-centering contract so container context cannot vertically move identical artwork. |
| 7. Controls and states | Candidate | `state-primitives.css` remains sole state-art owner. Complete/Current/Incomplete now use the same explicit host-centering rule inside the 24px state box; Current's bar and checks require exact-device revalidation. Tempo/Meter lane remains unchanged. |
| 8. Temporary UI | Candidate | Compact sheets still use the bounded small-viewport-safe frame and visible task title. Shell Test removes redundant helper narration; modal behavior is otherwise unchanged. |
| 9. Responsive behavior | Candidate | Previous exact builds passed 390/440/820. This candidate must pass the same matrix in Shell Test and real G7, then receive iPhone-first and iPad physical review. |
| 10. Accessibility and motion | Candidate | 44px toolbar hit targets remain unchanged and host centering does not alter hit geometry. Existing focus-visible/reduced-motion behavior remains; final physical/device accessibility review is still required. |

## Current evidence

- Developer Shell Test: `v7-preview/shell-test.html`.
- Shared symbol/accessory infrastructure: `v7-preview/shell-primitives.css`.
- Progress-state visual authority: `v7-preview/state-primitives.css`.
- Shared structural frame authority: `v7-preview/frame-primitives.css`, loaded by both real G7 and Shell Test after symbol/state layers.
- Shell Test-only comparison styling remains isolated in `v7-preview/shell-test-experiments.css`.
- PR #87 deployed `G7 · b35b783` with the refined outward chevron optical-anchor candidate; physical review reported the symbol family looked strong enough to promote.
- PR #88 merged the symbol architecture into real G7 at `109590e66038845849c832d3f4e3ea93ba5193c1`.
- Physical iPhone review of that build exposed broader frame contradictions rather than a reason to reopen the symbol metrics.
- PR #89 repaired header/action rows, 44px target vs 36px material, state visual ownership, Tempo/Meter lane, and modal framing at `d93729ff7a734035f25a6835323d19706f15186d`; pre/post Static + Chromium 390/440/820 and exact Pages deploy passed.
- PR #91 later simplified authority/documentation only at `f512b90065c58a2426e79e4a99941a22b22fe35e`; it made no G7/V6 runtime change. Exact Pages deploy and post-merge Static + Chromium 390/440/820 passed.
- Physical iPad review of `G7 · f512b90` found:
  - normalized comparison glyphs look well seated
  - toolbar/action `+` and `•••` read high
  - managed-row `•••` reads high
  - Current's status bar reads clearly high and checks may also be slightly inconsistent
  - Back/Forward look good and should be preserved
  - the prior legacy Current-arrow fallthrough remains resolved
- Code diagnosis: comparison symbols are block inline SVGs centered by Grid, while real G7 generated pseudo-elements were allowed to participate in host layout differently; the frame layer also changed toolbar pseudo-element positioning after the symbol layer loaded.
- Candidate fix: **stable host box → absolute inset/auto-margin centering → intrinsic symbol metric inside the asset**. No page-specific or glyph-specific vertical nudges are introduced.
- Candidate cleanup also removes the dead `--header-action-offset`/shell-level toolbar translation rule, removes the Shell Test adaptive-dialog helper sentence, and adds intentional inset to the sparse composition fixture.
- Liquid Glass remains rejected for the current FIRE shell direction.
- Accepted horizontal accessory lanes and far-right ownership remain unchanged. Arrangement metadata such as `8 bars` stays supporting text beneath the item name; Reorder remains the sole far-right affordance.
- Setup / Structure / Tracks remain disposable product fixtures. Their current behavior does not approve FIRE Core architecture.

## Reliability gate

Do not merge the host-centering candidate unless the exact PR head passes:
- Authority/Handoff
- Static
- Chromium 390 / 440 / 820
- Shell Test coverage
- real G7 Project → Setup → Structure coverage

A red regression is not merge-ready evidence. When a deliberate shell change invalidates an old regression expectation, reconcile implementation, active authority, test contract, zero-context handoff, and deployed asset revisioning in the same change.

**Shell Test passing is not sufficient for a shared-primitive merge.** Any shared primitive used by real G7 must also pass browser coverage in the actual G7 fixture path at compact and regular-width sizes.

After exact deployment, physical review is **iPhone first, then iPad/regular width**. Do not infer iPhone success from the iPad evidence that motivated this candidate.

Physical review must target the exact deployed revision shown by the G7/Shell Test build indicator.

## Freeze status

**0 / 10 Locked — G7 NOT FROZEN. FIRE Core breadboarding blocked.**

All ten categories are currently **Candidate**, not Locked. Candidate means there is a coherent implementation/evidence surface to review; it does not substitute for physical validation.

Do not change a category to Locked without satisfying `G7_SHELL_CERTIFICATION.md` and recording the physical-validation evidence that justified the change.
