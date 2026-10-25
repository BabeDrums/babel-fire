# G7 Shell Certification — Status Board

This file is the small mutable status board for `G7_SHELL_CERTIFICATION.md`. The certification contract defines what each category means and how it can be locked.

**Current phase:** real-G7 promotion of the physically approved symbol/button candidate under the repo reliability gate. Shell Test remains evidence, but no category is Locked yet and FIRE Core remains blocked.

| Category | State | Current note |
| --- | --- | --- |
| 1. Page frame | Candidate | Shell Test exposes sparse/normal/dense and long-content composition using the real page shell. Header trailing actions align to the large-title line instead of floating above it. Needs final compact/regular physical review before locking. |
| 2. Typography | Candidate | Representative title/meta/row/supporting roles and long wrapping are visible together in Shell Test. Needs final hierarchy review in real G7 context. |
| 3. Spacing and alignment | Candidate | Accepted horizontal accessory lanes, text anchors, hit targets, row geometry, and header geometry remain unchanged. The promoted symbol system removes the old global `+1px` baseline: symmetric artwork centers geometrically while symbol-specific optical data belongs to the symbol asset. |
| 4. Surfaces | Candidate | Existing grouped/selection/field/modal surfaces are exercised together in Shell Test. The symbol comparison card uses the standard FIRE grouped-surface tokens; Liquid Glass remains rejected. |
| 5. Actions | Candidate | Primary/secondary/destructive/add/management actions remain represented. Physical review chose the simple Circle treatment for standalone glyph buttons; the current promotion applies it to real G7 toolbar controls without boxing row accessories. |
| 6. Icons and accessories | Candidate | Physical review approved the refined Shell Test family for promotion. Real G7 now receives the same alignment architecture: Plus / More / Reorder use their geometric placement, Check owns its tiny intrinsic vertical metric, and Back / Forward own mirrored outward side bearings derived from the approved chevron optical anchor. Real-device validation of the promoted implementation is still required before locking. |
| 7. Controls and states | Candidate | Shell Test covers selection, segmented, field, selected/default/disabled/focusable examples using real G7 classes, and the real Setup fixture remains part of the browser regression gate. Error/custom depth may still extend if physical review exposes a need. |
| 8. Temporary UI | Candidate | Shell Test and the real Structure fixture exercise the same sheet/dialog classes. Shared primitives do not add unapproved action-divider or inset hairlines. Compact/regular presentation remains adaptive and needs physical review. |
| 9. Responsive behavior | Candidate | Shared-shell browser regressions exercise both Shell Test and real Project → Setup → Structure paths at 390/440/820 widths. The promoted symbol/button primitive must pass all three before merge and then physical iPhone/iPad review. |
| 10. Accessibility and motion | Candidate | Shared primitives retain ~44px targets, focus-visible behavior and reduced-motion baseline. Circular standalone controls preserve the 44px target. Needs physical/device accessibility review before locking. |

## Current evidence

- Developer Shell Test: `v7-preview/shell-test.html`.
- Shared shell/accessory infrastructure: `v7-preview/shell-primitives.css`, loaded by both G7 and Shell Test.
- Progress-state visual authority: `v7-preview/state-primitives.css`, loaded after the shared shell layer in both G7 and Shell Test.
- Shell Test-only comparison styling: `v7-preview/shell-test-experiments.css`; this file is intentionally not loaded by real G7.
- Physical iPhone review of `G7 · d00d146` rejected the production-wide `--symbol-optical-y: 1px` candidate as insufficiently systematic.
- PR #85 deployed `G7 · cf344e6` with a bounded inline-SVG normalization comparison.
- Physical iPad review isolated Back / Forward as the remaining symbol culprits while Plus / Check / Reorder / More read correctly enough to preserve.
- PR #86 deployed `G7 · 4e84bd5`; physical review rejected its inward chevron correction and preferred the simple Circle container over rounded-square / Liquid Glass directions.
- PR #87 deployed `G7 · b35b783` with the refined outward chevron optical-anchor candidate and the two-row Current-vs-Circle comparison. Babel physically reported that result looked really good and approved moving beyond the Shell Test experiment.
- The chevron family uses a symbol-owned optical metric rather than page/button nudges. In the experimental 24×24 geometry, Back's original hull anchor `x=13` and Forward's `x=11` resolve to mirrored outward seating when centered at `x=12`.
- The production translation bakes those approved side bearings into the Back / Forward SVG assets themselves; containers no longer translate the artwork.
- Plus / More / Reorder require no extra optical offset. Check owns its half-viewBox-unit vertical correction inside the canonical SVG asset rather than through a global CSS baseline.
- Current and Incomplete are symmetric state bars and center directly in their existing 24px state boxes; they do not inherit a glyph nudge.
- Standalone toolbar controls use the physically preferred simple Circle treatment: 44px target, 1px standard line, simple `#17171a` material, no glass. Row management / navigation / progress accessories remain unboxed according to their semantics.
- Liquid Glass is rejected for the current FIRE shell direction and is not retained as dormant production styling.
- Accepted horizontal accessory lanes and far-right ownership remain unchanged. Arrangement metadata such as `8 bars` stays supporting text beneath the item name; Reorder remains the sole far-right affordance.
- Progress-state language remains non-circular: Complete = canonical check only; Current = stronger 18px status bar; Incomplete/upcoming = quieter 18px status bar; Current has no persistent row-selection tint.
- The real-screen reliability gate covers Project → Setup → Structure at 390/440/820 widths so a shared primitive cannot pass only in Shell Test.
- G7 and Shell Test assets remain revisioned from the deployed commit so Safari/iOS cannot silently retain stale assets while the build indicator reports a newer deployment.
- Setup / Structure / Tracks remain disposable product fixtures. Their current behavior does not approve FIRE Core architecture.

## Reliability gate

A red regression is not merge-ready evidence. When a deliberate shell change invalidates an old regression expectation, reconcile the implementation, active authority, test contract, zero-context handoff, and deployed asset revisioning in the same change before merge.

**Shell Test passing is not sufficient for a shared-primitive merge.** Any shared primitive used by real G7 must also pass browser coverage in the actual G7 fixture path at the compact and regular-width regression matrix.

The current promotion must pass Authority/Handoff + Static + 390/440/820, merge/deploy, and then receive physical iPhone/iPad review in the actual G7 fixture before any category can lock.

Physical review must target the exact deployed revision shown by the G7/Shell Test build indicator.

## Freeze status

**0 / 10 Locked — G7 NOT FROZEN. FIRE Core breadboarding blocked.**

All ten categories are currently **Candidate**, not Locked. Candidate means there is a coherent implementation/evidence surface to review; it does not substitute for physical validation.

Do not change a category to Locked without satisfying `G7_SHELL_CERTIFICATION.md` and recording the physical-validation evidence that justified the change.
