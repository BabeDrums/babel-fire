# Babel FIRE — Start Here

Use **Babel** as the project-facing name.

This is the canonical zero-context FIRE handoff. For FIRE implementation/product work, read in this order:

1. `START_HERE.md`
2. `AGENTS.md`
3. `FIRE_CORE.md`
4. `V6.md` for production behavior
5. `V7_DRAFT.md` for G7 shell behavior
6. relevant unresolved items in `CONTINUITY_INBOX.md`
7. code/tests as implementation evidence

For wider ecosystem/surrounding-app work instead, route through `BABEL_START_HERE.md`, `BABEL_APPS.md`, and `BABEL_PLATFORM.md`. Do not let ecosystem brainstorming rewrite active FIRE runtime/spec behavior.

## Current verified continuity — corrected G7 shell is live but NOT frozen

Production remains V6. G7 remains the isolated successor preview at `/v7-preview/` using `production-projects-v1-v7-preview`; it must never mutate V6 `production-projects-v1` data.

The last merged baseline before the current system correction is PR **#56** on `main` at `6a9cfb18fbefd5e97735dabdc8fcb448ba0e9bcd`. At the start of the current task there were no open PRs. Always re-check current `main` and open PRs rather than assuming this SHA remains latest.

The G7 shell is still **not approved/frozen**. Do not begin FIRE Core breadboarding until Babel physically approves the generic shell fundamentals.

### Latest physical-device review — system correction required

Babel's iPhone review after #56 exposed a shared system problem rather than isolated cosmetic bugs:

- public `Recreation` naming feels less natural than **Cover**
- New Project changes shape after project-type choice and changes Title/Song + Artist label semantics
- mobile text-name fields no longer request word capitalization
- root/project/work title scale and vertical placement shift too much between screens
- project-card and toolbar `•••` should feel like one control
- Projects should surface meaningful recent activity first without permanent Original/Cover sections yet
- project-actions sheet repeats too much context
- Project Home still carries too much hierarchy/copy and future-phase clutter
- Song Setup / Tracks helper copy can be reduced
- Structure regressed into tap-type → auto-create 8 bars → reopen Edit; this is slower and less truthful than choosing type + length before insertion
- Move Up / Move Down belongs out of Edit; reorder should happen from the arrangement itself with an accessible alternative
- Section Study should not be a mandatory learning-flavored waypoint; FIRE Core already says learning is ambient/optional and quick-cover flow must stay usable

### Current G7 system correction

The active correction promotes those findings into one coherent shell contract rather than another pile of patches:

- musician-facing **Original / Cover**; internal legacy `study` compatibility remains
- one shared header scaffold and coherent page-title scale across Projects, Project Home, and work pages
- one reusable visual `•••` control
- New Project opens fully formed with stable **Title / Artist** fields; switching type changes validation, not geometry
- name/title inputs request `autocapitalize="words"` and avoid aggressive autocorrection without rewriting user-entered casing
- Projects sort by meaningful `lastActivityAt`; merely opening a project does not reorder it
- project actions become compact and stop repeating the song title
- Project Home is reduced to current Cover work plus revisitable work/Notes; future-phase dump is removed
- current Cover shell sequence is **Song Setup → Structure → Tracks**
- helper copy is removed where labels/controls already explain the task
- Structure Add Section chooses type + **4 / 8 / 12 / 16 / Custom** before insertion and stays open for fast repeated entry
- Structure rows expose direct reorder handles; keyboard Arrow Up/Down is the non-drag alternative
- Edit Section no longer owns Move Up / Move Down
- Tracks ends with **Done** back to Project Home instead of forcing Section Study
- completed current shell mapping shows a truthful quiet `Song map complete.` state; unbuilt learning/review placeholders do not masquerade as required progression

This correction does **not** equal physical approval. The next meaningful product action after merge/deploy is another real iPhone review.

## G7 interaction grammar

Protect these semantic rules:

- **Inline = choose/toggle/classify/confirm/evaluate** something already in the task.
- **Sheet = create/edit/manage a discrete thing** while staying in context.
- **Navigation = enter another meaningful workspace.**
- menu/secondary affordance = utilities that should not compete with musical work.

Delete before styling. Subtitle/helper text is optional, not default. Do not compensate for weak fundamentals with signature visual polish.

## Physical approval checklist

On real iPhone Safari, inspect:

1. Does Projects → project → work keep title position/scale calm and predictable?
2. Does **Cover** read naturally next to Original?
3. Does New Project feel complete immediately instead of revealing/reflowing basic fields?
4. Do Title/Artist keyboard capitalization suggestions behave naturally without forcing casing?
5. Does `•••` feel like the same control in rows and the toolbar?
6. Does meaningful recent activity ordering feel useful?
7. Is Project Home now lean enough to answer “what next?” without acting like a roadmap/dashboard?
8. Is Song Setup clear without helper-copy stacks, including Tempo focus/keyboard behavior?
9. Does Structure let Babel enter common/non-8-bar sections quickly without an edit round trip?
10. Does row reorder feel direct and understandable; is Edit Section compact?
11. Does the Cover flow stop cleanly after current mapped shell work without forcing learning chrome?
12. Overall: **can Babel move through the shell without wondering what kind of UI is going to happen next?**

If yes, explicitly record approval and stop broad shell polishing. Small later animation/personality/microinteraction improvements remain allowed after the product logic proves itself.

## After shell approval

Sequence:

**physical G7 shell approval → FIRE Core breadboard → thin end-to-end FIRE Core spine → real-project validation**

The breadboard is behavior-first, not pixel-first. Map Original + Recreation/Cover end to end and define, for every phase:

- entering problem
- what FIRE asks the musician to notice
- decision being made
- Logic action/experiment
- evaluation
- done criteria
- evidence retained
- carry-forward context

The breadboard must make a believable path from a Cover reference to finished release-ready audio and from Original material to finished release-ready audio. If a phase devolves into “then somehow mix it,” the product logic is not ready.

The thin FIRE Core should then implement the smallest real walking spine across that entire journey and validate it on real music before deep polish.

## Generation-spec retention

Git history is the archive. Keep the current production spec (`V6.md`) plus the active successor spec (`V7_DRAFT.md`) in the working tree by default. Do not resurrect retired generation specs as competing authority unless maintenance/migration/recovery genuinely requires them.

## Parallel-chat ownership

Babel may keep multiple chats open.

- FIRE build lane owns active runtime/spec implementation and follows this file + `AGENTS.md`.
- Ecosystem brainstorm lane follows `BABEL_START_HERE.md` + `BABEL_APPS.md` + `BABEL_PLATFORM.md`, is read-mostly toward FIRE runtime while a build is active, and must re-read latest `main`/open PRs before any durable write.
- an old branch without an open PR/current handoff reference is historical working state, not product authority.

## Normal workflow / standing permission

For FIRE implementation:

**branch → implement → test → reconcile docs → PR → checks → merge → Pages deploy → verify → physical-device approval when relevant**

Babel has standing permission to merge FIRE PRs once the diff is reviewed, required checks are green, production-data safety is clear, and no genuine product decision remains unresolved. Do not merge when tests fail, behavior is destructive/risky, data safety is uncertain, or a real decision is still unresolved.
