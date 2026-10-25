# G7 Shell Certification — Status Board

This file is the small mutable status board for `G7_SHELL_CERTIFICATION.md`. The certification contract defines what each category means and how it can be locked.

**Current phase:** shared frame repair after physical iPhone review of the real-G7 symbol promotion. Shell Test remains evidence, but no category is Locked yet and FIRE Core remains blocked.

| Category | State | Current note |
| --- | --- | --- |
| 1. Page frame | Candidate | Physical review exposed the old header split: Back stayed in the toolbar row while trailing Add/More was translated down into the title line. The current candidate restores one shared navigation row with the large title/meta in a separate row beneath it. |
| 2. Typography | Candidate | Representative title/meta/row/supporting roles remain intact; the frame repair changes their structural relationship rather than introducing new type roles. Needs final hierarchy review in real G7 context. |
| 3. Spacing and alignment | Candidate | Symbol-owned optical metrics remain in place. The new frame candidate removes header-side vertical drift, keeps 44px interaction frames, uses a quieter 36px visible toolbar material, and preserves accepted row/accessory horizontal lanes. |
| 4. Surfaces | Candidate | Existing grouped/selection/field/modal surfaces remain exercised. Toolbar material is now separated from its interaction frame, and compact sheets use one centered bounded surface rather than bottom-edge anchoring. |
| 5. Actions | Candidate | Standalone glyph actions retain circular semantics but no longer make the full 44px hit region visually heavy. Edit/manage sheet actions are being reviewed as task hierarchy rather than equal visual slabs. |
| 6. Icons and accessories | Candidate | The promoted symbol architecture remains the current direction: Plus / More / Reorder use geometric placement, Check owns its intrinsic vertical metric, and Back / Forward own mirrored outward side bearings. Current physical defects are frame-level, not evidence to reopen symbol nudging. |
| 7. Controls and states | Candidate | Current/Incomplete/Complete remain owned by `state-primitives.css`. The frame layer now explicitly suppresses legacy text glyph leakage so pseudo-element state artwork is the only visible owner. Tempo and Meter share one stable trailing-value lane instead of content-sized mini-buttons. |
| 8. Temporary UI | Candidate | Compact sheets are centered within a small-viewport-safe frame using `svh`, full rounded geometry, and a visible task title sourced from the existing dialog label. This avoids tying modal usability to Safari's dynamic bottom toolbar. |
| 9. Responsive behavior | Candidate | Shared-shell browser regressions must exercise Shell Test and the real Project → Setup → Structure path at 390/440/820. The frame candidate must preserve one product logic while remaining visually coherent on compact and regular widths. |
| 10. Accessibility and motion | Candidate | 44px toolbar hit targets are preserved even though visible material becomes smaller. Existing focus-visible/reduced-motion behavior remains; final physical/device accessibility review is still required. |

## Current evidence

- Developer Shell Test: `v7-preview/shell-test.html`.
- Shared symbol/accessory infrastructure: `v7-preview/shell-primitives.css`.
- Progress-state visual authority: `v7-preview/state-primitives.css`.
- Shared structural frame authority for the active candidate: `v7-preview/frame-primitives.css`, loaded by both real G7 and Shell Test after symbol/state layers.
- Shell Test-only comparison styling remains isolated in `v7-preview/shell-test-experiments.css`.
- PR #87 deployed `G7 · b35b783` with the refined outward chevron optical-anchor candidate; physical review reported the symbol family looked strong enough to promote.
- PR #88 merged the symbol architecture into real G7 at `109590e66038845849c832d3f4e3ea93ba5193c1`.
- Physical iPhone review of that real-G7 build found the symbol artwork largely convincing but exposed broader frame contradictions: Back and trailing actions occupied different vertical lanes, the full 44px circle carried too much resting visual mass, Current could reveal a legacy arrow beneath its status bar, Tempo/Meter used inconsistent content-sized value boxes, and compact edit sheets collided visually with mobile browser chrome / over-emphasized peer actions.
- Root cause for the header defect is structural, not optical: `toolbar-trailing` had a dedicated downward translation while Back remained in the toolbar row.
- Current repair rule: **one navigation row → separate large-title/meta row**. No side-specific header translation is allowed.
- Current control rule: **44px interaction frame → smaller visible material → symbol-owned optical placement**. Hit geometry and visible material geometry are intentionally separate.
- Current state rule: state artwork has one visible owner; legacy text content must not be able to reappear through specificity drift.
- Current editable-value rule: Tempo and Meter share one fixed trailing lane; content length does not determine control width.
- Current modal rule: compact sheets center within a small-viewport-safe frame rather than anchoring a large surface to Safari's dynamic bottom edge.
- Liquid Glass remains rejected for the current FIRE shell direction.
- Accepted horizontal accessory lanes and far-right ownership remain unchanged. Arrangement metadata such as `8 bars` stays supporting text beneath the item name; Reorder remains the sole far-right affordance.
- Setup / Structure / Tracks remain disposable product fixtures. Their current behavior does not approve FIRE Core architecture.

## Reliability gate

A red regression is not merge-ready evidence. When a deliberate shell change invalidates an old regression expectation, reconcile the implementation, active authority, test contract, zero-context handoff, and deployed asset revisioning in the same change before merge.

**Shell Test passing is not sufficient for a shared-primitive merge.** Any shared primitive used by real G7 must also pass browser coverage in the actual G7 fixture path at the compact and regular-width regression matrix.

The current frame repair must pass **Authority/Handoff + Static + 390/440/820**, merge/deploy, and then receive physical iPhone/iPad review in the actual G7 fixture before any category can lock.

Physical review must target the exact deployed revision shown by the G7/Shell Test build indicator.

## Freeze status

**0 / 10 Locked — G7 NOT FROZEN. FIRE Core breadboarding blocked.**

All ten categories are currently **Candidate**, not Locked. Candidate means there is a coherent implementation/evidence surface to review; it does not substitute for physical validation.

Do not change a category to Locked without satisfying `G7_SHELL_CERTIFICATION.md` and recording the physical-validation evidence that justified the change.
