# Babel FIRE — Guided Workspace Redesign (Draft)

**Status:** Working design direction on `sol/guided-workspace-redesign`. This is intentionally not the active product specification yet. `V6.md` remains production truth until this direction is physically reviewed and promoted.

## Why this reset exists

The current V6 shell became too focused on representing workflow hierarchy. Phase homes, Step states, Roadmap, Back history, and the center context navigator all try to explain where the user is. The result is more navigation and status UI than the musician needs.

The redesign goal is not to make that hierarchy prettier. It is to make FIRE useful enough that the user rarely needs to think about navigation or progress at all.

> FIRE should behave like a calm production coach: show the most useful next action, preserve the musician's work automatically, and keep everything else one obvious move away.

## Product principles

1. **One obvious next action.** The project should know the next useful thing to work on and surface it prominently.
2. **Flatten before adding navigation.** Do not solve deep hierarchy by adding another navigation control.
3. **One job per work screen.** Song Setup, Structure, Tracks, Section Study, Review, Session, Draft, and Bounce get dedicated workspaces when they contain meaningful work.
4. **Progress is inferred, not managed.** The user edits musical information; FIRE derives completion.
5. **Project Home is the hub.** It combines the current-action surface and the whole project journey. A separate Roadmap screen should not duplicate it.
6. **Browse and Continue are different modes.** `Continue` enters the current task. The project journey lets the user revisit prior work without forcing every screen to carry navigation chrome.
7. **Notes are a real app-level destination.** Project notes are one view into a cross-project Notes system, not a separate notes implementation.
8. **Use familiar platform patterns.** Prefer standard navigation bars, grouped lists, forms, sheets, and top-level tabs/sidebar over custom context menus or clever navigation widgets.
9. **Keep the musical engines.** Timeline semantics, IDs, migration, invalidation, Skeleton dependencies, and durable notes are valuable. Rebuild the shell around them rather than rewriting proven musical logic.
10. **Strong guidance, minimal gating.** `Continue` recommends the intended sequence, but the musician may open useful work directly. Only block an action when it literally cannot function without missing information; when that happens, explain what is missing and provide direct routes to fix it instead of showing a dead locked row.

## New information architecture

### App level

Two genuine top-level destinations:

- **Projects**
- **Notes**

On iPhone these may become a compact bottom tab bar once the Notes hub is implemented. On iPad the same destinations can adapt to a sidebar/split presentation. No top-level tab exists merely as decoration.

### Project level

Opening a project lands on a single **Project Home**. This is the user's home base.

Project Home contains:

- project title, artist, type, and project actions
- one **Continue** surface showing the next useful work item
- one **Journey** list containing the seven Recreation phases (or the appropriate Original progression)
- the current phase expanded just enough to expose its work items
- completed phases summarized quietly
- future phases visible without pretending they are implemented
- a project-scoped Notes entry that opens the global Notes system filtered to this project

**Project Home replaces the separate Roadmap destination.** The journey belongs where the project lives.

### Work level

Work screens push directly from Project Home and return directly to Project Home. Do not create a mandatory Phase Home between them.

For Recreation / The Map, the guided work sequence is:

- **Song Setup**
- **Structure**
- **Tracks**
- **Section Study**
- **Review Map**

The user-facing UI does not need to call these `Steps` or `Checkpoints`. Their names are enough.

The Skeleton follows the same model:

- **Session**
- **Draft**
- **Bounce**

A phase is a grouping in the Journey, not necessarily another screen the user must enter.

Structure and Tracks are useful on their own and should remain directly accessible even if Song Setup is incomplete. Section Study genuinely needs a structure and at least one track; if either is missing, open a helpful prerequisite screen with direct actions rather than a disabled destination.

## Navigation model

The current center context navigator is removed.

Navigation should be shallow enough that it is unnecessary:

- **Projects -> Project Home -> Work screen**
- work-screen Back returns to the project
- `Continue` advances within the guided sequence without creating a pile of browser-history depth
- revisiting old work happens from the Project Home Journey
- Projects / Notes handle app-level movement once Notes is real

The goal is a maximum practical depth of two pushes from the Projects list, not a richer way to jump around a deep stack.

## Song Setup

Song Setup deserves its own dedicated work screen.

It should use one stable grouped form containing:

- Reference
- Tempo
- Meter
- Grid alignment
- First Listen

No collapse state. No Step list beneath it. No competing phase navigation. Completion makes Structure the recommended continuation; Structure itself does not need to be hard-locked behind Setup.

## Structure

Structure should make the arrangement itself the interface.

- The main screen shows the ordered section list directly.
- **Add Section** opens a small, short task surface rather than a near-full-screen workflow.
- Choosing a common section type adds it immediately at a sensible default length (8 bars in the prototype).
- Tap an existing section to rename it, change bars, reorder, duplicate, or remove it.
- A simple confirmation such as **Structure matches the song** remains an explicit user attestation before `Continue` recommends Tracks.

The user should not have to choose a type, choose a length, press Add, and then separately dismiss a large sheet for every section.

## Project Home / Journey behavior

The Project Home should feel closer to Apple Music / Reminders / Settings hierarchy than a project-management dashboard.

- Use typography and grouped rows more than cards.
- Reserve one visually prominent surface for `Continue`.
- The current phase may be expanded inline to show its work items.
- Completed items can show a quiet completion accessory.
- The current work item gets the strongest row emphasis and disclosure.
- Future work stays visible but quiet.
- Do not show redundant `Phase 1 of 7`, `2 of 3 complete`, `Current`, `Next`, and a progress bar simultaneously.
- Do not label revisitable work as `Locked` merely because it is not the recommended next task.

## Notes hub

Notes become a canonical cross-project library.

Each note can know:

- project
- type (General, Takeaway, Parking Lot, etc.)
- phase/context
- song section or other musical context where relevant
- created/updated time

The Notes tab defaults to all notes and supports search plus lightweight filtering by project/type/context. A project-level Notes entry opens the same hub already filtered to that project.

Do not require the musician to manually tag information FIRE already knows from context.

## Helpfulness standard

Every screen should answer one of these questions immediately:

- **What should I do next?** -> Continue
- **Where am I in this project?** -> Project Home Journey
- **How do I edit something I already did?** -> tap it in Journey
- **What did I learn/write down?** -> Notes
- **What is this screen asking me to decide about the music?** -> title + one short instruction + the musical editor

If a screen mainly exists to explain navigation or status, challenge whether the screen should exist.

## iPhone / iPad adaptation

### iPhone

- Project Home is a vertically scrolling hub.
- Work screens are focused single-column pages.
- Native-feeling Back + title + contextual trailing action only.
- Avoid custom center navigation controls.
- If the Notes tab is introduced, account for Safari's real visual viewport and bottom chrome rather than assuming static safe-area geometry.

### iPad

- Prefer a sidebar/split composition when it materially reduces navigation: project Journey or app-level Projects/Notes can remain visible while work appears in the detail area.
- Do not simply enlarge the phone layout.

## What stays technically stable

Unless a later requirement proves otherwise, preserve:

- `production-projects-v1`
- schema 5
- stable project/section/track/range/event IDs
- migration behavior
- continuous timeline model
- Map -> Skeleton invalidation/dependency semantics
- durable notes
- browser persistence

This is an information-architecture and presentation reset, not permission to delete musical capability.

## Isolated preview contract

The first V7 shell is implemented as an isolated static preview under `/v7-preview/` before replacing the production root app.

- The production root remains V6 during physical review.
- The preview reads the current FIRE database only to create an initial **sandbox copy** under `production-projects-v1-v7-preview`.
- Preview edits never write to `production-projects-v1`.
- The preview intentionally covers Project Home, Song Setup, Structure, Tracks, and a Section Study handoff/prerequisite state only.
- This preview is disposable evidence for the shell direction, not a second permanent application architecture.

## Implementation order

1. Remove the center context navigator from the redesign direction.
2. Build the new Project Home as hub + Continue + Journey, folding Roadmap into it.
3. Make Song Setup its own work route/page.
4. Flatten Map navigation so work screens return to Project Home and `Continue` moves through work without accumulating needless depth.
5. Simplify Structure around direct arrangement editing and bring Tracks into the same focused work-page shell without changing its musical meaning.
6. Build the global Notes hub and only then introduce Projects / Notes top-level navigation.
7. Adapt Project Home/Work shell to iPad split/sidebar behavior.
8. Only after the shell is physically approved, migrate Section Study, Review Map, and Skeleton interiors.

## Approval gate

Do not promote this draft to the active product specification or broadly rewrite the specialized musical editors until the new Project Home + Song Setup + Structure/Tracks shell is physically reviewed on iPhone Safari. The redesign should prove that FIRE feels easier before the old shell is removed everywhere.
