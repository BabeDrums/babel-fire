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

## Current verified state — G7 live, NOT frozen

Production remains V6.

G7 remains the isolated successor preview at `/v7-preview/` using `production-projects-v1-v7-preview`; it must never mutate V6 `production-projects-v1` data.

Latest merged/deployed G7 implementation baseline:

- PR **#60 — Normalize the G7 rhythm and navigation after physical review**
- merge commit **`a62c29ab4a17b8ac11ac9eea165f4899cb6ce06a`**
- required static/handoff + 390 / 440 / 820 browser regressions passed before merge
- GitHub Pages deployed that exact merge commit successfully

At the start of the Babel Truth adoption pass there were no open FIRE PRs.

**G7 is not physically approved/frozen. FIRE Core breadboarding has not started.**

## Stable G7 behavior after #60

The current shell intentionally includes:

- Projects → project Home → Setup → Structure → Tracks
- musician-facing `Setup`, `Listen`, and Structure verification `Accurate`
- shared grouped-row rhythm across major work surfaces
- connected section-type / Tracks selection-surface family
- segmented `4 / 8 / 12 / 16 / Custom` bar selection
- Title/Artist grouped-field focus at the group level
- toolbar `+` for add/create on Projects / Structure / Tracks
- history-aware Back behavior: sequential work retraces actual route history; direct work entry falls back safely to Project Home
- Tracks Done confirms a non-empty current selection and returns Home without creating a Home → Back → Tracks loop
- shared non-sticky lower page-action region for Continue/Done
- iPhone/iPad share one product logic; modal presentation may adapt

Do not regress these while addressing the next physical-review findings.

## Latest real-device review after #60

The shell feels materially closer. The remaining problems are now system-level polish/consistency issues rather than broad architecture.

The authoritative unresolved detail list is preserved in **Babel Truth Issue #1** under `Pending FIRE physical-review deltas`.

Current findings to shape into the next FIRE pass:

- modal action composition is inconsistent: standalone Cancel becomes a small centered control while paired actions behave differently
- New Project needs a stronger major-group gap between Original/Cover and grouped Title/Artist, without blindly increasing every gap
- Add Section modal spacing between section type, bars, optional/notice regions, and Done/Add needs a coherent sheet-spacing grammar
- selected choices still draw nested/inset rectangles / ugly corner geometry; parent surface should own outer shape while selected child state stays visually clean
- Tracks still shows redundant selection checkmarks in the current implementation
- row label typography/weight and text anchors drift across state/screen
- visible Structure ordinal numbers push section names to a different horizontal anchor; strongest current hypothesis is to remove visible numbers while retaining ordinal meaning accessibly
- define one shared row-content grammar: leading text anchor, typography role, trailing metadata slot, accessory slot
- Setup / Structure / Tracks first-content position should remain visually stable; Projects → project Home may keep an intentional hierarchy transition if useful metadata earns it
- current centered iPad modal presentation feels good and should remain an adaptive presentation of the same semantics

These are hypotheses/feedback to solve as a coherent system pass, not literal implementation commands. Apply Babel Truth's Diagnose → Shape → Contract process before coding.

## Next FIRE pass goal

Working description:

> **Modal + row consistency consolidation**

Success means the user can move through the shell without noticing accidental changes in spacing, action alignment, label weight, text position, selection geometry, or first-content anchoring.

Prioritize the root system rules before screen-specific patches:

1. sheet spacing/action grammar
2. clean selection-state geometry
3. shared row content/typography grammar
4. stable work-screen content anchor
5. affected regression assertions
6. FIRE authority/handoff cleanup
7. resolve/promote relevant Truth-buffer items

Do **not** broaden this pass into FIRE Core features, animation/personality work, account/platform infrastructure, or Babel World implementation.

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

## Physical approval gate

After the next pass, review on real iPhone Safari first, then sanity-check iPad adaptation.

Focus on:

1. modal major-group vs related-control spacing
2. Cancel/action placement across New/Edit/Action/Add/Edit sheets
3. selection corners/outlines with no nested-box artifact
4. Tracks selection clarity without redundant checks if removed
5. stable label typography and horizontal text anchors
6. Structure rows after ordinal/alignment decision
7. Setup → Structure → Tracks first-content position
8. existing Back/history behavior
9. iPad centered dialogs preserving the same semantics
10. overall question: **does the shell now feel like one physical system rather than a collection of individually-good pages?**

Do not record shell approval automatically. Babel must explicitly approve/freeze the generic shell fundamentals.

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

All new unresolved durable Babel/FIRE deltas use Babel Truth Issue #1 under the persist-before-reply threshold. Mature FIRE-specific decisions still get promoted into FIRE authority here (`FIRE_CORE.md`, generation spec, or this current-state handoff); genuinely cross-app lessons get promoted into Babel Truth.

Git history is the archive for superseded implementation/history. Active docs should describe current truth, not every prior pass.
