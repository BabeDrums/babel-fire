# Babel FIRE — Guided Workspace Redesign (Draft)

**Status:** G7 is the isolated successor preview under `/v7-preview/`; V6 remains production until G7 is physically approved and deliberately promoted. `FIRE_CORE.md` governs cross-generation product doctrine; this file governs the G7 shell and must not redefine Original, Recreation, or learning semantics in conflict with FIRE Core.

## Why G7 exists

V6 made the musician think too much about FIRE's organization. G7 exists to make the shell disappear behind the music.

Core question:

> Can FIRE get the musician into useful musical work without making them think about how FIRE is organized?

Use **G7** in normal conversation. Keep technical identifiers `V7_DRAFT.md`, `/v7-preview/`, and `production-projects-v1-v7-preview` unless a real migration reason appears. G7 must never write to V6's `production-projects-v1` key.

## Current correction after physical review

The first Shell Freeze implementation (#48) improved duplication and density but did **not** pass physical visual review. Babel's feedback identified two system-level problems:

1. **Too much explanatory hierarchy** — titles, subtitles, section labels, helper copy, and repeated instructions stacked into unnecessary layers.
2. **Unpredictable interaction grammar** — similar-looking work sometimes happened inline, sometimes in a sheet, sometimes through navigation, making the interface harder to anticipate.

The shell therefore remains **unfrozen** until the simplification correction passes physical review.

## Shell rules

1. **Delete before styling.** If removing a label/subtitle/helper sentence does not make the next action harder to understand, remove it rather than making it smaller.
2. **One obvious next action.** Project Home recommends one current task and does not repeat it elsewhere.
3. **One job per work screen.** Each work page should explain itself primarily through the task and controls, not stacked prose.
4. **Progress is inferred.** The musician edits musical information; FIRE derives completion.
5. **Guided forward, flexible backward.** Forward guidance is clear; completed work stays revisitable; upcoming work remains inspectable when meaningful.
6. **Project Home is a hub, not a dashboard.** Project identity, one current destination, quiet revisiting/orientation, and only useful utilities.
7. **Notes earn attention.** Empty Notes does not appear. Existing notes stay reachable.
8. **One product across device classes.** iPhone/iPad share logic, hierarchy, actions, and states; only presentation adapts.
9. **Natural document scrolling only.** No VisualViewport-driven root overflow switching.
10. **No signature-feature creep during shell correction.** Fire, badges, Babel World, accounts, learning hub, monetization, and lore remain deferred.

## Interaction grammar

G7 uses a small semantic interaction language. Consistency comes from the **meaning** of the action, not making every control use the same container.

- **Inline** — choose, toggle, classify, confirm, or evaluate something already in the current task.
- **Sheet** — create, edit, or manage a discrete thing while staying in the current context.
- **Navigation** — enter another meaningful workspace.
- **Menu / secondary actions** — utility actions that should not compete with musical work.

Examples:

- Reference / Grid / First Listen → inline toggles.
- Common track choices → inline multi-select.
- Add custom track → sheet because a new named object is being created.
- Add/Edit Section → sheet because a section object is being created/edited.
- Project Edit / Reset / Delete → secondary management sheet.
- Structure → Tracks → Section Study → navigation between workspaces.

Do not introduce a sheet merely because a screen needs visual variety, and do not force object creation inline merely to avoid a sheet.

## Information architecture

### Projects

Projects has one job: open or create.

- `Projects` is the strongest root identity.
- Persistent `+` is the single create affordance.
- Empty state remains `No projects yet.`
- Project title is primary; artist + type are secondary.
- Each existing project has a quiet secondary actions affordance so Edit/Reset/Delete do not require entering the project first.
- New Project must explicitly expose **Original** and **Recreation** as first-class types.
- During physical review, the tiny preview-only `G7 · <commit>` identifier sits at the quiet bottom-center of the viewport, outside normal content hierarchy.
- The build trace is temporary review metadata, never permanent product chrome.

### Project Home

Project Home should feel like a document home, not a labeled dashboard.

- Project identity + project actions.
- One emphasized current destination.
- No visible `Continue` heading above the current destination.
- No visible `Journey` heading above the revisitable/upcoming work list.
- The current task is not repeated in the list below it.
- Completed work remains revisitable; upcoming work remains understandable.
- Future phases may use one quiet `Later` label because it communicates chronology the interface cannot otherwise show.
- Saved Notes may appear as a quiet utility row; empty Notes remains hidden.

Original is first-class in creation and project identity even before the Original FIRE Core workflow is breadboarded. Until that spine exists, Original Project Home must remain a truthful quiet placeholder rather than silently forcing Recreation behavior.

### Work pages

Work pages push directly from Project Home and return directly to it.

Current Recreation / The Map sequence:

- Song Setup
- Structure
- Tracks
- Section Study
- Review Map

No Step/Checkpoint labels. No required The Map intermediary screen. No duplicate project-name text inside work headers.

Nested work pages use a compact icon-only Back affordance with an accessible label; the project title does not need to be printed above every work-page title.

## Typography and copy hierarchy

Use a stable three-level hierarchy:

1. **Projects root** — strongest app/root title.
2. **Project Home** — strong project identity.
3. **Work page** — one consistent compact task-title scale.

Work-page title size must remain consistent across Song Setup, Structure, Tracks, Section Study, Review Map, and Notes.

A subtitle is optional, not default. Keep it only when it gives information the controls/title do not already communicate.

Current copy decisions:

- **Song Setup:** title only; row-level guidance carries the useful detail.
- **Structure:** title only; no `Build the song one section at a time` + `Add the first section you hear` duplication.
- **Tracks:** keep one concise instruction, `Choose everything you hear.` because the task benefits from it.
- **Section Study / Review Map:** title + truthful quiet built-later state; no extra explanatory subtitle.
- **Notes:** title only.

## Visual semantics

Use one meaning per visual state:

- **Selection** — selected surface/border; no completion checkmark.
- **Completion** — ring/check language.
- **Navigation** — row + chevron when opening another workspace.
- **Primary progression** — compact strong action after current work is sufficient.
- **Secondary management** — ellipsis or equivalent quiet utility affordance.

Primary Continue actions should not become giant full-width bars merely because the viewport is narrow.

Prove hierarchy in grayscale before adding signature color/personality.

## Song Setup

Song Setup is one grouped form:

- Reference
- Tempo
- Meter
- Grid
- First Listen

Reference is a requirement, not media FIRE owns. The musician confirms the reference is imported into the production/session environment; FIRE stores only completion state.

Useful row-level guidance stays concise:

- Reference — `Import it into your session.`
- Grid — `Align it to the bar grid.`
- First Listen — `Play the full song once.`

Continue appears only when setup is complete.

## Structure

Structure makes the arrangement itself the interface from the empty state forward.

- The arrangement group exists even before the first section.
- `Add Section` is always part of that same group.
- Common section types add at an 8-bar preview default.
- Tap a section row to edit name/bars/order/duplicate/delete.
- `Matches the song` is the quiet final verification row once sections exist.
- Continue appears only after verification.

Add/Edit Section uses a concise sheet because it creates/edits a section object.

## Tracks

Tracks keeps direct multi-select.

- Common track choices are direct inline selection.
- Custom track creation uses a concise `Add Track` sheet.
- Selection and completion remain distinct.
- Continue appears once at least one track exists.
- Keep density calm; do not turn the page into a wall of giant controls.

## Section Study + Review Map placeholders

These editors are not built yet.

- Missing prerequisites may show direct repair routes.
- When prerequisites are satisfied, use a quiet truthful placeholder.
- Do not expose internal migration/approval language.

## Sheets

Sheets are for brief create/edit/manage tasks closely related to the current context.

- Keep titles concise.
- Avoid giant empty vertical regions.
- Avoid turning sheets into hidden navigation pages.
- Body scrolling may be locked while a sheet is open.
- On wide layouts, sheets may become centered dialogs without changing product logic.

## Natural scrolling + keyboard behavior

- Document height decides whether the page scrolls.
- No VisualViewport-driven root scrolling logic.
- Use CSS safe-area/end clearance.
- Inputs stay at 16px+ to avoid iOS zoom.
- Use CSS scroll padding/margins so focused fields and following actions have breathing room above the software keyboard where the browser honors them.

## Acceptance gate before FIRE Core breadboard

G7 is not frozen until physical review says the shell feels coherent enough to stop discussing generic UI fundamentals.

Review for:

- Projects `+` alignment and root rhythm feel intentional.
- Build trace is visible only when sought and no longer sits inside content hierarchy.
- Project cards can be managed without entering them.
- Original and Recreation are both explicit in New Project.
- Project Home has no redundant Continue/Journey headings.
- Work pages do not stack unnecessary title/subtitle/helper layers.
- Work titles use one stable scale.
- Inline vs sheet vs navigation behavior becomes predictable after only a few interactions.
- Structure uses one arrangement surface from empty → populated.
- Tracks stays direct for normal selection and uses a sheet only for custom creation.
- Primary actions are compact rather than giant phone-width bars.
- Natural scrolling and sheets remain reliable at 390 / 440 / 820.
- V6 production data remains untouched.

Approval question:

> **Can Babel move through the shell without wondering what kind of UI is going to happen next?**

If yes, stop broad shell polishing and move immediately to the FIRE Core breadboard.

## After approval

Sequence:

**physical G7 shell approval → FIRE Core breadboard → thin end-to-end FIRE Core spine → real-project validation**

Breadboard Original + Recreation end to end using places / affordances / connections. For every phase define entering problem, what FIRE asks the musician to notice, decision, Logic action/experiment, evaluation, done criteria, evidence retained, and carry-forward context.

Then build the thinnest complete walking spine from start → release-ready audio and validate on:

- Recreation: **Creep**
- Original: **Even**

Deepen only where real use proves need.

## Technical stability

Preserve unless a real requirement proves otherwise:

- V6 `production-projects-v1`
- schema 5 compatibility
- stable project/section/track/range/event IDs
- migrations
- continuous timeline model
- Map → Skeleton invalidation/dependencies
- durable notes
- browser persistence
- G7 sandbox key `production-projects-v1-v7-preview`

G7 remains disposable product evidence until deliberately promoted.
