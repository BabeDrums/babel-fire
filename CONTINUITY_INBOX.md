# Babel — Continuity Inbox

**Purpose:** lightweight capture buffer for durable ideas, feedback, questions, and rules that are worth carrying into a fresh chat but are not mature enough to belong in a canonical spec/ledger yet.

This file is **not product authority**. Read the appropriate handoff and authority files first. If an inbox item conflicts with canonical doctrine/specs, the canonical source wins.

## How this works

Do **not** update this file for every message.

Capture a continuity delta here when at least one is true:

- Babel explicitly says the idea/rule/detail is important, should be remembered, locked in, or carried forward.
- The item changes scope, semantics, naming, product boundaries, workflow, guardrails, or the next meaningful step.
- It is concrete physical-device/product feedback that a future build chat would otherwise lose.
- It is a promising future hypothesis with enough specificity that reconstructing it later would cost real work.
- The conversation is approaching a handoff/context boundary and the idea has not yet been promoted into its final authority file.

Do **not** capture jokes, transient wording, every option in an unresolved brainstorm, repeated points already represented accurately in authority docs, implementation details already in code/tests/specs, or ideas Babel immediately rejects.

### Consolidation cadence

Prefer batching continuity updates at natural checkpoints: before/with a substantive PR, after a coherent brainstorm batch, when switching lanes, before likely context exhaustion, or immediately when Babel explicitly says a detail must not be lost.

### Promotion rule

When an item becomes mature:

- FIRE doctrine/behavior → `FIRE_CORE.md`, `V7_DRAFT.md`, or the relevant production spec
- current FIRE build/review state → `START_HERE.md`
- sibling-app concept/boundary → `BABEL_APPS.md`
- cross-app architecture/progression/platform → `BABEL_PLATFORM.md`
- ecosystem current-state handoff → `BABEL_START_HERE.md`
- research lesson → `REFERENCES.md`
- permanent repository/process rule → `AGENTS.md`

After promotion/rejection/supersession, remove it from the active inbox. Git history is the archive.

## Parallel-chat rule

### FIRE build lane

- owns active FIRE implementation/runtime/spec work
- follows `START_HERE.md` + `AGENTS.md`
- may merge/deploy under the standing FIRE workflow

### Ecosystem brainstorm lane

- follows `BABEL_START_HERE.md` + `BABEL_APPS.md` + `BABEL_PLATFORM.md`
- is **read-mostly by default** while a FIRE build chat is active
- may research/brainstorm without touching FIRE runtime
- must re-read latest `main` and open PRs before durable writes

If two chats could touch the same durable file at the same time, the later writer reconciles latest `main` first.

## Pending FIRE deltas

None currently. The latest physical-device refinement feedback — compact placeholder-led New/Edit project forms, terse project actions, removal of dead sheet grabbers, confirmation for destructive project actions, project-card menu targeting without active-project mutation, one unified Cover Home progression, removal of redundant completion chrome, retention/refinement of the Tracks grid, and explicit Done-based Tracks confirmation — is promoted into `V7_DRAFT.md` / `START_HERE.md` and protected by G7 regression coverage. Physical approval remains a current-state gate in `START_HERE.md`, not an inbox item.

## Pending repository/process deltas

### Ecosystem authority order should be clarified

`BABEL_APPS.md` describes itself as the future sibling-app concept authority while some summaries list `BABEL_START_HERE.md` above it. They agree today, but a future docs cleanup should make explicit that the handoff summarizes authorities rather than overriding them.

Recommended ownership:

- `BABEL_START_HERE.md` = entry point/current ecosystem handoff/routing summary
- `BABEL_APPS.md` = sibling-app jobs/boundaries
- `BABEL_PLATFORM.md` = cross-app architecture/progression hypotheses
- `FIRE_CORE.md` = FIRE semantics

### Branch existence is not product authority

Current `main` + authoritative handoff/specs are baseline truth. Open PRs and explicit current handoff/user direction identify active work. An old task branch without an open PR/current handoff reference is historical working state, not doctrine. Do not delete branches automatically merely to solve this documentation issue.

## Pending ecosystem deltas

None currently. Existing learning-app, Visual Identity, Babel World, elemental-name, evidence/xAPI, badge/source-mark, Fire/River, and collection hypotheses are already promoted into the ecosystem authority files.
