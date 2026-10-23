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

Do **not** capture:

- jokes, transient wording, or conversational filler
- every option in an unresolved brainstorm
- repeated points already represented accurately in authority docs
- implementation details that are already in code/tests/specs
- ideas Babel immediately rejects

### Consolidation cadence

Prefer batching continuity updates at natural checkpoints rather than writing on every turn:

- before/with a substantive PR
- after a coherent brainstorm batch reaches a stable stopping point
- when switching between FIRE and wider-ecosystem lanes
- before a long chat is likely to end or overflow
- immediately when Babel explicitly says a detail must not be lost

### Promotion rule

When an item becomes mature:

- FIRE doctrine/behavior → promote to `FIRE_CORE.md`, `V7_DRAFT.md`, or the relevant production spec
- current FIRE build/review state → promote to `START_HERE.md`
- sibling-app product concept/boundary → promote to `BABEL_APPS.md`
- cross-app architecture/progression/platform → promote to `BABEL_PLATFORM.md`
- ecosystem current-state handoff → promote to `BABEL_START_HERE.md`
- external inspiration/research lesson → promote to `REFERENCES.md`
- permanent repository/process rule → promote to `AGENTS.md`

After promotion/rejection/supersession, remove the inbox item from the active file. Git history preserves the old state. The active inbox should stay small and unresolved-only.

## Parallel-chat rule

Babel may intentionally run multiple chats.

### FIRE build lane

- owns active FIRE implementation/runtime/spec work
- follows `START_HERE.md` + `AGENTS.md`
- may merge/deploy under the standing FIRE workflow

### Ecosystem brainstorm lane

- follows `BABEL_START_HERE.md` + `BABEL_APPS.md` + `BABEL_PLATFORM.md`
- is **read-mostly by default** while a FIRE build chat is active
- may research, brainstorm, compare concepts, and form hypotheses without touching runtime
- when a genuinely durable ecosystem idea emerges, it may make a narrowly scoped docs-only continuity update from the latest `main`, after checking open PRs/branches
- must not edit FIRE runtime, active G7 spec behavior, storage/schema, or implementation files merely to preserve a brainstorm

If two chats could touch the same durable file at the same time, the later writer must re-read latest `main` and open PRs before changing it. Prefer one small docs-only continuity PR over competing overlapping edits.

## Pending FIRE deltas

None currently. The narrow physical-device follow-up for project-card action integration, Tempo focus treatment, and the Original placeholder copy is promoted into `V7_DRAFT.md` / `START_HERE.md` and protected by G7 regression coverage. Physical approval itself remains a current-state gate in `START_HERE.md`, not an inbox item.

## Pending repository/process deltas

### Ecosystem authority order should be clarified

`BABEL_APPS.md` explicitly describes itself as the future product-concept authority for sibling apps, while some current authority summaries list `BABEL_START_HERE.md` above it. They agree today because handoff freshness is enforced, but this creates avoidable future ambiguity.

Recommended cleanup when the documentation lane next changes these files:

- keep `BABEL_START_HERE.md` as the **entry point / current ecosystem handoff / routing summary**
- let `BABEL_APPS.md` own sibling-app jobs/boundaries
- let `BABEL_PLATFORM.md` own cross-app architecture/progression hypotheses
- let `FIRE_CORE.md` own FIRE semantics
- make it explicit that the handoff summarizes those authorities rather than overriding them

### Branch existence is not product authority

The repository retains many historical task branches. A fresh chat should not treat a branch as active/current merely because it still exists.

Recommended durable process clarification:

- current `main` + authoritative handoff/specs are the baseline truth
- open PRs and explicit current handoff/user direction identify active work
- an old task branch without an open PR/current handoff reference is historical working state, not doctrine
- parallel chats should still re-check latest `main` and open PRs before writing

Do not delete branches automatically merely to solve this documentation problem; branch cleanup is a separate repository-maintenance decision.

## Pending ecosystem deltas

None currently. The learning-app boundary, Visual Identity candidate, Babel World hub hypothesis, elemental-name rules, xAPI/evidence-first model, Open Badges-inspired achievement truth, source marks vs achievement badges, Fire/River local-metaphor separation, original pixel-language hypothesis, and centralized future badge/mark collection are already promoted into `BABEL_START_HERE.md`, `BABEL_APPS.md`, and `BABEL_PLATFORM.md`.
