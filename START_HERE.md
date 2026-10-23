# Babel FIRE — Start Here

**Purpose:** zero-context continuity for building/reviewing Babel FIRE.

- **Repository:** `BabeDrums/babel-fire`
- **Production branch:** `main`
- **Live production app:** https://babedrums.github.io/babel-fire/
- **Live G7 preview:** https://babedrums.github.io/babel-fire/v7-preview/
- **Cross-generation doctrine:** `FIRE_CORE.md`
- **Active G7 shell spec:** `V7_DRAFT.md`
- **Production-generation spec:** `V6.md`

When a new ChatGPT conversation begins with or clearly refers to **Babel FIRE**, resume immediately. Do not ask Babel to reconstruct documented decisions.

## If the conversation switches to surrounding Babel apps

Do **not** reconstruct the ecosystem from memory, old Smithereens files, old Babel World prototypes, or elemental-name guesses.

Switch to:

1. `BABEL_START_HERE.md`
2. `BABEL_APPS.md`
3. `BABEL_PLATFORM.md`
4. relevant pending items in `CONTINUITY_INBOX.md`

That lane preserves the learning-app boundary, Visual Identity candidate, Babel World, elemental-name rule, Fire/badges/pixel language, cross-app evidence, and open ecosystem questions.

If the conversation switches back to FIRE implementation, return here.

## Read in this order for FIRE work

1. `START_HERE.md`
2. `AGENTS.md`
3. `FIRE_CORE.md`
4. `V7_DRAFT.md`
5. current `main`, open PRs/branches, tests, and `CHANGELOG.md`
6. `V6.md` when production/migration compatibility matters
7. `CONTEXT.md` for durable supporting context not superseded above
8. **relevant unresolved items only** in `CONTINUITY_INBOX.md`
9. `REFERENCES.md` for inspiration/research only

`CONTINUITY_INBOX.md` is a low-authority capture buffer, never a substitute for the sources above it. It exists so concrete feedback and promising-but-unpromoted ideas survive chat boundaries without bloating canonical specs.

Always distinguish production V6 from experimental G7.

## Naming

Use **Babel** as the project-facing reference-user name. Do not use Gabriel in current FIRE handoff, approval, review, or product-facing instructions. Preserve immutable external account names and genuine historical artist references where appropriate.

Use **G7** in normal conversation for the seventh FIRE implementation/shell generation. Keep technical identifiers `V7_DRAFT.md`, `/v7-preview/`, and `production-projects-v1-v7-preview` unless a real migration reason appears.

Use **FIRE Core** for the first complete functional product spine. Do not introduce `M1` merely to create another taxonomy. **FIRE 1.0** remains the later validated release milestone.

## FIRE Core doctrine

`FIRE_CORE.md` is current cross-generation product authority.

Core promise:

> **What deserves my attention next, why, and what should I try in the DAW?**

North star:

> **After a useful FIRE session, the musician should know what to do in the DAW that they did not clearly know before opening FIRE. If they only updated FIRE, FIRE failed.**

FIRE is a production companion / decision engine, not a DAW replacement, plugin encyclopedia, generic checklist, automatic song generator, or mandatory course.

### First-class project types

**Original** — idea/material → finished, release-ready audio while preserving creative flexibility.

**Recreation** — reference → faithful cover, reconstruction, interpretation, reimagining, or production study. Recreation is a complete standalone workflow; someone may use FIRE only to make covers quickly.

Both share one reasoning engine:

**Feel → Identify → Reason → Experiment → Evaluate**

Recreation can **Match / Interpret / Reimagine**. Individual differences can be **Match / Intentional / Explore**. Do not force an intent question before a meaningful difference exists.

### Adaptive learning

Working principle:

> **Duolingo-like intelligence underneath, not Duolingo-like UI.**

Default guidance:

- **Do it** — concise mission/context
- **Why?** — rationale/listening target
- **Go deeper** — richer explanation/alternatives/diagnostics
- **I don't know / Not sure** — valid first-class path, never failure

Skill understanding is domain-specific, not one global Beginner/Intermediate/Advanced label. Strong evidence comes from intentional decisions, successful diagnosis/evaluation, independence, transfer, and repeated application—not taps or page completion.

Likely evidence ladder remains a hypothesis:

**Encountered → Guided → Independent → Transfer → Consistent**

### FIRE ↔ Logic boundary

Default rhythm:

**FIRE → Logic → FIRE → Logic**

Logic owns detailed regions/takes, plugin settings, routing, automation values, and mixer/session detail unless a future feature proves otherwise.

FIRE retains intention/hierarchy, perceived issue, diagnosis, meaningful experiment/result, accepted decision, unresolved problem, reusable lesson, and next useful decision.

## Repository state

### Production — V6

- root `/` remains V6
- V6 uses `production-projects-v1` and schema 5
- preserve stable identities, migrations, timeline semantics, durable notes, browser persistence, and downstream dependencies
- V6 remains fallback until G7 is physically approved and deliberately promoted

### Successor — G7

- preview lives at `/v7-preview/`
- G7 uses `production-projects-v1-v7-preview`
- G7 must never mutate V6 production data
- technical filenames/routes retain V7 wording for continuity; normal conversation says G7

### Generation-spec retention

Git history is the archive.

Keep only the **current production generation spec + active successor/preview spec** in the working tree by default. Older specs remain only when a concrete maintenance/migration/compatibility/recovery reason still depends on them.

`V5.md` is intentionally absent from the working tree and remains recoverable from Git history.

## Current verified continuity — corrected G7 shell is live but NOT frozen

PR **#48 — Freeze the G7 shell system** merged and deployed, but Babel's physical iPhone review **did not approve that shell freeze**. The structural direction improved, but the shell still felt ugly, text-heavy, inconsistent, and interactionally unpredictable.

Key physical-review evidence from #48:

- no project-card management action on Projects
- Projects title / `+` alignment felt off
- `G7 · <commit>` under Projects polluted content hierarchy; Babel preferred quiet bottom-center
- New Project exposed only Recreation although Original/Recreation are both first-class
- title/text scale felt inconsistent screen-to-screen
- too many headers/subtitles/helper layers repeated information
- visible Continue/Journey taxonomy felt unnecessary
- Structure repeated the same idea through title/subtitle/helper/button
- interaction behavior was unpredictable: similar work sometimes inline, sometimes sheet, sometimes navigation
- narrow-phone keyboard/input composition needed improvement

PR **#50 — Simplify the G7 shell interaction system** corrected those system-level problems. It merged to `main` at **`9095116ae1f791f85e6842124a64210da593c085`**, deployed successfully through GitHub Pages **#77**, and that exact runtime passed post-merge static + Chromium regressions at **390 / 440 / 820**.

PR **#51** sealed the zero-context FIRE handoff at **`f69a6427eccf8da84b04dabcbc984eb79855b162`**; Pages deployment **#78** succeeded and the unchanged runtime again passed 390 / 440 / 820.

Later docs-only ecosystem/continuity commits may make `main` newer than those runtime SHAs. Determine current `main`/PR state from Git rather than treating the runtime SHA as forever-latest.

### Latest physical-device impression after #50/#51

Babel's first impression is **broadly positive — the corrected shell "looks pretty good"** — but this is **not shell approval yet** and the physical review is incomplete.

Carry these specific observations into the next FIRE build conversation:

1. **Projects three-dot actions affordance:** the new actions area looks visually "stapled on" / attached as a separate strip because the divider makes it feel disconnected from the main project card. Preserve direct project management, but revisit how the affordance belongs to the card if the completed review confirms the problem.
2. **Tempo input focus/composition:** the Tempo entry on Song Setup gets a weird square/highlighted focus appearance when tapped and felt cleaner before. Review the actual iPhone focus/keyboard state rather than assuming simulated Chromium focus styling is sufficient.
3. **Headers / overall text hierarchy:** Babel has **not finished checking these yet**. Do not infer typography/header approval from the otherwise positive first impression.

**Current next action:** finish physical-device review of the corrected G7 shell, reconcile any confirmed issues, then explicitly approve/freeze it before beginning FIRE Core breadboarding.

## G7 Shell Simplification + Interaction Grammar

The correction is intentionally narrow; it does not add FIRE Core musical functionality.

### Core rules

- **Delete before styling.** If removing text does not make the next action harder to understand, remove it.
- **Inline = choose/toggle/classify/confirm/evaluate.**
- **Sheet = create/edit/manage a discrete thing.**
- **Navigation = enter another meaningful workspace.**
- **Menu/secondary affordance = utilities that should not compete with musical work.**
- consistency comes from semantic meaning, not making every interaction use the same container

### Projects

- `Projects` remains root identity; `+` shares one stable header alignment
- project cards separate primary open behavior from a quiet per-card actions affordance
- Edit/Reset/Delete can be reached from Projects without entering the project first
- New Project explicitly exposes **Original** and **Recreation**
- Original creation requires title; artist optional
- Recreation requires song title + artist
- tiny `G7 · <commit>` is quiet bottom-center review trace outside content hierarchy
- build trace is temporary review metadata, not permanent chrome

### Project Home

- no visible `Continue` heading
- no visible `Journey` heading
- one current recommendation remains visually primary
- current task is not repeated below
- revisitable/upcoming work remains in one quiet grouped list
- one tiny `Later` label may remain because it communicates chronology
- saved Notes may appear as a utility row; empty Notes stays hidden
- Original Project Home remains truthful even before its FIRE Core spine exists

### Work headers/copy

- nested work Back is icon-only with accessible label
- do not print project name above every work title
- Song Setup: title only
- Structure: title only
- Tracks: one useful instruction, `Choose everything you hear.`
- Section Study / Review Map: title + quiet built-later state only
- Notes: title only
- one stable work-title scale across work pages

### Structure

- arrangement group exists from empty state forward
- `Add Section` stays inside that group
- Add/Edit Section uses a sheet because it creates/edits an object
- verification is concise `Matches the song`
- Continue is compact after verification

### Tracks

- common tracks use direct inline multi-select
- custom `Other` uses an `Add Track` sheet because it creates a named custom object
- Continue is compact rather than a giant phone-width bar

### Sheets / keyboard

- sheets are concise create/edit/manage surfaces, not hidden navigation pages
- spacing/control sizing remains compact
- CSS scroll padding/margins help focused fields/actions breathe above the software keyboard without VisualViewport root-scroll logic

## Physical approval checklist

Babel should inspect the corrected G7 preview on iPhone:

1. Does `Projects` + `+` feel aligned/intended?
2. Is `G7 · <commit>` quiet bottom-center rather than part of content?
3. Can project Edit/Reset/Delete be reached naturally from Projects?
4. Are Original/Recreation both obvious without excess chrome?
5. Does removing Continue/Journey labels simplify Project Home without making it ambiguous?
6. Do Song Setup / Structure / Tracks feel like one typography/hierarchy system?
7. Does Add Section logically earn a sheet as object creation?
8. Do normal track choices feel direct while custom creation logically earns a sheet?
9. Are primary actions compact/intended rather than giant bars?
10. Is keyboard/input composition usable and less awkward?
11. Overall: **can Babel move through the shell without wondering what kind of UI is going to happen next?**

If approved, record approval and **stop broad shell polishing**.

## After shell approval

Sequence:

**physical G7 shell approval → FIRE Core breadboard → thin end-to-end FIRE Core spine → real-project validation**

Breadboard the entire Original + Recreation journey before deeply designing later phases. Use Shape Up-style places / affordances / connections.

For every phase define:

- entering problem
- what FIRE asks the musician to notice
- decision made
- Logic action/experiment
- evaluation
- done criteria
- evidence retained
- context carried forward

Breadboard work is primarily underground product logic/documentation; Babel should expect little or no visible runtime change.

Then build the thinnest complete walking spine from start → finished release-ready audio and validate on real music:

- Recreation: **Creep**
- Original: **Even**

Deepen only where real use proves need.

## Wider Babel ecosystem — preserve but do not build during this phase

Do not use this FIRE handoff to define sibling products.

For learning app / Visual Identity / Babel World / WATER / Fire/badges / pixel language / shared evidence / future accounts or cross-app questions, switch to `BABEL_START_HERE.md` + `BABEL_APPS.md` + `BABEL_PLATFORM.md`, then inspect relevant unresolved entries in `CONTINUITY_INBOX.md`.

Core boundary worth remembering here:

> **Product need earns an app. Naming/metaphor follows the job.**

Do not interrupt current FIRE work to build hypothetical sibling products or shared infrastructure.

## Reference registry

`REFERENCES.md` is the central inspiration/evidence registry. Current useful lenses include Apple, Logic/Ableton, Basecamp/Shape Up, Duolingo, Google/Material, Figma, GitHub/Primer, ChatGPT, Things, Procreate, Snapchat, Instagram/TikTok observationally, Pokémon GO collection/spatial patterns, xAPI/xAPI Profiles, Open Badges 3.0, Minecraft, and classic Pokémon-era pixel-art qualities.

Borrow principles, not branding/assets/templates. References never override product doctrine.

## Approval / execution contract

- Babel uses **“bet”** to mean **approved — execute now**.
- Approved FIRE work means **implement → test → fix → PR → green checks → merge → Pages deploy → verify → live G7 preview link**.
- Do not make Babel repeatedly say continue/merge/deploy/link.
- Standing permission exists to merge when checks are green, production-data safety is clear, and no genuine product decision remains unresolved.
- Stop only when tests fail, production-data safety is uncertain, destructive behavior is unresolved, or a genuine product decision is open.
- Never claim a change is live before merge + Pages verification.

## Automatic handoff + continuity capture

Babel should never need to request a routine handoff update, consistency sweep, or reminder that a durable new idea should be preserved.

For every substantive FIRE product/runtime/durable-rule change:

1. update the correct authority/spec
2. sweep active docs/implementation for stale contradictions
3. rewrite/remove/qualify superseded live rules
4. preserve historical material only when clearly scoped/useful; rely on Git otherwise
5. refresh `START_HERE.md`
6. refresh `BABEL_START_HERE.md` too if the change affects wider ecosystem semantics
7. run handoff/doctrine guards

For smaller durable deltas that are important enough to survive but not mature enough for authority, use `CONTINUITY_INBOX.md` according to its capture threshold and promotion rules. **Batch these at natural checkpoints rather than writing a repo commit for every message.**

`scripts/check_handoff.py` enforces watched handoff freshness. `scripts/check_product_doctrine.py` protects known settled markers. Scripts cannot prove natural-language semantic consistency; product judgment remains required.

Clear contradiction → reconcile automatically.
Historical statement → scope it.
Genuine product conflict → resolve through authority/product judgment rather than silently guessing.

## Parallel-chat ownership

Babel may intentionally keep two or more conversations open.

- **FIRE build chat:** owns active runtime/spec implementation and follows this handoff.
- **Ecosystem brainstorm chat:** follows `BABEL_START_HERE.md` and is read-mostly by default while FIRE implementation is active; it can research/brainstorm freely and may make narrowly scoped docs-only continuity updates when a durable idea genuinely needs preservation.

Before any parallel chat writes, it must re-read latest `main` and open PRs. Do not let an ecosystem brainstorm casually edit FIRE runtime/G7 behavior or create competing branches against active implementation.

## Authority summary

For FIRE:

1. `AGENTS.md`
2. `FIRE_CORE.md`
3. `V6.md` for live production-generation behavior
4. `V7_DRAFT.md` for G7 shell behavior
5. `START_HERE.md` for current verified state/next step
6. `CONTEXT.md` for durable supporting context
7. `CONTINUITY_INBOX.md` for unresolved low-authority deltas only
8. code/tests as implementation evidence

For the wider ecosystem:

1. `AGENTS.md`
2. `BABEL_START_HERE.md`
3. `BABEL_APPS.md`
4. `BABEL_PLATFORM.md`
5. `FIRE_CORE.md` where FIRE semantics matter
6. `CONTINUITY_INBOX.md` for unresolved low-authority deltas only
7. `REFERENCES.md`
8. older prototypes/history

When a lower source conflicts with a higher current authority, reconcile the lower source instead of preserving both as competing truth.