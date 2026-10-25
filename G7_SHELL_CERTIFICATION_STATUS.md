# G7 Shell Certification — Status Board

This file is the small mutable status board for `G7_SHELL_CERTIFICATION.md`. The certification contract defines what each category means and how it can be locked.

**Current phase:** fundamentals physical review under the repo reliability gate. Shell Test is useful evidence, but no category is Locked yet and FIRE Core remains blocked.

| Category | State | Current note |
| --- | --- | --- |
| 1. Page frame | Candidate | Shell Test exposes sparse/normal/dense and long-content composition using the real page shell. Header trailing actions align to the large-title line instead of floating above it. Needs final compact/regular physical review before locking. |
| 2. Typography | Candidate | Representative title/meta/row/supporting roles and long wrapping are visible together in Shell Test. Needs final hierarchy review in real G7 context. |
| 3. Spacing and alignment | Candidate | Shared primitives now give Complete / Current / Incomplete / Navigate / Reorder / More one physical trailing-lane center rather than merely similar icon boxes. Real G7 regression coverage still protects form-control columns and header alignment. Needs physical confirmation on the exact deployed revision. |
| 4. Surfaces | Candidate | Existing grouped/selection/field/modal surfaces are exercised together in Shell Test; material relationships remain subject to physical review. |
| 5. Actions | Candidate | Primary/secondary/destructive/add/management actions are compared on one real-primitives surface. Toolbar add/management actions are now glyph-first 44px hit targets with no permanent boxed background at rest. Needs physical review. |
| 6. Icons and accessories | Candidate | Standard interface glyphs now use one canonical Lucide 24x24 construction system instead of hand-built per-glyph CSS. Back/forward, check, plus, ellipsis, and reorder inherit one rounded stroke language. Progress state is deliberately separate: Complete = filled circle + canonical check; Current = one brighter/thicker ring; Incomplete = quieter/thinner ring. Needs physical confirmation before lock. |
| 7. Controls and states | Candidate | Shell Test covers selection, segmented, field, selected/default/disabled/focusable examples using real G7 classes, and the real Setup fixture is part of the browser regression gate so field controls cannot be squeezed into the accessory lane. Error/custom depth may still extend if physical review exposes a need. |
| 8. Temporary UI | Candidate | Shell Test and the real Structure fixture exercise the same sheet/dialog classes. Shared primitives do not add unapproved action-divider or inset hairlines. Compact/regular presentation remains adaptive and needs physical review. |
| 9. Responsive behavior | Candidate | Shared-shell browser regressions exercise both Shell Test and real Project → Setup → Structure paths at 390/440/820 widths, including real header action alignment and accessory-state geometry. Needs iPhone/iPad physical validation after the exact deployed build is verified. |
| 10. Accessibility and motion | Candidate | Shared primitives retain ~44px targets, focus-visible behavior and reduced-motion baseline; Shell Test supports Escape for temporary UI. Needs physical/device accessibility review before locking. |

## Current evidence

- Developer Shell Test: `v7-preview/shell-test.html`.
- Shared real-G7 primitive layer: `v7-preview/shell-primitives.css`, loaded by both G7 and Shell Test.
- Shell Test is not a parallel FIRE implementation: it uses disposable certification content and the same class/token layer as real G7.
- Physical review found the certification surface broadly useful while still exposing fundamentals to correct: project-row divider removal, accessory alignment, progress-state language, modal/group rhythm, real-screen regressions caused by over-broad shared selectors, header/navigation consistency, and finally the limits of a homemade per-glyph CSS icon system.
- The icon/accessory reset replaces individually invented check/chevron/plus/ellipsis/reorder geometry with canonical Lucide 24x24 SVG-mask paths in the shared primitive layer. Commodity glyphs inherit one optical grid and rounded stroke vocabulary instead of being manually tuned one by one.
- The trailing accessory lane is now physically aligned across grouped rows, project cards and arrangement rows. Browser coverage compares the actual x-center of Complete / Current / Incomplete / Navigate / Reorder / More instead of assuming matching boxes imply matching placement.
- Toolbar add/management actions remain 44px interaction targets but no longer render permanent dark rounded-square surfaces at rest; the glyph carries the resting visual weight and active/focus states can reveal the target.
- The progress-state candidate has been simplified after physical review: Incomplete = quiet outer ring; Current = the same state geometry with stronger ring weight/contrast and no inner bullseye; Complete = filled state circle plus the canonical check glyph.
- Back and forward use the same canonical chevron family with direction as the only change; Shell Test Back uses the same primitive as real G7.
- The real-screen reliability gate still covers Project → Setup → Structure at 390/440/820 widths so Shell Test cannot certify a shared primitive that breaks the product fixture.
- G7 and Shell Test assets are revisioned from the deployed commit so Safari/iOS cannot silently keep an older CSS/JS shell while the build indicator reports a newer deployment.
- Setup / Structure / Tracks remain disposable product fixtures. Their current behavior does not approve FIRE Core architecture.

## Reliability gate

A red regression is not merge-ready evidence. When a deliberate shell change invalidates an old regression expectation, reconcile the implementation, active authority, test contract, zero-context handoff, and deployed asset revisioning in the same change before merge.

**Shell Test passing is not sufficient for a shared-primitive merge.** Any shared primitive used by real G7 must also pass browser coverage in the actual G7 fixture path at the compact and regular-width regression matrix. The current minimum real-screen path is Project → Setup → Structure temporary UI, covering current-state geometry, form-control containment, header action alignment, navigation glyph construction, and sheet chrome.

Physical review must target the exact deployed revision shown by the G7/Shell Test build indicator.

## Freeze status

**0 / 10 Locked — G7 NOT FROZEN. FIRE Core breadboarding blocked.**

All ten categories are currently **Candidate**, not Locked. Candidate means there is a coherent implementation/evidence surface to review; it does not substitute for physical validation.

Do not change a category to Locked without satisfying `G7_SHELL_CERTIFICATION.md` and recording the physical-validation evidence that justified the change.
