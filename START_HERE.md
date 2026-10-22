# Babel FIRE

- **Repository:** `BabeDrums/babel-fire`
- **Production branch:** `main`
- **Live production app:** https://babedrums.github.io/babel-fire/
- **Live V7 preview:** https://babedrums.github.io/babel-fire/v7-preview/
- **Cross-generation product doctrine:** [FIRE_CORE.md](FIRE_CORE.md)
- **Active production specification:** [V6.md](V6.md)
- **Experimental next-shell direction:** [V7_DRAFT.md](V7_DRAFT.md)

When a new ChatGPT conversation begins with or clearly refers to **Babel FIRE**, resume this project immediately. Do not ask Gabriel to reconstruct documented FIRE decisions.

## Read in this order

1. `START_HERE.md`
2. `AGENTS.md`
3. `FIRE_CORE.md` for current cross-generation product doctrine
4. `V6.md` for shipped production-generation requirements
5. `V7_DRAFT.md` for the redesign shell
6. `CONTEXT.md` for supporting history/detail not superseded above
7. Current `main`, open PRs, relevant branches, and tests
8. `CHANGELOG.md` for shipped milestones

Always distinguish shipped production work from experimental V7 preview work.

## FIRE Core product doctrine

`FIRE_CORE.md` is the canonical current product doctrine. Key direction:

- FIRE is a **production companion that teaches through use**, not a mandatory learning course.
- Original and Recreation are both first-class project types. Recreation must work standalone for someone who only wants to make a cover quickly.
- Learning is ambient and adaptive: concise action by default, optional `Why?` / deeper help, domain-specific growth, and `I don't know` as a valid path.
- Recreation can **Match, Interpret, or Reimagine** a reference; individual differences can be matched, intentional, or explored.
- One shared FIRE reasoning engine serves both modes: **Feel → Identify → Reason → Experiment → Evaluate**.
- Historical V6/V7 rules remain useful generation-specific evidence but cannot override current FIRE Core doctrine.


## Current verified continuity — October 22, 2026

PR #39, **Stabilize V7 Safari scrolling and setup semantics**, is merged and deployed at `d459a4f…`; its exact post-merge regression matrix passed at 390px, 440px, and 820px, Pages deployment #64 succeeded on the same SHA, and physical iPhone Safari review confirmed the scrolling behavior is improved. PR #38 remains the preceding grayscale interaction-fidelity milestone.

The earlier PR #34 browser-run hang was infrastructure-only; the merged code passed on `main`. Browser jobs now have a 15-minute timeout so a stuck runner becomes an explicit failure instead of waiting indefinitely.

The V7 shell is now consolidated: New Project, the persistent `+`, quiet zero state, build stamp, and creation sheet live directly in the V7 renderer/styles. `new-project.js`, MutationObserver visual patching, and runtime CSS injection are gone.

The current direction is **V7 Shell Freeze + FIRE Core shaping**: perform one deliberate declutter/system pass so headers, typography, spacing/rhythm, grouping, states, sheets, natural scrolling, and adaptive presentation stop being re-litigated route by route; then breadboard the complete FIRE Core Original + Recreation journeys before deeply designing later phases.

## Production state — V6

- Root `/` remains V6 on schema 5 using `production-projects-v1`.
- Preserve stable project/section/track/range/event IDs, migrations, timeline semantics, durable notes, browser persistence, and Map → Skeleton dependencies.
- V6 remains the production fallback until V7 is physically approved and deliberately promoted.
- Do not use V6 screenshots as the redesign target merely because production is visible there.

## V7 architecture — settled at the shell level

The isolated preview lives at `/v7-preview/` and uses `production-projects-v1-v7-preview`. It must never mutate V6 production data.

The core question is:

> Can FIRE get the musician into useful musical work without making them think about FIRE's organization?

The settled shell architecture is:

**Projects → Project Home → direct musical work**

Project Home contains:

- **Continue** — one recommended next destination
- **Journey** — orientation, direct access, and revisiting
- **Notes** — project thinking

V7 does **not** carry forward:

- the center context navigator
- a separate Roadmap destination
- a required The Map intermediary menu
- Step 1 of 3 workflow chrome
- broad `Locked` status rows
- completion percentages everywhere

**The Map is a phase/grouping inside Journey, not a screen the musician must enter to reach Structure, Tracks, or Section Study.**

Rule: **guided forward, flexible backward.** Completed work stays revisitable. Upcoming work stays understandable. Hard-block only when a task literally cannot operate without missing context.

## Current V7 fundamentals direction

Projects:

- one job: open or create a project
- persistent `+` is the single create affordance
- zero state is only `No projects yet.`
- no duplicate giant New Project CTA
- preview build/commit traceability stays available in subordinate project actions/debug UI rather than occupying the main Projects canvas
- the Projects subtitle is intentionally removed in the consolidation pass because it did not add useful context

Project Home:

- project identity + project actions
- Continue + Journey + Notes
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

- Project Home = Continue + Journey + Notes
- no center navigator in V7
- no separate Roadmap in V7
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
- game-like progression mechanics (likely reject most literal forms)

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
- Approved FIRE work means **implement → test → fix → PR → green checks → merge → Pages deploy → verify → live V7 link**.
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

These are intentionally deferred until the shell/fundamentals pass is physically approved.

## Automatic handoff rule

Gabriel should never need to request a handoff update.

Product/runtime or durable-rule PRs that materially change `app.js`, `styles.css`, `index.html`, V7 preview runtime, or durable product rules must refresh this file. `scripts/check_handoff.py` and CI enforce handoff freshness.

## Operating workflow

- **No Codex for FIRE.** Use direct GitHub/repository tools.
- Fresh `main` → task branch → implementation → tests → PR → merge when safe/green → Pages deploy → verify live → physical-device review.
- It is acceptable to ship isolated `/v7-preview/` iterations while root V6 remains unchanged.

## Next physical-review gate

Review the deployed V7 preview, not root V6:

https://babedrums.github.io/babel-fire/v7-preview/

Review in this order:

1. Projects — `+`, one create path, quiet empty state, no visible prototype stamp, no needless subtitle
2. Project Home — Continue hierarchy, restrained Journey, completed/current/upcoming clarity, future-phase density, Notes
3. Song Setup — Reference as a clear ring/check setup requirement with no file picker, filename, Replace/Remove sheet, or media ownership implication
4. Structure — arrangement first, verification quieter than musical content, continuation only when useful
5. Tracks — direct selection and clear separation of custom entry vs continuation
6. Section Study / Review Map placeholders — truthful, concise, no fake completion

Specifically test short-page scrolling, tall-page Safari clearance, spacing/density, direct revisiting, Back behavior, core action discoverability, and that one adaptive interface preserves identical product logic across compact and wide layouts.

Do not promote the stylized signal-path concept until this restrained shell passes physical review.

`V5.md` is historical. `V6.md` remains production truth until V7 is physically approved and formally promoted.
