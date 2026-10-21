# Babel FIRE

- **Repository:** `BabeDrums/babel-fire`
- **Production branch:** `main`
- **Live production app:** https://babedrums.github.io/babel-fire/
- **Active production specification:** [V6.md](V6.md)
- **Experimental next-shell direction:** [V7_DRAFT.md](V7_DRAFT.md)

When a new ChatGPT conversation begins with or clearly refers to **Babel FIRE**, resume this project immediately. Do not ask the user to reconstruct documented FIRE decisions.

## Read in this order

1. `START_HERE.md`
2. [AGENTS.md](AGENTS.md)
3. [V6.md](V6.md) for current production requirements
4. [V7_DRAFT.md](V7_DRAFT.md) when working on the guided-workspace redesign
5. [CONTEXT.md](CONTEXT.md)
6. Current `main`, open PRs, relevant branches, and tests
7. [CHANGELOG.md](CHANGELOG.md) for shipped milestones

Always distinguish shipped work on `main`, experimental preview work, and planned work. `README.md` is the zero-context pointer into this handoff; it intentionally does not duplicate the product specification.

## Current production state — V6

- Production remains schema 5 on `production-projects-v1`; preserve stable project/section/track/range/event IDs, migrations, continuous timeline semantics, durable notes, browser persistence, and Map → Skeleton invalidation/dependencies.
- The root app currently ships the V6 Project → Phase → Step shell, including the center context navigator and Phase Home Step lists.
- Project actions are Edit Project / Reset Progress / Delete Project. Reset preserves identity/details/creation date/durable notes while clearing workflow progress.
- Song Setup no longer collapses. Reference, Tempo, Meter, Grid, and First Listen remain editable in one grouped surface.
- Dormant Backup/Restore is removed from the active product.
- Notes are moving toward one canonical cross-project knowledge layer; the full global Notes hub is not shipped yet.

## Latest physical-device finding — important

The most recent physical iPhone Safari review **did not approve the V6 Steps + center-context-navigation shell** as the direction to continue polishing.

The user reported that the new center navigator is glitchy/visually heavy, the app still feels like too much hierarchy, and the overall experience does not feel meaningfully easier. The correct response is **not** another route-by-route cosmetic pass on that shell.

The redesign question is now:

> Can FIRE get the musician into useful musical work without making them think about FIRE's organization?

## Experimental V7 guided-workspace direction

`V7_DRAFT.md` captures the current redesign hypothesis. It is intentionally a draft until physically approved.

Core direction:

- **Project Home becomes the hub**: identity + one recommended **Continue** surface + the whole project **Journey** + project-scoped Notes entry.
- **Roadmap is folded into Project Home** instead of being a separate duplicate hierarchy screen.
- **No center context navigator** in the redesign.
- Work screens push directly from Project Home and return directly to Project Home. Avoid mandatory Phase Home screens.
- For The Map, named work is **Song Setup → Structure → Tracks → Section Study → Review Map**. Do not force `Step` or `Checkpoint` terminology into the UI.
- **Song Setup gets its own focused page.** No Step list below it.
- **Structure becomes direct arrangement editing.** Add Section should be a short task; common sections add immediately at a sensible default length and can be edited afterward.
- Tracks keeps the successful direct multi-select interaction but loses workflow-navigation chrome.
- **Strong guidance, minimal gating:** Continue recommends the intended order, but Structure/Tracks remain directly accessible when they are independently useful. Only block work that literally cannot function without missing context; explain the dependency and provide a direct way to fix it.
- A global Notes hub should become a genuine app-level destination before Projects/Notes top-level navigation is introduced.
- Preserve the musical/data engines. This is a shell/information-architecture reset, not permission to rebuild stable timeline logic.

## Isolated V7 preview

The repository contains an isolated static prototype under `v7-preview/` for physical shell review before replacing the production root.

- It uses a sandbox localStorage copy: `production-projects-v1-v7-preview`.
- It may read `production-projects-v1` once to seed that sandbox, but preview edits must never write to the production key.
- It covers Project Home, Song Setup, simplified Structure, Tracks, and the Section Study prerequisite/handoff state.
- The preview intentionally leaves the full Section Study timeline, Review Map, and Skeleton interiors untouched until the shell is approved.
- Treat the preview as disposable product evidence, not a permanent second architecture.

## What physical review should judge next

On iPhone Safari, judge the V7 preview primarily on whether it feels **easier**, not whether every old feature is already migrated.

Key questions:

- Can the user open a project and immediately understand what to do next?
- Does Project Home make Journey/revisiting obvious without feeling like a dashboard?
- Does dedicated Song Setup feel calmer than embedding it above workflow navigation?
- Does Structure feel faster when the arrangement itself is the main interface and Add Section is short?
- Do Structure and Tracks feel useful without Step/Checkpoint/status chrome?
- Does returning to Project Home feel more natural than navigating a deep stack?

Do not migrate the specialized Section Study/Review Map/Skeleton interiors until this shell passes that physical gate.

## Automatic handoff rule

The user should **never need to ask for a handoff update again**.

- `START_HERE.md` is the canonical zero-context continuation file.
- Product/runtime or durable-rule PRs that change `app.js`, `styles.css`, `index.html`, `V6.md`, `V7_DRAFT.md`, `CONTEXT.md`, or `AGENTS.md` should refresh this file when the current direction/handoff materially changes.
- `scripts/check_handoff.py` and CI handoff checks enforce the production-file rule set; keep this file current even for experimental redesign branches when the next action changes.
- A new chat pointed at `BabeDrums/babel-fire` should read `README.md` → `START_HERE.md` and continue from the repository rather than requesting a long context prompt.

## Operating workflow

- **No Codex for FIRE.** Use the normal ChatGPT GitHub connector/direct repository tools.
- Work on a task branch → review diff → run static/browser regressions → PR → merge under standing permission only when checks are green and data safety is clear → Pages deploy → physical-device review for visual/interaction changes.
- Production replacement still requires the V7 shell to pass physical review. It is acceptable to ship an isolated `/v7-preview/` path while leaving the root V6 app unchanged.
- Stop instead of merging when tests fail, production data safety is uncertain, destructive behavior is unresolved, or a genuine product decision remains open.

Fallback continuation phrase:

> Babel FIRE — continue from GitHub repo BabeDrums/babel-fire. Read START_HERE.md and resume from the latest verified state.

`V5.md` is historical. `V6.md` remains active production truth until V7 is physically approved and formally promoted.
