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

### Physical review after PR #50/#51 — review still incomplete

Status: **PENDING REVIEW**

Babel's first impression of the corrected G7 shell is broadly positive: **"looks pretty good"** and the simplification direction appears meaningfully better. This is **not shell approval yet**; the full header/text/system review is still incomplete.

Specific observations to carry into the next FIRE build chat:

1. **Projects card actions affordance** — the new three-dot area looks visually "stapled on" / attached as a separate strip because the divider/bar makes it feel disconnected from the main project card. Preserve the direct management capability, but revisit how the affordance belongs to the card if the completed physical review confirms the issue.
2. **Tempo input focus/composition** — the tempo entry field on Song Setup has a weird square/highlighted focus appearance when tapped; it felt cleaner before. Review actual iPhone focus/keyboard composition rather than assuming Chromium focus styling tells the whole story.
3. **Headers / overall text hierarchy** — Babel has **not finished checking this yet**. Do not infer that typography/header consistency is approved simply because the rest of the shell looks better.

Next FIRE action remains: finish physical-device review of the corrected G7 shell, reconcile any confirmed issues, then explicitly approve/freeze before FIRE Core breadboarding.

## Pending ecosystem deltas

None currently. The current learning-app boundary, Visual Identity candidate, Babel World hub hypothesis, elemental-name rules, xAPI/evidence-first model, Open Badges-inspired achievement truth, source marks vs achievement badges, Fire/River local-metaphor separation, original pixel-language hypothesis, and centralized future badge/mark collection are already promoted into `BABEL_START_HERE.md`, `BABEL_APPS.md`, and `BABEL_PLATFORM.md`.
