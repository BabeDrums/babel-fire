# G7 Shell Certification — Status Board

This file is the small mutable status board for `G7_SHELL_CERTIFICATION.md`. The certification contract defines what each category means and how it can be locked.

**Current phase:** fundamentals physical review under the repo reliability gate. Shell Test is useful evidence, but no category is Locked yet and FIRE Core remains blocked.

| Category | State | Current note |
| --- | --- | --- |
| 1. Page frame | Candidate | Shell Test exposes sparse/normal/dense and long-content composition using the real page shell. Header trailing actions align to the large-title line instead of floating above it. Needs final compact/regular physical review before locking. |
| 2. Typography | Candidate | Representative title/meta/row/supporting roles and long wrapping are visible together in Shell Test. Needs final hierarchy review in real G7 context. |
| 3. Spacing and alignment | Candidate | Accepted horizontal accessory lanes, text anchors, hit targets, row geometry, and header geometry remain unchanged. Physical iPhone review of `G7 · d00d146` did not approve the shared `+1px` visible-artwork offset, so Shell Test now evaluates geometry-derived SVG centering instead of another manual nudge. Needs physical comparison before any real-G7 primitive change. |
| 4. Surfaces | Candidate | Existing grouped/selection/field/modal surfaces are exercised together in Shell Test. A bounded three-row button-container comparison is now present only in Shell Test; it does not redefine real G7 surfaces. |
| 5. Actions | Candidate | Primary/secondary/destructive/add/management actions remain represented. The symbol experiment compares Current rounded-square, plain Circle, and circular Liquid-Glass-style containers while holding symbol geometry and 44px targets constant. No container direction is approved yet. |
| 6. Icons and accessories | Candidate | Standard production glyphs still use the current canonical Lucide-based family, but the global `+1px` candidate is not physically approved. Shell Test now renders the same six symbol meanings as inline 24×24 SVGs whose visible vector bounds are automatically centered at 12×12. Needs iPhone/iPad review before promotion to real G7. |
| 7. Controls and states | Candidate | Shell Test covers selection, segmented, field, selected/default/disabled/focusable examples using real G7 classes, and the real Setup fixture remains part of the browser regression gate. Error/custom depth may still extend if physical review exposes a need. |
| 8. Temporary UI | Candidate | Shell Test and the real Structure fixture exercise the same sheet/dialog classes. Shared primitives do not add unapproved action-divider or inset hairlines. Compact/regular presentation remains adaptive and needs physical review. |
| 9. Responsive behavior | Candidate | Shared-shell browser regressions exercise both Shell Test and real Project → Setup → Structure paths at 390/440/820 widths. The new symbol/container comparison must remain usable at compact and regular widths before merge/deploy review. |
| 10. Accessibility and motion | Candidate | Shared primitives retain ~44px targets, focus-visible behavior and reduced-motion baseline. The experimental symbol rows keep 44px controls and suppress transitions under reduced motion. Needs physical/device accessibility review before locking. |

## Current evidence

- Developer Shell Test: `v7-preview/shell-test.html`.
- Shared shell/accessory infrastructure: `v7-preview/shell-primitives.css`, loaded by both G7 and Shell Test.
- Progress-state visual authority: `v7-preview/state-primitives.css`, loaded after the shared shell layer in both G7 and Shell Test.
- Shell Test-only experiment styling: `v7-preview/shell-test-experiments.css`; this file is intentionally not loaded by real G7.
- Real G7 still uses the PR #83 `--symbol-optical-y: 1px` candidate while the experiment is evaluated. The experiment does not silently change production controls.
- Physical iPhone review of `G7 · d00d146` found the family close but still slightly off, so the `+1px` candidate is not approved.
- The experimental palette uses inline 24×24 SVG source geometry for Back, Forward, Plus, Check, Reorder, and More. JavaScript measures each symbol's visible vector bounds with `getBBox()` and translates the artwork so those bounds center on the 12×12 viewBox center.
- The experimental palette does not use `--symbol-optical-y`; placement is derived from vector geometry rather than a universal pixel offset.
- The three Shell Test rows hold symbol source, normalized placement, icon size, and 44px hit target constant while comparing only container treatment: Current rounded-square, plain Circle, and circular Liquid-Glass-style.
- The Liquid Glass row is a static-web approximation, not Apple's native system material. It uses translucency, backdrop filtering/adaptation, edge/specular highlights, depth, and press response for directional evidence.
- Apple platform guidance treats Liquid Glass as a distinct controls/navigation material and recommends standard/native glass APIs where available; G7's static web stack cannot invoke those native APIs directly.
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
