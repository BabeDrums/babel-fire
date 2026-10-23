# Babel FIRE

- **Repository:** `BabeDrums/babel-fire`
- **Production branch:** `main`
- **Live production app:** https://babedrums.github.io/babel-fire/
- **Live G7 preview:** https://babedrums.github.io/babel-fire/v7-preview/
- **Cross-generation doctrine:** `FIRE_CORE.md`
- **Future Babel platform hypotheses:** `BABEL_PLATFORM.md`
- **External references / inspiration:** `REFERENCES.md`
- **Production-generation spec:** `V6.md`
- **Active successor spec:** `V7_DRAFT.md`

When a new ChatGPT conversation begins with or clearly refers to **Babel FIRE**, resume this project immediately. Do not ask Babel to reconstruct documented decisions.

## Read in this order

1. `START_HERE.md`
2. `AGENTS.md`
3. `FIRE_CORE.md`
4. `V7_DRAFT.md` for current G7 shell behavior
5. `V6.md` when production behavior/migration compatibility matters
6. `BABEL_PLATFORM.md` only for future accounts/sync/ecosystem/monetization/Practice/Fire/badges/social/lore work
7. `REFERENCES.md` for design/research inspiration; references are not authority
8. `CONTEXT.md` for supporting history not superseded above
9. current `main`, open PRs/branches, tests, and `CHANGELOG.md`

Always distinguish production V6 from experimental G7.

## Naming

Use **Babel** as the project-facing reference-user name. Do not use Gabriel in current FIRE handoff, approval, review, or product-facing instructions. Preserve immutable external account names and genuine artist/history references where appropriate.

Use **G7** in normal conversation for the seventh FIRE implementation/shell generation. Keep the existing technical identifiers `V7_DRAFT.md`, `/v7-preview/`, and `production-projects-v1-v7-preview` unless a real migration reason appears.

Use **FIRE Core** for the first complete functional product spine. Do not invent an `M1` taxonomy. **FIRE 1.0** remains the future validated release milestone.

## FIRE Core product doctrine

`FIRE_CORE.md` is current cross-generation product authority.

Core promise:

> **What deserves my attention next, why, and what should I try in the DAW?**

North star:

> **After a useful FIRE session, the musician should know what to do in the DAW that they did not clearly know before opening FIRE. If they only updated FIRE, FIRE failed.**

FIRE is a production companion / decision engine, not a DAW replacement, plugin encyclopedia, generic checklist, auto-song generator, or mandatory course.

### First-class project types

**Original** — idea/material → finished, release-ready audio while preserving creative flexibility.

**Recreation** — reference → faithful cover, reconstruction, interpretation, reimagining, or production study. Recreation is a complete standalone workflow; someone may use FIRE only to make covers quickly.

Both share one reasoning engine:

**Feel → Identify → Reason → Experiment → Evaluate**

Recreation can **Match / Interpret / Reimagine**. Individual differences can be **Match / Intentional / Explore**. Do not force the intent question before a meaningful difference exists.

### Adaptive learning

Working principle:

> **Duolingo-like intelligence underneath, not Duolingo-like UI.**

Default guidance:

- **Do it** — concise mission/context
- **Why?** — rationale/listening target
- **Go deeper** — richer explanation/alternatives/diagnostics
- **I don't know / Not sure** — valid first-class path, never failure

Skill understanding is domain-specific, not one global Beginner/Intermediate/Advanced level. Strong evidence comes from intentional decisions, successful diagnosis/evaluation, independence, transfer, and repeated use—not taps or page completion.

The likely evidence ladder remains a hypothesis: **Encountered → Guided → Independent → Transfer → Consistent**.

### FIRE ↔ Logic boundary

Default rhythm: **FIRE → Logic → FIRE → Logic**.

Logic owns detailed regions/takes, plugin settings, routing, automation values, and mixer state unless a future feature proves otherwise.

FIRE retains intention/hierarchy, perceived issue, diagnosis, meaningful experiment/result, accepted decision, unresolved problem, reusable lesson, and next useful decision.

## Future platform state — preserved, not current scope

Read `BABEL_PLATFORM.md` before changing future ecosystem semantics.

Current future rules/hypotheses include:

- one optional Babel-level identity/account rather than separate accounts invented per app
- **shared evidence, local identity** across apps
- a future versioned Babel Learning Contract for overlapping skill identities/evidence meanings
- **evidence first, interpretation second** — store what was demonstrated + provenance/context, derive current skill state later
- source/origin marks and achievement badges are different semantics
- a future learning-focused app should exist only if a distinct product job actually emerges; do not reverse-engineer apps merely to complete an element set
- a future Babel World is an optional hub hypothesis, never a dependency or global producer score
- Babel World's final collection shape is intentionally open: gallery/trophy case/map/neighborhood/park/world should be earned by real content and relationships
- the evolving **Fire** is both a truthful progress artifact and an expressive collectible identity layer; it does not claim bigger = objectively better producer
- pixel-art Fire/badge language inspired by constrained game-art readability is a later visual hypothesis
- ambient Fire glow on FIRE's home surface is a later discovery/personality hypothesis, never required navigation or engagement pressure
- other Babel apps may contribute to the same production skill evidence only when they genuinely demonstrate the same capability; app usage alone never grows the Fire
- an app-specific River/other metaphor may represent that app's local journey while shared production evidence can still inform production growth
- monetization philosophy: **desire, not deprivation; pay to go deeper, not to be allowed to make music**
- account-level entitlements are preferred over hidden universal premium passwords or permanent friend builds
- lore/Easter eggs may reward curiosity but never hide required workflow/accessibility/privacy/account recovery/purchased functionality

Do **not** build Babel World, Fire/badges, accounts, cloud sync, monetization, social, lore, or a second app during G7 Shell Freeze/FIRE Core breadboarding.

## Reference registry

`REFERENCES.md` is the central inspiration/evidence registry. Current useful lenses include Apple, Logic, Ableton, Basecamp/Shape Up, Duolingo, Google/Material, Figma, GitHub/Primer, ChatGPT, Things, Procreate, Snapchat, Instagram/TikTok as observational interaction references, Pokémon GO collection/spatial patterns, xAPI/xAPI Profiles, Open Badges 3.0, Minecraft, and classic Pokémon-era pixel-art qualities.

Borrow principles, not branding/assets/templates. External references never override product doctrine.

## Current repository state

### Production — V6

- Root `/` remains V6.
- V6 uses `production-projects-v1` and schema 5.
- Preserve stable project/section/track/range/event IDs, migrations, timeline semantics, durable notes, browser persistence, and Map → Skeleton dependencies.
- V6 remains the fallback until G7 is physically approved and deliberately promoted.

### Successor — G7

- Preview lives at `/v7-preview/`.
- G7 uses `production-projects-v1-v7-preview` and must never mutate V6 production data.
- Technical filenames/routes retain V7 wording for continuity; normal product conversation says G7.

### Generation-spec retention rule

Keep only the **current production generation spec + active successor/preview spec** in the working tree by default. Git history is the archive for retired generations. Older specs remain only when a concrete maintenance/migration/compatibility/recovery reason still depends on them.

`V5.md` is intentionally removed from the working tree and remains recoverable from Git history.

## Current active direction

**G7 Shell Freeze → physical review → FIRE Core breadboard → thin end-to-end FIRE Core spine → real-project validation**

PR **#48 — Freeze the G7 shell system** is the active Shell Freeze implementation.

This is the final broad generic shell/system pass for a while. It must not expand FIRE Core functionality or add signature/platform features.

### #48 Shell Freeze decisions

**Projects**

- one job: open/create
- persistent `+` remains the single create affordance
- empty state remains `No projects yet.`
- tiny preview-only **`G7 · <commit>`** appears near the Projects title for deployment confirmation; it is subordinate review traceability, not permanent product chrome

**Project Home**

- project identity + actions
- **Continue owns the current recommended task**
- Journey does **not** repeat the same current task
- Journey shows completed work for revisiting + upcoming work for orientation/direct access
- remove adjacent `Journey` + `The Map` double-label clutter
- later phases remain visible as a quieter compact collection rather than one dense sentence
- hide empty/dead Notes chrome; if real saved notes exist, Project Notes remains reachable

**Shared header hierarchy**

1. Projects root = strongest identity
2. Project Home = strong project identity
3. Work page = compact task title + minimum-useful subtitle

Work pages must not use root-sized titles.

**Song Setup**

- focused grouped form
- Reference remains `Import the reference into your session.` with ring/check completion semantics
- no media picker/ownership implication

**Structure**

- arrangement first
- Add Section stays inside the arrangement group once sections exist
- `Structure matches the song` becomes a quiet final arrangement row rather than a separate competing card
- Continue appears after verification

**Tracks**

- direct multi-select remains
- tiles become denser without changing logic
- custom-track control stays compact
- Continue appears once the task has started

**Section Study / Review Map**

- missing prerequisites may use actionable context repair
- built-later states use quiet truthful placeholders rather than feature-looking cards

**Viewport/adaptation**

- natural document scrolling only; no VisualViewport-driven root overflow switching
- modest CSS-only bottom clearance for tall Safari pages
- sheets may lock body scroll while open
- 390 / 440 / 820 layouts keep identical product hierarchy/actions/states and adapt presentation only

## What Babel should inspect after #48 deploys

This pass should be **visibly cleaner but not a dramatic redesign**.

Review in order:

1. **Projects** — still calm; confirm `G7 · <commit>` matches the deployed build and is visually subordinate
2. **Project Home** — current task appears once; Journey feels lighter; no Journey/The Map label clutter; later phases are quiet; empty Notes no longer competes
3. **Song Setup** — work title is smaller/cleaner; form still obvious
4. **Structure** — verification feels attached to the arrangement rather than floating separately
5. **Tracks** — noticeably denser but not cramped
6. **Section Study / Review Map** — unfinished states feel truthful and quiet
7. **System** — headers, spacing, rows, actions, sheets, Back behavior, short/tall scrolling, compact/wide adaptation feel like one product

Approval question:

> **Can the musician open a project and start useful musical work without thinking about how FIRE is organized?**

Do not judge #48 by new functionality; it intentionally adds almost none.

## After physical Shell Freeze approval

Immediately stop broad shell polishing and breadboard FIRE Core using Shape Up-style places / affordances / connections.

For every phase define:

- entering problem
- what FIRE asks the musician to notice
- decision made
- Logic action/experiment
- evaluation
- done criteria
- evidence retained
- context carried forward

Breadboard the **whole Original + Recreation journey** before deeply designing later phases. The breadboard is primarily underground/documentation/product-logic work; Babel should expect little or no visible runtime change from that pass.

After breadboard agreement, build the **thinnest complete walking spine** from start → finished release-ready audio for both project types, then test it on real music:

- Recreation: **Creep**
- Original: **Even**

Deepen only where real use proves need.

## Approval / execution contract

- Babel uses **“bet”** to mean **approved — execute now**.
- Approved FIRE work means **implement → test → fix → PR → green checks → merge → Pages deploy → verify → live G7 preview link**.
- Do not make Babel repeatedly say continue/merge/deploy/link.
- Standing permission exists to merge when checks are green, production-data safety is clear, and no genuine product decision remains unresolved.
- Stop when tests fail, production-data safety is uncertain, destructive behavior is unresolved, or a genuine product decision is actually open.
- Never claim a change is live before merge + Pages verification.

## Automatic handoff + consistency

Babel should never need to request a handoff update or routine consistency sweep.

Any substantive product/runtime/durable-rule PR must:

1. update the correct authority/spec
2. sweep other active docs/implementation for stale contradictions
3. rewrite/remove/qualify superseded live rules
4. preserve historical material only when clearly scoped and still useful
5. refresh `START_HERE.md`
6. run the handoff/doctrine guards

`scripts/check_handoff.py` enforces START_HERE freshness for watched product/runtime/spec changes. `scripts/check_product_doctrine.py` protects known settled doctrine markers. Semantic consistency still requires product judgment; scripts must not blindly rewrite genuine ambiguity.

Clear contradiction → reconcile automatically. Historical statement → scope it. Genuine product conflict → resolve through authority/product judgment rather than silently guessing.

## Authority order

1. `AGENTS.md` — repository/workflow rules
2. `FIRE_CORE.md` — current cross-generation product doctrine
3. `V6.md` — shipped production-generation behavior while V6 is live
4. `V7_DRAFT.md` — G7 shell behavior where Core-compatible
5. `BABEL_PLATFORM.md` — future/platform hypotheses only
6. `REFERENCES.md` — inspiration/research only
7. `CONTEXT.md` — supporting history/detail
8. code/tests — implementation evidence

When a lower source conflicts with a higher current authority, reconcile the lower source instead of preserving both as competing truth.
