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

### Shared frame repair

PR **#89 — Repair G7 shared header, control, state, and modal frames** merged at `d93729ff7a734035f25a6835323d19706f15186d` and was successfully deployed/tested.

Current shared frame rules:
- Back and trailing Add/More share one navigation/action row; large title/meta live below it
- toolbar keeps a 44px interaction target with quieter 36px visible material
- `state-primitives.css` owns progress/completion artwork; legacy text glyphs cannot leak through
- Tempo and Meter share one stable trailing value lane
- compact sheets use bounded small-viewport-safe geometry rather than depending on Safari's dynamic bottom edge
- edit-sheet action hierarchy avoids three equal oversized action slabs

`frame-primitives.css` owns those structural relationships; `shell-primitives.css` owns symbol/accessory artwork; `state-primitives.css` owns progress-state artwork.

PR #91 later simplified authority/documentation only and made no G7/V6 runtime change. Exact Pages deployment and post-merge Static + Chromium 390/440/820 passed on `f512b90065c58a2426e79e4a99941a22b22fe35e`.

PR **#92 — Center generated G7 symbols consistently across hosts** merged at `8d26e015da05aa4836d31bde0cb5405f50e448c1`. It fixed the host-centering contradiction exposed on iPad: generated `+`, `•••`, completion/state art, and shared row accessories now seat from one stable host contract rather than inheriting context-specific line-box behavior. Exact Pages deployment and post-merge Static + Chromium **390 / 440 / 820** passed on that merge.

Physical iPhone review of deployed `G7 · 8d26e01` reported the shell as dramatically improved and broadly loved. The Shell Test chevron looked correctly seated, while the selected-project real-G7 Back chevron still appeared slightly high.

## Active physical review finding — real Back host

The remaining Back issue is classified as a **legacy host transform contradiction**, not a reason to reopen the chevron artwork or optical metric:
- Shell Test Back uses the shared chevron asset without the nested real-G7 `.back-glyph` host and looks correct.
- Real G7 Back wraps that same artwork in `.back-glyph`.
- the base stylesheet still applies a historical `transform: translateY(-1px)` to `.back-glyph`
- the shared frame layer otherwise centers the host correctly

Current candidate on `fix-g7-back-host-center`:
- `frame-primitives.css` explicitly neutralizes host-level transform on `.back-glyph`
- chevron artwork, mirrored side bearing, circle material, 44px hit target, 36px visible material, toolbar geometry, title geometry, and all other symbols remain unchanged
- the real-product browser contract now asserts `.back-glyph` computes to `transform: none`

This candidate is not physically approved and does not lock any category.

## Immediate next gate — Back host validation

First require the normal engineering gate on the exact PR head:
- Authority/Handoff
- Static
- Chromium 390 / 440 / 820
- real G7 fixture coverage

After exact deployment, review on **iPhone first**. Compare:
- Shell Test top Back
- selected-project home Back
- Setup / Structure / Tracks Back

The goal is one thing only: the real nested Back host should now seat exactly like the already-approved Shell Test Back. Do not change the chevron asset or add a new optical offset unless new physical evidence proves the shared asset itself is wrong.

After iPhone confirmation, continue the broader iPad / regular-width shell certification sweep. Browser evidence alone cannot lock a certification category. Physical evidence + the certification contract govern locking.

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
