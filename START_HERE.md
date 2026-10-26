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

PR #92 fixed generated-art host seating and merged at `8d26e015da05aa4836d31bde0cb5405f50e448c1`.

PR #93 removed the final real-G7 Back-host contradiction and merged at `c444d9b2a26d8e9196a901155586763c78af2f86`. Physical review reports the chevron now looks great. Do not reopen the chevron system without new contradictory evidence.

### Shared frame

`frame-primitives.css` owns structural relationships; `shell-primitives.css` owns symbol/accessory artwork; `state-primitives.css` owns progress-state artwork.

Historical frame milestone: PR **#89** repaired the shared header/control/state/modal frame and merged at `d93729ff7a734035f25a6835323d19706f15186d`.

Current verified frame rules:
- Back and trailing Add/More share one navigation/action row; large title/meta live below it
- toolbar keeps a 44px interaction target with quieter 36px visible material
- `state-primitives.css` owns progress/completion artwork; legacy text glyphs cannot leak through
- Tempo and Meter share one stable trailing value lane
- symbol/state hosts seat generated artwork consistently instead of inheriting line-box behavior

### Adaptive sheets and rhythm

PR #94 restored the intended adaptive presentation and merged at `c4c69f7927a6c34221e3044d2660b5d50fc75726`:
- `<700px`: edge-attached bottom sheet
- `>=700px`: centered card
- routine `aria-label` stays semantic and is not duplicated as a visible heading
- explicit destructive confirmation headings remain visible
- Custom Section / Custom Bars stay progressively disclosed and focusable

Physical review of PR #94 then exposed inconsistent vertical rhythm across sheet types.

PR #95 unified that rhythm and merged at `5d6ab57a6cd2109c873689c758d0e32b437cace1`:
- **related disclosure gap:** 12px
- **major section gap:** 24px
- **task content → footer actions:** 24px
- single-action and multi-action footers use the same separation
- Custom Section / Custom Bars attach with the same related gap
- Custom Bars no longer stacks a second local top margin
- compact bottom-sheet and regular-width centered-card presentation remain intact

Exact pre/post merge browser coverage passed at 390 / 440 / 820, and subsequent physical iPhone/iPad review found the sheets broadly solid.

## Active physical review finding — final generic shell polish

The latest physical iPhone/iPad review of exact G7 `5d6ab57` surfaced two remaining generic shell defects before freeze:

1. **Normal iOS text assistance is suppressed in routine text fields.** Legacy fixture markup still emits restrictive `autocomplete`, `autocorrect`, and `spellcheck` attributes, so Title/Artist and similar ordinary text entry lose predictive/correction assistance even though word capitalization and Next/Done progression still work.
2. **Split-action rows paint pressed state on child controls instead of the full parent row.** Project rows split main-open vs `•••`; Structure rows split edit vs reorder. Pressing either side currently highlights only that child region, which reads as a glitch rather than one coherent row.

Current candidate on `g7-final-shell-interaction-polish` fixes those at the shell level:
- `input-primitives.js` restores normal assistance only for ordinary `.field` text inputs; specialized `inputmode` controls such as numeric Custom Bars remain untouched
- existing capitalization and Enter-key focus progression stay intact
- Project and Structure split-action rows now let the **parent row own one edge-to-edge pressed surface**
- child controls retain separate semantics/accessory emphasis but no longer paint competing pressed rectangles
- no symbol geometry, sheet rhythm, product fixture content, V6 runtime/data, or FIRE Core behavior changes in this pass

Fixture-specific wording/content cleanup such as `Accurate` → `Confirmed` or Tracks/FX decisions is outside this shell-polish pass.

## Immediate next gate — final shell-polish validation

Require the normal engineering gate on the exact PR head:
- Authority/Handoff
- Static
- Chromium 390 / 440 / 820
- real G7 fixture coverage

The browser contract must prove:
- New Project Title/Artist receive normal correction/spelling assistance instead of explicit suppression
- `autocapitalize="words"` and Next → Done keyboard progression remain intact
- specialized numeric inputs are not generalized into text-assistance behavior
- pressing either side of a Project split row paints one full parent-row surface
- pressing either side of a Structure edit/reorder row paints one full parent-row surface
- child controls do not add a second local pressed rectangle
- PR #94/#95 adaptive sheet geometry and rhythm remain intact

After exact deployment, run one final physical sanity pass on **iPhone first, then iPad / regular width**. If those two interaction defects are resolved and no new systemic contradiction appears, proceed to explicit shell approval/freeze rather than reopening fixture-specific product content.

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
