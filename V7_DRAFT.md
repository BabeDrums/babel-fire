# Babel FIRE — Guided Workspace Redesign (Draft)

**Status:** G7 is the isolated successor preview under `/v7-preview/`; V6 remains production until G7 is physically approved and deliberately promoted. `FIRE_CORE.md` governs cross-generation product doctrine; this file governs the G7 shell and must not redefine Recreation, Original, or learning semantics in conflict with FIRE Core.

## Why G7 exists

V6 became too focused on representing workflow hierarchy. Phase homes, Step states, Roadmap, Back history, and a custom center navigator made the musician think about FIRE's organization instead of the music.

G7 asks a simpler question:

> Can FIRE get the musician into useful musical work without making them think about FIRE's organization?

The shell should feel like a calm production companion: one obvious next action, automatic preservation of work, direct revisiting, and only as much interface as the current decision needs.

## Naming + technical continuity

Use **G7** in normal product conversation. Keep existing technical identifiers unless a separate migration reason appears:

- `V7_DRAFT.md`
- `/v7-preview/`
- `production-projects-v1-v7-preview`

The preview must never write to V6's `production-projects-v1` key.

## Core shell principles

1. **One obvious next action.** Project Home recommends one current task through Continue.
2. **Do not repeat the current task.** Journey must not duplicate the same current work already presented by Continue.
3. **Flatten before adding navigation.** Do not solve hierarchy with another navigator.
4. **One job per work screen.** Song Setup, Structure, Tracks, Section Study, Review Map, Session, Draft, and Bounce get focused workspaces when they contain real work.
5. **Progress is inferred.** The musician edits musical information; FIRE derives completion.
6. **Guided forward, flexible backward.** Continue guides forward; completed work remains revisitable; upcoming work can remain inspectable unless missing context makes it impossible.
7. **Project Home is the hub.** Continue + Journey + useful Notes access replace duplicate overview/roadmap navigation.
8. **Notes must earn attention.** A dead/empty Notes destination does not compete on Project Home. Existing useful project notes remain reachable.
9. **Use familiar platform patterns.** Prefer standard back navigation, grouped lists, forms, concise sheets, and shallow hierarchy.
10. **Keep the musical engines.** Preserve stable IDs, migrations, timeline semantics, invalidation, Skeleton dependencies, durable notes, and browser persistence.

## Information architecture

### App level

Future genuine top-level areas may include Projects and Notes, but do not add a Projects/Notes tab bar until a real cross-project Notes hub exists.

### Project level

Opening a project lands on one Project Home containing:

- project identity + project actions
- **Continue** — exactly one recommended current destination
- **Journey** — orientation, completed-work revisiting, and understandable upcoming work
- project Notes access only when it has something useful to show in the current shell

There is no separate Roadmap destination.

### Work level

Work pages push directly from Project Home and return directly to it.

For Recreation / The Map, the current G7 work sequence is:

- Song Setup
- Structure
- Tracks
- Section Study
- Review Map

The UI does not need Step/Checkpoint labels. The Map is a Journey grouping in product logic, not an intermediary screen the musician must enter.

## Navigation model

The V6 center context navigator does not carry forward.

Navigation remains shallow:

- Projects → Project Home → Work screen
- Back from work returns to Project Home
- Continue advances through recommended work without building unnecessary browser-history depth
- Journey revisits completed work and exposes upcoming work
- the current recommended work is represented by Continue, not repeated as a second Journey row

## Projects

Projects has one job: open or create a project.

- Persistent `+` is the single create affordance.
- Empty state is only `No projects yet.`
- Project title is primary; artist + type are secondary.
- No root-screen Roadmap/progress chrome.
- During G7 physical review, keep one tiny subordinate **`G7 · <commit>`** identifier near the Projects title so Babel can confirm a newly deployed build even when a pass is mostly underground.
- The identifier is review traceability, not permanent product chrome or a prototype banner.

## Project Home — Shell Freeze behavior

Project Home should feel like a document home, not a dashboard.

### Continue

- One emphasized grouped destination.
- Owns the current recommended task.
- Shows only the task name + minimum useful context.

### Journey

- Does **not** repeat the current Continue task.
- Shows completed work with quiet completion language so it remains revisitable.
- Shows upcoming work quietly and directly.
- Do not stack `Journey` + `The Map` as two adjacent labels when there is only one active phase worth showing; avoid double-label hierarchy.
- Future phases remain visible as a quiet compact collection rather than one dense explanatory sentence.
- Avoid Recommended / In progress / Current / Phase X of Y / percentages when hierarchy already communicates position.

### Notes

- If the project already has saved notes, expose Project Notes quietly and keep them revisitable.
- If Notes has no creation/action value and there are no notes, hide that dead destination from Project Home.
- A future real Notes system can restore a stronger entry once it earns the space.

## Shared header hierarchy

Shell Freeze establishes three header archetypes:

1. **Projects root** — strongest app/root identity.
2. **Project Home** — strong song/project identity.
3. **Work page** — compact task title + optional minimum-useful subtitle.

Work pages must not use the same oversized title scale as Projects or Project Home. Content-heavy musical tasks need more vertical room than root identity screens.

## Visual semantics

Use one meaning per visual state:

- **Selection** — restrained selected surface/border; no completion checkmark.
- **Completion** — ring/check language.
- **Status/value** — concise text when text is the information itself.
- **Navigation** — row + chevron when opening another destination.
- **Primary progression** — strongest compact button treatment on the work page.

Do not show two indicators for one state. Prove hierarchy in grayscale before adding signature color/personality.

Reference is a setup requirement, not media FIRE needs to own. The user confirms the reference is imported into their production/session environment; FIRE stores only completion state. Do not request/upload/retain the media unless a future feature genuinely needs it.

## Song Setup

Song Setup is one dedicated grouped form:

- Reference
- Tempo
- Meter
- Grid alignment
- First Listen

No collapse state. No Step list. No competing phase navigation. Continue to Structure only appears when Setup is complete.

## Structure

Structure makes the arrangement itself the interface.

- Show the ordered section list directly.
- Add Section is part of the same arrangement group once sections exist.
- Common section types add immediately at an 8-bar preview default.
- Tap a section row to rename, change bars, reorder, duplicate, or delete.
- **Structure matches the song** is integrated as a quiet final row of the arrangement group rather than a competing standalone card.
- Continue to Tracks appears only after Structure is verified.

## Tracks

Tracks keeps direct multi-select.

- Instruction: **Choose everything you hear in the song.**
- No Step/Checkpoint/status chrome.
- Tiles are intentionally denser than before so musical content, not shell chrome, owns the page.
- Custom-track entry remains one compact control.
- Continue is separated from selection/custom controls and appears once the task has started.

## Section Study + Review Map placeholders

These editors are not migrated during Shell Freeze.

- Missing real prerequisites may use an actionable prerequisite surface with direct routes to fix context.
- If prerequisites are satisfied but the editor is simply not built yet, use a quiet truthful placeholder rather than a large card that looks like a feature.
- Do not expose internal V6 migration/approval language.

## Natural scrolling + adaptive layout

FIRE has one product logic across device classes.

- Document height determines whether a page scrolls naturally.
- Never toggle root overflow from `VisualViewport` movement.
- Tall pages get modest CSS-only Safari end clearance.
- Modal sheets may temporarily lock body scrolling while open.
- Project logic, navigation semantics, completion, selection, Journey, and Continue behavior do not change between iPhone and iPad.
- Presentation may adapt: column count, spacing, content width, and sheet placement can change with available space.

Do not create separate iPhone and iPad FIRE products.

## Shell Freeze acceptance gate

Before FIRE Core breadboarding begins, the deployed G7 preview should pass physical review for:

- Projects remains calm and the tiny `G7 · <commit>` trace is readable but subordinate.
- Project Home shows the current task once.
- Journey is understandable without Journey/The Map label clutter.
- Empty Notes does not compete; existing Notes remains reachable.
- Work-page headers are compact and consistent.
- Structure verification feels like part of the arrangement.
- Tracks is denser without becoming cramped.
- Section Study / Review Map unfinished states are truthful and quiet.
- Natural scrolling works on short and tall Safari pages.
- 390px / 440px / 820px layouts preserve the same product model.
- Back behavior and direct revisiting remain reliable.

This is the final broad generic shell-polish pass for a while. Once physically approved, stop re-litigating ordinary headers/spacing/cards and move to the FIRE Core breadboard.

## After Shell Freeze

Next sequence:

**G7 Shell Freeze → FIRE Core breadboard → thin end-to-end FIRE Core spine → real-project validation**

The breadboard is expected to be primarily underground product-logic/documentation work: places, affordances/actions, connections, decisions, evidence, Logic handoffs, evaluation, and carry-forward context for Original + Recreation end to end.

Only after that agreement should the thin complete FIRE Core spine become runtime functionality. Signature FIRE glow, pixel Fire/badges, Babel World, accounts, learning hub, and broader platform work remain deferred.

## Technical stability

Until a requirement proves otherwise, preserve:

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
