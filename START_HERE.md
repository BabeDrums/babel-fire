# Babel FIRE — Start Here

Use **Babel** as the project-facing name.

## Read order

1. `BABEL_TRUTH.md` — immutable pointer to the cross-app Babel Truth commit this repo has reconciled against
2. Babel Truth `START_HERE.md` / `AGENTS.md` / relevant shared authority at that pinned commit
3. this file — current FIRE build/review/next-step state
4. `FIRE_CORE.md`
5. `V6.md` for live production behavior
6. `V7_DRAFT.md` for G7 successor behavior
7. Babel Truth Issue #1 body **plus newer comments** for unresolved FIRE items
8. code/tests as implementation evidence

For wider ecosystem/surrounding-app work instead, use `BABEL_START_HERE.md`, `BABEL_APPS.md`, and `BABEL_PLATFORM.md` after Babel Truth.

## Current state — G7 live, NOT frozen

Production remains V6.

G7 remains the isolated successor preview at `/v7-preview/` using `production-projects-v1-v7-preview`; it must never mutate V6 `production-projects-v1` data.

PR **#63 — Refine G7 shell clarity after physical review** is merged at `a39b306b02c66c3cd3ed9749005af9966780e617`.

Physical review found the shell materially closer but **not ready to freeze**. In particular, the modal/surface language still needs visual-system exploration rather than another sequence of local production patches.

**G7 is not physically approved/frozen. FIRE Core breadboarding has not started.**

## Current routing — shell exploration moves to Lab

Exploratory visual-shell work now happens in Babel Lab's dedicated **Visual Lab / FIRE Shell Lab** harness.

This does **not** move FIRE ownership or the FIRE project into Lab:

- FIRE remains the product authority and owns product doctrine, runtime, data, specs, tests, and production/successor code
- Visual Lab is a disposable visual-interaction harness using fake/prototype state
- Lab may contain contradictory candidates and does not define a canonical Babel style
- **Lab is evidence, never authority**
- do not make G7 automatically match Lab; a chosen candidate must be deliberately implemented in FIRE

The current Structure modal study is the first specimen in Visual Lab. It is not sufficient by itself to prove the shell. The harness should expand across representative pages, rows, controls, forms, sheets/dialogs, menus, states, focus/keyboard behavior, and iPhone/iPad adaptation before a shell candidate is considered mature.

Default promotion path:

**Lab experiment → physical-device testing → candidate → FIRE implementation → FIRE physical validation → transferable rules promoted to Babel Truth.**

Pause further exploratory shell styling directly in G7 while this candidate work is active. Production fixes or safety fixes remain FIRE-local and should not be blocked by Lab.

## Critical boundary — shell fixtures are not FIRE Core architecture

Current G7 `Setup → Structure → Tracks` is **shell/workspace fixture content**. It is useful because it exercises the reusable shell:

- Setup → rows, editable values, state, form behavior
- Structure → sheets, single selection, segmented values, creation, editing, reordering
- Tracks → multi-selection, adaptive collections, custom creation, explicit confirmation

Do **not** interpret eventual shell approval as approval of:

- The Map being exactly Setup → Structure → Tracks
- exactly three checkpoints per phase
- these exact fixture interactions being final FIRE Core workflow

After shell approval, FIRE Core breadboarding revisits the journey from first principles. For each real workspace/checkpoint, define the musician's problem, decision, required evidence, DAW action, evaluation, done criteria, retained context, and the most natural interaction. Selection, drag/reorder, connect/group, mark/draw, compare, toggle, or other direct manipulation can all be valid when they match the musical mental model.

Few visible destinations are desirable, but checkpoint count is earned by the work rather than fixed at three.

## Stable G7 behavior / evidence to preserve while experimenting

These are useful tested behaviors and constraints, not a command that every Lab candidate must visually copy them:

- Projects → project Home → current shell-fixture workspaces
- public project types Original / Cover
- stable grouped-row rhythm/anchors
- history-aware Back retraces actual route history; direct work entry falls back safely to Project Home
- toolbar `+` means add/create the primary discrete thing for the current view
- toolbar `•••` means management/actions
- Tracks Done confirms a non-empty current selection and returns Home without a Home → Back → Tracks loop
- iPhone/iPad share one product logic; sheet/dialog presentation may adapt
- V6 production schema/data remain untouched

Existing interaction semantics remain useful evidence:

- **Inline = choose/toggle/classify/confirm/evaluate** something already in the current task
- **Sheet = create/edit/manage a discrete thing** while staying in context
- Navigation enters another meaningful workspace
- Menu/secondary affordance holds utilities that should not compete with musical work

Visual Lab is allowed to challenge presentation details and candidate component geometry without silently changing these semantics. If an experiment challenges a semantic rule itself, label that explicitly rather than smuggling it in as styling.

## Approval gate

Do not record shell approval automatically. Babel must explicitly approve/freeze the generic shell fundamentals **after** the chosen candidate has been implemented back into FIRE and physically validated in the real product.

Physical validation should cover iPhone first and iPad adaptation, plus representative default/selected/custom/disabled/focus/keyboard/long-content states as applicable.

## After shell approval

Sequence:

**Lab candidate → FIRE implementation → physical FIRE shell approval → promote genuinely transferable shell primitives into Babel Truth → FIRE Core breadboard → thin FIRE Core spine → real-project validation.**

Lab can continue holding future visual experiments after approval; their existence does not mutate Truth or FIRE automatically.

## Data / generation safety

- V6 production key: `production-projects-v1`
- G7 preview key: `production-projects-v1-v7-preview`
- no G7 change may mutate/wipe V6 production data
- schema changes require tested migration
- V6 remains production until an explicit later migration/release decision

## Continuity

`CONTINUITY_INBOX.md` is retired as an active local buffer.

All new unresolved durable Babel/FIRE deltas use Babel Truth Issue #1 under the persist-before-reply threshold. Routine capture is append-only through new comments; do not replace the Issue #1 body during ordinary work.

Git history is the archive for superseded implementation/history. Active docs should describe current truth, not every prior pass.
