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

## Current state — G7 shell-cohesion pass awaiting physical review

Production remains V6.

G7 remains the isolated successor preview at `/v7-preview/` using `production-projects-v1-v7-preview`; it must never mutate V6 `production-projects-v1` data.

PR **#63 — Refine G7 shell clarity after physical review** is merged at `a39b306b02c66c3cd3ed9749005af9966780e617`.

PR **#66 — Return coordinated shell iteration to G7** is merged. The full-shell Lab replica is rejected evidence; coordinated FIRE shell work belongs in the real isolated G7 context.

PR **#67 — Refine G7 shell cohesion after physical review** is the current implementation pass. It tightens the shared toolbar/title relationship, integrates project-row management, normalizes typography/value-control treatment, and stabilizes sheet action composition. It does not change FIRE Core architecture or V6 data/runtime.

**G7 is not physically approved/frozen. FIRE Core breadboarding has not started.** The next gate is real-device review of the deployed #67 result after merge.

## Current routing — coordinated shell iteration stays in G7

G7 is already an isolated successor and contains the real FIRE navigation, state relationships, responsive behavior, and shell interactions. It is therefore the correct place to continue coordinated FIRE shell iteration.

Do not rebuild the complete FIRE shell in Babel Lab merely to create a visual test environment. The attempted full-shell Lab replica is rejected evidence: reconstruction bugs, missing interactions, and visual drift added variables that obscured the actual design question and created duplicate implementation work.

Babel Lab remains useful as a bounded test bench. Use it for isolated questions that genuinely benefit from separation — for example a few modal treatments, a row language, selection control, navigation concept, motion idea, or surface/material study. If the complete shell context is needed to judge the idea, work directly in G7.

A Lab step is optional.

Default shell workflow:

**observe G7 on physical device → diagnose repeated/systemic defects → optionally explore a bounded idea in Lab → implement the promising decision in G7 → physical-device review → iterate → explicit shell approval/freeze → promote genuinely transferable principles to Babel Truth.**

Do not make G7 automatically match a Lab specimen. Lab is evidence, never authority.

## Critical boundary — shell fixtures are not FIRE Core architecture

Current G7 `Setup → Structure → Tracks` is **shell/workspace fixture content**. It is useful because it exercises the reusable shell:

- Setup → rows, editable values, state, form behavior
- Structure → sheets, single selection, segmented values, creation, editing, reordering
- Tracks → multi-selection, adaptive collections, custom creation, explicit confirmation

Do **not** interpret eventual shell approval as approval of:

- The Map being exactly Setup → Structure → Tracks
- exactly three checkpoints per phase
- these exact fixture interactions being final FIRE Core workflow

After shell approval, FIRE Core breadboarding revisits the journey from first principles. For each real workspace/checkpoint, define the musician's problem, decision, required evidence, DAW action, evaluation, done criteria, retained context, and the most natural interaction.

## Stable G7 behavior / evidence to preserve while experimenting

- Projects → project Home → current shell-fixture workspaces
- public project types Original / Cover
- stable grouped-row rhythm/anchors
- history-aware Back retraces actual route history; direct work entry falls back safely to Project Home
- toolbar `+` means add/create the primary discrete thing for the current view
- toolbar `•••` means management/actions
- Tracks Done confirms a non-empty current selection and returns Home without a Home → Back → Tracks loop
- iPhone/iPad share one product logic; presentation may adapt
- V6 production schema/data remain untouched

Existing interaction semantics remain useful evidence:

- **Inline = choose/toggle/classify/confirm/evaluate** something already in the current task
- **Sheet = create/edit/manage a discrete thing** while staying in context
- Navigation enters another meaningful workspace
- Menu/secondary affordance holds utilities that should not compete with musical work

## Current physical-review targets

Review the #67 shell-cohesion result on real iPhone Safari first, then sanity-check iPad. Pay particular attention to:

- whether the lowered/integrated toolbar `+` now feels attached to the page rather than stranded at the top edge
- whether project-card `•••` feels integrated into the row while remaining discoverable and tappable
- whether New/Edit Project Return/Next behavior feels natural on the actual iPhone keyboard
- whether Tempo focus/keyboard appearance now feels like part of the value-control system
- whether headers, metadata, row labels, and work-page titles feel like one coherent typography hierarchy
- whether Cancel now reads as a real secondary action beside Create/Save/Add
- modal/surface language across iPhone bottom-sheet and iPad centered-dialog presentations
- spacing/density on both sparse and content-heavy pages
- consistent row/control geometry and selection language
- sparse pages should not scroll unnecessarily; dense pages should scroll naturally

Repeated defects should be solved as component/system defects rather than patched independently on every page.

## Approval gate

Do not record shell approval automatically. Babel must explicitly approve/freeze the generic shell fundamentals after physical validation in the real G7 product context.

Physical validation should cover iPhone first and iPad adaptation, plus representative default/selected/custom/disabled/focus/keyboard/long-content states as applicable.

## After shell approval

Sequence:

**physical G7 shell approval → promote genuinely transferable shell primitives into Babel Truth → FIRE Core breadboard → thin FIRE Core spine → real-project validation.**

Lab remains available for future bounded experiments; its existence does not mutate Truth or FIRE automatically.

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
