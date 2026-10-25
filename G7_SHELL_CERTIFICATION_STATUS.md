# G7 Shell Certification — Status Board

This file is the small mutable status board for `G7_SHELL_CERTIFICATION.md`. The certification contract defines what each category means and how it can be locked.

**Current phase:** fundamentals physical review under the repo reliability gate. Shell Test is useful evidence, but no category is Locked yet and FIRE Core remains blocked.

| Category | State | Current note |
| --- | --- | --- |
| 1. Page frame | Candidate | Shell Test exposes sparse/normal/dense and long-content composition using the real page shell. Needs final compact/regular physical review before locking. |
| 2. Typography | Candidate | Representative title/meta/row/supporting roles and long wrapping are visible together in Shell Test. Needs final hierarchy review in real G7 context. |
| 3. Spacing and alignment | Candidate | Shared primitive layer owns canonical accessory geometry, optical `+` / `•••` centering, and named modal spacing tokens. Needs physical confirmation on the exact deployed revision. |
| 4. Surfaces | Candidate | Existing grouped/selection/field/modal surfaces are exercised together in Shell Test; material relationships remain subject to physical review. |
| 5. Actions | Candidate | Primary/secondary/destructive/add/management actions are compared on one real-primitives surface; project-row management has no decorative divider. Needs physical review. |
| 6. Icons and accessories | Candidate | Completion/current/incomplete/chevron/ellipsis/add/drag share canonical geometry; the current state now uses the stronger outlined ring language rather than an inner dot. Needs physical review. |
| 7. Controls and states | Candidate | Shell Test covers selection, segmented, field, selected/default/disabled/focusable examples using real G7 classes. Error/custom depth may still extend if physical review exposes a need. |
| 8. Temporary UI | Candidate | Shell Test exercises selection, confirmation, and destructive temporary UI through the same sheet/dialog classes used by G7; compact/regular presentation remains adaptive. Needs physical review. |
| 9. Responsive behavior | Candidate | Shell Test uses the same compact/regular breakpoints and deliberately includes wrapping/density/modal cases. Needs iPhone/iPad physical validation after the exact deployed build is verified. |
| 10. Accessibility and motion | Candidate | Shared primitives retain ~44px targets, focus-visible behavior and reduced-motion baseline; Shell Test supports Escape for temporary UI. Needs physical/device accessibility review before locking. |

## Current evidence

- Developer Shell Test: `v7-preview/shell-test.html`.
- Shared real-G7 primitive layer: `v7-preview/shell-primitives.css`, loaded by both G7 and Shell Test.
- Shell Test is not a parallel FIRE implementation: it uses disposable certification content and the same class/token layer as real G7.
- Physical review found the certification surface broadly useful while still exposing fundamentals to correct: project-row divider removal, optical `+` alignment, current-state language, recurring accessory geometry, and modal/group rhythm.
- The current candidate implements those corrections at the shared primitive level; they still require physical confirmation on the exact deployed revision before any category can lock.
- G7 and Shell Test assets are revisioned from the deployed commit so Safari/iOS cannot silently keep an older CSS/JS shell while the build indicator reports a newer deployment.
- Setup / Structure / Tracks remain disposable product fixtures. Their current behavior does not approve FIRE Core architecture.

## Reliability gate

A red regression is not merge-ready evidence. When a deliberate shell change invalidates an old regression expectation, reconcile the implementation, active authority, test contract, zero-context handoff, and deployed asset revisioning in the same change before merge.

Physical review must target the exact deployed revision shown by the G7/Shell Test build indicator.

## Freeze status

**0 / 10 Locked — G7 NOT FROZEN. FIRE Core breadboarding blocked.**

All ten categories are currently **Candidate**, not Locked. Candidate means there is a coherent implementation/evidence surface to review; it does not substitute for physical validation.

Do not change a category to Locked without satisfying `G7_SHELL_CERTIFICATION.md` and recording the physical-validation evidence that justified the change.
