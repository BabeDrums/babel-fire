# Babel FIRE — Repository Instructions

Use **Babel** as the project-facing name.

Shared Babel process, feedback interpretation, research expectations, foundations, contradiction handling, continuity, Lab-incubation ownership, and shared-surface concurrency live in the pinned Babel Truth authority. Read `BABEL_TRUTH.md` first; do not duplicate those rules here unless FIRE needs a real local exception.

## Zero-context FIRE entry

After `BABEL_TRUTH.md` and the pinned Truth authority:
1. `START_HERE.md` — current verified FIRE state and next gate
2. `FIRE_CORE.md` — canonical cross-generation FIRE product doctrine
3. `V6.md` — current production-generation behavior
4. `V7_DRAFT.md` — frozen G7 shell behavior/primitive grammar
5. `G7_SHELL_CERTIFICATION.md` — completed shell certification/freeze contract
6. `G7_SHELL_CERTIFICATION_STATUS.md` — completed category evidence/status
7. relevant Babel Truth Issue #1 items
8. code/tests as implementation evidence

Do not reconstruct current state from old PRs or Git history unless investigating history.

## FIRE authority

For FIRE-local behavior:
1. `FIRE_CORE.md`
2. `V6.md` for shipped production behavior
3. `V7_DRAFT.md` for frozen successor shell behavior
4. `G7_SHELL_CERTIFICATION.md` for certification definitions/freeze criteria
5. `G7_SHELL_CERTIFICATION_STATUS.md` for completed category state/evidence
6. `START_HERE.md` for exact current build/review/next step
7. code/tests as implementation evidence

Current authority should contain one present truth. Git/PR history is the archive.

## Build/review workflow

For durable FIRE work in the owning product:

**re-read current main/open PRs → branch → diagnose/shape → implement → test → reconcile authority/handoff → PR → required checks → merge → Pages deploy → verify exact merge → physical-device review when relevant**

- Never implement directly on `main`.
- Preserve unfinished work; never reset/discard it merely to get a clean tree.
- Babel has standing permission to merge when the diff is reviewed, required gates are green, production-data safety is clear, and no genuine product decision remains unresolved.
- Stop instead of merging when tests fail, data safety is uncertain, behavior is destructive/risky, or a real product decision remains unresolved.
- Automated browser checks do not replace physical iOS Safari review for visual/interaction work.

## Frozen shell boundary

- V6 remains production until deliberate promotion.
- G7 remains the isolated successor at `/v7-preview/`.
- The approved frozen shell runtime anchor is `4a258c5170dd1d96dcbc0f2b0a9c35b283cec489`; all 10 certification categories are Locked.
- Current `Setup → Structure → Tracks` content is disposable shell-fixture content, not FIRE Core architecture.
- Shell Test is developer infrastructure inside G7, not a second FIRE implementation and not Babel Lab.
- **FIRE Core work is unblocked.** Product work should now start from `FIRE_CORE.md`, not by continuing generic shell polish.
- Do not casually reopen frozen categories because Core content differs from the fixtures. Extend the smallest necessary primitive when Core proves a genuinely new need; reopen a locked category only when evidence shows the foundation itself is wrong.

## FIRE Core incubation boundary

Babel Truth ADR 0006 allows a bounded **unproven FIRE Core interaction** to incubate in Babel Lab while FIRE remains the sole product owner.

Current FIRE-specific rules:
- doctrine, canonical behavior, production/runtime data, specs, migrations, and promoted implementation stay in `babel-fire`
- a disposable interaction audition may live under `babel-lab/fire/core/**` using fake/local isolated state
- Lab prototype code is evidence, not production code; promote the behavior deliberately back into FIRE only after it survives real use
- the Lab Core lane must never read/write V6 or G7 FIRE storage merely to feel realistic
- the existing Lab Fire visualization experiment is separate and must not be silently redefined as Core
- the historical G7 Shell Test remains frozen FIRE certification evidence; Lab Shell Gallery is a different shared-UI proving environment
- Draft FIRE PR #99 is seed/history unless `START_HERE.md` records a newer disposition; do not merge it merely because its code exists

When working in Lab for a FIRE audition, respect Lab path ownership and Babel Truth shared-surface concurrency rails. A FIRE pass may own `fire/core/**`; it must reconcile before changing Lab root/shared/shell/Truth-pointer/cross-cutting CI surfaces and must not rewrite WORLD product logic.

## Engineering/data safety

- V6 localStorage: `production-projects-v1`
- G7 preview localStorage: `production-projects-v1-v7-preview`
- G7 must never mutate V6 production data.
- Schema changes require tested forward migration; never wipe projects.
- Preserve stable IDs and V6 downstream dependencies/browser-history behavior during V6 maintenance.
- Keep GitHub Pages simple static HTML/CSS/JS unless a real approved need justifies architecture change.
- Preserve ~44px touch targets, keyboard/focus accessibility, reduced-motion alternatives, and discoverable interactions.
- One product logic/hierarchy/actions/states across iPhone/iPad; presentation may adapt.
- Do not add overlay-polish files or MutationObserver visual rewrites; fix the owning primitive/component.
- Permanent regressions belong in `tests/`; do not commit debug/browser artifacts.

## Tooling

**No Codex for FIRE.** Use the normal ChatGPT GitHub connector/direct repository workflow unless Babel explicitly changes this rule.

## Documentation ownership

- `BABEL_TRUTH.md` — immutable shared-Truth adoption pointer
- `START_HERE.md` — current verified FIRE state / immediate next gate
- `FIRE_CORE.md` — canonical FIRE doctrine
- `V6.md` — shipped production-generation spec
- `V7_DRAFT.md` — frozen G7 shell spec and local primitive grammar
- `G7_SHELL_CERTIFICATION.md` — completed shell-certification contract
- `G7_SHELL_CERTIFICATION_STATUS.md` — completed certification evidence/status

That is the active FIRE documentation set. Do not recreate separate ecosystem ledgers, continuity inboxes, changelog-as-authority, research registries, or supporting-context catchalls. Use Babel Truth/Issue #1, the owning spec, and Git history instead.

## Definition of done

A FIRE change is not done until:
- behavior matches active authority
- user data is preserved/migrated safely
- relevant regressions pass
- startup/JS has no known app errors
- representative compact/wide behavior is checked
- dead/replaced code and active documentation are removed
- `START_HERE.md` accurately states the current next gate
- durable unresolved findings are captured in Truth Issue #1 when appropriate
- merged/deployed state is verified when the workflow calls for it

For visual work, physical Safari review is a distinct gate. The G7 shell has completed its certification/freeze gate; future shell-affecting changes must respect the frozen-state rule above.
