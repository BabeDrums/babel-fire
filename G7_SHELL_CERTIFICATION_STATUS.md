# G7 Shell Certification — Status Board

This file is the small mutable status board for `G7_SHELL_CERTIFICATION.md`. The certification contract defines what each category means and how it can be locked.

**Current phase:** fundamentals physical review under the repo reliability gate. Shell Test is useful evidence, but no category is Locked yet and FIRE Core remains blocked.

| Category | State | Current note |
| --- | --- | --- |
| 1. Page frame | Candidate | Shell Test exposes sparse/normal/dense and long-content composition using the real page shell. Header trailing actions align to the large-title line instead of floating above it. Needs final compact/regular physical review before locking. |
| 2. Typography | Candidate | Representative title/meta/row/supporting roles and long wrapping are visible together in Shell Test. Needs final hierarchy review in real G7 context. |
| 3. Spacing and alignment | Candidate | Horizontal accessory lanes remain physically aligned across state / Navigate / Reorder / More. Physical review of `66c43bf` isolated the remaining defect to visible artwork sitting slightly high inside otherwise-correct centered hit targets, so the active candidate preserves x/layout geometry and applies one shared 1px downward optical baseline to symbol artwork only. Needs physical confirmation. |
| 4. Surfaces | Candidate | Existing grouped/selection/field/modal surfaces are exercised together in Shell Test; material relationships remain subject to physical review. |
| 5. Actions | Candidate | Primary/secondary/destructive/add/management actions are compared on one real-primitives surface. Toolbar add/management actions remain glyph-first 44px hit targets with no permanent boxed background at rest; only the visible glyph artwork participates in the shared optical baseline. Needs physical review. |
| 6. Icons and accessories | Candidate | Standard interface glyphs use one canonical Lucide 24x24 construction system. Progress state remains deliberately separate and non-circular: Complete = canonical check; Current = stronger 18px bar; Incomplete = quieter 18px bar. Commodity and state artwork share one vertical optical baseline while retaining their existing horizontal lanes and hit targets. Needs physical confirmation before lock. |
| 7. Controls and states | Candidate | Shell Test covers selection, segmented, field, selected/default/disabled/focusable examples using real G7 classes, and the real Setup fixture is part of the browser regression gate so field controls cannot be squeezed into the accessory lane. Error/custom depth may still extend if physical review exposes a need. |
| 8. Temporary UI | Candidate | Shell Test and the real Structure fixture exercise the same sheet/dialog classes. Shared primitives do not add unapproved action-divider or inset hairlines. Compact/regular presentation remains adaptive and needs physical review. |
| 9. Responsive behavior | Candidate | Shared-shell browser regressions exercise both Shell Test and real Project → Setup → Structure paths at 390/440/820 widths, including real header action alignment, accessory-state geometry, and the shared vertical optical baseline. Needs iPhone/iPad physical validation after the exact deployed build is verified. |
| 10. Accessibility and motion | Candidate | Shared primitives retain ~44px targets, focus-visible behavior and reduced-motion baseline; the optical correction moves only visible pseudo-element artwork, never interaction targets. Shell Test supports Escape for temporary UI. Needs physical/device accessibility review before locking. |

## Current evidence

- Developer Shell Test: `v7-preview/shell-test.html`.
- Shared shell/accessory infrastructure: `v7-preview/shell-primitives.css`, loaded by both G7 and Shell Test.
- Progress-state visual authority: `v7-preview/state-primitives.css`, loaded after the shared shell layer in both G7 and Shell Test. Superseded circular state rules were removed from `shell-primitives.css` so there is one active state implementation.
- Shell Test is not a parallel FIRE implementation: it uses disposable certification content and the same class/token layers as real G7.
- The icon/accessory reset replaced individually invented check/chevron/plus/ellipsis/reorder geometry with canonical Lucide 24x24 SVG-mask paths in the shared primitive layer.
- Deployed `66c43bf` substantially improved the accessory family. Subsequent physical review clarified that the horizontal lanes were not the remaining problem: visible glyph/state ink read slightly high inside correctly centered containers. The interrupted horizontal-lane experiment was rejected and not merged.
- PR #83's active alignment candidate leaves row columns, x-centers, hit targets, text, and header geometry unchanged. One named `--symbol-optical-y` token moves visible pseudo-element artwork down 1px across Add, More, Back/Forward, Check, Current/Incomplete state bars, Reorder, and the Shell Test glyph palette.
- Browser coverage keeps the existing accessory x-center contract while checking the shared visible-artwork y offset in Shell Test and the real G7 fixture path.
- Arrangement metadata such as `8 bars` remains supporting text beneath the item name; Reorder remains the sole far-right affordance.
- Toolbar add/management actions remain 44px interaction targets but do not render permanent dark rounded-square surfaces at rest; active/focus states can reveal the target.
- Progress-state language is non-circular: Complete = canonical check only; Current = stronger 18px status bar; Incomplete/upcoming = quieter 18px status bar; Current has no persistent row-selection tint.
- Back and forward use the same canonical chevron family with direction as the only semantic difference; Shell Test Back uses the same primitive as real G7.
- The real-screen reliability gate covers Project → Setup → Structure at 390/440/820 widths so Shell Test cannot certify a shared primitive that breaks the product fixture.
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
