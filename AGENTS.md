# Babel FIRE — Repository Instructions

Use **Babel** as the project-facing name.

## Shared Babel authority

Read `BABEL_TRUTH.md` before substantive work. It pins the immutable `BabeDrums/babel-truth` commit this repo last reconciled against and routes shared product/design/process rules.

Do not duplicate Babel-wide rules here unless FIRE needs an explicit local exception.

## FIRE zero-context entry

After Babel Truth:

1. `START_HERE.md` — current FIRE implementation/review/next step
2. `FIRE_CORE.md` — cross-generation FIRE product doctrine
3. `V6.md` — shipped production-generation behavior
4. `V7_DRAFT.md` — current G7 successor-shell behavior where compatible with FIRE Core
5. `G7_SHELL_CERTIFICATION.md` — active G7 shell-completion checklist, Shell Test contract, and freeze gate
6. relevant FIRE items in Babel Truth Issue #1 (`Babel Continuity Buffer`)
7. code/tests as implementation evidence

For wider ecosystem/sibling-app work instead, use `BABEL_START_HERE.md` → `BABEL_APPS.md` → `BABEL_PLATFORM.md` after Babel Truth.

## FIRE authority and conflict policy

For FIRE-specific product behavior, use:

1. `FIRE_CORE.md`
2. current production spec (`V6.md`) for shipped behavior
3. `V7_DRAFT.md` for active successor behavior
4. `G7_SHELL_CERTIFICATION.md` for G7 shell completion/certification status and freeze criteria
5. `START_HERE.md` for current verified build/review state
6. `CONTEXT.md` for durable supporting history not superseded above
7. code/tests as implementation evidence

Babel Truth owns cross-app rules. FIRE authorities own FIRE-specific behavior. If a conflict is ambiguous, classify whether it is global or FIRE-local before editing either side.

`CONTINUITY_INBOX.md` is retired as an active buffer and remains only as a compatibility pointer. Do not add new continuity items there.

## Git / review workflow

Use Babel Truth `PROCESS.md` for the shared operating model.

FIRE implementation workflow remains:

**branch → implement → test → reconcile local authority/handoff → PR → required checks → merge → Pages deploy → verify → physical-device approval when relevant**

- Never do implementation work directly on `main`.
- Start from current `main` and check open PRs before writing.
- Preserve unfinished work; never reset/discard it merely to get a clean tree.
- Babel has standing permission to merge FIRE PRs when the diff is reviewed, required checks are green, production-data safety is clear, and no genuine product decision remains unresolved.
- Stop instead of merging when tests fail, data safety is uncertain, behavior is destructive/risky, or a real product decision remains unresolved.
- Automated browser checks do not replace physical iOS Safari review for visual/interaction work.

## Parallel-chat ownership

### FIRE build lane

Owns active FIRE runtime/spec implementation and may merge/deploy under the standing workflow.

### Ecosystem / Lab lane

May research and prototype independently but must not casually edit FIRE runtime/spec/data. Before any durable cross-repo write, re-read current `main`, open PRs, the repo's Truth pointer, and relevant local authority.

If two chats might edit the same durable file, the later writer reconciles the newer state first.

## FIRE-specific product boundaries

- FIRE is a production companion / decision engine, not a mandatory course.
- Original and Recreation/Cover remain first-class project paths.
- Project Home is a hub, not a dashboard.
- Delete before styling.
- Learning is contextual/optional unless a distinct product job later earns separation.
- Do not use theme/metaphor to obscure musician-facing meaning.
- G7 shell approval is a real gate; do not begin FIRE Core breadboarding until `START_HERE.md` records explicit physical approval and `G7_SHELL_CERTIFICATION.md` records the certification freeze gate as satisfied.
- Current Setup / Structure / Tracks are disposable shell fixtures. Do not confuse polishing them with approving FIRE Core architecture.
- A developer Shell Test inside G7 may exercise actual G7 primitives/states. It is developer infrastructure, not a second FIRE implementation, not Babel Lab, and not a FIRE Core destination.

## FIRE interaction grammar

- **Inline** — choose/toggle/classify/confirm/evaluate something already in the task.
- **Sheet** — create/edit/manage a discrete thing while staying in context.
- **Navigation** — enter another meaningful workspace.
- **Menu/secondary affordance** — utilities that should not compete with musical work.

Use semantic consistency; do not force every interaction into one container.

## Engineering / data safety

- Production V6 localStorage key: `production-projects-v1`.
- G7 preview localStorage key: `production-projects-v1-v7-preview`.
- G7 must never mutate V6 production data.
- Schema changes require tested forward migration; never wipe projects.
- Preserve stable project/section/track/range/event IDs where applicable.
- Preserve V6 downstream Skeleton Session → Draft → Bounce dependencies and browser-history behavior during V6 maintenance.
- Keep GitHub Pages simple static HTML/CSS/JS unless an approved need justifies architecture change.
- Roughly 44px touch targets, keyboard/focus accessibility, reduced-motion alternatives, and discoverable interactions are required.
- No essential action should depend on a skinny line or undiscoverable gesture.
- Modal sheets may temporarily lock background scrolling.
- One product logic/hierarchy/actions/states across iPhone/iPad; presentation may adapt.
- Do not imitate Liquid Glass decoratively.
- Do not add overlay-polish files or MutationObserver visual rewrites; change core components/styles.
- Permanent regression tests belong in `tests/`; do not commit debug/browser artifacts.

## FIRE tooling rule

**No Codex for FIRE.** Use the normal ChatGPT GitHub connector/direct repository workflow unless Babel explicitly changes this rule.

## Local documentation ownership

- `FIRE_CORE.md` — canonical FIRE doctrine
- `V6.md` — live production-generation behavior
- `V7_DRAFT.md` — active G7 behavior and primitive grammar
- `G7_SHELL_CERTIFICATION.md` — active shell-completion checklist, Shell Test contract, category status, and freeze gate
- `START_HERE.md` — current FIRE state / next gate
- `CONTEXT.md` — durable supporting history only
- `CHANGELOG.md` — meaningful FIRE milestones
- `BABEL_START_HERE.md` / `BABEL_APPS.md` / `BABEL_PLATFORM.md` — current ecosystem concept lane hosted here until/unless ownership intentionally moves
- `BABEL_TRUTH.md` — immutable pointer to current reconciled cross-app Truth
- `CONTINUITY_INBOX.md` — retired compatibility pointer; no new items

Git history is the archive. Remove superseded current wording instead of preserving contradictory live instructions.

## Continuity and handoff maintenance

Unresolved durable deltas now go to Babel Truth Issue #1 under the persist-before-reply threshold defined by Truth `PROCESS.md` / `AGENTS.md`.

For every substantive FIRE change:

1. update the correct FIRE authority
2. sweep active FIRE docs/implementation/tests for stale contradictions
3. refresh `START_HERE.md`
4. update Babel Truth only if the lesson is genuinely cross-app
5. reconcile/remove resolved items from Truth Issue #1
6. run handoff/doctrine guards

Do not copy temporary PR/SHA state into global Babel Truth.

## Definition of done

FIRE implementation is not complete until:

- behavior matches active FIRE authority
- user data is preserved/migrated safely
- relevant regressions pass
- startup/JS is clean with no known app console errors
- touch/responsive behavior is checked at representative compact/wide widths
- replaced/dead code and temporary artifacts are removed
- current FIRE handoff is accurate
- relevant Truth-buffer items are resolved or intentionally left open
- PR is merged/deployed under the standing workflow when gates are satisfied

For visual work, real-device Safari review remains a distinct gate. For G7 shell freeze, the stricter `G7_SHELL_CERTIFICATION.md` gate applies.
