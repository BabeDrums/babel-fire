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

PR #89 passed Static + Chromium **390 / 440 / 820**, including the real G7 Project → Setup → Structure path and Shell Test. Pages deployed the exact merge successfully.

PR #91 later simplified authority/documentation only and made no G7/V6 runtime change. Exact Pages deployment and post-merge Static + Chromium 390/440/820 passed on `f512b90065c58a2426e79e4a99941a22b22fe35e`.

## Active physical-review finding — host centering

Physical iPad review of deployed `G7 · f512b90` found that the normalized glyphs look correct in the Shell Test container comparison, while the same generated artwork can sit visibly high in toolbar/action/row/state hosts.

The defect is classified as a **host-centering contract problem**, not a new per-symbol optical-nudge problem:
- `+` / `•••` read high in toolbar/action hosts
- managed-row `•••` reads high
- Current's status bar is the clearest high state mark; checks also need the same host consistency
- Back / Forward and the intrinsic symbol metrics themselves should remain unchanged unless new evidence proves otherwise
- accepted x-lanes, row/text geometry, 44px hit targets, and 36px visible toolbar material stay fixed

Current candidate on `fix-g7-host-centering`:
- generated symbol/state pseudo-elements are explicitly centered inside their stable host boxes using absolute inset + auto margins
- host centering does not consume the CSS transform channel used by intrinsic symbol metrics
- `frame-primitives.css` no longer changes symbol pseudo-elements back to relative positioning
- the obsolete shell-level header action offset rule is removed; structural header placement has one owner in `frame-primitives.css`
- Shell Test removes the redundant adaptive-dialog helper sentence and gives the sparse composition fixture intentional internal inset

This candidate is not physically approved and does not lock any category.

## Immediate next gate — candidate validation

First require the normal engineering gate on the exact PR head:
- Authority/Handoff
- Static
- Chromium 390 / 440 / 820
- Shell Test and real G7 fixture coverage

After exact deployment, review on **iPhone first**, then **iPad / regular width**. Specifically judge:
- Add / More vertical seating inside top controls
- managed-row More vertical seating
- Complete / Current / Incomplete vertical seating as one state family
- Back / Forward preservation
- Reorder preservation
- 44px interaction target vs 36px visible button material
- title/meta spacing and hierarchy
- Tempo / Meter lane
- keyboard/focus progression
- add/edit sheet hierarchy and placement
- interaction with Safari browser chrome

Do not infer iPhone approval from this iPad finding. Browser evidence alone cannot lock a certification category. Physical evidence + the certification contract govern locking.

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
