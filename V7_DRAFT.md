# Babel FIRE — Guided Workspace Redesign (Draft)

**Status:** G7 is the isolated successor preview under `/v7-preview/`; V6 remains production until G7 is physically approved and deliberately promoted. `FIRE_CORE.md` governs cross-generation product doctrine; this file governs the G7 shell and must not redefine Original, Recreation, or learning semantics in conflict with FIRE Core.

G7 uses **Cover** as the musician-facing label for the canonical FIRE Core **Recreation** workflow. Internal compatibility may continue using the legacy `study` project type; public naming does not require a storage migration.

## Why G7 exists

G7 exists to make the shell disappear behind the music.

Core question:

> Can FIRE get the musician into useful musical work without making them think about how FIRE is organized?

The shell is the reusable interaction and layout grammar: headers, navigation, sheets, forms, grouped rows, selection/completion states, scrolling, editing, and responsive behavior. Shell approval does **not** mean final animation, personality, signature visuals, or every future musical workspace is finished.

## Shell rules

1. **Delete before styling.** If removing a label/subtitle/helper sentence does not make the next action harder to understand, remove it rather than making it smaller.
2. One obvious current action; do not duplicate it elsewhere.
3. One stable page scaffold across root, project, and work pages.
4. Subtitle/helper text is exceptional, not default.
5. Progress is inferred from musical state where practical.
6. Project Home is a hub, not a dashboard.
7. One product across iPhone/iPad; presentation adapts, semantics do not.
8. Natural document scrolling only; no VisualViewport-driven root overflow switching.
9. Learning remains ambient and optional. A Cover must not require a learning-flavored waypoint merely to keep moving.
10. No signature-feature creep during shell correction.

## Interaction grammar

- **Inline** — choose, toggle, classify, confirm, or evaluate something already in the current task.
- **Sheet** — create/edit/manage a discrete thing while staying in context.
- **Navigation** — enter another meaningful workspace.
- **Menu / secondary affordance** — utilities that should not compete with musical work.

Consistency comes from semantic meaning, not from forcing every interaction into one container.

## Header and title scaffold

Every G7 screen uses the same structural scaffold:

- a stable 44px-equivalent toolbar region first
- Back occupies the leading slot when applicable
- `+` or `•••` occupies the trailing slot when applicable
- the page title begins at the same vertical location across Projects, Project Home, and work pages
- one coherent page-title scale on phone instead of a 40 → 34 → 30 staircase
- project metadata may sit quietly below the project title

The `•••` action is one reusable visual control whether it appears in a project row or the trailing toolbar. Its location may change; its visual size/meaning should not.

## Projects

Projects has one job: open or create.

- one ungrouped list by default; do not split Originals and Covers into permanent sections yet
- sort by meaningful project activity (`lastActivityAt`), not by accidental opening
- older preview records without activity metadata normalize safely from existing timestamps
- project title is primary; artist + type are secondary
- public project types are **Original** and **Cover**
- internal legacy `study` compatibility is preserved
- per-card `•••` visually belongs to the card and remains a 44px-equivalent target
- build trace remains quiet bottom-center review metadata only

## New Project

New Project opens in one stable sheet. Do not reveal required fields only after project-type selection.

- **Original | Cover** is visible immediately
- fields are always **Title** and **Artist** in the same positions for both types
- switching type changes validation/behavior, not geometry or field labels
- Original requires Title; Artist may be empty
- Cover requires Title + Artist
- text/name inputs request word capitalization from the mobile keyboard with `autocapitalize="words"`
- do not programmatically force title casing; intentional stylization must remain possible
- avoid aggressive autocorrection for song/artist/section/track names
- opening the sheet itself should not summon a keyboard

## Project Home

Project Home answers: what project is this, and what deserves attention next?

- title + quiet metadata
- one current destination when work remains
- no helper sentence under the current destination when the title already explains it
- no visible `Continue` or `Journey` taxonomy
- current shell Cover work is **Song Setup → Structure → Tracks**
- Section Study is not a mandatory shell waypoint
- Review Map is not exposed as a placeholder destination merely to fill progression
- after current mapped shell work is complete, show a truthful quiet completion state rather than forcing an unbuilt learning/review route
- saved Notes may appear; empty Notes stays hidden
- do not dump future phases onto Project Home merely to imply completeness

Original remains first-class even before its full FIRE Core workflow is breadboarded; unfinished copy stays musician-facing.

## Work pages

Current Cover shell workspaces:

- Song Setup
- Structure
- Tracks

All use the shared header/title scaffold. Default helper copy is removed when the controls are self-explanatory.

### Song Setup

One grouped surface:

- Reference
- Tempo
- Meter
- Grid
- First Listen

Tempo remains an inline value field with 16px+ input behavior and an integrated focus treatment. Continue appears only when canonical setup requirements are satisfied.

### Structure

Structure is an ordered arrangement, not a two-step create-then-fix workflow.

Arrangement rows show:

- index
- section name
- bar length
- permanent reorder handle

Row tap/edit and reorder are distinct actions.

**Add Section** uses one builder sheet:

- choose Intro / Verse / Pre-Chorus / Chorus / Bridge / Instrumental / Outro / Custom
- choose **4 / 8 / 12 / 16 / Custom** bars before insertion
- tapping a section type alone does not create anything
- Add commits one valid section
- the builder stays open after Add so repeated arrangement entry is fast
- retain the chosen bar length, clear/re-arm section type, and show concise inline confirmation
- Done closes the builder
- Custom type/length reveal only their required fields

**Edit Section** edits name and bar length only, plus quiet Duplicate/Delete utilities. Reordering does not live in Edit.

Reordering belongs to the visible row handle:

- direct pointer/touch drag path
- keyboard Arrow Up/Down alternative on the handle
- roughly 44px target
- reordering invalidates Structure verification but preserves section identity/data

`Matches the song` remains the final Structure verification. Continue appears only after current Structure completion.

### Tracks

Common tracks remain direct inline multi-select. `Other` opens a compact named-track sheet. Name fields request word capitalization. Once at least one track exists, the final shell action is **Done**, returning to Project Home rather than forcing Section Study.

## Project management sheets

The project-actions sheet does not repeat the song title. It contains only useful management actions:

- Edit Details
- Reset Progress (Cover only)
- Delete Project
- Cancel

Edit Details uses the same **Title / Artist** labels and capitalization behavior as New Project.

## Sheets / keyboard / scrolling

- sheets are concise create/edit/manage surfaces, not hidden navigation pages
- opening a selection/manage sheet does not automatically summon a keyboard
- controls remain reachable above the iOS software keyboard
- background scrolling locks only while the modal sheet is open
- no VisualViewport root-scroll machinery
- normal document height decides whether a page scrolls

## Acceptance gate before FIRE Core breadboard

G7 is not frozen until physical review says generic UI fundamentals are coherent enough to stop redesigning them.

Review for:

- stable title position/scale across Projects → Project → work
- Cover naming feels natural
- New Project no longer changes shape when type changes
- Title/Artist fields keep stable labels and mobile word capitalization
- `•••` feels like one control everywhere
- recent-first Projects order feels useful without category clutter
- Project Home feels lean and focused
- Song Setup has enough context without helper-copy noise
- Structure builder is fast, predictable, and does not assume 8 bars prematurely
- reorder feels direct on device; Edit remains compact
- no mandatory learning-flavored route blocks a quick Cover
- natural scrolling/sheets remain reliable at 390 / 440 / 820
- V6 production data remains untouched

Approval question:

> **Can Babel move through the shell without wondering what kind of UI is going to happen next?**

If yes, stop broad shell polishing.

## After approval

Sequence:

**physical G7 shell approval → FIRE Core breadboard → thin end-to-end FIRE Core spine → real-project validation**

Breadboard Original + Recreation/Cover end to end using places / affordances / connections. For every phase define the entering problem, what FIRE asks the musician to notice, the decision, the Logic action/experiment, evaluation, done criteria, evidence retained, and carry-forward context.

The thin FIRE Core must prove a believable path from starting material/reference to finished release-ready audio before deep polish. Real-project validation should include a Cover and an Original.

## Technical stability

Preserve unless a real requirement proves otherwise:

- V6 `production-projects-v1`
- G7 `production-projects-v1-v7-preview`
- schema 5 compatibility
- stable project/section/track/range/event IDs where applicable
- migrations and existing preview normalization
- static GitHub Pages delivery
- no runtime framework/build dependency added for shell work
