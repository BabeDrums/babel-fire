# Babel FIRE — Guided Workspace Redesign (Draft)

**Status:** Isolated V7 shell preview is live from `main` under `/v7-preview/`. V6 remains the production app and active production specification until the V7 shell passes physical iPhone review and is deliberately promoted.

## Why this reset exists

V6 became too focused on representing workflow hierarchy. Phase homes, Step states, Roadmap, Back history, and a custom center navigator made the musician think about FIRE's organization instead of the music.

The V7 goal is simpler:

> FIRE should behave like a calm production coach: show the most useful next action, preserve work automatically, and keep everything else one obvious move away.

## Product principles

1. **One obvious next action.** Project Home recommends the most useful next task.
2. **Flatten before adding navigation.** Do not solve hierarchy with another navigation control.
3. **One job per work screen.** Song Setup, Structure, Tracks, Section Study, Review, Session, Draft, and Bounce each get a focused workspace when they contain real work.
4. **Progress is inferred, not managed.** The user edits musical information; FIRE derives completion.
5. **Project Home is the hub.** Continue + Journey + Notes replace duplicate overview/roadmap navigation.
6. **Browse and Continue are different.** Continue guides forward; Journey lets the user revisit work.
7. **Strong guidance, minimal gating.** Recommend the intended order, but only block an action when it literally cannot function without missing context.
8. **Notes are a real app-level destination.** Project notes are one filtered view of the future cross-project Notes system.
9. **Use familiar platform patterns.** Prefer standard back navigation, grouped lists, forms, concise sheets, tabs/sidebar only when they represent genuine top-level areas.
10. **Keep the musical engines.** Preserve schema, stable IDs, migrations, timeline semantics, invalidation, Skeleton dependencies, and durable notes.

## Information architecture

### App level

Future genuine top-level areas:

- **Projects**
- **Notes**

Do not add a Projects/Notes tab bar until the Notes hub is implemented. On iPad, the same areas may later adapt to a sidebar/split view.

### Project level

Opening a project lands on one **Project Home** containing:

- project identity and project actions
- one quiet **Continue** destination
- one **Journey** view of the full project
- project Notes entry

Project Home replaces the separate Roadmap destination.

### Work level

Work screens push directly from Project Home and return directly to it.

For Recreation / The Map, the guided work sequence is:

- Song Setup
- Structure
- Tracks
- Section Study
- Review Map

The UI does not need to call these Steps or Checkpoints. Their names are enough.

The Skeleton follows the same idea:

- Session
- Draft
- Bounce

A phase is a grouping in Journey, not necessarily another screen the user must enter.

## Navigation model

The V6 center context navigator does not carry forward.

Navigation should remain shallow:

- Projects → Project Home → Work screen
- work-screen Back returns to Project Home
- Continue advances through guided work without building unnecessary browser-history depth
- revisiting old work happens from Journey
- future Projects / Notes navigation belongs at the app level only when Notes is real

## Projects

Projects should read like a calm grouped list rather than a grid of large cards.

- No empty toolbar on the root screen.
- Project title is primary; artist + type are secondary.
- Keep project rows concise; detailed progress belongs inside Project Home.
- Preview-only sandbox information stays visually subordinate.

## Project Home

Project Home should feel like a document home, not a dashboard.

- **Continue** is one emphasized grouped destination, not a hero/marketing card.
- **Journey** owns project position and revisitability.
- The active phase may expose its named work inline.
- Completed work gets a quiet completion accessory.
- Future phases remain visible but quiet.
- Avoid redundant labels such as Recommended, In progress, Current, Later, Phase 1 of 7, 2 of 3 complete, or progress bars when the hierarchy is already obvious.
- Roadmap does not exist as a separate destination.

## Visual semantics

Use one meaning per visual state:

- **Selection** — restrained selected surface/border; no completion checkmark.
- **Completion** — ring/check language.
- **Status/value** — concise text when a word communicates the state better than an icon.
- **Navigation** — list row + chevron where the row opens another destination.
- **Primary progression** — the strongest compact button treatment on the work page.

Do not show two indicators for the same state. A primary action must read differently from a selected option.

Inactive future phases should orient without masquerading as disabled controls. Keep them visible in a compact quiet summary; expand the active phase’s work in Journey.

## Song Setup

Song Setup is a dedicated work page containing one stable grouped form:

- Reference
- Tempo
- Meter
- Grid alignment
- First Listen

No collapse state. No Step list. No competing phase navigation. Completion makes Structure the recommended continuation, but Structure is still directly revisitable from Journey.

## Structure

Structure makes the arrangement itself the interface.

- Show the ordered section list directly.
- Add Section is a short task.
- Choosing a common section type adds it immediately at an 8-bar default in the preview.
- Tap a section row to rename it, change bars, reorder, duplicate, or delete it.
- Keep a simple explicit attestation such as **Structure matches the song** before Continue recommends Tracks.
- Do not require type → bars → Add → Done for every section.

## Tracks

Tracks keeps the successful direct multi-select interaction.

- Short instruction: **Choose everything you hear in the song.**
- No Step/Checkpoint/status chrome.
- Keep custom-track entry compact.
- Give the continuation action clear separation from the custom-track controls.

## Section Study and Review Map

The isolated preview may show prerequisite/placeholder states, but the full specialized editors remain V6 until the shell is approved physically.

Section Study genuinely needs a structure and at least one track. If context is missing, explain what is missing and provide direct routes to fix it instead of showing dead locked rows.

Review Map stays visible in Journey so the project shape remains understandable, but its full editor is not migrated yet.

## Notes hub

Notes become a canonical cross-project library. Each note can know project, type, phase/context, musical section/context, and timestamps. A project Notes entry opens the same system filtered to that project.

Do not require manual tagging for context FIRE already knows.

## Fundamentals polish gate

Before migrating specialized editors or adding a Babel/FIRE signature treatment, the shell must pass a physical fundamentals gate:

- **Content-aware scrolling:** short phone pages that fit the real visual viewport do not create root scrolling or rubber-band drift. Only genuinely tall pages receive Safari scroll-end clearance.
- **Page necessity:** every visible element must support the page’s primary musical task, necessary context/navigation, or progressive disclosure. Duplicated workflow explanation and redundant escape/continuation controls are removed.
- **Shared rhythm:** title offsets, subtitle spacing, grouped-row density, action placement, control states, and bottom breathing room should feel like one system across Projects, Project Home, Song Setup, Structure, Tracks, and preview placeholders.
- **Real-state testing:** review short, partial, completed, and genuinely tall states at realistic phone heights rather than judging only a generous desktop-like viewport.
- **No signature compensation:** progress-path, animation, or other Babel-specific delight remains deferred until the plain shell is calm and useful on its own.

## iPhone / iPad adaptation

### Universal adaptive interface

FIRE has one product logic, hierarchy, and interaction model across device classes.

- Project Home remains the hub.
- Work screens remain focused.
- Back/navigation semantics do not change by device.
- Completion, selection, Journey, and Continue behavior do not change by device.
- Presentation may adapt to available space: column count, content width, spacing, and sheet placement can change when useful.
- Respect the real visual viewport for scrolling/end clearance.
- Do not create “iPhone FIRE” and “iPad FIRE” as separate product experiences.

## Technical stability

Unless a later requirement proves otherwise, preserve:

- `production-projects-v1`
- schema 5
- stable project/section/track/range/event IDs
- migrations
- continuous timeline model
- Map → Skeleton invalidation/dependencies
- durable notes
- browser persistence

The preview uses `production-projects-v1-v7-preview` and must never write to the production key.

## Isolated preview contract

The prototype lives under `/v7-preview/`.

- Production root stays V6 during physical review.
- Preview may clone production data into its sandbox key.
- Preview edits only the sandbox copy.
- Current preview scope: Projects, Project Home, Song Setup, simplified Structure, Tracks, Section Study prerequisite/handoff, Review Map placeholder, project Notes view.
- Treat the preview as disposable product evidence, not a permanent second architecture.

## Approval gate

Do not replace the production shell or migrate the specialized Section Study / Review Map / Skeleton interiors until the lighter Project Home + focused work-screen shell passes physical iPhone Safari review.

The primary approval question is:

> Can the musician open a project and start doing useful musical work without thinking about how FIRE is organized?
