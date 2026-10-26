# Babel FIRE — Repository Instructions

Use **Babel** as the project-facing name.

Shared process, feedback interpretation, continuity, closeout, and cross-app architecture come from the Truth commit pinned in `BABEL_TRUTH.md`. Keep this file FIRE-local.

## Entry

1. `BABEL_TRUTH.md`
2. pinned Truth `START_HERE.md` / `AGENTS.md`
3. local `START_HERE.md`
4. `FIRE_CORE.md`
5. generation/frozen-shell authority only when the task needs it
6. current Issue #1 state when unresolved context matters
7. code/tests as implementation evidence

Do not reconstruct current state from old PRs/Git history unless investigating history.

## FIRE authority

For FIRE-local behavior:
1. `FIRE_CORE.md` — canonical cross-generation product doctrine
2. `V6.md` — shipped production-generation behavior
3. `V7_DRAFT.md` — frozen G7 shell behavior/primitive grammar
4. `G7_SHELL_CERTIFICATION.md` / `G7_SHELL_CERTIFICATION_STATUS.md` — completed shell certification evidence
5. `START_HERE.md` — exact current gate
6. code/tests — implementation evidence

Current authority contains one present truth. History stays in Git/PRs.

## Durable workflow

**refresh main/open PRs → branch → diagnose/shape → implement → test → reconcile authority/handoff → PR → recheck overlap/gates → merge → verify exact merge/deploy → physical review when relevant**

- never implement directly on `main`
- preserve unfinished work; never discard it just to clean the tree
- automated browser checks do not replace physical iOS Safari review for visual/interaction work
- merge only when behavior/ownership/data safety are clear and required gates pass

## Frozen shell boundary

- V6 remains production until deliberate promotion.
- G7 remains isolated at `/v7-preview/`.
- G7 is **10 / 10 Locked and Frozen** at runtime anchor `4a258c5170dd1d96dcbc0f2b0a9c35b283cec489`.
- `Setup → Structure → Tracks` is disposable fixture content, not FIRE Core architecture.
- the historical Shell Test stays FIRE certification evidence; Lab Shell Gallery is separate
- do not casually reopen frozen shell categories for Core content. Extend the smallest needed primitive only when evidence proves a genuinely new need; reopen a category only when the foundation itself is wrong.

## FIRE Core incubation boundary

ADR 0006 allows a bounded **unproven** FIRE Core interaction under `babel-lab/fire/core/**` while FIRE remains sole product owner.

- doctrine, canonical behavior, production/runtime data, specs, migrations, and promoted implementation stay in `babel-fire`
- Lab audition uses fake/local isolated state and never touches V6/G7 storage
- Fire Visualization and FIRE Core are separate experiments
- Lab prototype code is evidence; surviving behavior is deliberately implemented/reconciled back into FIRE
- closed PR #99 is seed/history for the first audition, not a merge path

Respect Lab's path ownership/concurrency rules before touching shared Lab surfaces. Do not rewrite WORLD logic from the FIRE lane.

## Engineering / data safety

- V6 localStorage: `production-projects-v1`
- G7 preview localStorage: `production-projects-v1-v7-preview`
- G7 must never mutate V6 production data
- schema changes require tested forward migration; never wipe projects
- preserve stable IDs and existing downstream/browser-history dependencies during V6 maintenance
- keep GitHub Pages simple static HTML/CSS/JS unless a real need earns architecture change
- preserve touch/focus/keyboard/reduced-motion accessibility and one product logic across iPhone/iPad
- fix the owning primitive/component rather than stacking overlay polish or MutationObserver rewrites
- permanent regressions belong in tests; debug/browser artifacts do not

## Tooling

**No Codex for FIRE.** Use the normal ChatGPT GitHub connector/direct repository workflow unless Babel explicitly changes this rule.

## Active documentation set

- `BABEL_TRUTH.md`
- `AGENTS.md`
- `START_HERE.md`
- `FIRE_CORE.md`
- `V6.md`
- `V7_DRAFT.md`
- `G7_SHELL_CERTIFICATION.md`
- `G7_SHELL_CERTIFICATION_STATUS.md`

Do not recreate ecosystem ledgers, continuity inboxes, changelog-as-authority, or catchall context docs. Use Truth/Issue #1, the owning spec, and Git history.

## Done

A FIRE change is done when:
- behavior matches active authority
- user data is preserved/migrated safely
- relevant regressions pass
- representative compact/wide behavior is checked
- physical Safari review is completed when applicable
- dead/replaced code and active documentation are removed
- `START_HERE.md` states the current next gate
- durable unresolved findings are captured in Truth Issue #1
- merged/deployed state is verified when required
