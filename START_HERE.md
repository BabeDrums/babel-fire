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

PR **#66 — Return coordinated shell iteration to G7** established that coordinated FIRE shell implementation/certification belongs in the real isolated G7 context rather than a parallel Lab shell.

PR **#67 — Refine G7 shell cohesion after physical review** remains the important historical baseline for the current certification sequence; later certification passes supersede its visual details where explicitly documented.

**G7 is not approved/frozen. FIRE Core breadboarding has not started.** All ten certification categories remain Candidate; **0 / 10 are Locked**.

Coordinated FIRE shell implementation/certification belongs in the real isolated G7 context. Babel Lab remains optional bounded evidence only and must not become a parallel FIRE shell.

## Current symbol/alignment finding

The deployed real-G7 candidate still contains PR #83's shared `--symbol-optical-y: 1px` correction. That candidate preserved the accepted horizontal row/accessory lanes, text anchors, hit targets, and header geometry while moving visible symbol/state artwork down 1px.

Physical iPhone review of `G7 · d00d146` did not approve that global 1px candidate, so PR #85 introduced a Shell Test-only inline-SVG normalization experiment. Plus / Check / Reorder / More now read correctly enough in the bounded experiment and should remain undisturbed.

PR #86 deployed `G7 · 4e84bd5` with Liquid Glass removed, a standard FIRE comparison card, Current vs Circle only, and a mirrored **inward** chevron correction. Physical iPad review rejected that chevron direction: Back / Forward now read too far inward. The helper paragraphs beneath the symbol comparison and Rows · accessories also add unnecessary developer narration and should be removed from the visual review surface.

The research/implementation conclusion is that **bounding-box centering and optical centering are different problems**. Runtime `getBBox()` can mechanically center geometry, but a directional asymmetric glyph can still read off. The next Shell Test candidate therefore treats alignment as an intrinsic symbol metric instead of another container-specific pixel nudge:

- Plus / Check / Reorder / More keep their accepted geometry-bounds centering.
- Back / Forward use the centroid of the triangular convex hull formed by their three chevron vertices as the optical anchor.
- For the current 24×24 source geometry, Back's hull center is `x=13` and Forward's is `x=11`; centering those anchors at `x=12` deterministically yields `-1` for Back and `+1` for Forward — equal-and-opposite **outward** movement derived from the glyph geometry rather than a hand-entered correction.
- The optical rule remains Shell Test-only. Real G7 production controls are unchanged until physical approval.

**Liquid Glass remains rejected.** Plain Circle remains the current physical preference, but it is not yet promoted into real G7.

### Active Shell Test experiment

Shell Test contains a bounded two-row symbol/container comparison that does **not** alter real G7 production controls:

- the same six commodity symbols render as inline 24×24 SVG artwork
- Plus / Check / Reorder / More use geometry-bounds centering
- Back / Forward derive their optical anchor from their own triangular convex-hull centroid, producing mirrored outward seating without a magic offset constant
- the comparison card uses the standard FIRE grouped surface tokens; it is not a special ambient/glass field
- the same symbol implementation is shown in two rows:
  1. **Current** — existing rounded-square Shell Test container treatment
  2. **Circle** — the same simple material in a circular container
- no Liquid Glass treatment remains in the experiment
- the two now-redundant explanatory helper paragraphs beneath the symbol comparison and Rows · accessories are removed

The comparison intentionally changes only container shape. Symbol source geometry, alignment model, target size, simple material, and 44px interaction boxes stay consistent across the two rows.

## Immediate next gate

Deploy the refined Shell Test and physically review it on iPhone first, then iPad/regular width.

Judge two questions separately:

1. **Chevron seating:** does the intrinsic convex-hull optical anchor make Back / Forward feel naturally centered relative to each other and to Plus / Check / Reorder / More without requiring another arbitrary nudge?
2. **Container direction:** with symbol geometry/alignment held constant, does plain Circle still clearly beat Current rounded-square?

Do **not** promote Circle or the chevron optical-anchor model into real G7 until Babel physically approves the refined comparison. Do not reopen accepted horizontal accessory lanes unless new physical evidence specifically proves they are wrong.

After a direction is approved, implement the smallest shared real-G7 primitive change, reconcile tests/authority/handoff, run all gates, merge/deploy, then repeat physical iPhone/iPad validation before locking any category.

## Reliability baseline

Shell work must leave implementation, active authority, regression expectations, handoff state, and deployed assets describing the same candidate.

- Do not merge a shell change with known red regressions.
- If a deliberate decision supersedes an old regression, update that regression in the same change rather than restoring obsolete behavior.
- **Shell Test passing is not sufficient** for any shared primitive used by real G7. Real-G7 browser coverage must still pass at 390 / 440 / 820 widths.
- Shell Test-only experiments may remain isolated from production primitives until a direction is physically chosen.
- G7 and Shell Test assets use the exact GitHub Pages build revision for cache busting.
- Physical review targets the exact deployed revision shown by the G7/Shell Test build indicator.
- The authority/handoff gate must pass before merge.
- Production V6 runtime/data/schema remain untouched throughout shell certification.

## Current strategy — certify grammar, not fixture workflow

Current `Setup → Structure → Tracks` content is disposable shell/workspace fixture content. It exists to exercise transferable primitives; it is **not** frozen FIRE Core architecture, not a promise of exactly three checkpoints, and not a final Tracks/Map design.

The developer-only Shell Test lives **inside G7** and is a certification showroom/torture chamber, not a second FIRE implementation and not Babel Lab.

Routing is explicit:

- **G7** owns coordinated FIRE shell implementation, Shell Test, in-context validation, and certification.
- **Babel Lab** is optional bounded evidence only. **Lab is evidence, never authority.**
- **Babel Truth** owns only genuinely transferable cross-app principles after deliberate promotion and owning-product validation.
- **FIRE Core** remains blocked until explicit G7 shell freeze.

Default process:

**Observe → Diagnose → Shape → Contract → Build → Verify → Consolidate.**

For active FIRE shell work:

**physical finding → shared/system diagnosis → bounded Shell Test evidence when useful → branch → implementation/tests/docs → 390/440/820 gates → merge/deploy → exact-build physical iPhone/iPad review.**

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
- Complete = canonical check; Current = stronger short bar; Incomplete/upcoming = quieter short bar
- Current does not tint the whole row
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
