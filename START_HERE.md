# Babel FIRE

- **Repository:** `BabeDrums/babel-fire`
- **Production branch:** `main`
- **Live app:** https://babedrums.github.io/babel-fire/
- **Active product generation/specification:** [V6.md](V6.md)

When a new ChatGPT conversation begins with or clearly refers to **Babel FIRE**, resume this project immediately. Do not ask the user to reconstruct documented FIRE decisions.

## Read in this order

1. `START_HERE.md`
2. [AGENTS.md](AGENTS.md)
3. [V6.md](V6.md)
4. [CONTEXT.md](CONTEXT.md)
5. Current `main`, open PRs, relevant branches, and tests
6. [CHANGELOG.md](CHANGELOG.md) for shipped product milestones

Always distinguish shipped work on `main`, unmerged work, and planned work. `README.md` is the zero-context pointer into this handoff; it intentionally does not duplicate the product specification.

## Current approved product direction — October 2026

- FIRE targets roughly **70% calm Apple-like app hierarchy / 30% focused creative-tool density**. Default screens should be simple, quiet, and touch-first; specialized musical workspaces may become denser only when the task requires it.
- Projects, New Project, Project Overview, The Map, Structure, Tracks, and Roadmap establish the current visual language. Preserve their restraint and stable geometry while continuing to remove redundant information.
- **Project → Phase → Step → Musical content** is the approved user-facing hierarchy. `Checkpoint` is historical/internal terminology and must not return as a manual-checklist navigation metaphor.
- The Map Steps are **Structure → Tracks → Section Study**. The Skeleton Steps are **Session → Draft → Bounce**. Completion is derived automatically from canonical state. Phase homes keep all useful Steps visible and communicate **Done / Current / Locked** without large leading checklist circles.
- Normal work screens use quiet positional progress such as **Step 1 of 3**. Section Study prioritizes local section position once inside the musical workspace. Roadmap remains the complete seven-phase journey.
- **Back = actual eligible browser/history navigation.** The center toolbar may host a quiet, real **context navigator**. Phase homes use the project as context; Step/review screens use their parent Phase. The navigator can jump to Project Overview, Roadmap, Notes, the current Phase, and relevant Steps. Passive center pills remain prohibited.
- Do **not** add a persistent Projects/Notes tab bar yet. A top-level iPhone tab / iPad sidebar may be reconsidered when the planned global Notes hub becomes a genuine app-level destination.
- **Song Setup never collapses.** Reference, Tempo, Meter, Grid, and First Listen stay in one stable grouped editing surface; First Listen is the final row. Setup completion gates the first Map Step without hiding the Step list.
- **Project actions are one shared system:** Edit Project, Reset Progress, Delete Project. Reset preserves project identity/details, creation date, and durable notes while clearing workflow progress; Delete removes the project and its notes.
- **Notes are becoming a first-class cross-project knowledge layer.** Canonical project notes may carry type/context metadata. Reset archives active Parking Lot/Takeaway observations instead of discarding them. A global Notes hub remains a separate future product chunk.
- Root scrolling is **content-driven, not route-driven**. Short phone pages that fit the real visual viewport stay planted; genuinely scrolling pages receive enough end clearance for the final interactive content to rise above Safari’s dynamic bottom chrome.
- Action prominence comes from hierarchy/style rather than giant full-width light slabs. Selection and completion are separate semantics. Structured text-heavy information prefers grouped rows/lists over card soup.
- iPad task sheets should use compact centered presentation when appropriate; narrow phone task sheets may remain bottom-oriented. Do not imitate Liquid Glass decoratively.

## Current implementation / cleanup state

- The design-system foundation lives in core `app.js` and `styles.css`; do not recreate `polish.css`, `polish.js`, MutationObserver visual rewrites, or a second override layer.
- Map and Skeleton should share the same Phase Home / Step-list primitives rather than drifting into separate generations.
- Dormant Backup/Restore UI and implementation are not part of the current product. Keep the app focused on active workflow needs.
- Preserve `production-projects-v1`, schema 5, stable section/track/range/event IDs, migrations, browser history, timeline semantics, durable notes, and downstream Skeleton behavior.
- `app.js` remains a large static file by design for now. Prefer targeted consolidation/removal of dead or duplicate code; do **not** broad-module-refactor the stable timeline engine without a clear approved need.

## Physical-device review state

Recent physical iPhone Safari review established that the redesign is moving in the right direction and approved the calm visual system, stable Song Setup, quieter project surfaces, and the move away from Checkpoints. The next physical approval gate is the **Steps + center context navigation + scrolling behavior** chunk. Automated Chromium viewport tests are not a substitute for this review.

## Automatic handoff rule

The user should **never need to ask for a handoff update again**.

- `START_HERE.md` is the canonical zero-context continuation file.
- Product/runtime or durable-rule PRs that change `app.js`, `styles.css`, `index.html`, `V6.md`, `CONTEXT.md`, or `AGENTS.md` must refresh this file.
- `scripts/check_handoff.py` and the CI **Handoff freshness** job enforce that rule on pull requests.
- A new chat that is pointed at `BabeDrums/babel-fire` should read `README.md` → `START_HERE.md` and continue from the repository rather than asking for a long context prompt.

## Operating workflow

- **No Codex for FIRE.** Use the normal ChatGPT GitHub connector/direct repository tools.
- Work on a task branch → review diff → run static/browser regressions → PR → merge under the user’s standing permission only when checks are green and data safety is clear → verify Pages deployment → physical-device review for visual/interaction changes.
- Stop instead of merging if tests fail, data safety is uncertain, a destructive/risky change is unresolved, or a genuine product decision remains open.
- Use `python3 scripts/serve.py` for local development. Run `node --check app.js` and `python3 -B -m unittest discover -s tests -v`; the CI browser matrix covers 390px, 440px, and 820px widths.

## Next after this navigation/progression chunk is approved physically

Continue the remaining V6 surfaces based on real-use friction rather than another broad visual rewrite. The likely priority is **Section Study / Review Map / remaining Skeleton interior screens**, while the global Notes hub should be designed intentionally as its own product feature.

Fallback continuation phrase:

> Babel FIRE — continue from GitHub repo BabeDrums/babel-fire. Read START_HERE.md and resume from the latest verified state.

`V5.md` is historical. `V6.md` is active.
