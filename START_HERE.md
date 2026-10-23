# Babel FIRE

- **Repository:** `BabeDrums/babel-fire`
- **Production branch:** `main`
- **Live production app:** https://babedrums.github.io/babel-fire/
- **Live G7 preview:** https://babedrums.github.io/babel-fire/v7-preview/
- **Cross-generation doctrine:** `FIRE_CORE.md`
- **Active G7 shell spec:** `V7_DRAFT.md`
- **Production-generation spec:** `V6.md`
- **Future platform hypotheses:** `BABEL_PLATFORM.md`
- **External references / inspiration:** `REFERENCES.md`

When a new ChatGPT conversation begins with or clearly refers to **Babel FIRE**, resume immediately. Do not ask Babel to reconstruct documented decisions.

## Read in this order

1. `START_HERE.md`
2. `AGENTS.md`
3. `FIRE_CORE.md`
4. `V7_DRAFT.md`
5. current `main`, open PRs/branches, tests, and `CHANGELOG.md`
6. `V6.md` when production/migration compatibility matters
7. `BABEL_PLATFORM.md` only for future account/sync/ecosystem/monetization/Practice/Fire/badges/social/lore work
8. `REFERENCES.md` for design/research lenses only
9. `CONTEXT.md` for supporting history not superseded above

Always distinguish production V6 from experimental G7.

## Naming

Use **Babel** as the project-facing reference-user name. Do not use Gabriel in current FIRE handoff, approval, review, or product-facing instructions. Preserve immutable external account names and genuine artist/history references where appropriate.

Use **G7** in normal conversation for the seventh FIRE implementation/shell generation. Keep technical identifiers `V7_DRAFT.md`, `/v7-preview/`, and `production-projects-v1-v7-preview` unless a real migration reason appears.

Use **FIRE Core** for the first complete functional product spine. Do not introduce an `M1` taxonomy merely to create another name. **FIRE 1.0** remains the later validated release milestone.

## FIRE Core doctrine

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

Skill understanding is domain-specific, not one global Beginner/Intermediate/Advanced label. Strong evidence comes from intentional decisions, successful diagnosis/evaluation, independence, transfer, and repeated application—not taps or page completion.

Likely evidence ladder remains a hypothesis: **Encountered → Guided → Independent → Transfer → Consistent**.

### FIRE ↔ Logic boundary

Default rhythm: **FIRE → Logic → FIRE → Logic**.

Logic owns detailed regions/takes, plugin settings, routing, automation values, and mixer state unless a future feature proves otherwise.

FIRE retains intention/hierarchy, perceived issue, diagnosis, meaningful experiment/result, accepted decision, unresolved problem, reusable lesson, and next useful decision.

## Future platform state — preserved, not current scope

Read `BABEL_PLATFORM.md` before changing future ecosystem semantics.

Important preserved future rules/hypotheses:

- one optional Babel-level identity/account rather than separate accounts invented per app
- **shared evidence, local identity** across apps
- future versioned Babel Learning Contract for overlapping skills/evidence meanings
- **evidence first, interpretation second** — preserve what was demonstrated + provenance/context and derive current skill state later
- source/origin marks and achievement badges are separate semantics
- future learning-focused app only if a distinct product job actually emerges
- Babel World is an optional hub hypothesis, never a dependency or global producer score
- Babel World's collection shape is intentionally open: gallery/trophy case/map/neighborhood/park/world should be earned by real content and relationships
- evolving **Fire** is both a truthful progress artifact and expressive collectible identity layer; bigger never means objectively better producer
- pixel-art Fire/badge language is a later visual hypothesis inspired by constrained, readable game-art qualities—not copied assets/styles
- ambient Fire glow on FIRE home is a later discovery/personality hypothesis, never required navigation or engagement pressure
- other Babel apps may contribute to the same production-skill evidence only when they genuinely demonstrate the same capability; app usage alone never grows Fire
- an app-specific River/other metaphor may represent that app's local journey while shared production evidence can still inform production growth
- monetization: **desire, not deprivation; pay to go deeper, not to be allowed to make music**
- account-level entitlements are preferred over hidden universal premium passwords/permanent friend builds
- lore/Easter eggs may reward curiosity but never hide required workflow/accessibility/privacy/account recovery/purchased functionality

Do **not** build Babel World, Fire/badges, accounts, cloud sync, monetization, social, lore, or a second app during the G7 shell correction or FIRE Core breadboarding.

## Reference registry

`REFERENCES.md` is the central inspiration/evidence registry. Current useful lenses include Apple, Logic, Ableton, Basecamp/Shape Up, Duolingo, Google/Material, Figma, GitHub/Primer, ChatGPT, Things, Procreate, Snapchat, Instagram/TikTok as observational interaction references, Pokémon GO collection/spatial patterns, xAPI/xAPI Profiles, Open Badges 3.0, Minecraft, and classic Pokémon-era pixel-art qualities.

Borrow principles, not branding/assets/templates. References never override product doctrine.

## Repository state

### Production — V6

- Root `/` remains V6.
- V6 uses `production-projects-v1` and schema 5.
- Preserve stable project/section/track/range/event IDs, migrations, timeline semantics, durable notes, browser persistence, and Map → Skeleton dependencies.
- V6 remains fallback until G7 is physically approved and deliberately promoted.

### Successor — G7

- Preview lives at `/v7-preview/`.
- G7 uses `production-projects-v1-v7-preview` and must never mutate V6 production data.
- Technical filenames/routes retain V7 wording for continuity; normal conversation says G7.

### Generation-spec retention

Keep only the **current production generation spec + active successor/preview spec** in the working tree by default. Git history is the archive for retired generations. Older specs remain only when a concrete maintenance/migration/compatibility/recovery reason still depends on them.

`V5.md` is intentionally removed from the working tree and remains recoverable from Git history.

## Current verified continuity — Shell Freeze was NOT approved

PR **#48 — Freeze the G7 shell system** merged to `main` at `20d5d26a652648083dc3695ea60e0889dc415eb8` and deployed successfully. Its automated 390 / 440 / 820 regression matrix passed.

Babel then performed physical iPhone review and **did not approve the shell freeze**. The structural direction was better, but the shell still felt ugly, text-heavy, inconsistent, and interactionally unpredictable.

Key physical-review evidence:

- no project-card management action existed on Projects; Edit required entering the project first
- Projects title / `+` alignment felt off
- `G7 · <commit>` under the Projects title polluted content hierarchy; Babel preferred the old quiet bottom-center review trace
- New Project exposed only Recreation even though Original and Recreation are both first-class FIRE project types
- title/text scale felt inconsistent screen-to-screen
- too many headers/subtitles/helper layers repeated information
- Project Home `Continue` + `Journey` labels felt like unnecessary taxonomy
- Structure repeated the same idea through title/subtitle/helper/button
- interaction behavior felt unpredictable: some choices were inline, others opened sheets, with no obvious semantic rule
- narrow-phone input/keyboard composition still looked rough enough to keep under review

**Therefore G7 is still unfrozen. Do not begin the FIRE Core breadboard until the shell simplification correction receives physical approval.**

## Active correction — G7 Shell Simplification + Interaction Grammar

Current working branch: **`sol/g7-shell-simplification`**. Check open PRs before doing new work; if this branch/PR is still open, continue it rather than starting another competing shell pass.

The correction is intentionally narrow. It does not add FIRE Core musical functionality.

### Core rules

- **Delete before styling.** If removing text does not make the next action harder to understand, remove it.
- **Inline = choose/toggle/classify/confirm/evaluate.**
- **Sheet = create/edit/manage a discrete thing.**
- **Navigation = enter another meaningful workspace.**
- **Menu/secondary affordance = utilities that should not compete with musical work.**
- Consistency comes from semantic meaning, not making every interaction use the same container.

### Implemented correction direction

**Projects**

- `Projects` remains root identity; `+` shares one stable header alignment.
- project cards now separate primary open behavior from a quiet per-card actions affordance
- Edit/Reset/Delete can be reached from Projects without entering the project first
- New Project explicitly exposes **Original** and **Recreation**
- Original creation requires a title; artist is optional
- Recreation requires song title + artist
- tiny `G7 · <commit>` moves back to quiet bottom-center fixed review trace, outside normal content hierarchy
- build trace is removed from project-management sheets

**Project Home**

- visible `Continue` heading removed
- visible `Journey` heading removed
- one current recommendation remains visually primary
- current task is not repeated below
- revisitable/upcoming work remains in one quiet grouped list
- one tiny `Later` label may remain because it communicates chronology
- saved Notes may appear as a utility row; empty Notes remains hidden
- Original Project Home exists truthfully even before its FIRE Core spine is built; it must not silently behave like Recreation

**Work headers/copy**

- nested work Back becomes icon-only with accessible label instead of printing project title above every work title
- Song Setup: title only
- Structure: title only
- Tracks: keeps one useful instruction, `Choose everything you hear.`
- Section Study / Review Map: title + quiet built-later state only
- Notes: title only
- one stable work-title size across work pages

**Structure**

- arrangement group exists from the empty state onward
- `Add Section` is always inside that same group
- no `Build the song one section at a time` + `Add the first section you hear` duplication
- Add/Edit Section uses a sheet because it creates/edits a section object
- verification becomes concise `Matches the song`
- Continue becomes a compact action after verification

**Tracks**

- common tracks stay direct inline multi-select
- custom `Other` opens an `Add Track` sheet because it creates a named custom object
- Continue becomes compact rather than a giant phone-width bar

**Sheets / keyboard**

- sheets are concise create/edit/manage surfaces, not hidden navigation pages
- sheet spacing/control sizing is reduced
- CSS scroll padding/margins help focused fields keep breathing room above software keyboard without reintroducing VisualViewport logic

### Physical approval checklist for this correction

After deploy, Babel should inspect the same iPhone path again:

1. Projects header: does `Projects` + `+` feel aligned/intended?
2. Build trace: is `G7 · <commit>` back where it belongs—quiet bottom-center, not part of content?
3. Project card: can Edit/Reset/Delete be reached naturally without opening the project?
4. New Project: are Original/Recreation both obvious without feeling like extra chrome?
5. Project Home: does removing Continue/Journey labels make the page easier rather than ambiguous?
6. Song Setup / Structure / Tracks: do titles feel like one system rather than changing personalities?
7. Structure: does Add Section feel predictable as object creation rather than a random modal?
8. Tracks: do normal choices feel direct while custom creation logically earns a sheet?
9. Primary actions: are they compact and intentional rather than giant bars?
10. Keyboard/input state: does the composition remain usable and less awkward?
11. Overall: **can Babel move through the shell without wondering what kind of UI is going to happen next?**

If approved, record approval and **stop broad shell polishing**. Then begin the FIRE Core breadboard.

## After shell approval

Sequence:

**physical G7 shell approval → FIRE Core breadboard → thin end-to-end FIRE Core spine → real-project validation**

Breadboard the whole Original + Recreation journey before deeply designing later phases. Use Shape Up-style places / affordances / connections.

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

After agreement, build the thinnest complete walking spine from start → finished release-ready audio, then validate on real music:

- Recreation: **Creep**
- Original: **Even**

Deepen only where real use proves need.

## Approval / execution contract

- Babel uses **“bet”** to mean **approved — execute now**.
- Approved FIRE work means **implement → test → fix → PR → green checks → merge → Pages deploy → verify → live G7 preview link**.
- Do not make Babel repeatedly say continue/merge/deploy/link.
- Standing permission exists to merge when checks are green, production-data safety is clear, and no genuine product decision remains unresolved.
- Stop only when tests fail, production-data safety is uncertain, destructive behavior is unresolved, or a genuine product decision is actually open.
- Never claim a change is live before merge + Pages verification.

## Automatic handoff + consistency

Babel should never need to request a handoff update or routine consistency sweep.

Any substantive product/runtime/durable-rule PR must:

1. update the correct authority/spec
2. sweep other active docs/implementation for stale contradictions
3. rewrite/remove/qualify superseded live rules
4. preserve historical material only when clearly scoped and still useful
5. refresh `START_HERE.md`
6. run handoff/doctrine guards

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
