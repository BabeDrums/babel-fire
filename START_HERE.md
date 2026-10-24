# Babel FIRE — Start Here

Use **Babel** as the project-facing name.

## Read order

1. `BABEL_TRUTH.md` — immutable pointer to the cross-app Babel Truth commit this repo has reconciled against
2. Babel Truth `START_HERE.md` / `AGENTS.md` / relevant shared authority at that pinned commit
3. this file — current FIRE build/review/next-step state
4. `FIRE_CORE.md`
5. `V6.md` for live production behavior
6. `V7_DRAFT.md` for active G7 successor behavior
7. relevant FIRE items in Babel Truth Issue #1 (`Babel Continuity Buffer`)
8. code/tests as implementation evidence

For wider ecosystem/surrounding-app work instead, use `BABEL_START_HERE.md`, `BABEL_APPS.md`, and `BABEL_PLATFORM.md` after Babel Truth.

## Current state — G7 live, NOT frozen

Production remains V6.

G7 remains the isolated successor preview at `/v7-preview/` using `production-projects-v1-v7-preview`; it must never mutate V6 `production-projects-v1` data.

Current G7 implementation lineage:

- PR **#60 — Normalize the G7 rhythm and navigation after physical review** established the last physically reviewed/deployed shell baseline at merge `a62c29ab4a17b8ac11ac9eea165f4899cb6ce06a`.
- the subsequent Babel Truth adoption changed authority/handoff wiring only; it did not change G7 runtime behavior.
- the next G7 implementation after #60 is **Modal + row consistency consolidation**. On a working branch it is the active candidate; once that implementation is on `main`, it is the current G7 implementation baseline. Use `main`/PR state and Pages deployment state to determine whether it is deployed rather than treating old “candidate” wording as authority.

**G7 is not physically approved/frozen. FIRE Core breadboarding has not started.**

## Stable G7 behavior to preserve

The shell intentionally includes:

- Projects → project Home → Setup → Structure → Tracks
- musician-facing `Setup`, `Listen`, and Structure verification `Accurate`
- shared 64px grouped-row rhythm across major work surfaces
- connected section-type / Tracks selection-surface family
- segmented `4 / 8 / 12 / 16 / Custom` bar selection
- Title/Artist grouped-field focus at the group level
- toolbar `+` for add/create on Projects / Structure / Tracks
- history-aware Back behavior: sequential work retraces actual route history; direct work entry falls back safely to Project Home
- Tracks Done confirms a non-empty current selection and returns Home without creating a Home → Back → Tracks loop
- shared non-sticky lower page-action region for Continue/Done
- iPhone/iPad share one product logic; modal presentation may adapt

Do not regress these while correcting visual consistency.

## Latest real-device review after #60

The shell feels materially closer. The remaining problems were system-level consistency issues rather than broad architecture.

The **Modal + row consistency consolidation** resolves the current implementation contract at the system level:

- sheet spacing now distinguishes strong conceptual-group separation from related-control/action spacing
- New Project uses stronger separation between Original/Cover and grouped Title/Artist without inflating every gap
- standalone project-action Cancel uses the full action-group width; paired form/confirmation actions remain paired
- connected Selection/Segmented surfaces own their outer geometry; selected children use fill without nested selected outlines
- Tracks selection uses fill without redundant selection checks
- repeated row labels use one stable typography role instead of changing weight with state
- Structure removes the visible ordinal column so section names share the common row text anchor; ordinal context remains in accessible edit/reorder labels
- Setup / Structure / Tracks share the same first-content vertical anchor
- centered iPad dialogs remain the adaptive presentation of the same modal semantics

These are shell-system rules, not new FIRE features. V6/runtime data/schema remain untouched.

## Physical approval gate for this implementation

After the modal + row pass is merged/deployed, review on real iPhone Safari first, then sanity-check iPad adaptation.

Focus on:

1. New Project Original/Cover → Title/Artist major-group spacing vs Title/Artist → actions
2. Cancel/action placement across New/Edit/Action/Add/Edit/confirmation sheets
3. Add Section spacing between section type, bars, optional custom fields/notices, and actions
4. selection corners/outlines with no nested-box artifact
5. Tracks selected-fill clarity without checkmarks
6. stable row label weight and horizontal anchor across Project Home / Setup / Structure
7. Structure rows without visible numbers while order remains obvious
8. Setup → Structure → Tracks first-content position
9. existing Back/history behavior
10. iPad centered dialogs preserving the same semantics
11. overall question: **does the shell now feel like one physical system rather than a collection of individually-good pages?**

Do not record shell approval automatically. Babel must explicitly approve/freeze the generic shell fundamentals.

## FIRE interaction grammar

- **Inline = choose/toggle/classify/confirm/evaluate** something already in the task.
- **Sheet = create/edit/manage a discrete thing** while staying in context.
- **Navigation = enter another meaningful workspace.**
- menu/secondary affordance = utility actions that should not compete with musical work.

Same meaning should reuse the same visual grammar. Different meaning may use a different accessory/presentation.

## Current state/accessory grammar

- `○` = incomplete/upcoming progression
- `→` = current/recommended progression
- `✓` = actual completion where that meaning is needed
- selected fill = chosen option
- drag handle = reorderable object
- chevron = navigation deeper
- `•••` = management/actions
- `+` = create/add the primary discrete object for the current view

Do not add state/accessories merely for visual symmetry.

## After shell approval

Sequence remains:

**physical G7 shell approval → FIRE Core breadboard → thin end-to-end FIRE Core spine → real-project validation**

The breadboard is behavior-first, not pixel-first. For every phase define:

- entering problem
- what FIRE asks the musician to notice
- decision being made
- Logic action/experiment
- evaluation
- done criteria
- evidence retained
- carry-forward context

The thin FIRE Core then proves the smallest believable full journey on real music before deep polish.

## Data / generation safety

- V6 production key: `production-projects-v1`
- G7 preview key: `production-projects-v1-v7-preview`
- no G7 change may mutate/wipe V6 production data
- schema changes require tested migration
- V6 remains production until an explicit later migration/release decision

## Continuity

`CONTINUITY_INBOX.md` is retired as an active local buffer.

All new unresolved durable Babel/FIRE deltas use Babel Truth Issue #1 under the persist-before-reply threshold. Mature FIRE-specific decisions get promoted into FIRE authority here (`FIRE_CORE.md`, generation spec, or this current-state handoff); genuinely cross-app lessons get promoted into Babel Truth.

At consolidation of this pass, resolved modal/row items should leave the active Truth buffer; only the next physical-review gate or genuinely unresolved findings should remain.

Git history is the archive for superseded implementation/history. Active docs should describe current truth, not every prior pass.
