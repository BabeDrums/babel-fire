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

The developer Shell Test is now the shared-primitives certification surface inside G7. Physical review has found it broadly useful while still exposing fundamentals to correct: project-row management treatment, accessory alignment, current-state language, modal/group rhythm, reliable deployed-build identification, real-screen regressions caused by over-broad shared selectors, header/navigation consistency, and the limits of a homemade per-glyph CSS icon system.

The first canonical-icon reset reached deployed build `0cc4cba`, but physical review of that exact revision found that mathematical shared-center alignment still did not read as optically aligned. The main cause was unequal visible mass: 28px state circles beside 18–20px commodity glyphs. Build `02e1e10` improved commodity-glyph balance and added the six-glyph comparison palette, but physical review then isolated the remaining problem more clearly: the circular Complete / Current / Incomplete state vocabulary still read like a radio-control system, and the inherited Current-row background tint looked like a selected button.

Deployed build `c02ac89` retired that circular treatment: Complete = canonical check only; Current = stronger short status bar; Incomplete/upcoming = quieter short status bar; Current row = no persistent background tint. Physical review of that exact build was a clear improvement and kept the direction, but exposed one final refinement layer: the three state marks still felt independently drawn rather than generated from one optical system, and trailing `8 bars` metadata competed visually with the reorder affordance.

Deployed build `66c43bf` kept the accepted non-circular state language, normalized Complete / Current / Incomplete onto one 18px optical frame, and moved arrangement metadata such as `8 bars` beneath the section name so Reorder alone owns the far-right affordance. Physical iPhone review found this substantially better. That same review then clarified the remaining alignment issue: the horizontal lanes and hit-target centers are already correct, while the visible glyph/state artwork reads slightly high inside those centered boxes.

An interrupted follow-up that tried to rewrite the horizontal accessory lane was rejected and closed without merge. The active candidate deliberately preserves the `66c43bf` horizontal layout and instead gives visible symbol artwork one shared 1px downward optical baseline. Add, More, Back/Forward, Check, Current/Incomplete state bars, Reorder, and the Shell Test glyph palette inherit that token while row columns, x-centers, text, hit targets, and header geometry remain unchanged.

**G7 is not approved/frozen. FIRE Core breadboarding has not started.**

The active phase is **G7 Shell Certification**. `G7_SHELL_CERTIFICATION.md` defines the finite ten-category completion contract, `Unresolved → Candidate → Locked` states, the developer-only Shell Test, and the final freeze gate. `G7_SHELL_CERTIFICATION_STATUS.md` records mutable review evidence.

No category is automatically Locked. Existing G7 work remains evidence and can become Locked only through the certification criteria and physical-device validation.

## Reliability baseline

Shell work must leave implementation, active authority, regression expectations, handoff state, and deployed assets describing the same candidate.

- Do not merge a shell change with known red regressions.
- If a deliberate product/shell decision makes an old regression obsolete, update that regression in the same change rather than restoring superseded behavior just to get green.
- **Shell Test passing is not sufficient for a shared-primitive merge.** Shared primitives used by real G7 must also pass browser coverage in the actual G7 fixture path at 390/440/820 widths. The current minimum real-screen path is Project → Setup → Structure temporary UI.
- Real-screen regression coverage must guard current-state geometry, form-control containment, header action alignment, navigation glyph construction, and sheet chrome so a certification specimen cannot be green while the project fixture is visibly broken.
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

Shell Test includes a compact comparison-only glyph palette containing Back, Forward, Add, Check, Reorder, and More. Those temporary boxes exist only to make the icon family easy to compare during certification; they are not a proposal to put every production glyph in a visible button.

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
- trailing header actions align to the visual center of the large title line rather than floating in a separate vertical rhythm
- toolbar add/management actions keep ~44px interaction targets but are glyph-first at rest rather than permanently boxed surfaces
- project-row management has no decorative divider from the row
- standard interface glyphs use one canonical Lucide 24×24 construction source instead of being redrawn independently in CSS
- Back and forward/navigation use the same canonical chevron family, with direction as the only semantic difference; tiny optical offsets are allowed when needed so mirrored geometry reads centered on-device
- recurring state/accessory meanings share one physical trailing-lane center while different meanings are not forced into the same visible container or equal visible mass
- visual artwork may use a small shared optical correction inside an otherwise-centered interaction box; that correction must not move hit targets, row geometry, text, or the established horizontal accessory lane
- progress-state language remains under physical review; the active candidate is deliberately non-circular and optically normalized: Complete = canonical check only; Current = stronger 18px status bar; Incomplete/upcoming = quieter 18px status bar
- Current state must not create a persistent selected-row background; state and row selection are different semantics
- arrangement supporting metadata belongs to the content hierarchy; the far-right accessory lane is reserved for the row's affordance
- state marks and commodity glyphs may differ deliberately in visible mass while sharing the same interaction lane
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

- project-row `•••` divider remains removed and management stays in the shared accessory lane
- the prior homemade per-glyph CSS system has been retired for commodity interface symbols after physical review showed mismatched visual centers, joins, proportions, and stroke personalities
- check, chevron, plus, ellipsis, and reorder use canonical Lucide SVG-mask geometry from one 24×24 source system in `shell-primitives.css`
- trailing row accessories keep one actual x-center across state / Navigate / Reorder / More without forcing different meanings into identical visible containers
- the physical review after `66c43bf` specifically rejected further horizontal-lane movement; the active alignment candidate preserves those x-centers and moves only visible artwork down through the shared `--symbol-optical-y` token
- forward/back chevrons retain tiny direction-specific x offsets while sharing the same 1px downward optical baseline as the rest of the symbol family
- Shell Test exposes Back / Forward / Add / Check / Reorder / More in one temporary comparison row so remaining family-level inconsistencies are easy to spot
- toolbar `+` / `•••` keep 44px hit targets but no longer render permanent dark rounded-square backgrounds at rest; active/focus behavior can reveal the control target
- trailing header action containers remain aligned to the large-title centerline; only their visible glyph artwork receives the optical-y correction
- Back and forward navigation use the same canonical chevron family
- Shell Test Back uses the same canonical back primitive as the real project rather than a separate text-arrow treatment
- the circular Complete / Current / Incomplete candidate is retired; the active state candidate uses check / strong bar / quiet bar with one shared 18px optical width and explicitly removes the inherited Current-row tint
- Current and Incomplete share the same cap geometry, with state hierarchy expressed through stroke weight and contrast rather than independent dimensions
- Complete / Current / Incomplete visible artwork participates in the same shared 1px downward optical baseline as commodity glyphs
- arrangement metadata such as `8 bars` is supporting text under the item name; reorder is the sole far-right affordance
- state overrides are loaded after the base and commodity primitive layers in both real G7 and Shell Test, using the same deployed build revision
- shared accessory layout does not override `.form-row`; Setup value controls retain their own label/control grid and stay contained at compact widths
- shared sheet styling does not add an action-divider hairline or inset top hairline that was not part of the approved shell language
- modal content-group and action rhythm use named shared tokens rather than test-only magic numbers
- Shell Test subtitle is the live G7 deployed-version indicator
- browser coverage keeps the established accessory x-center contract while checking the optical-y baseline, current-state geometry, transparent Current-row background, the glyph comparison palette, and the actual G7 Project → Setup → Structure path at 390/440/820 widths
- Setup / Structure / Tracks remain disposable fixture semantics; `Accurate` wording and the Tracks layout are not FIRE Core doctrine

Next product-facing work is physical confirmation of the exact deployed vertical-optical-alignment candidate: inspect the plus, ellipsis, Back/Forward, state marks, reorder glyph, and Shell Test palette as one family and confirm that the 1px downward artwork baseline resolves the “slightly pushed up” feeling without disturbing the accepted horizontal layout. Do not infer additional FIRE Core architecture from the fixture content.

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
