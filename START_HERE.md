# Babel FIRE — Start Here

Use **Babel** as the project-facing name.

Read `BABEL_TRUTH.md` first, then the pinned Truth `START_HERE.md` / `AGENTS.md` / `FOUNDATIONS.md`. This file owns only the **current FIRE state and immediate next gate**.

## Current state

- Production remains **V6** at the root app. No production promotion has occurred.
- G7 remains isolated at `/v7-preview/` using `production-projects-v1-v7-preview`; it must never mutate V6 `production-projects-v1` data.
- **G7 SHELL IS FROZEN. 10 / 10 Locked.**
- The exact owning-product runtime that received final explicit Babel approval is `4a258c5170dd1d96dcbc0f2b0a9c35b283cec489` (PR #96).
- Current `Setup → Structure → Tracks` content remains disposable shell-fixture content, not FIRE Core architecture.
- The historical G7 Shell Test remains developer/certification infrastructure inside FIRE. It is not a second FIRE implementation, not Babel Lab, and not the living shared Shell Gallery.
- `FIRE_CORE.md` now owns the current FIRE Core operating model: **Target → Production Map → Active Focus → FIRE Loop → DAW → Evaluate/Update → Next Focus**, with Original and Recreation/Cover using one production engine.
- The current Production Map uses nine production domains as orientation/dependency, not a compulsory course. Domain state is evidence-based and reversible rather than permanent completion.
- Babel Truth ADR 0005 governs cross-app context/handoff. ADR 0006 permits bounded unproven FIRE interaction behavior to incubate in Lab without transferring FIRE ownership.
- **FIRE PR #99 is Draft seed material, not merge-ready runtime.** It contains the first coded Active Focus → DAW experiment → evaluation → changed-focus proof plus Creep/Even fixtures, but its interaction proof should be auditioned/reshaped in Lab before any promoted FIRE runtime implementation.

## Frozen shell baseline

The reusable shell grammar proven through the G7 certification cycle includes:

- stable toolbar/navigation/action row with title/meta composing below it
- roughly 44px interaction targets with quieter visible material where appropriate
- shared structural ownership split across `frame-primitives.css`, `shell-primitives.css`, and `state-primitives.css`
- symbol placement model: **geometry baseline → optional intrinsic symbol optical metric → container placement**
- familiar accessory semantics: `+` add/create, `•••` management, chevron navigation, drag handle reorder, canonical completion/current/upcoming marks
- parent-owned grouped/split-row pressed surfaces rather than competing child rectangles
- stable trailing value/control lanes
- adaptive temporary UI: compact bottom sheet, regular-width centered card, same semantics/action hierarchy
- sheet rhythm proven at 12px related disclosure spacing and 24px major/footer separation
- ordinary text fields preserve normal platform correction/spelling/predictive assistance; specialized input modes remain specialized
- one product logic across iPhone/iPad; presentation may adapt
- content-before-chrome, quiet-until-important, tactile-not-decorative composition

Genuinely transferable versions of these rules live in Babel Truth. FIRE-specific fixture workflow/copy and implementation code were not promoted.

## Core architecture now in force

`FIRE_CORE.md` is canonical for the product model. Important current rules include:

- **Original** may begin from nothing, a seed, demo, developed production, or near-finished record; FIRE orients to actual state rather than forcing restart.
- **Recreation / Cover** uses the external reference as a persistent overlay across production, not only a final comparison phase. Match / Interpret / Reimagine is a mutable overall bias; individual differences may be Match / Intentional / Explore.
- The Production Map is a finite set of domains, not a rigid staircase or percentage-completion system.
- A domain can be not-yet-relevant, active, **provisionally stable under current evidence**, or reopened by new evidence.
- **Prevent what can reasonably be prevented now. Commit when there is enough evidence. Reopen only when new evidence earns it.** Reopening is not an excuse for FIRE missing a problem it could reasonably have caught earlier.
- **Active Focus** chooses what deserves attention now using leverage, dependency, target relevance, uncertainty, reversibility/cost, constraints, history, and finish risk rather than blindly advancing to a next stage.
- FIRE should be information-rich underneath and information-light for the musician. Questions exist only to obtain evidence that materially changes the next useful recommendation or prevents a bad one; a small DAW experiment may be better than asking.
- Reporting/perception/intention/state questions never randomize. Playful choice belongs only after FIRE has narrowed the space to genuinely viable action alternatives.
- FIRE retains production meaning the DAW does not already understand well rather than requiring the entire Logic session to be mirrored.
- Fire visualization remains a hypothesis; do not use generic XP/percent-complete. Current semantic candidate is where the record has unresolved **heat/attention**.

## Immediate next gate — bounded FIRE Core audition in Lab

Do **not** begin another architecture pass by default and do **not** merge PR #99 as-is.

The next deliberate FIRE step is:

1. Work under `BabeDrums/babel-lab/fire/core/**`, which is the explicitly non-canonical FIRE Core incubation lane.
2. Use Draft PR #99 as seed evidence/code, not authority and not production code.
3. Build only the thin interaction contract already defined by FIRE doctrine:
   **Active Focus → concise why → one useful Logic/DAW experiment → return with result → preserve evidence/decision → update domain/project state → changed next Active Focus.**
4. Use fake/local isolated Lab state only. Never read/write FIRE production or G7 storage from the Lab specimen.
5. Exercise the same spine with the current proof pair: a Recreation/reference case (`Creep` is current seed) and the Original `Even`, reusing already-known artist-authored context rather than re-asking it.
6. Physically use the specimen on iPhone first, then regular width as useful. Judge whether it feels production-useful and information-light—not whether the prototype looks complete.
7. Reshape/delete freely in Lab until the behavior earns promotion.
8. Only after the interaction survives, deliberately implement/reconcile the surviving behavior back into `babel-fire` against real FIRE navigation/state/data. Prototype code is not automatically promoted code.

FIRE remains independently usable. A user who only wants to make a song should be able to do exactly that without World setup, artist profiling, career planning, or ecosystem prompts getting in the way.

## Parallel-lane boundary

FIRE and WORLD work may proceed in parallel, but ownership is strict:

- FIRE doctrine/canonical behavior/runtime/data/promoted implementation → `babel-fire`
- FIRE Core experimental interaction → `babel-lab/fire/core/**`
- Fire visualization experiment → `babel-lab/fire/visualization/**`
- WORLD experimental product logic → its owned Lab paths
- generic shared UI candidate work → Lab Shell Gallery / shared-shell lane

Before touching shared Lab surfaces such as root navigation, `shared/**`, `shell/**`, Truth adoption pointers, or cross-cutting CI/tests, reconcile current Lab `main` and open PRs first. Do not let a FIRE pass silently rewrite WORLD logic or shared shell work.

## Stable boundaries

- public project types remain Original / Cover; canonical doctrine calls the second workflow Recreation
- history-aware Back retraces actual in-app path with a safe fallback for direct entry
- `+` = add/create the primary discrete object for the current view
- `•••` = management/actions
- arrangement metadata belongs in content hierarchy; reorder owns its far-right affordance
- Complete = canonical check; Current = stronger short bar; Incomplete/upcoming = quieter short bar
- Current does not tint the whole row
- one product logic across iPhone/iPad; presentation may adapt
- V6 runtime/data/schema remain untouched unless a separate approved V6 change requires otherwise

New durable unresolved FIRE findings go to Babel Truth Issue #1 under the shared persist-before-reply rule.
