# Babel FIRE — Start Here

Use **Babel** as the project-facing name.

## Read order

1. `BABEL_TRUTH.md`
2. Babel Truth shared authority at that pinned commit
3. this file
4. `FIRE_CORE.md`
5. `V6.md` for live production behavior
6. `V7_DRAFT.md` for G7 successor behavior
7. Babel Truth Issue #1 body plus newer comments
8. code/tests as implementation evidence

## Current state — G7 live, NOT frozen

Production remains V6. G7 remains the isolated successor preview at `/v7-preview/` using `production-projects-v1-v7-preview`; it must never mutate V6 `production-projects-v1` data.

PR #63 shell-clarity work is merged. Physical review found G7 materially closer but not ready to freeze. **FIRE Core breadboarding has not started.**

## Current routing — shell exploration in Lab, FIRE remains authority

Exploratory visual-shell work happens in Babel Lab's **Visual Lab / FIRE Shell Lab**.

FIRE remains the product authority and owns doctrine, runtime, data, specs, tests, and canonical production/successor implementation. **Lab is evidence, never authority.**

### Control-baseline requirement

Visual Lab must first establish a **faithful observable replica of the current G7 shell** with isolated Lab-only fake/local state. The purpose is a control condition, not a second FIRE product.

The control baseline should reproduce every user-facing shell surface and interaction needed to judge visual changes. Visible shell affordances should not be knowingly dead or replaced by invented harness behavior. In particular, preserve representative:

- Projects → project Home → Setup / Structure / Tracks navigation
- toolbar Back / `+` / `•••` semantics
- project create/edit/delete/reset management
- Setup inputs/toggles and keyboard/focus behavior
- Structure add/edit/reorder/verify and sheet/dialog behavior
- Tracks selection/custom creation/confirmation
- selection/completion states and row geometry
- iPhone/iPad adaptive sheet/dialog presentation

Lab-only navigation pills, explanatory footers, or developer shortcuts must not alter the normal FIRE canvas. Developer controls may exist outside it or behind an explicitly Lab-only control.

Visual Lab must use its own storage and must never read/write V6 production or G7 preview storage.

Once parity is verified, Lab may deliberately diverge to test candidate visual systems. Differences should be attributable to the experiment rather than missing functionality or harness chrome.

Current path:

**current G7 → faithful isolated Lab baseline → physical parity check → visual experiments → physical comparison → approved candidate → deliberate FIRE implementation → physical FIRE validation → transferable rules promoted to Babel Truth.**

Do not make G7 automatically match Lab. Do not promote Lab code as canonical implementation by default.

## Critical boundary — shell fixtures are not FIRE Core architecture

Current G7 `Setup → Structure → Tracks` is shell/workspace fixture content. It exercises rows, editable values, state, forms, sheets, selection, creation, editing, reordering, and confirmation. It does not prove that FIRE Core's eventual Map is exactly those workspaces or exactly three checkpoints.

After shell approval, FIRE Core breadboarding revisits the musician journey from first principles.

## Stable G7 behavior / evidence to preserve while experimenting

- Projects → project Home → current shell-fixture workspaces
- public project types Original / Cover
- history-aware Back retraces actual route history with safe fallback
- toolbar `+` means add/create the primary discrete thing for the current view
- toolbar `•••` means management/actions
- Tracks Done confirms a non-empty current selection and returns Home
- iPhone/iPad share one product logic; presentation may adapt
- V6 production schema/data remain untouched

Existing semantic evidence:

- **Inline = choose/toggle/classify/confirm/evaluate** something already in the current task
- **Sheet = create/edit/manage a discrete thing** while staying in context
- Navigation enters another meaningful workspace
- Menu/secondary affordance holds utilities that should not compete with musical work

An experiment may explicitly challenge a semantic rule, but must label that as a semantic experiment rather than smuggling it in as styling.

## Approval gate

Do not record shell approval automatically. Babel must explicitly approve/freeze generic shell fundamentals after the chosen candidate has been implemented back into FIRE and physically validated in the real product.

Physical validation covers iPhone first, iPad adaptation, and representative default/selected/custom/disabled/focus/keyboard/long-content states as applicable.

## After shell approval

**FIRE physical shell approval → promote genuinely transferable shell primitives into Babel Truth → FIRE Core breadboard → thin FIRE Core spine → real-project validation.**

## Data / generation safety

- V6 production key: `production-projects-v1`
- G7 preview key: `production-projects-v1-v7-preview`
- Lab must use a separate Lab-only key
- no G7/Lab change may mutate or wipe V6 production data
- V6 remains production until an explicit later migration/release decision

## Continuity

`CONTINUITY_INBOX.md` is retired as an active local buffer. New unresolved durable Babel/FIRE deltas use Babel Truth Issue #1 under the persist-before-reply threshold. Git history is the archive for superseded implementation/history; active docs describe current truth.
