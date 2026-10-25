# G7 Shell Certification — Status Board

This file is the small mutable status board for `G7_SHELL_CERTIFICATION.md`. The certification contract defines what each category means and how it can be locked.

**Current phase:** exact-build physical review after the shared frame repair merged and deployed in PR #89. Shell Test and browser regressions are green evidence, but no category is Locked yet and FIRE Core remains blocked.

| Category | State | Current note |
| --- | --- | --- |
| 1. Page frame | Candidate | PR #89 restored one shared navigation/action row with the large title/meta in a separate row beneath it. Browser evidence is green; exact-build iPhone/iPad physical review is still required before lock. |
| 2. Typography | Candidate | Representative title/meta/row/supporting roles remain intact; the frame repair changed their structural relationship rather than introducing new type roles. Needs final hierarchy review in real G7 context. |
| 3. Spacing and alignment | Candidate | Symbol-owned optical metrics remain in place. PR #89 removed header-side vertical drift, keeps 44px interaction frames, uses a quieter 36px visible toolbar material, and preserves accepted row/accessory horizontal lanes. Physical review remains the deciding evidence. |
| 4. Surfaces | Candidate | Existing grouped/selection/field/modal surfaces remain exercised. Toolbar material is separated from its interaction frame, and compact sheets use one centered bounded surface rather than bottom-edge anchoring. |
| 5. Actions | Candidate | Standalone glyph actions retain circular semantics without making the full 44px hit region visually heavy. Edit/manage sheet actions now preserve primary-task hierarchy rather than reading as equal stacked slabs. |
| 6. Icons and accessories | Candidate | The promoted symbol architecture remains the current direction: Plus / More / Reorder use geometric placement, Check owns its intrinsic vertical metric, and Back / Forward own mirrored outward side bearings. PR #89 intentionally repaired the surrounding frame rather than reopening symbol nudging. |
| 7. Controls and states | Candidate | Current/Incomplete/Complete remain owned by `state-primitives.css`. The frame layer suppresses legacy text glyph leakage so pseudo-element state artwork is the only visible owner. Tempo and Meter share one stable trailing-value lane instead of content-sized mini-buttons. |
| 8. Temporary UI | Candidate | Compact sheets center within a small-viewport-safe frame using `svh`, full rounded geometry, and a visible task title sourced from the existing dialog label. This avoids tying modal usability to Safari's dynamic bottom toolbar. |
| 9. Responsive behavior | Candidate | Shell Test and the real Project → Setup → Structure path passed the 390/440/820 matrix before merge and again after merge on the exact deployed commit. Physical iPhone/iPad review is still required. |
| 10. Accessibility and motion | Candidate | 44px toolbar hit targets are preserved even though visible material is smaller. Existing focus-visible/reduced-motion behavior remains; final physical/device accessibility review is still required. |

## Current evidence

- Developer Shell Test: `v7-preview/shell-test.html`.
- Shared symbol/accessory infrastructure: `v7-preview/shell-primitives.css`.
- Progress-state visual authority: `v7-preview/state-primitives.css`.
- Shared structural frame authority: `v7-preview/frame-primitives.css`, loaded by both real G7 and Shell Test after symbol/state layers.
- Shell Test-only comparison styling remains isolated in `v7-preview/shell-test-experiments.css`.
- PR #87 deployed `G7 · b35b783` with the refined outward chevron optical-anchor candidate; physical review reported the symbol family looked strong enough to promote.
- PR #88 merged the symbol architecture into real G7 at `109590e66038845849c832d3f4e3ea93ba5193c1`.
- Physical iPhone review of that real-G7 build found the symbol artwork largely convincing but exposed broader frame contradictions: Back and trailing actions occupied different vertical lanes, the full 44px circle carried too much resting visual mass, Current could reveal a legacy arrow beneath its status bar, Tempo/Meter used inconsistent content-sized value boxes, and compact edit sheets collided visually with mobile browser chrome / over-emphasized peer actions.
- PR #89 repaired those contradictions at the shared-primitive level and merged to `main` as `d93729ff7a734035f25a6835323d19706f15186d`.
- PR #89 passed Authority/Handoff + Static + Chromium 390/440/820 before merge, including Shell Test and the real G7 Project → Setup → Structure path.
- GitHub Pages successfully deployed the exact `d93729ff…` merge commit.
- Post-merge Static + Chromium 390/440/820 passed again on that exact merge SHA.
- Current frame rule: **one navigation row → separate large-title/meta row**. No side-specific header translation is allowed.
- Current control rule: **44px interaction frame → smaller visible material → symbol-owned optical placement**. Hit geometry and visible material geometry are intentionally separate.
- Current state rule: state artwork has one visible owner; legacy text content must not be able to reappear through specificity drift.
- Current editable-value rule: Tempo and Meter share one fixed trailing lane; content length does not determine control width.
- Current modal rule: compact sheets center within a small-viewport-safe frame rather than anchoring a large surface to Safari's dynamic bottom edge.
- Liquid Glass remains rejected for the current FIRE shell direction.
- Accepted horizontal accessory lanes and far-right ownership remain unchanged. Arrangement metadata such as `8 bars` stays supporting text beneath the item name; Reorder remains the sole far-right affordance.
- Setup / Structure / Tracks remain disposable product fixtures. Their current behavior does not approve FIRE Core architecture.

## Reliability gate

The PR #89 engineering gate is complete and green. Do not repeat that repair unless new physical evidence proves a remaining systemic contradiction.

A red regression is not merge-ready evidence. When a deliberate shell change invalidates an old regression expectation, reconcile the implementation, active authority, test contract, zero-context handoff, and deployed asset revisioning in the same change before merge.

**Shell Test passing is not sufficient for a shared-primitive merge.** Any shared primitive used by real G7 must also pass browser coverage in the actual G7 fixture path at the compact and regular-width regression matrix.

The current next gate is physical review of the exact deployed `G7 · d93729f` build on **iPhone first, then iPad/regular width**. Any discovered issue must be classified before changing code: shared-frame, symbol/state, page-local, or disposable product-fixture content.

Physical review must target the exact deployed revision shown by the G7/Shell Test build indicator.

## Freeze status

**0 / 10 Locked — G7 NOT FROZEN. FIRE Core breadboarding blocked.**

All ten categories are currently **Candidate**, not Locked. Candidate means there is a coherent implementation/evidence surface to review; it does not substitute for physical validation.

Do not change a category to Locked without satisfying `G7_SHELL_CERTIFICATION.md` and recording the physical-validation evidence that justified the change.
