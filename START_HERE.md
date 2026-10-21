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

Latest physical iPhone review said the V7 direction is **definitely getting better**. The architecture is approved enough to keep iterating in the preview, but **not yet approved to replace production**.

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

## Latest physical-review feedback to carry forward

The comparison screenshots confirmed:

- The V7 hierarchy is easier than V6.
- Projects still had too much empty space at the top and should feel more like a grouped list than a large card layout.
- Project Home should become even less dashboard-like: one quiet Continue destination, then Journey.
- Avoid extra status words such as Recommended / In progress / Later when hierarchy already communicates the state.
- Dedicated Song Setup is the right direction.
- Structure should make the arrangement itself the main interface; adding a common section should be immediate and editing happens afterward.
- Tracks is one of the strongest existing interactions; preserve the grid while simplifying its surrounding chrome and copy.
- Do not add app-level tabs yet.

## Current preview scope

The preview currently covers:

- Projects
- Project Home
- Song Setup
- simplified Structure
- Tracks
- Section Study prerequisite/handoff
- Review Map placeholder
- project Notes view

Full Section Study timeline, full Review Map, Skeleton interiors, and production-shell replacement stay deferred until the shell passes another physical iPhone review.

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

Continue tightening the isolated V7 preview on iPhone Safari. Judge whether Projects, Project Home, Song Setup, Structure, and Tracks feel calm and obvious. Do **not** migrate the specialized editors or replace V6 until that shell passes the physical gate.

Fallback continuation phrase:

> Babel FIRE — continue from GitHub repo BabeDrums/babel-fire. Read START_HERE.md and resume from the latest verified state.

`V5.md` is historical. `V6.md` remains production truth until V7 is physically approved and formally promoted.
