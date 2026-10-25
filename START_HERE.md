# Babel FIRE — Start Here

Use **Babel** as the project-facing name.

## Read order

1. `BABEL_TRUTH.md` — immutable pointer to the cross-app Babel Truth commit this repo has reconciled against
2. Babel Truth `START_HERE.md` / `AGENTS.md` / relevant shared authority at that pinned commit
3. this file — current FIRE build/review/next-step state
4. `FIRE_CORE.md`
5. `V6.md` for live production behavior
6. `V7_DRAFT.md` for G7 successor shell grammar
7. `G7_SHELL_CERTIFICATION.md` for the active shell-completion contract and freeze gate
8. `G7_SHELL_CERTIFICATION_STATUS.md` for mutable category/evidence status
9. Babel Truth Issue #1 body **plus newer comments** for unresolved FIRE items
10. code/tests as implementation evidence

## Current state — G7 Shell Certification active

Production remains **V6**. G7 is the isolated successor preview at `/v7-preview/` using `production-projects-v1-v7-preview`; it must never mutate V6 `production-projects-v1` data.

PR **#66 — Return coordinated shell iteration to G7** established that complete coordinated FIRE shell work belongs in the real isolated G7 context; the former full-shell Lab replica is rejected evidence.

PR **#67 — Refine G7 shell cohesion after physical review** is an important historical baseline for the current certification sequence. Later certification passes supersede its visual details where explicitly documented.

**G7 is not approved/frozen. FIRE Core breadboarding has not started.** All ten certification categories remain Candidate; **0 / 10 are Locked**.

## Current visual candidate

The active candidate is the result of the Shell Test / real-G7 accessory refinement sequence culminating in PR #83's vertical optical-baseline change. A later maintenance-only commit may have a newer build SHA without changing this visible candidate; the live `G7 · <short SHA>` indicator identifies the exact deployment under review.

Current accepted structure:

- horizontal row/accessory lanes, text anchors, hit-target boxes, and header geometry are preserved
- visible symbol/state artwork uses one shared **1px downward optical baseline** (`--symbol-optical-y`) because physical iPhone review found the artwork reading slightly high, not too far left/right
- commodity interface glyphs use one canonical Lucide 24×24 source family for Check, Chevron, Plus, Ellipsis, and Reorder rather than independent hand-drawn CSS shapes
- Back and Forward use the same chevron family; direction is the semantic difference
- progress state is deliberately non-circular: **Complete = canonical check; Current = stronger 18px bar; Incomplete/upcoming = quieter 18px bar**
- Current does not tint the whole row; selection and progression are separate semantics
- arrangement metadata such as `8 bars` sits beneath the section name as supporting text; Reorder alone owns the far-right affordance
- Shell Test contains a comparison-only glyph palette so Back / Forward / Add / Check / Reorder / More can be judged side-by-side
- `state-primitives.css` is the sole owner of progress-state visual language; shared shell primitives own lane/grid/glyph infrastructure

The last user physical feedback before the current vertical-baseline candidate was: **the overall shell looks very nice, but the visible glyph/state artwork feels slightly pushed up.** The required correction is vertical/down, not a horizontal lane shift. Do not reopen the accepted x-centers unless new physical evidence proves they are wrong.

## Immediate next gate

Open the exact deployed G7 and Shell Test, verify the build indicator, and physically review the current candidate on iPhone first, then iPad/regular width.

Judge the symbol family together: Plus, Ellipsis, Back/Forward, Complete/Current/Incomplete, Reorder, and the Shell Test palette. Confirm whether the shared 1px downward artwork baseline resolves the slightly-high feeling without disturbing the accepted horizontal layout.

If a systemic defect remains, fix the **shared primitive**, add/update regression coverage, run all gates, auto-merge when green, verify the exact Pages deployment, then repeat physical review. Do not jump to FIRE Core and do not lock a category from screenshots alone.

## Reliability baseline

Shell work must leave implementation, active authority, regression expectations, handoff state, and deployed assets describing the same candidate.

- Do not merge a shell change with known red regressions.
- If a deliberate decision supersedes an old regression, update that regression in the same change rather than restoring obsolete behavior.
- **Shell Test passing is not sufficient.** Shared primitives used by real G7 must also pass actual-G7 browser coverage at 390 / 440 / 820 widths; the minimum real-screen path includes Project → Setup → Structure temporary UI.
- G7 and Shell Test assets use the exact GitHub Pages build revision for cache busting, including `model.js`.
- Shell Test and real G7 display the deployed short commit from `build-info.json`; physical review targets that exact revision.
- The authority/handoff gate must pass before merge.
- Production V6 runtime/data/schema remain untouched throughout shell certification.

## Current strategy — certify grammar, not fixture workflow

Current `Setup → Structure → Tracks` content is disposable shell/workspace fixture content. It exists to exercise transferable primitives; it is **not** frozen FIRE Core architecture, not a promise of exactly three checkpoints, and not a final Tracks/Map design.

The developer-only Shell Test lives **inside G7** and renders the same primitives/tokens/styles used by real G7. It is a certification showroom/torture chamber, not a second FIRE implementation and not Babel Lab.

Routing is explicit:

- **G7** owns coordinated FIRE shell implementation, Shell Test, in-context validation, and certification.
- **Babel Lab** is optional bounded evidence only. **Lab is evidence, never authority.** Do not rebuild a parallel full FIRE shell there.
- **Babel Truth** owns only genuinely transferable cross-app principles after deliberate promotion and owning-product validation.
- **FIRE Core** remains blocked until explicit G7 shell freeze.

Default process:

**diagnose → shape shared primitive → implement on branch → exercise Shell Test + real G7 → run authority/static/390/440/820 gates → auto-merge if green → verify exact Pages commit → physical iPhone/iPad review → update certification evidence → repeat.**

## Stable semantic evidence

Preserve unless certification proves a better transferable primitive:

- Projects → project Home → temporary shell-fixture workspaces
- public project types Original / Cover
- history-aware Back retraces actual in-app path; direct work entry has safe fallback
- `+` = add/create the primary discrete object for the current view
- `•••` = management/actions
- project-row management has no decorative divider
- ~44px interaction targets remain even when resting toolbar actions are visually glyph-first
- arrangement supporting metadata belongs to content hierarchy; the far-right lane belongs to the affordance
- iPhone/iPad share one product logic even when presentation adapts

Interaction semantics:

- **Inline = choose/toggle/classify/confirm/evaluate** something already in the current task
- **Sheet = create/edit/manage a discrete thing** while staying in context
- Navigation enters another meaningful workspace
- Menu/secondary affordance holds utilities that should not compete with musical work

## Certification and approval gate

`G7_SHELL_CERTIFICATION.md` is the contract. `G7_SHELL_CERTIFICATION_STATUS.md` is the mutable evidence/status board.

A category becomes Locked only after its primitive family is coherent, has representative Shell Test coverage where applicable, is exercised in real G7, and passes relevant physical iPhone/iPad validation.

Final freeze requires:

**10/10 categories Locked → final real G7 physical-device sweep → no unresolved systemic contradiction → explicit Babel approval → G7 Shell Frozen.**

After freeze:

**G7 Shell Frozen → promote genuinely transferable validated principles into Babel Truth → FIRE Core breadboard → thin FIRE Core spine → real-project validation.**

## Continuity

`CONTINUITY_INBOX.md` is retired as an active local buffer.

All new unresolved durable Babel/FIRE deltas use Babel Truth Issue #1 under the persist-before-reply threshold. Routine capture is append-only through new comments; do not replace the Issue #1 body during ordinary work.

Git history preserves superseded implementation/history. Active docs should describe one current truth rather than every prior pass.
