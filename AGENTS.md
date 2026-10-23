# Babel FIRE — Repository Instructions

Babel FIRE is an iPhone/iPad-first music-production companion. Production runs on GitHub Pages from `main`.

Use **Babel** as the project-facing reference-user name.

## Zero-context entry points

There are two continuity lanes:

- **FIRE implementation/product work:** read `START_HERE.md` first.
- **Wider Babel ecosystem / surrounding apps / Babel World / learning app / visual identity:** read `BABEL_START_HERE.md` first.

Do not ask Babel to reconstruct decisions already documented in the appropriate handoff.

## Authority and scope

### FIRE authority

When FIRE sources conflict, use:

1. **AGENTS.md** — repository workflow, engineering, maintenance, review, documentation rules.
2. **FIRE_CORE.md** — current cross-generation FIRE product doctrine.
3. **Active production spec, currently `V6.md`** — shipped behavior for the live production generation.
4. **`V7_DRAFT.md`** — current G7 successor-shell behavior where compatible with FIRE Core.
5. **`START_HERE.md`** — current verified implementation/review/next-step state.
6. **`CONTEXT.md`** — durable supporting context/history not superseded above.
7. **Current code/tests** — implementation evidence, not product authority.

### Wider Babel ecosystem authority

For surrounding-app/platform work:

1. `AGENTS.md` — process/maintenance rules.
2. `BABEL_START_HERE.md` — current zero-context ecosystem boundaries.
3. `BABEL_APPS.md` — sibling-app concept ledger: real/candidate/unassigned/open.
4. `BABEL_PLATFORM.md` — shared architecture/infrastructure/progression hypotheses.
5. `FIRE_CORE.md` — FIRE semantics that ecosystem work must not redefine.
6. `REFERENCES.md` — inspiration/research only.
7. older prototypes/context — historical evidence only.

Do not use old Smithereens/FIRE_CONTEXT/Babel World prototypes to override current product docs.

## History and working-document retention

**Git history is the archive.**

Keep the current production-generation spec plus the active successor/preview spec in the working tree by default. Retain an older generation spec only when a concrete maintenance, migration, compatibility, or recovery need still depends on it.

Do not rewrite or destroy Git history. Removing a retired working spec from the current tree is not erasing its history.

Likewise, durable docs should contain current useful truth, not every phrasing the project has ever used. Scope historical evidence clearly or remove it from active guidance when Git already preserves it.

## Git and review workflow

- Never do implementation work directly on `main`.
- Start from the latest appropriate `main` state on a dedicated task branch.
- Inspect and preserve unfinished work before syncing/switching; never reset/discard work just to obtain a clean tree.
- Commit/push completed task work and open a PR to `main`.
- PRs are the review checkpoint before production.
- Babel has standing permission to merge FIRE PRs once the diff is reviewed, required checks are green, production-data safety is clear, and no genuine product decision remains unresolved.
- Stop instead of merging when tests fail, data safety is uncertain, behavior is destructive/risky, or a real product decision is unresolved.
- For visual/interaction work, automated CI does not replace physical-device review.

Normal sequence:

**branch → implement → test → reconcile docs → PR → checks → merge → Pages deploy → verify → physical-device approval when relevant**

## Product/design iteration protocol

Babel should not need to repeatedly request research, consistency review, cleanup, or handoff maintenance. Treat them as part of nontrivial product work when materially relevant.

User ideas/examples are inputs and hypotheses unless explicitly locked/approved/required. Evaluate them against product goals, platform guidance, evidence, and architecture.

Use a lightweight cycle:

1. **Discover** — review device feedback, current behavior, repo state, and relevant references.
2. **Define** — identify the actual problem and success condition; distinguish architecture, usability, correctness, polish, and delight.
3. **Develop** — consider plausible solutions; prefer removing complexity over adding compensating UI.
4. **Deliver** — implement/prototype in the safest surface and run relevant checks.
5. **Verify + consolidate** — physical review when visual, remove superseded UI/code, reconcile docs, refresh handoffs.

Do not turn the process into bureaucracy.

### Page necessity audit

Before adding/polishing a screen, ask what job it performs.

Classify visible elements as:

- essential to primary task
- necessary context/navigation
- conditional/advanced detail for progressive disclosure
- duplicated/system-explanation content that should disappear/move

Every focused work page should have one clear primary task, minimum required context, obvious continuation/exit where appropriate, and no redundant explanation. Also ask whether the page needs to exist at all.

### Delete before styling

If removing a label/subtitle/helper sentence does not make the next action harder to understand, remove it instead of merely shrinking it.

### Fundamentals before signature polish

Stabilize information architecture, navigation, task purpose, scrolling, spacing, interaction states, and consistency before signature personality.

Distinctive Fire/pixel/glow/lore behavior must not compensate for weak fundamentals.

## Current G7 shell principles

Do **not** duplicate current route-by-route state here. `V7_DRAFT.md` owns G7 shell rules and `START_HERE.md` owns current review/next-step status.

Permanent current principles worth protecting:

- **Projects → Project Home → direct musical work.**
- Project Home is a hub, not a dashboard.
- one current recommendation is visually primary and is not repeated below
- visible `Continue` / `Journey` taxonomy is not required
- saved Notes may earn a utility row; empty Notes stays hidden
- completed work remains revisitable; upcoming work remains understandable when useful
- no V6 center navigator or separate Roadmap should be reintroduced merely because V6 still ships
- one product logic/hierarchy/actions/states across iPhone/iPad; presentation adapts
- document height determines scrolling; no VisualViewport-driven root overflow switching
- G7 data stays isolated from V6 production data

### Interaction grammar

Use semantic consistency:

- **Inline** — choose/toggle/classify/confirm/evaluate something already in the task.
- **Sheet** — create/edit/manage a discrete thing while staying in context.
- **Navigation** — enter another meaningful workspace.
- **Menu/secondary affordance** — utility actions that should not compete with musical work.

Do not use sheets for visual variety or force object creation inline merely to avoid a sheet.

## Engineering/product rules

- Read `FIRE_CORE.md`, current `START_HERE.md`, relevant generation spec, and relevant code/tests before FIRE work.
- Production V6 uses localStorage key `production-projects-v1`; preserve it.
- G7 preview uses `production-projects-v1-v7-preview`; never mutate V6 production data from G7.
- Schema changes require tested forward migration; never wipe projects.
- Preserve stable project/section/track/range/event IDs where applicable. Real split/merge may create identities, but preserve surviving identities whenever possible.
- V6 continuous timeline remains V6 production source of truth; do not recreate duplicate Parts/Enters/Leaves state in V6 maintenance.
- Preserve downstream Skeleton Session → Draft → Bounce dependencies and browser-history behavior in V6 maintenance.
- Keep GitHub Pages simple static HTML/CSS/JS unless a clear approved need justifies architecture change.
- Roughly 44px touch targets, accessible alternatives, reduced-motion support, and discoverable interactions are required.
- No essential action should depend on a skinny line or undiscoverable gesture.
- Favor direct manipulation, progressive disclosure, and hierarchy over forms/readouts/nested menus/unnecessary modals.
- FIRE remains neutral/premium. Smithereens is a Recreation project, not FIRE's brand identity.
- Remove replaced/dead interactions. Do not commit screenshots, temporary/debug fixtures, browser artifacts, caches, or environment-only files.
- Permanent regression tests/test data belong in `tests/`.

## FIRE design-system operating rules

- **No Codex for FIRE.** Use the normal ChatGPT GitHub connector/direct repository tools.
- Use one coherent hierarchy for root title, project identity, work title, row title, support text, metadata/status.
- Subtitle/helper text is optional, not default.
- Use coherent interaction states: normal, hover (fine pointer only), pressed, selected, focus-visible, disabled, destructive, completed.
- Geometry should not jump between states.
- Selection and completion are different semantics.
- Prefer grouped rows/lists for structured text-heavy work; reserve cards for meaningful conceptual groups.
- Primary actions should fit the composition; do not default to giant full-width slabs.
- Leading toolbar = navigation; trailing toolbar = contextual/secondary action.
- Same task semantics across device sizes; sheets/dialog presentation may adapt without changing logic.
- Short pages remain genuinely short; tall pages scroll naturally.
- Tall iOS Safari pages may use modest CSS-only end clearance; do not reserve fake-scroll tails.
- Modal sheets may temporarily lock background scrolling.
- Dense phone layouts should remove/compact secondary detail before shrinking touch targets.
- Do not imitate Liquid Glass decoratively.
- Do not add overlay polish files or MutationObserver visual rewrites; modify core components/styles directly.
- Automated viewport tests are not physical iOS Safari verification.

## Product versioning / naming

- **V6** remains the production generation's established name.
- Use **G7** in normal conversation for the active successor generation.
- Keep technical identifiers `V7_DRAFT.md`, `/v7-preview/`, and `production-projects-v1-v7-preview` unless a real migration reason appears.
- **FIRE Core** = first complete functional product definition/spine, not “V1.”
- **FIRE 1.0** = future validated release milestone.
- Do not invent `M1` or other taxonomy merely to create another label.
- Major approved implementation/interaction generations may increment whole generation numbers; meaningful approved refinements may use minor versions if genuinely useful.
- Git commits are independent of product-generation numbers.
- Never silently invent/increment a product version.

## Documentation hygiene and automatic handoff

### FIRE docs

- `FIRE_CORE.md` = canonical cross-generation doctrine.
- `START_HERE.md` = canonical zero-context current FIRE state/handoff.
- `V6.md` = live production-generation behavior while V6 ships.
- `V7_DRAFT.md` = current G7 shell behavior.
- `CONTEXT.md` = durable supporting context/history only; it must not contain current G7 rules that compete with `V7_DRAFT.md`.
- `CHANGELOG.md` = meaningful milestones, not every commit.

### Ecosystem docs

- `BABEL_START_HERE.md` = canonical zero-context ecosystem handoff.
- `BABEL_APPS.md` = current app-concept ledger.
- `BABEL_PLATFORM.md` = future shared architecture/platform/progression hypotheses.
- `REFERENCES.md` = inspiration/research, not authority.

### Automatic maintenance

Babel should never need to ask for a routine handoff update or consistency sweep.

For every substantive product/durable-rule change:

1. update the correct authority
2. sweep active docs/implementation for stale contradictions
3. rewrite/remove/qualify superseded live rules
4. keep history only when clearly scoped/useful; rely on Git otherwise
5. refresh the relevant handoff(s)
6. run handoff/doctrine guards

`scripts/check_handoff.py` enforces watched handoff freshness. `scripts/check_product_doctrine.py` protects known settled markers but cannot prove semantic consistency; human/product review remains required.

Clear contradiction → reconcile automatically.
Historical statement → scope it.
Genuine product conflict → resolve through authority/product judgment rather than silently guessing.

## Verification / definition of done

Implementation work is not complete until:

- behavior matches the active product/spec
- user data is preserved or migrated safely
- relevant regressions pass
- startup/JS is clean with no known application console errors
- touch/responsive behavior is checked at representative compact/wide widths
- replaced/dead code and temporary artifacts are removed
- durable docs/handoffs are reconciled
- remaining risks are stated
- work is committed/pushed/PR'd and merged/deployed under standing permission when gates are satisfied

For visual/interaction work, physical-device Safari review remains a distinct gate. Never call simulated Chromium viewports physical verification.

For detailed V6 regression requirements, use `V6.md` and the tests rather than duplicating them here.