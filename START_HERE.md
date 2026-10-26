# Babel FIRE — Start Here

Use **Babel** as the project-facing name.

Read `BABEL_TRUTH.md` first, then the pinned Truth `START_HERE.md` / `AGENTS.md` / `FOUNDATIONS.md`. This file owns only the **current FIRE state and immediate next gate**.

## Current state

- Production remains **V6**.
- G7 is the isolated successor preview at `/v7-preview/` using `production-projects-v1-v7-preview`; it must never mutate V6 `production-projects-v1` data.
- G7 shell certification is active.
- All ten certification categories remain **Candidate**; **0 / 10 Locked**.
- **G7 is NOT FROZEN. FIRE Core breadboarding has not started.**
- Current `Setup → Structure → Tracks` content is disposable shell-fixture content, not FIRE Core architecture.
- Shell Test is developer infrastructure inside G7, not a second FIRE implementation and not Babel Lab.

## Current verified implementation

### Symbol system

PR #88 promoted the physically preferred symbol architecture into real G7:

**geometry baseline → optional intrinsic symbol optical metric → container placement**

- Plus / More / Reorder use normal centered placement.
- Check owns its small intrinsic vertical correction.
- Back / Forward own mirrored outward side bearings.
- Current / Incomplete are symmetric status bars.
- standalone toolbar glyph buttons may use the simple Circle treatment
- Liquid Glass is rejected
- symbol alignment belongs to the symbol primitive, never page-specific CSS

PR #92 later fixed the broader host-centering contradiction so generated `+`, `•••`, completion/state art, and shared row accessories seat from one stable host contract. Exact Pages deployment and post-merge Static + Chromium 390 / 440 / 820 passed on `8d26e015da05aa4836d31bde0cb5405f50e448c1`.

PR #93 then removed the final real-G7 Back-only host contradiction by neutralizing the legacy nested `.back-glyph` transform while leaving chevron artwork/optical metrics untouched. It merged at `c444d9b2a26d8e9196a901155586763c78af2f86`, deployed successfully, and physical review reported the chevron looks great. Do not reopen the chevron system without new contradictory evidence.

### Shared frame

`frame-primitives.css` owns structural relationships; `shell-primitives.css` owns symbol/accessory artwork; `state-primitives.css` owns progress-state artwork.

Historical frame milestone: PR **#89** repaired the shared header/control/state/modal frame and merged at `d93729ff7a734035f25a6835323d19706f15186d`. Later physical review and PRs #92/#93 refined generated-art seating and the Back host without reopening that frame architecture.

Current verified frame rules:
- Back and trailing Add/More share one navigation/action row; large title/meta live below it
- toolbar keeps a 44px interaction target with quieter 36px visible material
- `state-primitives.css` owns progress/completion artwork; legacy text glyphs cannot leak through
- Tempo and Meter share one stable trailing value lane
- symbol/state hosts seat generated artwork consistently instead of inheriting line-box behavior

### Adaptive sheets

PR #94 restored the intended adaptive presentation and merged at `c4c69f7927a6c34221e3044d2660b5d50fc75726`:
- `<700px`: edge-attached bottom sheet
- `>=700px`: centered card
- routine `aria-label` stays semantic and is not duplicated as a visible heading
- explicit destructive confirmation headings remain visible
- Custom Section / Custom Bars stay progressively disclosed and focusable
- symbol/header/state systems remain untouched

Pre-merge Authority/Handoff + Static + Chromium 390/440/820 passed. Exact Pages deployment on the merge succeeded. Physical iPhone review confirmed the adaptive direction is much better, but exposed one remaining systemic contradiction: **sheet vertical rhythm is inconsistent across sheet types and disclosure states**.

## Active physical review finding — sheet rhythm

The current issue is not presentation mode anymore; it is competing vertical-spacing ownership:
- `.project-type-control` has its own bottom margin
- `.sheet-content-group + .sheet-content-group` owns another major gap
- `.sheet-actions` and `.sheet-actions.single-action` use different footer gaps
- Custom Bars stacks the disclosure-wrapper margin with `.numeric-field` margin, creating an accidental double gap
- as a result, New Project, Project actions, Add Track, Add Section, Edit Section, and Custom states can all be locally valid while reading as one inconsistent family

Current candidate on `g7-sheet-rhythm-system` establishes one semantic rhythm:
- **related disclosure gap:** 12px
- **major section gap:** 24px
- **task content → footer actions:** 24px
- single-action and multi-action footers use the same separation
- Custom Section / Custom Bars fields attach to the triggering group with the same related gap
- the Custom Bars field no longer adds a second local top margin
- keyboard/focus scrolling preserves the same internal rhythm instead of introducing a second layout

No symbol, header, state-art, product-flow, V6, or FIRE Core change belongs to this candidate.

## Immediate next gate — sheet rhythm validation

Require the normal engineering gate on the exact PR head:
- Authority/Handoff
- Static
- Chromium 390 / 440 / 820
- real G7 fixture coverage

The browser contract must prove:
- New Project uses 24px project-type → fields → footer rhythm
- Project actions uses the same 24px content → single-action footer rhythm
- Add Section keeps 24px between major groups and before footer actions
- Custom Section / Custom Bars disclosures use 12px attachment gaps
- Custom Bars has no stacked field margin
- compact bottom-sheet and regular-width centered-card presentation from PR #94 remain intact

After exact deployment, physical review is **iPhone first**, especially New Project, Project actions, Add Track, Add Section with both Custom disclosures, Edit Section, and keyboard-open state. Then review the same family on iPad / regular width.

Browser evidence alone cannot lock a certification category. Physical evidence + the certification contract govern locking.

## Stable boundaries

- public project types remain Original / Cover
- history-aware Back retraces actual in-app path with a safe fallback for direct entry
- `+` = add/create the primary discrete object for the current view
- `•••` = management/actions
- arrangement metadata belongs to content hierarchy; reorder owns its far-right affordance
- Complete = canonical check; Current = stronger short bar; Incomplete/upcoming = quieter short bar
- Current does not tint the whole row
- one product logic across iPhone/iPad; presentation may adapt
- V6 runtime/data/schema remain untouched throughout shell certification

## Freeze sequence

`G7_SHELL_CERTIFICATION.md` defines the contract; `G7_SHELL_CERTIFICATION_STATUS.md` owns mutable evidence.

Final sequence:

**10/10 Locked → final real-G7 physical sweep → no unresolved systemic contradiction → explicit Babel approval → G7 Shell Frozen → promote genuinely transferable shell rules into Babel Truth → FIRE Core breadboarding**

New durable unresolved FIRE findings go to Babel Truth Issue #1 under the shared persist-before-reply rule.
