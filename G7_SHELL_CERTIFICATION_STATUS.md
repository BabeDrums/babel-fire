# G7 Shell Certification — Status Board

This file is the small mutable status board for `G7_SHELL_CERTIFICATION.md`. The certification contract defines what each category means and how it can be locked.

**Current phase:** fundamentals physical review under the repo reliability gate. Shell Test is useful evidence, but no category is Locked yet and FIRE Core remains blocked.

| Category | State | Current note |
| --- | --- | --- |
| 1. Page frame | Candidate | Shell Test exposes sparse/normal/dense and long-content composition using the real page shell. Header trailing actions align to the large-title line instead of floating above it. Needs final compact/regular physical review before locking. |
| 2. Typography | Candidate | Representative title/meta/row/supporting roles and long wrapping are visible together in Shell Test. Needs final hierarchy review in real G7 context. |
| 3. Spacing and alignment | Candidate | Accepted horizontal accessory lanes, text anchors, hit targets, row geometry, and header geometry remain unchanged. Geometry-derived symbol centering now reads correctly for Plus / Check / Reorder / More; Shell Test applies one mirrored inward correction only to Back / Forward for the next physical pass. |
| 4. Surfaces | Candidate | Existing grouped/selection/field/modal surfaces are exercised together in Shell Test. The symbol comparison card now uses the standard FIRE grouped-surface tokens; the special ambient/glass substrate is rejected and removed. |
| 5. Actions | Candidate | Primary/secondary/destructive/add/management actions remain represented. The symbol experiment now compares only Current rounded-square vs plain Circle with the same simple material and 44px targets. Circle is physically preferred but not yet promoted into real G7. |
| 6. Icons and accessories | Candidate | Standard production glyphs still use the current canonical Lucide-based family and real G7 remains unchanged. In Shell Test, visible-bounds normalization is retained; physical review isolated Back / Forward as the only remaining symbol offenders, so they receive one equal-and-opposite inward optical correction pending validation. |
| 7. Controls and states | Candidate | Shell Test covers selection, segmented, field, selected/default/disabled/focusable examples using real G7 classes, and the real Setup fixture remains part of the browser regression gate. Error/custom depth may still extend if physical review exposes a need. |
| 8. Temporary UI | Candidate | Shell Test and the real Structure fixture exercise the same sheet/dialog classes. Shared primitives do not add unapproved action-divider or inset hairlines. Compact/regular presentation remains adaptive and needs physical review. |
| 9. Responsive behavior | Candidate | Shared-shell browser regressions exercise both Shell Test and real Project → Setup → Structure paths at 390/440/820 widths. The refined two-row comparison must remain usable at compact and regular widths before merge/deploy review. |
| 10. Accessibility and motion | Candidate | Shared primitives retain ~44px targets, focus-visible behavior and reduced-motion baseline. The experimental symbol rows keep 44px controls and suppress transitions under reduced motion. Needs physical/device accessibility review before locking. |

## Current evidence

- Developer Shell Test: `v7-preview/shell-test.html`.
- Shared shell/accessory infrastructure: `v7-preview/shell-primitives.css`, loaded by both G7 and Shell Test.
- Progress-state visual authority: `v7-preview/state-primitives.css`, loaded after the shared shell layer in both G7 and Shell Test.
- Shell Test-only experiment styling: `v7-preview/shell-test-experiments.css`; this file is intentionally not loaded by real G7.
- Real G7 still uses the PR #83 `--symbol-optical-y: 1px` candidate while the experiment is evaluated. The experiment does not silently change production controls.
- Physical iPhone review of `G7 · d00d146` found the production family close but still slightly off, so the global `+1px` candidate is not approved.
- PR #85 deployed `G7 · cf344e6` with a Shell Test-only inline SVG palette using automatic visible-bounds centering.
- Physical iPad review of `G7 · cf344e6` found Plus / Check / Reorder / More convincing enough to preserve while isolating Back / Forward as the remaining symbol culprits.
- Back / Forward in the refined experiment share one mirrored optical rule: after geometry centering, Back shifts inward/right and Forward shifts inward/left by the same amount. This remains Shell Test evidence only.
- The comparison now has two rows only: Current rounded-square and plain Circle. Symbol source, normalized placement, icon size, simple material, and 44px hit target remain consistent across them.
- Liquid Glass is rejected for the current FIRE shell direction. The glass row, glass-only material rules, and ambient comparison substrate are removed rather than retained as dormant styling.
- The comparison card itself uses the same standard `--surface`, `--line`, and `--group-radius` tokens as normal FIRE grouped containers.
- Physical review currently prefers the plain Circle treatment, but it is not yet an approved real-G7 primitive. The refined chevron pass must be reviewed first.
- Accepted horizontal accessory lanes and far-right ownership remain unchanged. Arrangement metadata such as `8 bars` stays supporting text beneath the item name; Reorder remains the sole far-right affordance.
- Progress-state language remains non-circular: Complete = canonical check only; Current = stronger 18px status bar; Incomplete/upcoming = quieter 18px status bar; Current has no persistent row-selection tint.
- The real-screen reliability gate continues to cover Project → Setup → Structure at 390/440/820 widths so a Shell Test experiment cannot silently break shared product primitives.
- G7 and Shell Test assets remain revisioned from the deployed commit so Safari/iOS cannot silently retain stale experiment assets while the build indicator reports a newer deployment.
- Setup / Structure / Tracks remain disposable product fixtures. Their current behavior does not approve FIRE Core architecture.

## Reliability gate

A red regression is not merge-ready evidence. When a deliberate shell change invalidates an old regression expectation, reconcile the implementation, active authority, test contract, zero-context handoff, and deployed asset revisioning in the same change before merge.

**Shell Test passing is not sufficient for a shared-primitive merge.** Any shared primitive used by real G7 must also pass browser coverage in the actual G7 fixture path at the compact and regular-width regression matrix.

A Shell Test-only experiment may remain isolated until Babel physically chooses a direction. Promotion into real G7 requires a new shared-primitive implementation pass plus the full real-G7 reliability gate.

Physical review must target the exact deployed revision shown by the G7/Shell Test build indicator.

## Freeze status

**0 / 10 Locked — G7 NOT FROZEN. FIRE Core breadboarding blocked.**

All ten categories are currently **Candidate**, not Locked. Candidate means there is a coherent implementation/evidence surface to review; it does not substitute for physical validation.

Do not change a category to Locked without satisfying `G7_SHELL_CERTIFICATION.md` and recording the physical-validation evidence that justified the change.
