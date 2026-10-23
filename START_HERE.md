# Babel FIRE

- **Repository:** `BabeDrums/babel-fire`
- **Production branch:** `main`
- **Live production app:** https://babedrums.github.io/babel-fire/
- **Live G7/V7 preview:** https://babedrums.github.io/babel-fire/v7-preview/
- **Cross-generation product doctrine:** [FIRE_CORE.md](FIRE_CORE.md)
- **Future Babel platform hypotheses:** [BABEL_PLATFORM.md](BABEL_PLATFORM.md)
- **External references / inspiration:** [REFERENCES.md](REFERENCES.md)
- **Active production specification:** [V6.md](V6.md)
- **Experimental next-shell direction:** [V7_DRAFT.md](V7_DRAFT.md)

When a new ChatGPT conversation begins with or clearly refers to **Babel FIRE**, resume this project immediately. Do not ask Gabriel to reconstruct documented FIRE decisions.

## Read in this order

1. `START_HERE.md`
2. `AGENTS.md`
3. `FIRE_CORE.md` for current cross-generation product doctrine
4. `BABEL_PLATFORM.md` only when the task involves future accounts/sync, cross-app ecosystem, monetization/entitlements, the deeper learning/practice surface, the user’s Fire, badges/collections, social sharing, or lore/Easter eggs
5. `REFERENCES.md` when doing product/design research or comparing external systems; references are inspiration/evidence, never authority
6. `V6.md` for shipped production-generation requirements
7. `V7_DRAFT.md` for the redesign shell
8. `CONTEXT.md` for supporting history/detail not superseded above
9. Current `main`, open PRs, relevant branches, and tests
10. `CHANGELOG.md` for shipped milestones

Always distinguish shipped production work from experimental V7 preview work.

## Naming shorthand

Use **G7** in normal product conversation for the current seventh FIRE implementation/shell generation. Keep existing technical identifiers (`V7_DRAFT.md`, `/v7-preview/`, `production-projects-v1-v7-preview`) unchanged unless there is a separate migration reason; renaming stable routes/storage/docs solely for wording would add risk without product value.

Use **FIRE Core** for the first complete functional product spine. Do not introduce an `M1` label merely to create another taxonomy; FIRE Core already communicates the milestone. **FIRE 1.0** remains the future release-quality milestone after Core has been validated and refined.

## FIRE Core product doctrine

`FIRE_CORE.md` is the canonical current product doctrine. Key direction:

- FIRE is a **production companion that teaches through use**, not a mandatory learning course.
- Original and Recreation are both first-class project types. Recreation must work standalone for someone who only wants to make a cover quickly.
- Learning is ambient and adaptive: concise action by default, optional `Why?` / deeper help, domain-specific growth, and `I don't know` as a valid path.
- Recreation can **Match, Interpret, or Reimagine** a reference; individual differences can be matched, intentional, or explored.
- One shared FIRE reasoning engine serves both modes: **Feel → Identify → Reason → Experiment → Evaluate**.
- Historical V6/V7 rules remain useful generation-specific evidence but cannot override current FIRE Core doctrine.
- Future accounts/sync, Babel app harmony, monetization/entitlements, the deeper Practice/Skills surface, the user’s Fire, badges/collections, social sharing, and lore/Easter eggs are preserved as **future hypotheses** in `BABEL_PLATFORM.md`; they do not expand current Shell/Core implementation scope.
- Cross-app learning follows **shared evidence, local identity**: overlapping production skills should eventually use a shared versioned Babel Learning Contract and familiar progress/learning primitives, while app-specific journeys/metaphors stay distinct. A future Babel World is only a hub hypothesis and must never become a dependency or global skill score.
- Learning architecture is **evidence first, interpretation second**: preserve meaningful evidence/provenance/context and derive current skill state from it rather than storing only an unexplained score.
- Source/origin marks and achievement badges are separate semantics. Pixel-art Fire/badge language is a later visual hypothesis, not current shell scope.

## Current verified continuity — October 22, 2026

PR #44, **Finalize G7 preflight and Babel badge/evidence doctrine**, is merged at `0bce359…`. Its PR gate passed handoff/doctrine, static checks, and Chromium 390px / 440px / 820px. It reconciled the latest badge/evidence/pixel-Fire hypotheses into authoritative future-platform doctrine, expanded the reference registry, adopted human shorthand `G7`, and refreshed this handoff without changing runtime behavior, storage, schema, or user data.

PR #43, **Add FIRE reference registry**, is merged at `7113d14…`; it created `REFERENCES.md`. PR #42 established shared evidence/local identity, the Babel Learning Contract hypothesis, Babel World as an optional hub, and ambient Fire discovery. PR #41 remains the broader future-platform/monetization/learning-Fire milestone; PR #40 remains the FIRE Core doctrine milestone; PR #39 remains the latest physical iPhone runtime review.

The G7/V7 shell is consolidated: New Project, the persistent `+`, quiet zero state, build metadata, and creation sheet live directly in the V7 renderer/styles. `new-project.js`, MutationObserver visual patching, and runtime CSS injection are gone.

The current active direction is **G7 Shell Freeze → FIRE Core breadboard → thin end-to-end FIRE Core spine → real-project validation**.

The next pass is the final deliberate generic shell/system cleanup for a while. It should make headers, typography, spacing/rhythm, grouping, states, sheets, natural scrolling, density, and adaptive presentation consistent enough that those fundamentals stop being re-litigated route by route. After physical approval, move away from shell polishing and breadboard the complete Original + Recreation product journeys before deeply designing later phases.

## Production state — V6

- Root `/` remains V6 on schema 5 using `production-projects-v1`.
- Preserve stable project/section/track/range/event IDs, migrations, timeline semantics, durable notes, browser persistence, and Map → Skeleton dependencies.
- V6 remains the production fallback until G7/V7 is physically approved and deliberately promoted.
- Do not use V6 screenshots as the redesign target merely because production is visible there.

## G7 / V7 architecture — settled at the shell level

The isolated preview lives at `/v7-preview/` and uses `production-projects-v1-v7-preview`. It must never mutate V6 production data.

The core question is:

> Can FIRE get the musician into useful musical work without making them think about FIRE's organization?

The settled shell architecture is:

**Projects → Project Home → direct musical work**

Project Home contains:

- **Continue** — one recommended next destination
- **Journey** — orientation, direct access, and revisiting
- **Notes** — project thinking at the architecture level; do not let a dead/empty Notes destination compete for attention before it has a useful action

G7 does **not** carry forward:

- the center context navigator
- a separate Roadmap destination
- a required The Map intermediary menu
- Step 1 of 3 workflow chrome
- broad `Locked` status rows
- completion percentages everywhere

**The Map is a phase/grouping inside Journey, not a screen the musician must enter to reach Structure, Tracks, or Section Study.**

Rule: **guided forward, flexible backward.** Completed work stays revisitable. Upcoming work stays understandable. Hard-block only when a task literally cannot operate without missing context.

## Current G7 fundamentals direction

Projects:

- one job: open or create a project
- persistent `+` is the single create affordance
- zero state is only `No projects yet.`
- no duplicate giant New Project CTA
- during G7 preview/physical review, keep a **tiny, quiet, preview-only `G7 · <commit>` identifier** on the main Projects/home surface so Gabriel can confirm he is looking at the newly deployed build even when a pass is mostly underground; it must remain subordinate and should not read like product chrome or a prototype banner
- the Projects subtitle is intentionally removed because it did not add useful context

Project Home:

- project identity + project actions
- Continue + Journey + Notes at the architecture level, while Shell Freeze may reduce/hide dead or duplicated presentation
- restrained Journey state treatment only; exact signature styling remains experimental
- current work is visually distinct without another status label
- completed work is still tappable
- future phases remain visible but quiet

Work pages:

- default heuristic is **title → minimum useful instruction → actual musical task → continuation when it becomes useful**
- do not show premature disabled continuation controls just to explain the workflow
- Song Setup is dedicated
- Structure edits the arrangement directly
- Tracks keeps direct multi-select
- Section Study and Review Map specialized editors remain deferred

Visual semantics:

- **selection** uses restrained selected surfaces, not completion marks
- **completion** uses ring/check language
- **status/value** uses text when text is the information itself; Reference is a completion requirement (“Import the reference into your session”) and uses ring/check feedback without asking FIRE to own the media
- **navigation** uses rows/chevrons
- **primary progression** gets the strongest compact button treatment
- do not stack two indicators for one state

Viewport:

- document height determines whether a page scrolls naturally
- never toggle root `overflow` from `VisualViewport` measurements while Safari chrome is moving
- short pages remain naturally short; tall pages receive modest CSS-only Safari end clearance
- modal sheets may temporarily lock body scrolling while open, but page scrollability itself is never runtime-switched

## What is locked vs still experimental

### Locked / current direction

- Project Home = Continue + Journey + Notes at the architecture level; exact density/presentation is still part of Shell Freeze
- no center navigator in G7
- no separate Roadmap in G7
- The Map is a Journey grouping, not a required intermediary
- Song Setup is a dedicated page
- Structure and Tracks are directly revisitable
- persistent `+` is the Projects create affordance
- quiet Projects empty state
- natural CSS document scrolling with no VisualViewport-driven root lock
- V7 sandbox isolation
- core preview UI should render directly from `app.js` / `styles.css`, not through visual MutationObserver overlays

### Testing

- grayscale interaction-fidelity refinements: material contrast, primary-action weight, field focus, Reference completion semantics, and compact-vs-regular composition
- exact Journey signature treatment beyond the restrained semantic hierarchy
- exact future FIRE/signal-path personality treatment
- shell spacing/density refinements after physical review
- how much explanatory copy dense migrated editors will need

### Parking lot / later experiment

- fully stylized Babel/FIRE signal-path Journey
- stronger music-native signature identity
- signature animation/interactions
- app-level Projects/Notes navigation
- meaningful optional learning/progression experiments — including a targeted Practice/Skills surface and the user’s evolving Fire; reject fake mastery, mandatory XP/streak pressure, and default global leaderboards
- pixel-art Fire / badge language, ambient Fire glow, Babel World collections, source marks, and achievement badge presentation

Duolingo is a **logic reference**, not a visual target: one obvious next action, ordered progression, visible movement, completed work remains accessible. Do not import XP, streaks, cartoon lesson paths, fake percentages, or hard locks everywhere.

## Page necessity + design process

For every substantive pass, automatically use the lightweight FIRE loop:

**Discover → Define → Develop → Deliver → Verify + consolidate**

Before polishing a page ask:

1. What is this page's one job?
2. What does the musician need here?
3. What is duplicated elsewhere?
4. What can be hidden, moved, or deleted?
5. Does the page itself need to exist?

Subtraction comes before addition, but subtraction must never remove the only path to a core action.

Gabriel's brainstormed ideas are hypotheses unless explicitly locked. Use product judgment. Fundamentals come before signature personality.

Target feeling remains roughly **70% calm Apple-like app hierarchy / 30% focused creative-tool density**: calm shell, density where the musical task genuinely requires it, then calm shell again.

## Gabriel's approval / execution contract

- Gabriel uses **“bet”** to mean **approved — go execute it now**.
- Approved FIRE work means **implement → test → fix → PR → green checks → merge → Pages deploy → verify → live G7/V7 preview link**.
- Do not make Gabriel repeatedly say “continue,” “merge it,” “deploy it,” or “give me the link.”
- Standing permission exists to merge FIRE PRs when checks are green, production-data safety is clear, and no genuine product decision remains unresolved.
- Stop instead when tests fail, production data safety is uncertain, destructive behavior is unresolved, or a genuine product decision remains open.
- Never claim a change is live until merge and Pages deployment are verified.

## Deferred scope

Do not lose track of:

- full V7 Section Study timeline/editor
- full Review Map workspace
- Skeleton interiors
- The Sounds
- The Balance
- The Shape
- The World
- The Finish
- true cross-project Notes destination
- final production-shell replacement
- FIRE/Babel signature visual experiment
- optional Practice/Growth system, Fire, badges, and cross-app platform work

These are intentionally deferred until the shell/fundamentals pass is physically approved and FIRE Core is breadboarded.

## Automatic handoff + consistency rule

Gabriel should never need to request a handoff update or a routine consistency sweep.

Product/runtime or durable-rule PRs that materially change `app.js`, `styles.css`, `index.html`, V7 preview runtime, or durable product rules must refresh this file. `scripts/check_handoff.py` and CI enforce handoff freshness.

For every substantive FIRE pass, also perform a semantic consistency sweep across current doctrine, active generation docs, future platform hypotheses, reference wiring, handoff state, and implementation. Fix clear stale/duplicate contradictions automatically. CI protects known settled markers through `scripts/check_product_doctrine.py`; genuine ambiguous product conflicts still require authority-order/product judgment rather than blind rewriting.

## Operating workflow

- **No Codex for FIRE.** Use direct GitHub/repository tools.
- Fresh `main` → task branch → implementation → tests → PR → merge when safe/green → Pages deploy → verify live → physical-device review.
- It is acceptable to ship isolated `/v7-preview/` iterations while root V6 remains unchanged.

## Next physical-review gate — G7 Shell Freeze

Review the deployed V7 preview, not root V6:

https://babedrums.github.io/babel-fire/v7-preview/

The Shell Freeze pass should be **visibly cleaner but not a dramatic redesign**. Review in this order:

1. Projects — preserve the already-good simple create/open surface; avoid unnecessary churn; verify the tiny preview-only `G7 · <commit>` identifier matches the newly deployed build
2. Project Home — reduce duplicated/current-work density; one obvious continuation path, quieter Journey, cleaner future-phase presentation, and no dead destination competing for attention
3. Song Setup — compact, consistent work-page header/rhythm; Reference remains a clear ring/check setup requirement with no media-ownership implication
4. Structure — arrangement first; verification integrated/quieter rather than floating as a competing card
5. Tracks — denser direct selection where useful; consistent header/action spacing
6. Section Study / Review Map placeholders — truthful and visually quiet
7. Shared shell system — consistent header archetypes, typography, section/group spacing, row rhythm, states, action placement, safe-area behavior, sheets, and natural scrolling across compact/wide layouts

Specifically test short-page scrolling, tall-page Safari clearance, spacing/density, direct revisiting, Back behavior, core action discoverability, and that one adaptive interface preserves identical product logic across compact and wide layouts.

Do **not** add the Fire glow, pixel art, badge collection, signature signal-path treatment, learning hub, accounts, or new FIRE Core phase functionality during Shell Freeze.

After Shell Freeze is physically approved, expect the **FIRE Core breadboard** to be primarily product-logic/documentation work with little or no visible runtime change. It should define places, actions, connections, decisions, evidence, and carry-forward context for Original + Recreation end to end. After the breadboard is agreed, build the **thin end-to-end FIRE Core spine** so the whole journey works in plain form before deepening individual phases.

Do not promote the stylized signal-path concept until this restrained shell passes physical review.

`V5.md` is historical. `V6.md` remains production truth until G7/V7 is physically approved and formally promoted.
