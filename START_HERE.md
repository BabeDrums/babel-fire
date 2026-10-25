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

PR **#66 — Return coordinated shell iteration to G7** established the current ownership boundary: coordinated FIRE shell implementation/certification belongs in the real isolated G7 context rather than a parallel Lab shell.

PR **#67 — Refine G7 shell cohesion after physical review** is the historical baseline that the finite certification sequence superseded; later certification passes may replace its visual details, but its role in the handoff chain remains explicit.

Coordinated FIRE shell implementation/certification belongs in the real isolated G7 context. Babel Lab remains optional bounded evidence only and must not become a parallel FIRE shell.

**G7 is not approved/frozen. FIRE Core breadboarding has not started. All ten certification categories remain Candidate; 0 / 10 are Locked.**

## Current physically validated symbol direction

The production-wide `--symbol-optical-y` nudge is retired.

The current symbol rule is:

**geometry baseline → optional intrinsic symbol optical metric → container placement**

- Plus / More / Reorder use normal centered placement.
- Check owns its small intrinsic vertical correction.
- Back / Forward own mirrored outward side bearings.
- Current / Incomplete are symmetric status bars.
- Liquid Glass is rejected.
- Symbol alignment belongs to the symbol primitive, never page-specific CSS.

PR #87 proved the refined symbol family in Shell Test. PR #88 promoted that architecture into real G7 at `109590e66038845849c832d3f4e3ea93ba5193c1`.

## Current physical finding — frame repair required after PR #88

Real-device iPhone review of `G7 · 109590e` showed that the remaining defects are **not primarily symbol-offset defects**. The shared shell frame is contradicting the symbol work.

Durable findings:

1. **Header frame:** Back remained in the toolbar row while trailing Add/More was translated down into the large-title line. This produced visibly split controls. The fix must be structural: one navigation/action row, then the large title/meta row beneath it. No independent side-specific toolbar translation.
2. **Control frame:** keep the 44px interaction target, but do not make the full hit region visually heavy. Interaction geometry and visible material geometry are separate concerns.
3. **State rendering:** `state-primitives.css` must remain the only visible state owner. Legacy text glyphs may exist as fixture residue only if they cannot render; they must never leak beneath Current/Incomplete/Complete artwork.
4. **Editable-value frame:** Tempo and Meter must share one stable trailing lane rather than size themselves from content.
5. **Modal frame:** compact sheets must not depend on bottom-edge anchoring under dynamic mobile browser chrome. The active candidate centers a bounded sheet using small-viewport-safe geometry and keeps task identity visible.
6. **Edit-sheet action hierarchy:** Save / Duplicate / Delete must not collapse into three equivalent oversized slabs on narrow phones. The primary task remains visually primary; management actions remain secondary.

These findings are captured in Babel Truth Issue #1 under the persist-before-reply rule.

## Active implementation candidate

Branch: `g7-shell-frame-repair`

The active pass introduces `v7-preview/frame-primitives.css` as the shared owner for structural frame relationships while preserving existing ownership boundaries:

- `shell-primitives.css` — symbol/accessory artwork and shared symbol metrics
- `state-primitives.css` — progress/completion state artwork
- `frame-primitives.css` — header frame, toolbar hit-vs-material geometry, editable-value lane, compact modal frame

Current candidate rules:

- one 44px toolbar interaction row for Back + trailing contextual action
- large title/meta in a separate row beneath toolbar actions
- 44px tap target with a quieter 36px visible circular material
- no horizontal accessory-lane rewrite
- one fixed Tempo/Meter value lane
- state glyph leakage explicitly suppressed at the shared frame level
- compact sheets centered and bounded with `svh` rather than pinned to Safari's dynamic bottom edge
- sheet task title sourced from the existing dialog label
- three-action edit sheets avoid narrow-phone three-slab stacking

This is a shared-primitive pass, not a page-specific visual patch.

## Immediate next gate

Run the full reliability gate on the frame candidate:

**Authority/Handoff + Static + Chromium 390 / 440 / 820**, including the actual G7 Project → Setup → Structure path and Shell Test.

If green:

1. re-check current `main` and open PRs
2. merge automatically
3. verify the exact merge commit deploys to GitHub Pages
4. verify post-merge 390 / 440 / 820
5. physically review the exact deployed build on iPhone first, then iPad/regular width

Do **not** lock any certification category from browser evidence alone. FIRE Core remains blocked.

## Reliability baseline

- Do not merge a shell change with known red regressions.
- If a deliberate decision supersedes an old regression expectation, update that regression in the same change rather than restoring obsolete behavior.
- **Shell Test passing is not sufficient** for any shared primitive used by real G7.
- G7 and Shell Test assets use the exact GitHub Pages build revision for cache busting.
- Physical review targets the exact deployed revision shown by the G7/Shell Test build indicator.
- The authority/handoff gate must pass before merge.
- Production V6 runtime/data/schema remain untouched throughout shell certification.

## Current strategy — certify grammar, not fixture workflow

Current `Setup → Structure → Tracks` content is disposable shell/workspace fixture content. It exists to exercise transferable primitives; it is **not** frozen FIRE Core architecture, not a promise of exactly three checkpoints, and not a final Tracks/Map design.

The developer-only Shell Test lives **inside G7** and is a certification showroom/torture chamber, not a second FIRE implementation and not Babel Lab.

Routing:

- **G7** owns coordinated FIRE shell implementation, Shell Test, in-context validation, and certification.
- **Babel Lab** is optional bounded evidence only. **Lab is evidence, never authority.**
- **Babel Truth** owns only genuinely transferable cross-app principles after deliberate promotion and owning-product validation.
- **FIRE Core** remains blocked until explicit G7 shell freeze.

Default process:

**Observe → Diagnose → Shape → Contract → Build → Verify → Consolidate.**

## Stable semantic evidence

Preserve unless certification proves a better transferable primitive:

- Projects → project Home → temporary shell-fixture workspaces
- public project types Original / Cover
- history-aware Back retraces actual in-app path; direct work entry has safe fallback
- `+` = add/create the primary discrete object for the current view
- `•••` = management/actions
- project-row management has no decorative divider
- ~44px interaction targets remain even when resting toolbar actions are visually compact
- standalone glyph-button containers may be circular; semantic row/accessory marks remain unboxed unless their role independently earns a control surface
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
