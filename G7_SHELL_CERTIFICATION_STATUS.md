# G7 Shell Certification — Status Board

This file is the small mutable status board for `G7_SHELL_CERTIFICATION.md`. The certification contract defines what each category means and how it can be locked.

**Current phase:** narrow Back-host candidate after iPhone physical review of deployed `G7 · 8d26e01`. PR #92 resolved the broader host-centering problem and the shell now reads dramatically better; one legacy `-1px` transform still affects the nested real-G7 Back host. No category is Locked and FIRE Core remains blocked.

| Category | State | Current note |
| --- | --- | --- |
| 1. Page frame | Candidate | PR #89 restored one shared navigation/action row with large title/meta below it. PR #92 preserved that frame while standardizing generated-art host centering. Current candidate changes only the nested Back host transform. |
| 2. Typography | Candidate | Representative title/meta/row/supporting roles remain intact. No type change is part of the current candidate. |
| 3. Spacing and alignment | Candidate | PR #92 fixed the broader host-centering inconsistency across generated toolbar/row/state artwork. iPhone review found one remaining Back-only contradiction: real `.back-glyph` still receives a legacy `translateY(-1px)` while Shell Test does not. Candidate neutralizes that host transform only. |
| 4. Surfaces | Candidate | Grouped/selection/field/modal surfaces remain unchanged. Toolbar material stays separated from its 44px interaction frame. |
| 5. Actions | Candidate | Add/More semantics and circle treatment remain. PR #92 physically improved their seating; current candidate does not change Add/More. |
| 6. Icons and accessories | Candidate | Intrinsic symbol architecture remains: Plus/More/Reorder geometric, Check with intrinsic vertical metric, Back/Forward with mirrored outward side bearings. Current candidate keeps the chevron asset untouched and makes the real nested Back host obey `transform: none`, matching Shell Test. |
| 7. Controls and states | Candidate | `state-primitives.css` remains sole state-art owner. PR #92 unified host seating for Complete/Current/Incomplete; physical iPhone review reported this as a major improvement. No state-art change is part of the Back candidate. |
| 8. Temporary UI | Candidate | Compact sheets still use the bounded small-viewport-safe frame and visible task title. No temporary-UI change is part of the current candidate. |
| 9. Responsive behavior | Candidate | PR #92 exact merge passed post-merge 390/440/820 and deployed successfully. Current Back candidate must pass the same matrix before merge, then receive iPhone physical confirmation before broader iPad review continues. |
| 10. Accessibility and motion | Candidate | 44px toolbar hit targets remain unchanged. Neutralizing the nested Back host transform does not alter hit geometry, focus, or motion behavior. |

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
- Physical iPad review of `G7 · f512b90` exposed generated-art host centering as a systemic issue while the comparison specimen itself looked correct.
- PR #92 implemented **stable host box → absolute inset/auto-margin centering → intrinsic symbol metric inside the asset** and merged at `8d26e015da05aa4836d31bde0cb5405f50e448c1`; exact Pages deployment and post-merge Static + Chromium 390/440/820 passed.
- Physical iPhone review of `G7 · 8d26e01` reported the shell as dramatically better and broadly loved. The remaining visual concern is narrow: Shell Test Back looks correctly centered, but selected-project real-G7 Back looks slightly high.
- Code diagnosis for that remaining concern:
  - Shell Test Back does not use the nested `.back-glyph` host.
  - real G7 Back does.
  - base `styles.css` still applies `transform: translateY(-1px)` to `.back-glyph` from the pre-normalization era.
  - `frame-primitives.css` now owns host placement, so the legacy transform is a contradiction rather than an optical requirement.
- Current candidate on `fix-g7-back-host-center` explicitly sets `.back-glyph { transform: none; }` in the shared frame and adds a real-product browser assertion for that computed style.
- Chevron asset geometry, intrinsic mirrored side bearing, circle material, 44px hit target, 36px visible material, accepted x-lanes, and every other symbol remain unchanged.
- Liquid Glass remains rejected for the current FIRE shell direction.
- Setup / Structure / Tracks remain disposable product fixtures. Their current behavior does not approve FIRE Core architecture.

## Reliability gate

Do not merge the Back-host candidate unless the exact PR head passes:
- Authority/Handoff
- Static
- Chromium 390 / 440 / 820
- real G7 Project → Setup → Structure coverage

A red regression is not merge-ready evidence. When a deliberate shell change invalidates an old regression expectation, reconcile implementation, active authority, test contract, zero-context handoff, and deployed asset revisioning in the same change.

After exact deployment, physical review is **iPhone first**. Compare Shell Test Back against selected-project and work-page Back controls. The goal is not to retune the chevron; it is to prove the real nested host now seats the already-approved chevron exactly like Shell Test.

Physical review must target the exact deployed revision shown by the G7/Shell Test build indicator.

## Freeze status

**0 / 10 Locked — G7 NOT FROZEN. FIRE Core breadboarding blocked.**

All ten categories are currently **Candidate**, not Locked. Candidate means there is a coherent implementation/evidence surface to review; it does not substitute for physical validation.

Do not change a category to Locked without satisfying `G7_SHELL_CERTIFICATION.md` and recording the physical-validation evidence that justified the change.
