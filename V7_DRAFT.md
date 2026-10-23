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
5. Progress is inferred from musical state where practical; when FIRE cannot truthfully infer completion, use an explicit lightweight confirmation.
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
- opening a card's action menu must not silently change the active/current project
- build trace remains quiet bottom-center review metadata only

## New Project / Edit Project

New Project opens in one stable sheet. Do not reveal required fields only after project-type selection.

- **Original | Cover** is visible immediately in New Project
- fields are always **Title** and **Artist** in the same positions for both types
- switching type changes validation/behavior, not geometry or field semantics
- Original requires Title; Artist may be empty
- Cover requires Title + Artist
- compact project create/edit sheets do not need redundant visible `New Project` / `Edit Details` headings or visible Title/Artist field labels when the two-field context is already clear
- Title/Artist remain the input placeholders and accessible semantic labels so clearing a field restores visible context and assistive technology still receives the field meaning
- text/name inputs request word capitalization from the mobile keyboard with `autocapitalize="words"`
- do not programmatically force title casing; intentional stylization must remain possible
- avoid aggressive autocorrection for song/artist/section/track names
- opening the sheet itself should not summon a keyboard

This compact placeholder-only treatment is specific to the simple project form; do not remove labels from more complex forms merely for visual minimalism.

## Project Home

Project Home answers: what project is this, and what deserves attention next?

- title + quiet metadata
- current Cover shell work remains **Song Setup → Structure → Tracks**
- all current mapping steps live in **one coherent progression group** rather than splitting the recommended step into a separate card
- completed steps use a quiet completed state, the current step is visually strongest, and upcoming work stays understandable without competing
- the progression itself communicates completion; do not add a separate `Song map complete.` card when all three checked rows already say the same thing
- no helper sentence under the current destination when the title/state already explains it
- no visible `Continue` or `Journey` taxonomy
- Section Study is not a mandatory shell waypoint
- Review Map is not exposed as a placeholder destination merely to fill progression
- saved Notes may appear as a separate utility group; empty Notes stays hidden
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

Tracks remains a fast musician-facing multi-select **grid**, not a generic settings list.

- common tracks remain direct inline multi-select
- phone grid stays compact and two-column by default; selected state should be clear without turning every choice into a heavy slab
- selected tracks use a subtle state plus a visible check
- `Other` belongs to the same selection surface and opens a compact named-track sheet
- custom names request word capitalization
- selecting one track does **not** prove the track map is complete
- once at least one track exists, **Done** becomes available as the explicit lightweight confirmation that the current track selection represents the song
- track selection changes invalidate that confirmation; pressing Done restores it
- only a confirmed non-empty track selection counts as Tracks complete on Project Home
- Done returns to Project Home rather than forcing Section Study

The data model records this distinction as track selection plus a separate confirmation state (`tracksVerified`); older preview data without the field normalizes safely to unverified rather than inventing completion.

## Project management sheets

The project-actions sheet does not repeat the song title or add explanatory chrome. It contains only useful management actions:

- Edit
- Reset (Cover only)
- Delete
- Cancel

Edit opens the compact Title/Artist form above. Reset and Delete are uncommon destructive actions and require a short confirmation step because G7 does not provide a real undo path. The first action menu stays terse; confirmation is where consequence/context belongs.

## Sheets / keyboard / scrolling

- sheets are concise create/edit/manage surfaces, not hidden navigation pages
- do not show a grabber/drag indicator on custom sheets that cannot actually drag, resize, or dismiss through that affordance
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
- compact New/Edit project forms remain obvious without redundant visible headings/labels
- Title/Artist fields keep stable semantics and mobile word capitalization
- `•••` feels like one control everywhere and card actions do not mutate active-project state
- project action wording is terse; destructive actions do not execute accidentally
- recent-first Projects order feels useful without category clutter
- Project Home reads as one calm progression rather than a current-task card plus a second system
- completed mapping does not need a redundant completion card
- Song Setup has enough context without helper-copy noise
- Structure builder is fast, predictable, and does not assume 8 bars prematurely
- reorder feels direct on device; Edit remains compact
- Tracks grid remains fast while selected state, `Other`, and Done feel integrated
- Tracks completion reflects explicit confirmation rather than merely having one selected track
- no mandatory learning-flavored route blocks a quick Cover
- custom sheets do not advertise dead drag/resize behavior
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
