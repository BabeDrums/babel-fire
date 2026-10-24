# G7 Shell Certification — Status Board

This file is the small mutable status board for `G7_SHELL_CERTIFICATION.md`. The certification contract defines what each category means and how it can be locked.

**Current phase:** Shell Test exists; run category-based physical validation of certification pass 1. No category is Locked yet.

| Category | State | Current note |
| --- | --- | --- |
| 1. Page frame | Candidate | Shell Test now exposes sparse/normal/dense and long-content composition using the real page shell. Needs physical compact/regular review before locking. |
| 2. Typography | Candidate | Representative title/meta/row/supporting roles and long wrapping are now visible together in Shell Test. Needs physical hierarchy review. |
| 3. Spacing and alignment | Candidate | Shared primitive layer now owns canonical accessory geometry and optical `+` / `•••` centering; Shell Test exposes them side by side. Needs physical review. |
| 4. Surfaces | Candidate | Existing grouped/selection/field/modal surfaces are exercised together in Shell Test; material relationships remain subject to physical review. |
| 5. Actions | Candidate | Primary/secondary/destructive/add/management actions are now compared on one real-primitives surface; project-row management divider is removed by the shared layer. Needs physical review. |
| 6. Icons and accessories | Candidate | Completion/current/incomplete/chevron/ellipsis/add/drag now share canonical boxes/alignment in the shared primitive layer and Shell Test. Needs physical review. |
| 7. Controls and states | Candidate | Shell Test covers selection, segmented, field, selected/default/disabled/focusable examples using real G7 classes. Error/custom depth may still be extended if physical review exposes a need. |
| 8. Temporary UI | Candidate | Shell Test exercises selection, confirmation, and destructive temporary UI through the same sheet/dialog classes used by G7; compact/regular presentation remains adaptive. Needs physical review. |
| 9. Responsive behavior | Candidate | Shell Test is available at the same compact/regular breakpoints and deliberately includes wrapping/density/modal cases. Needs iPhone/iPad physical validation. |
| 10. Accessibility and motion | Candidate | Shared primitives retain ~44px targets, focus-visible behavior and reduced-motion baseline; Shell Test adds keyboard Escape for temporary UI. Needs physical/device accessibility review before locking. |

## Pass 1 evidence

- Developer Shell Test: `v7-preview/shell-test.html`
- Shared real-G7 primitive layer: `v7-preview/shell-primitives.css`, loaded by both G7 and Shell Test.
- Shell Test is not a parallel FIRE implementation: it uses disposable certification content and the same class/token layer as real G7.
- Latest known physical findings addressed systemically in this candidate: project-row `•••` divider removal; optical `+` / `•••` centering; recurring accessory box/geometry; stronger modal action/group hierarchy.
- Setup / Structure / Tracks remain disposable product fixtures. This pass does not approve their FIRE Core architecture.

## Freeze status

**0 / 10 Locked — G7 NOT FROZEN. FIRE Core breadboarding blocked.**

All ten categories are currently **Candidate**, not Locked. Candidate means there is now a coherent implementation/evidence surface to review; it does not substitute for physical validation.

Do not change a category to Locked without satisfying `G7_SHELL_CERTIFICATION.md` and recording the physical-validation evidence that justified the change.