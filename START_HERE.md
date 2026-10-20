# Babel FIRE

- **Repository:** BabeDrums/babel-fire
- **Production branch:** `main`
- **Live app:** https://babedrums.github.io/babel-fire/
- **Active product generation/specification:** [V6.md](V6.md)

When a new ChatGPT conversation begins with or clearly refers to **Babel FIRE**, resume this project immediately; do not ask the user to explain FIRE again.

## Read in this order

1. `START_HERE.md`
2. [AGENTS.md](AGENTS.md)
3. [CONTEXT.md](CONTEXT.md)
4. [V6.md](V6.md)
5. Current `main`, open PRs, relevant branches, and tests
6. [CHANGELOG.md](CHANGELOG.md) for shipped product milestones

Always distinguish shipped work on `main`, unmerged work, and planned work. Resume from the latest verified state and do not make the user repeat documented decisions.

## Current verified direction — October 2026

- **Projects + New Project are useful visual references, not untouchable templates.** Preserve their restraint, spacing, hierarchy, and stable geometry while improving them when a shared-system change makes FIRE calmer or clearer.
- FIRE should lean roughly **70% calm Apple-like app hierarchy / 30% focused creative-tool density**. Navigation, setup, project, review, and checkpoint surfaces should stay simple and minimal; specialized musical workspaces may become denser only when the task genuinely requires it.
- The shared workflow shell has been carried through Project → The Map → Structure → Tracks, but the older interior component language still feels inconsistent across Map, Structure, Tracks, Roadmap, Notes, Review Map, Section Study, and Skeleton screens.
- The representative **FIRE Design System foundation** is being consolidated in the core stylesheet so shared primitives carry the design instead of a second route-specific override layer. The Map, Structure, Tracks, Roadmap, and Skeleton/Session remain the approval set; physical iPhone/iPad approval is required before broad rollout to remaining routes.
- The design-system pass should standardize typography, spacing, radii, grouped surfaces, rows, inputs, segmented controls, selections, completion states, primary/secondary/quiet/destructive actions, navigation placement, hover/pressed/focus/disabled states, and adaptive sheets.
- **Selection is not completion.** Checkmarks/circles are reserved for genuine completion semantics, not generic selected state.
- On iPad, task sheets such as Add Sections should use compact centered form/page-style presentation where practical; narrow iPhone layouts may remain bottom-oriented.
- Physical iPhone review after the foundation consolidation established two phone-specific rules: short routes that fit the visual viewport must not create root scroll/bounce, and dense routes should compact redundant secondary information before shrinking touch targets.
- **Adaptive composition is now a shared rule:** current/incomplete work stays expanded and visually dominant; completed work compresses into an editable summary that remains one tap away; future work stays quiet. The Map collapses completed Song Setup, Project makes the current-phase surface the action, and Roadmap reserves full detail for the current phase.
- **Unavailable work-screen continuation controls should not occupy visual space.** Keep future journey destinations visible where they help orientation, but only reveal Next-style actions when they can actually be used; when prerequisites are incomplete, summarize the lock once instead of repeating disabled destination rows; remove headings that merely repeat the page or task.
- Root scrolling must be **content-driven rather than route-driven**. Measure rendered in-flow content against the real visual viewport; lock root scroll only when the page genuinely fits, and automatically restore it whenever content becomes taller.
- On narrow phones, Roadmap should prioritize full detail for the current phase and compact non-current phases; The Map may collapse redundant checkpoint descriptions while preserving titles, state, and progression.
- Huge light full-width CTA slabs are not the default FIRE action pattern. Action prominence should come from hierarchy/style, not simply width.
- Passive center pills are being retired. Leading toolbar = navigation; trailing toolbar = contextual action; page title = current location.
- Typography should use a consistent hierarchy and reduce unnecessary tracked-uppercase labels or redundant copy.
- Meaningful cards stay cards, but text-heavy structured information should prefer coherent grouped rows/lists rather than card soup.
- Arrangement/Section Study may keep specialized geometry, but must inherit the same FIRE control, typography, state, and spacing language.
- Do not add fake Liquid Glass or decorative blur/gradient effects. Borrow Apple-like hierarchy, geometry, restraint, adaptive behavior, and interaction clarity instead.

## Operating workflow

- **No Codex for FIRE.** Use the normal ChatGPT GitHub connector/direct repository tools.
- Work on a task branch, review the diff, run the regression suite, then merge when green under the user's standing merge permission.
- Stop instead of merging when tests fail, data safety is uncertain, the change is risky/destructive, or a genuine product decision is unresolved.
- Automated/browser tests do not establish visual completion. After deployment, physical iPhone/iPad Safari testing by the user is the visual/interaction approval gate.
- Keep implementation in core `app.js` / `styles.css` / shared components. Do not recreate the failed `polish.css` / `polish.js` / MutationObserver override architecture.
- Preserve `production-projects-v1`, schema 5, stable IDs, migrations, timeline semantics, notes, history, and downstream Skeleton behavior.

Fallback continuation phrase:

> Babel FIRE — continue from GitHub repo BabeDrums/babel-fire. Read START_HERE.md and resume the current FIRE Design System work.

`V5.md` is historical. `V6.md` is active. Use `python3 scripts/serve.py` for local development and the existing regression workflow for validation.