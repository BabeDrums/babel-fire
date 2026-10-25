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
8. `G7_SHELL_CERTIFICATION_STATUS.md` for mutable category/evidence status
9. Babel Truth Issue #1 body **plus newer comments** for unresolved FIRE items
10. code/tests as implementation evidence

## Current state — G7 Shell Certification active

Production remains V6.

G7 remains the isolated successor preview at `/v7-preview/` using `production-projects-v1-v7-preview`; it must never mutate V6 `production-projects-v1` data.

PR **#66 — Return coordinated shell iteration to G7** established that complete coordinated FIRE shell work belongs in the real isolated G7 context; the former full-shell Lab replica is rejected evidence.

PR **#67 — Refine G7 shell cohesion after physical review** is merged. Its deployed result is useful evidence, but physical review continued to expose systemic shell inconsistencies rather than final FIRE-workflow questions.

The developer Shell Test is now the shared-primitives certification surface inside G7. Physical review has found it broadly useful while still exposing fundamentals to correct: project-row management treatment, optical glyph/accessory geometry, current-state language, modal/group rhythm, reliable deployed-build identification, and real-screen regressions caused by over-broad shared selectors.

**G7 is not approved/frozen. FIRE Core breadboarding has not started.**

The active phase is **G7 Shell Certification**. `G7_SHELL_CERTIFICATION.md` defines the finite ten-category completion contract, `Unresolved → Candidate → Locked` states, the developer-only Shell Test, and the final freeze gate. `G7_SHELL_CERTIFICATION_STATUS.md` records mutable review evidence.

No category is automatically Locked. Existing G7 work remains evidence and can become Locked only through the certification criteria and physical-device validation.

## Reliability baseline

Shell work must leave implementation, active authority, regression expectations, handoff state, and deployed assets describing the same candidate.

- Do not merge a shell change with known red regressions.
- If a deliberate product/shell decision makes an old regression obsolete, update that regression in the same change rather than restoring superseded behavior just to get green.
- **Shell Test passing is not sufficient for a shared-primitive merge.** Shared primitives used by real G7 must also pass browser coverage in the actual G7 fixture path at 390/440/820 widths. The current minimum real-screen path is Project → Setup → Structure temporary UI.
- Real-screen regression coverage must guard current-state geometry, form-control containment, and sheet chrome so a certification specimen cannot be green while the project fixture is visibly broken.
- G7 and Shell Test CSS/JS asset URLs are tied to the deployed GitHub Pages build revision rather than a manually bumped cache string.
- G7's module dependency mapping revisions `model.js` with the same deployed build revision.
- Shell Test and real G7 display the deployed short commit from `build-info.json`; physical review should target that exact revision.
- CI preprocesses the same Pages revision placeholders for local browser regressions, so test behavior matches deployed asset wiring.
- Browser-test dependencies are pinned for reproducibility instead of silently changing under the repo.
- The authority/handoff gate protects current semantic markers, not exact wording from retired G7 drafts.

## Current strategy — certify the grammar, not the fixture screens

The goal is not to perfect Setup, Structure, Tracks, or any other temporary FIRE workflow. The goal is to establish reusable visual/interaction grammar strong enough that a future section, screen, modal, menu, form, or workspace can be composed from solved fundamentals and already feel like Babel.

Current G7 `Setup → Structure → Tracks` is disposable **shell/workspace fixture content**. It exists to exercise the shell. FIRE Core breadboarding may rename, regroup, deepen, replace, or remove it.

Do not spend shell work product-designing a fixture interaction merely because it is visible. Change fixture content when doing so helps stress-test the shell; otherwise keep attention on transferable primitives.

### Developer Shell Test

The developer-only Shell Test lives **inside G7** and uses the actual G7 primitives/tokens/styles. It is a component/state stress-test surface, not a second FIRE implementation and not a FIRE Core destination.

It deliberately exercises the ten certification categories and representative sparse/normal/dense, short/long, default/selected/custom/disabled/focus/error states where applicable. A primitive fixed in Shell Test must be the same primitive used by real G7.

Shell Test does not replace real-product or physical-device validation. Shared primitive changes must survive both the Shell Test and the real G7 fixture browser path before merge.

## Routing — G7, Lab, Truth, FIRE Core

- **G7** owns coordinated FIRE shell implementation, Shell Test, in-context validation, and certification.
- **Babel Lab** remains an optional bounded sandbox for isolated experiments. Lab is evidence, never authority. Do not rebuild the full FIRE shell there.
- **Babel Truth** owns only genuinely transferable cross-app principles/contracts after deliberate promotion and owning-product validation.
- **FIRE Core** owns the real end-to-end production-companion workflow and remains blocked until the G7 shell freeze gate is explicitly passed.

Default shell workflow:

**diagnose a certification category → exercise actual primitives in Shell Test and real G7 → optionally use Lab for a bounded experiment → implement the candidate in G7 → run/reconcile regression + authority gates → deploy exact revision → physical-device validation → mark category Candidate/Locked only when its gate is satisfied → repeat → final physical sweep → explicit shell freeze.**

Do not make G7 automatically match a Lab specimen.

## Stable G7 evidence to preserve unless certification proves a better primitive

- Projects → project Home → current shell-fixture workspaces
- public project types Original / Cover
- history-aware Back retraces actual route history; direct work entry falls back safely to Project Home
- toolbar `+` means add/create the primary discrete thing for the current view
- toolbar `•••` means management/actions
- project-row management has no decorative divider from the row
- recurring state/accessory meanings use one canonical shared geometry while different meanings are not forced into the same visible container
- current progress state uses a neutral nested-ring language under physical review: a brighter outer ring plus a quieter faded inner ring touching the inside edge of the outer ring; color alone does not carry the state
- the accessory family uses one rounded construction vocabulary for drawn strokes/caps while preserving semantic hierarchy between state, navigation, reorder, add, and management affordances
- Tracks Done currently confirms a non-empty current selection and returns Home without a Home → Back → Tracks loop; this is fixture behavior, not promised FIRE Core architecture
- iPhone/iPad share one product logic; presentation may adapt
- V6 production schema/data remain untouched

Existing interaction semantics remain useful evidence:

- **Inline = choose/toggle/classify/confirm/evaluate** something already in the current task
- **Sheet = create/edit/manage a discrete thing** while staying in context
- Navigation enters another meaningful workspace
- Menu/secondary affordance holds utilities that should not compete with musical work

## Current certification findings / physical-review focus

The following are **implemented Candidate evidence, not Locked conclusions**:

- project-row `•••` divider removed and management aligned through the shared accessory lane
- `+` drawn from centered CSS strokes rather than a font glyph so Safari/iOS font metrics cannot shift it
- management `•••`, chevron, reorder, and completion check use fixed drawn geometry on the shared accessory artboard rather than font baseline metrics where practical
- canonical completion/current/incomplete/chevron/ellipsis/add/drag accessory boxes and optical corrections live in the shared primitive layer
- current state borrows only the older roadmap's nested-state structure: neutral outer ring plus a subtle faded inner ring touching the outer ring's inside edge, not the old yellow accent and not a center dot
- Current's generated inner ring is absolutely positioned so hidden legacy text in the real fixture cannot move it onto another grid row
- shared accessory layout no longer overrides `.form-row`; Setup value controls retain their own label/control grid and stay contained at compact widths
- shared sheet styling no longer adds an action-divider hairline or inset top hairline that was not part of the approved shell language
- rounded terminals/caps unify the accessory family's visual handwriting without forcing different semantic meanings into identical containers
- modal content-group and action rhythm use named shared tokens rather than test-only magic numbers
- Shell Test subtitle is the live G7 deployed-version indicator
- Setup / Structure / Tracks remain disposable fixture semantics; `Accurate` wording and the Tracks layout are not FIRE Core doctrine

Next product-facing work is physical confirmation of the repaired exact deployed revision, followed by category-by-category certification. Do not infer additional FIRE Core architecture from the fixture content.

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
