# Babel FIRE

- **Repository:** `BabeDrums/babel-fire`
- **Production branch:** `main`
- **Live production app:** https://babedrums.github.io/babel-fire/
- **Live V7 preview:** https://babedrums.github.io/babel-fire/v7-preview/
- **Active production specification:** [V6.md](V6.md)
- **Experimental next-shell direction:** [V7_DRAFT.md](V7_DRAFT.md)

When a new ChatGPT conversation begins with or clearly refers to **Babel FIRE**, resume this project immediately. Do not ask the user to reconstruct documented FIRE decisions.

## Read in this order

1. `START_HERE.md`
2. `AGENTS.md`
3. `V6.md` for current production requirements
4. `V7_DRAFT.md` for the redesign preview
5. `CONTEXT.md`
6. Current `main`, open PRs, relevant branches, and tests
7. `CHANGELOG.md` for shipped milestones

Always distinguish shipped production work from experimental V7 preview work.

## Current production state — V6

- Root `/` remains V6 on schema 5 using `production-projects-v1`.
- Preserve stable project/section/track/range/event IDs, migrations, timeline semantics, durable notes, browser persistence, and Map → Skeleton dependencies.
- V6 still contains the Phase/Step shell and center context navigator. Physical review rejected that shell as the direction to keep polishing.
- Project actions are Edit Project / Reset Progress / Delete Project.
- Song Setup no longer collapses.
- Backup/Restore is not part of the active product.

## Current redesign state — V7 preview

The V7 preview is intentionally isolated at `/v7-preview/` and uses `production-projects-v1-v7-preview`.

Latest physical iPhone review moved V7 into a **fundamentals polish gate**. The shell direction is promising, but **not yet approved to replace production**.

The redesign question remains:

> Can FIRE get the musician into useful musical work without making them think about FIRE's organization?

Current V7 direction:

- Project Home is the hub: **Continue + Journey + Notes**.
- Separate Roadmap is removed from the redesign direction.
- No center context navigator.
- Song Setup is its own focused page.
- Structure is direct arrangement editing with quick Add Section.
- Tracks keeps direct multi-select and loses workflow/status chrome.
- Strong guidance, minimal gating.
- Work screens return directly to Project Home.
- Notes will become a true cross-project destination before Projects/Notes top-level navigation is introduced.
- **Core actions must survive subtraction.** Physical review caught that Projects had lost its only New Project path. V7 keeps a persistent Projects `+` as the single creation affordance; the empty state stays quiet instead of duplicating that action. Project creation remains sandbox-only and must never mutate V6 production data.
- During preview review, Projects shows a subtle automatic `FIRE V7 PREVIEW · <commit>` build stamp so physical screenshots can be tied to the deployed revision.

## Latest physical-review feedback to carry forward

The current shell is meaningfully better and Project Home is starting to feel like a real home page.

Next concerns:

- The current fundamentals pass replaces blanket preview scroll padding with **content-aware visual-viewport fitting**: short phone pages should lock naturally while genuinely tall pages receive Safari end clearance.
- The Page Necessity Audit is being applied route by route: redundant bottom “Back to Project” controls and duplicated completion wording are removed instead of restyled.
- Shared spacing, heading offsets, row density, action placement, and placeholder presentation are being normalized before more editors migrate.
- Subtraction is not allowed to remove a core route or primary task. Verify create/open/edit/reset/delete/navigation affordances after every declutter pass.
- Do not duplicate a core action merely to make it more obvious when one clear, persistent affordance is sufficient.
- Fundamentals come before personality. Do not add decorative brand behavior until page purpose, navigation, scrolling, spacing, and consistency are stable.
- A future Babel/FIRE signature is desirable but not yet approved. One promising exploration is a subtle music-native progress path / signal-path treatment in Project Home Journey, inspired by the useful part of path-based products like Duolingo: visible forward movement and one obvious next action. Do not copy game mechanics, fake percentages, XP, or lesson-board visuals literally.

## Default FIRE iteration behavior

The user does **not** want to repeatedly request research, project review, cleanup, or handoff maintenance.

For nontrivial FIRE design/product passes, automatically:

- review the latest physical feedback and current repo state,
- research relevant current platform/product references when they can improve the decision,
- define the root problem before changing UI,
- treat user suggestions as hypotheses unless explicitly locked,
- perform the Page Necessity Audit from `AGENTS.md`,
- prototype the smallest coherent solution,
- run relevant tests,
- remove superseded UI/code,
- update project documentation and this handoff when durable/current direction changes.

The lightweight FIRE loop is **Discover → Define → Develop → Deliver → Verify + consolidate**. It is a guardrail against solving the wrong problem, not a rigid bureaucracy.

## Current preview scope

The preview currently covers:

- Projects, including sandbox New Project creation from the persistent `+`
- Project Home
- Song Setup
- simplified Structure
- Tracks
- Section Study prerequisite/handoff
- Review Map placeholder
- project Notes view

Full Section Study timeline, full Review Map, Skeleton interiors, and production-shell replacement stay deferred until the shell passes the declutter/polish physical gate.

## Automatic handoff rule

The user should **never need to ask for a handoff update again**.

- `START_HERE.md` is the canonical zero-context continuation file.
- Product/runtime or durable-rule PRs that change `app.js`, `styles.css`, `index.html`, `V6.md`, `V7_DRAFT.md`, `CONTEXT.md`, `AGENTS.md`, or `v7-preview/` must refresh this file when the current handoff materially changes.
- `scripts/check_handoff.py` and CI enforce handoff freshness for relevant changes.
- A new chat pointed at `BabeDrums/babel-fire` should read `README.md` → `START_HERE.md` and continue without requesting a long context prompt.

## Operating workflow

- **No Codex for FIRE.** Use normal GitHub connector/direct repository tools.
- Work on a task branch → review diff → run static/browser regressions → PR → merge only when checks are green and data safety is clear → verify Pages → physical-device review.
- It is acceptable to ship isolated `/v7-preview/` iterations while leaving the root V6 app unchanged.
- Stop instead of merging when tests fail, production data safety is uncertain, destructive behavior is unresolved, or a genuine product decision remains open.

## Next action

Complete and physically review the V7 fundamentals polish pass before migrating more editors:

1. verify the persistent Projects `+` is sufficient and the quiet zero-project state no longer competes with it,
2. verify the V7 build stamp correctly identifies the deployed commit during physical review,
3. verify short pages no longer fake-scroll on physical iPhone Safari and genuinely tall pages still clear browser chrome,
4. review the route-by-route subtraction and shared spacing/density polish,
5. fix any physical-only issues without expanding scope,
6. only after the fundamentals gate passes, consider a separate Babel signature/progress-path experiment.

Fallback continuation phrase:

> Babel FIRE — continue from GitHub repo BabeDrums/babel-fire. Read START_HERE.md and resume from the latest verified state.

`V5.md` is historical. `V6.md` remains production truth until V7 is physically approved and formally promoted.
