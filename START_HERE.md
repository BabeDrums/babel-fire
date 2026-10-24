# Babel FIRE — Start Here

Use **Babel** as the project-facing name.

## Read order

1. `BABEL_TRUTH.md` — immutable pointer to the cross-app Babel Truth commit this repo has reconciled against
2. Babel Truth `START_HERE.md` / `AGENTS.md` / relevant shared authority at that pinned commit
3. this file — current FIRE build/review/next-step state
4. `FIRE_CORE.md`
5. `V6.md` for live production behavior
6. `V7_DRAFT.md` for active G7 successor behavior
7. Babel Truth Issue #1 body **plus newer comments** for unresolved FIRE items
8. code/tests as implementation evidence

For wider ecosystem/surrounding-app work instead, use `BABEL_START_HERE.md`, `BABEL_APPS.md`, and `BABEL_PLATFORM.md` after Babel Truth.

## Current state — G7 shell clarity refinement, NOT frozen

Production remains V6.

G7 remains the isolated successor preview at `/v7-preview/` using `production-projects-v1-v7-preview`; it must never mutate V6 `production-projects-v1` data.

The last deployed baseline before this pass is PR **#62 — Consolidate G7 modal and row consistency**, merge `cdbcd23fca4fad338f62ce024dc6e89558b602d4`.

Physical review of that deployment found the shell materially closer, but not ready to freeze. The next coherent implementation is the **shell clarity refinement**:

- keep the shared Back / trailing-action toolbar-slot structure; make trailing `+` / `•••` feel like intentional controls rather than isolated glyphs
- remove redundant chevrons from project rows and Project Home progression rows
- keep project entries named **project rows** in product/design vocabulary
- give Setup editable values a shared trailing-value control grammar
- make Title Return/Next advance to Artist
- make custom Bars numeric-only in behavior as well as keyboard intent
- strengthen modal hierarchy through conceptual grouping, not additional decorative boxes
- remove redundant Add Section success/helper copy
- rebalance Tracks selection layout to item count + viewport rather than rendering filler-looking gaps
- simplify `Section name` → `Section` and `Track name` → `Track`
- make secondary sheet actions visibly pressable without competing with primary actions

This pass must preserve the pieces that already physically tested well: Original/Cover selection, connected selection geometry, stable row rhythm/anchors, history-aware Back, non-sticky page actions, and one product logic across iPhone/iPad.

**G7 is not physically approved/frozen. FIRE Core breadboarding has not started.**

## Critical boundary — shell fixtures are not FIRE Core architecture

Current G7 `Setup → Structure → Tracks` is **shell/workspace fixture content**. It is useful because it exercises the reusable shell:

- Setup → rows, editable values, state, form behavior
- Structure → sheets, single selection, segmented values, creation, editing, reordering
- Tracks → multi-selection, adaptive collections, custom creation, explicit confirmation

Do **not** interpret shell approval as approval of:

- The Map being exactly Setup → Structure → Tracks
- exactly three checkpoints per phase
- these exact fixture interactions being final FIRE Core workflow

After shell approval, FIRE Core breadboarding revisits the journey from first principles. For each real workspace/checkpoint, define the musician's problem, decision, required evidence, DAW action, evaluation, done criteria, retained context, and the most natural interaction. Selection, drag/reorder, connect/group, mark/draw, compare, toggle, or other direct manipulation can all be valid when they match the musical mental model.

Few visible destinations are desirable, but checkpoint count is earned by the work rather than fixed at three.

## Stable G7 shell behavior to preserve

- Projects → project Home → current shell-fixture workspaces
- public project types Original / Cover
- shared 64px grouped-row rhythm across major work surfaces
- connected section-type / Tracks selection-surface family
- segmented `4 / 8 / 12 / 16 / Custom` family
- grouped Title/Artist field focus at the group level
- toolbar `+` means add/create the primary discrete thing on Projects / Structure / Tracks
- toolbar `•••` means management/actions
- history-aware Back retraces actual route history; direct work entry falls back safely to Project Home
- Tracks Done confirms a non-empty current selection and returns Home without a Home → Back → Tracks loop
- shared non-sticky lower page-action region for Continue/Done
- iPhone/iPad share one product logic; sheet/dialog presentation may adapt
- V6 production schema/data remain untouched

## Current shell/accessory grammar

- `○` = incomplete/upcoming progression state
- `→` = current/recommended progression state
- `✓` = actual completion where that meaning is needed
- selected fill = chosen option
- drag handle = reorderable object
- chevron = deeper navigation only when another cue does not already make navigation clear
- `•••` = management/actions
- `+` = create/add the primary discrete object for the current view

Do not add state/accessories merely for visual symmetry. Project rows and progression rows no longer need redundant chevrons; Notes may retain one as a utility-navigation cue.

## Physical approval gate for this pass

After the shell clarity refinement is merged and deployed, review on real iPhone Safari first, then sanity-check iPad adaptation.

Focus on:

1. toolbar system as a whole: Back, trailing `+` / `•••`, title relationship, touch targets, and whether the trailing action still feels stranded
2. project rows without chevrons: opening remains obvious while `•••` still clearly means management
3. Project Home progression without chevrons: state mark remains sufficient and rows remain obviously tappable
4. New/Edit Project keyboard progression: Title Return/Next → Artist
5. Cancel/secondary action treatment: clearly a button, still quieter than primary
6. Setup Tempo/Meter: one clean, intentional trailing-value grammar
7. Add/Edit Section modal hierarchy: related custom fields read as part of their parent group; major groups remain distinct
8. custom Bars: numeric keyboard + nonnumeric rejection
9. Add Section repeated-entry flow without redundant `Added …` helper copy
10. Tracks adaptive layout: no filler-looking empty cells or awkward orphan treatment at phone/iPad widths
11. microcopy (`Section`, `Track`) feels concise without losing meaning
12. connected selection corners/outlines and stable 64px/52px geometry remain clean
13. Setup / Structure / Tracks first-content position and Back/history behavior remain stable
14. centered iPad dialogs preserve the same semantics/action hierarchy
15. overall: **does the generic shell now feel predictable enough to stop redesigning it?**

Do not record shell approval automatically. Babel must explicitly approve/freeze the generic shell fundamentals.

## After shell approval

Sequence:

**physical G7 shell approval → promote proven generic shell primitives into Babel Truth → FIRE Core breadboard + Lab shell reconciliation may then proceed in their appropriate lanes → thin FIRE Core spine → real-project validation**

FIRE Core does not need to wait for Lab visual reconciliation once the shared shell contract has been promoted; both can proceed without conflating product-specific behavior.

## Data / generation safety

- V6 production key: `production-projects-v1`
- G7 preview key: `production-projects-v1-v7-preview`
- no G7 change may mutate/wipe V6 production data
- schema changes require tested migration
- V6 remains production until an explicit later migration/release decision

## Continuity

`CONTINUITY_INBOX.md` is retired as an active local buffer.

All new unresolved durable Babel/FIRE deltas use Babel Truth Issue #1 under the persist-before-reply threshold. Routine capture is append-only through new comments; do not replace the Issue #1 body during ordinary work.

At consolidation of this pass, the old post-#62 physical-review findings become implementation-resolved; the remaining unresolved item should be the new physical approval gate until Babel explicitly approves or reports another system-level defect.

Git history is the archive for superseded implementation/history. Active docs should describe current truth, not every prior pass.
