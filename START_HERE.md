# Babel FIRE — Start Here

Use **Babel** as the project-facing name.

## Read order

1. `BABEL_TRUTH.md` — immutable pointer to the cross-app Babel Truth commit this repo has reconciled against
2. Babel Truth `START_HERE.md` / `AGENTS.md` / relevant shared authority at that pinned commit
3. this file — current FIRE build/review/next-step state
4. `FIRE_CORE.md`
5. `V6.md` for live production behavior
6. `V7_DRAFT.md` for G7 successor behavior
7. `G7_SHELL_CERTIFICATION.md` for the active shell-completion contract and freeze gate
8. Babel Truth Issue #1 body **plus newer comments** for unresolved FIRE items
9. code/tests as implementation evidence

## Current state — G7 Shell Certification active

Production remains V6.

G7 remains the isolated successor preview at `/v7-preview/` using `production-projects-v1-v7-preview`; it must never mutate V6 `production-projects-v1` data.

PR **#66 — Return coordinated shell iteration to G7** established that complete coordinated FIRE shell work belongs in the real isolated G7 context; the former full-shell Lab replica is rejected evidence.

PR **#67 — Refine G7 shell cohesion after physical review** is merged. Its deployed result is useful evidence, but physical review still exposed systemic shell inconsistencies: project-row management treatment, glyph/accessory geometry, modal composition, and fixture-specific UI being mistaken for shell work.

**G7 is not approved/frozen. FIRE Core breadboarding has not started.**

The active phase is now **G7 Shell Certification**. `G7_SHELL_CERTIFICATION.md` defines the finite ten-category completion contract, `Unresolved → Candidate → Locked` states, the developer-only Shell Test, and the final freeze gate.

At adoption of that contract, no category is automatically Locked. Existing G7 work remains evidence and can become Candidate/Locked only through the certification criteria.

## Current strategy — certify the grammar, not the fixture screens

The goal is not to perfect Setup, Structure, Tracks, or any other temporary FIRE workflow. The goal is to establish reusable visual/interaction grammar strong enough that a future section, screen, modal, menu, form, or workspace can be composed from solved fundamentals and already feel like Babel.

Current G7 `Setup → Structure → Tracks` is disposable **shell/workspace fixture content**. It exists to exercise the shell. FIRE Core breadboarding may rename, regroup, deepen, replace, or remove it.

Do not spend shell work product-designing a fixture interaction merely because it is visible. Change fixture content when doing so helps stress-test the shell; otherwise keep attention on transferable primitives.

### Developer Shell Test

Build a developer-only Shell Test **inside G7** using the actual G7 primitives/tokens/styles. It is a component/state stress-test surface, not a second FIRE implementation and not a FIRE Core destination.

It should deliberately exercise the ten certification categories and representative sparse/normal/dense, short/long, default/selected/custom/disabled/focus/error states where applicable. A primitive fixed in Shell Test must be the same primitive used by real G7.

Shell Test does not replace real-product or physical-device validation.

## Routing — G7, Lab, Truth, FIRE Core

- **G7** owns coordinated FIRE shell implementation, Shell Test, in-context validation, and certification.
- **Babel Lab** remains an optional bounded sandbox for isolated experiments. Lab is evidence, never authority. Do not rebuild the full FIRE shell there.
- **Babel Truth** owns only genuinely transferable cross-app principles/contracts after deliberate promotion and owning-product validation.
- **FIRE Core** owns the real end-to-end production-companion workflow and remains blocked until the G7 shell freeze gate is explicitly passed.

Default shell workflow:

**diagnose a certification category → exercise actual primitives in Shell Test and real G7 → optionally use Lab for a bounded experiment → implement the candidate in G7 → physical-device validation → mark category Candidate/Locked only when its gate is satisfied → repeat → final physical sweep → explicit shell freeze.**

Do not make G7 automatically match a Lab specimen.

## Stable G7 evidence to preserve unless certification proves a better primitive

- Projects → project Home → current shell-fixture workspaces
- public project types Original / Cover
- history-aware Back retraces actual route history; direct work entry falls back safely to Project Home
- toolbar `+` means add/create the primary discrete thing for the current view
- toolbar `•••` means management/actions
- Tracks Done currently confirms a non-empty current selection and returns Home without a Home → Back → Tracks loop; this is fixture behavior, not promised FIRE Core architecture
- iPhone/iPad share one product logic; presentation may adapt
- V6 production schema/data remain untouched

Existing interaction semantics remain useful evidence:

- **Inline = choose/toggle/classify/confirm/evaluate** something already in the current task
- **Sheet = create/edit/manage a discrete thing** while staying in context
- Navigation enters another meaningful workspace
- Menu/secondary affordance holds utilities that should not compete with musical work

## Immediate certification findings / next implementation pass

Use the latest physical review as input to the first Shell Certification pass:

- remove the divider separating project-row `•••`; make management feel native to and optically aligned within the row
- optically center `+` inside its control surface and keep shared toolbar geometry coherent
- establish one canonical recurring glyph/accessory system: check/current/incomplete/chevron/ellipsis/add/drag geometry, optical weight, size, and accessory slots
- eliminate accidental differences between checkmarks/circles used for the same meaning
- improve the shared modal/sheet primitive as Babel composition rather than polishing one Structure fixture
- treat `Accurate` wording and the current Tracks UI as disposable fixture semantics; do not lock product architecture from them
- use wider/different fixture density only when it helps stress-test the shell
- continue solving typography, spacing, surfaces, actions, controls, responsive behavior, accessibility, and motion through the ten-category contract rather than page-by-page taste

No additional FIRE Core architecture should be inferred from this pass.

## Certification and approval gate

`G7_SHELL_CERTIFICATION.md` is the active checklist. Categories are **Unresolved**, **Candidate**, or **Locked**.

A category becomes Locked only after its primitive family is coherent, has representative Shell Test coverage where applicable, is exercised in real G7 context, and passes relevant physical iPhone/iPad validation.

Do not record final shell approval automatically.

Final freeze requires:

**10/10 categories Locked → final real G7 physical-device sweep → no unresolved systemic contradiction → explicit Babel approval → G7 Shell Frozen.**

Shell freeze means the foundation is stable enough to build confidently. A genuinely new requirement discovered during FIRE Core may deliberately extend the smallest necessary part of the shell; that does not casually reopen unrelated locked categories.

## After shell freeze

Sequence:

**G7 Shell Frozen → promote genuinely transferable validated principles into Babel Truth → FIRE Core breadboard → thin FIRE Core spine → real-project validation.**

The FIRE Core breadboard then revisits the journey from first principles. For each real workspace/checkpoint, define the musician's problem, decision, required evidence, DAW action, evaluation, done criteria, retained context, and most natural interaction.

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
