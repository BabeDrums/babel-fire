# Babel FIRE — Guided Workspace Redesign (Draft)

**Status:** G7 is the isolated successor preview under `/v7-preview/`; V6 remains production until G7 is physically approved and deliberately promoted. `FIRE_CORE.md` governs cross-generation product doctrine; this file governs the G7 shell and must not redefine Original, Recreation, or learning semantics in conflict with FIRE Core.

G7 uses **Cover** as the musician-facing label for the canonical FIRE Core **Recreation** workflow. Internal compatibility may continue using the legacy `study` project type; public naming does not require a storage migration.

## Why G7 exists

G7 exists to make the shell disappear behind the music.

Core question:

> Can FIRE get the musician into useful musical work without making them think about how FIRE is organized?

The shell is the reusable interaction and layout grammar: headers, navigation, sheets, forms, grouped rows, selection/completion states, scrolling, editing, and responsive behavior. Shell approval does **not** mean final animation, personality, signature visuals, every future musical workspace, or FIRE Core's final Map/checkpoint architecture is finished.

The current **Setup → Structure → Tracks** flow is deliberate **shell/workspace fixture content**. It exercises page scaffolds, row/value grammar, navigation, sheets, selection, creation, reordering, confirmation, and responsive behavior. It must not be interpreted as a frozen definition of The Map, a promise of exactly three checkpoints, or proof that FIRE Core should keep these exact interactions. FIRE Core breadboarding will reconsider the actual musical journey from first principles after the generic shell is physically approved.

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
11. **Same meaning uses the same visual grammar.** If two controls perform the same kind of choice/action, reuse the same component family instead of inventing near-duplicates.
12. **Different meaning may use different accessories.** Visual unity does not justify fake chevrons, menus, completion marks, or reorder affordances.
13. **Physical rhythm is a system, not a page decision.** Repeated row/control geometry comes from shared tokens rather than one-off heights and gaps.
14. **Back means where the musician actually came from.** Visible Back and browser/history Back must agree whenever G7 has a usable in-app route history.
15. **State must not move the object.** Repeated labels keep the same typography and anchor across current/done/upcoming/selected state; state uses fill, color, or a semantic accessory instead.
16. **Fixtures do not become product architecture by polish.** Shell work may prove a control or interaction family without freezing the FIRE Core phase/checkpoint structure that currently demonstrates it.

## Interaction grammar

- **Inline** — choose, toggle, classify, confirm, or evaluate something already in the current task.
- **Sheet** — create/edit/manage a discrete thing while staying in context.
- **Navigation** — enter another meaningful workspace.
- **Menu / secondary affordance** — utilities that should not compete with musical work.

Consistency comes from semantic meaning, not from forcing every interaction into one container.

## Physical rhythm and visual grammar primitives

G7 should not accumulate one-off versions of the same control. Reuse these families and geometry rules:

- **Grouped surface** — one material/radius/separator language for Projects, Project Home progression, Setup, Structure arrangement, verification, and other row-based collections. The canonical grouped page-row height is **64px**; accessories may differ by function.
- **Shared row-content grid** — primary row labels use one stable leading inset/typography role; trailing metadata and accessories occupy predictable slots rather than pushing the label around. Project Home state changes must not change label weight.
- **Trailing value control** — editable/value rows use one compact trailing control grammar so values such as Tempo and Meter read as deliberate controls rather than loose text. Value controls share geometry, material, alignment, and focus behavior while preserving the right input semantics for each value.
- **Selection surface** — one connected outer rounded container with internal hairline dividers for direct option sets. The parent owns the outer border/radius. Child choices remain square to that parent and communicate selection through fill/contrast rather than nested outlines. Section types and Tracks share this family. Canonical selection-cell height is **52px**. Section type is single-select; Tracks is multi-select.
- **Segmented control** — compact mutually exclusive choices such as **Original / Cover** and **4 / 8 / 12 / 16 / Custom** bars. The parent owns the outer geometry; segments do not draw competing rounded outlines.
- **Page action footer** — the final non-sticky region of a work page for Continue/Done. Short pages use flexible document space so the action naturally occupies a stable lower region; long pages push it below the content and scroll normally.
- **Sheet action hierarchy** — primary actions are filled; secondary/cancel actions are quieter but still use a subtle filled button treatment rather than reading as empty borders; destructive actions use the same geometry with danger treatment. Paired form actions use the shared two-action composition; a standalone action-sheet Cancel spans the same content width as the action group above it rather than becoming a small centered control.
- **Sheet spacing grammar** — sheet inset and distinct conceptual-group separation use the stronger rhythm; tightly related controls use the smaller rhythm. Current G7 uses a **20px** major-group/inset rhythm and a **16px** content-to-action gap where that relationship applies. Related custom fields stay visually attached to the control that revealed them.
- **Spacing scale** — prefer the shared 4 / 8 / 12 / 16 / 20 / 24 rhythm rather than arbitrary page-specific gaps. Optical exceptions are allowed when deliberate.

Do not visually clone unrelated controls just to make screenshots symmetrical.

## State and accessory grammar

Use visual marks only when their meaning is true:

- `○` = incomplete/upcoming progression state
- `→` = current/recommended progression state
- `✓` = completed progression/state where completion is actually true
- selected fill = chosen option
- drag handle = reorderable object
- chevron = navigation deeper **only when the row still needs that navigation cue**
- `•••` = management/actions
- `+` = create/add the primary discrete object for the current view

Do not stack redundant navigation indicators. A Project Home progression row already has a state mark and a fully tappable row, so it does not also need a chevron. A Projects row is already a large open target with a separate `•••` management control, so it also omits the chevron. Utility rows such as Notes may keep a chevron when it is the clearest remaining navigation cue.

A Structure section row is an arrangement object, not a completed task, so merely existing does **not** earn a checkmark. Tracks selection is already clear through selected fill and does **not** add redundant checkmarks.

## Header and title scaffold

Every G7 screen uses the same structural scaffold:

- a stable 44px-equivalent toolbar region first
- Back occupies the leading slot when applicable
- `+` or `•••` occupies the trailing slot when applicable
- toolbar and title are one visual system with a tight, shared vertical relationship rather than a detached action floating high above the title
- trailing create/manage actions use a subtle control surface so they read as intentional controls rather than isolated glyphs; Back remains a quieter navigation affordance
- the page title begins at the same vertical location across Projects, Project Home, and work pages
- one coherent page-title scale on phone instead of a 40 → 34 → 30 staircase
- project metadata may sit quietly below the project title

The trailing slot itself is part of the scaffold and should not be nudged independently per page. If the `+` feels visually stranded, solve the shared toolbar/action treatment before relocating it and re-check `•••`, Back, title alignment, and touch geometry together.

The `•••` action is one reusable visual control whether it appears in a project row or the trailing toolbar. Its location may change; its visual size/meaning should not.

A toolbar `+` consistently means create/add the primary discrete thing for that view:

- Projects → New Project
- Structure → Add Section
- Tracks → Add Track

## Navigation and Back behavior

G7 navigation must feel like a native hierarchy rather than a collection of hash routes.

- entering a work page from Project Home creates a real history step
- Continue from Setup → Structure and Structure → Tracks adds the next work page to that history rather than replacing the current page
- visible Back retraces that actual in-app path when available
- browser/history Back must resolve to the same previous work page
- direct entry to a work page from Project Home backs to Project Home
- a refreshed/deep-linked work page without usable G7 history safely falls back to Project Home
- **Done** on Tracks is a completion action: it confirms Tracks and returns to Project Home without creating a Home → Back → Tracks loop
- Project Home Back returns to Projects; a direct/deep-linked Project Home safely falls back to Projects

## Projects

Projects has one job: open or create.

- one ungrouped list by default; do not split Originals and Covers into permanent sections yet
- sort by meaningful project activity (`lastActivityAt`), not by accidental opening
- older preview records without activity metadata normalize safely from existing timestamps
- project title is primary; artist + type are secondary
- public project types are **Original** and **Cover**
- internal legacy `study` compatibility is preserved
- repeated project entries are called **project rows**; they use the shared 64px grouped-row rhythm
- the whole project row's main area opens the project; it does not need a redundant chevron
- per-row `•••` visually belongs to the row and remains a 44px-equivalent target
- opening a row's action menu must not silently change the active/current project
- build trace remains quiet bottom-center review metadata only

Projects is a reference for the shared grouped-row material and vertical rhythm, not a mandate that other row types copy its accessories.

## New Project / Edit Project

New Project opens in one stable sheet. Do not reveal required fields only after project-type selection.

- **Original | Cover** is visible immediately in New Project as one segmented control
- fields are always **Title** and **Artist** in the same positions for both types
- Title + Artist live in one grouped field surface with one internal separator rather than two unrelated floating boxes
- switching type changes validation/behavior, not geometry or field semantics
- Original requires Title; Artist may be empty
- Cover requires Title + Artist
- compact project create/edit sheets do not need redundant visible `New Project` / `Edit Details` headings or visible Title/Artist field labels when the two-field context is already clear
- Title/Artist remain the input placeholders and accessible semantic labels so clearing a field restores visible context and assistive technology still receives the field meaning
- Title/Artist focus belongs to the **outer grouped field surface**; individual rectangular focus rings must not clip/cut the rounded group corners
- the focused row may receive a subtle internal state, but the group keeps one clean rounded focus emphasis
- **Original / Cover → Title/Artist** uses the stronger major-group gap; Title/Artist → actions uses the standard action gap rather than repeating the same spacing everywhere
- text/name inputs request word capitalization from the mobile keyboard with `autocapitalize="words"`
- Return/Next from Title advances focus to Artist in both create and edit flows; field order and keyboard progression agree
- do not programmatically force title casing; intentional stylization must remain possible
- avoid aggressive autocorrection for song/artist/section/track names
- opening the sheet itself should not summon a keyboard
- Cancel is a real secondary button, not floating label-like text or an empty outline

This compact placeholder-only treatment is specific to the simple project form; do not remove labels from more complex forms merely for visual minimalism.

## Project Home

Project Home answers: what project is this, and what deserves attention next?

- title + quiet metadata
- current Cover **shell fixture** work is **Setup → Structure → Tracks**; this is not the frozen FIRE Core Map
- all current fixture steps live in **one coherent progression group** rather than splitting the recommended step into a separate card
- progression rows use the same 64px grouped-row rhythm as the other page-level groups
- completed/current/upcoming state changes color/fill/accessory emphasis without changing the row label's size/weight/anchor
- the state mark plus fully tappable row is enough; progression rows do not add a redundant chevron
- the progression itself communicates completion; do not add a separate `Song map complete.` card when all three checked rows already say the same thing
- no helper sentence under the current destination when the title/state already explains it
- no visible `Continue` or `Journey` taxonomy
- Section Study is not a mandatory shell waypoint
- Review Map is not exposed as a placeholder destination merely to fill progression
- saved Notes may appear as a separate utility group; empty Notes stays hidden
- do not dump future phases onto Project Home merely to imply completeness

Original remains first-class even before its full FIRE Core workflow is breadboarded; unfinished copy stays musician-facing.

## Work pages

Current Cover **shell-fixture** workspaces:

- Setup
- Structure
- Tracks

These exist to prove transferable shell mechanics. FIRE Core breadboarding may rename, regroup, deepen, replace, or remove them if real musical workflow evidence points elsewhere.

All use the shared header/title scaffold. Their first primary content surface begins at the same vertical anchor so moving Setup → Structure → Tracks does not make the work area jump. Default helper copy is removed when the controls are self-explanatory. When a work page exposes a final Continue/Done action, it uses the shared non-sticky page action footer and flexible document layout rather than inventing page-specific placement.

Projects → Project Home may retain an intentional hierarchy change because Project Home carries project identity metadata; do not delete useful context merely to force mathematical alignment with the root library.

### Setup

One grouped surface using the shared 64px row rhythm:

- Reference
- Tempo
- Meter
- Grid
- Listen

Setup labels use the shared primary row-label role/leading inset. Tempo and Meter use one compact trailing-value control grammar so their values feel intentionally placed rather than like loose metadata. Tempo remains a 16px+ inline numeric/text value field with integrated group focus behavior. Continue appears only when canonical fixture requirements are satisfied and uses the shared page action footer.

The data field may remain named `firstListen` internally for compatibility; the musician-facing row is simply **Listen**.

### Structure

Structure is an ordered arrangement, not a two-step create-then-fix workflow.

Arrangement rows use the same 64px grouped-row physical rhythm and primary label anchor as Setup while retaining Structure-specific semantics. Visible rows show:

- section name
- bar length
- permanent reorder handle

Visible ordinal numbers are removed because vertical order already communicates sequence and the number column pushed section labels off the shared text anchor. Accessible edit/reorder labels preserve the section ordinal so assistive interaction still has explicit ordering context.

Do **not** add a project-style chevron, `•••`, or completion check merely for visual similarity. Row tap/edit and reorder remain distinct actions.

**Add Section** lives in the trailing Structure toolbar `+` and opens one builder sheet:

- choose Intro / Verse / Pre-Chorus / Chorus / Bridge / Instrumental / Outro / Custom
- section types live in one connected two-column Selection Surface rather than eight independent rounded cards
- the parent owns the rounded outline; selected type uses fill without a nested inner border
- choose **4 / 8 / 12 / 16 / Custom** bars before insertion using one five-segment control
- Section Type/custom name form one conceptual group; Bars/custom length form a second group; the two groups use the stronger sheet gap while revealed fields stay close to their parent controls
- tapping a section type alone does not create anything
- Add commits one valid section
- the builder stays open after Add so repeated arrangement entry is fast
- retain the chosen bar length and clear/re-arm section type after insertion
- do **not** show redundant success copy such as `Added Intro · 8 bars`; the visible arrangement update is the confirmation
- Done closes the builder
- Custom section copy is simply **Section**; custom bar entry accepts positive integer digits only and requests the numeric mobile keyboard
- the visible `Add Section` sheet heading is omitted because the toolbar action already supplies context; the dialog keeps an accessible name

**Edit Section** edits name and bar length only, plus Duplicate/Delete utilities. It reuses the same bar segmented control, numeric custom-length semantics, and semantic sheet grouping. Reordering does not live in Edit. The visible `Edit Section` sheet heading may be omitted when the tapped section already supplies enough context; the dialog remains accessibly named.

Reordering belongs to the visible row handle:

- direct pointer/touch drag path
- keyboard Arrow Up/Down alternative on the handle
- roughly 44px target
- reordering invalidates Structure verification but preserves section identity/data

**Accurate** is the one-word verification row below the arrangement. It is a separate grouped surface using the same 64px row/material system rather than a special tint. It means “the current Structure is accurate to the song.” Continue appears only after current Structure completion and uses the shared page action footer.

### Tracks

Tracks remains a fast musician-facing multi-select shell fixture, not a generic settings list.

- common tracks remain direct inline multi-select
- phone choices use one connected two-column **Selection Surface** rather than a collection of individually rounded cards
- regular-width layouts may use three columns, but the final row must rebalance to the available item count instead of leaving filler-looking empty cells
- selection cells use the same 52px geometry and parent-owned outer shape as Structure section-type choices
- Tracks is the multi-select variant; selected fill is the complete visual selection signal and **does not add redundant checkmarks**
- selected state should be clear without turning every choice into a heavy slab
- **Add Track** moves to the trailing toolbar `+`; there is no special `Other` tile mixed into the selection surface
- toolbar `+` opens the compact named-track sheet; visible/placeholder copy is simply **Track** and the heading may remain omitted because the source action already supplies context
- custom names request word capitalization
- selecting one track does **not** prove the track map is complete
- once at least one track exists, **Done** becomes available as the explicit lightweight confirmation that the current track selection represents the song
- track selection changes invalidate that confirmation; pressing Done restores it
- only a confirmed non-empty track selection counts as Tracks complete on Project Home
- Done returns to Project Home rather than forcing Section Study and resets the local work-history endpoint so Back from Home does not reopen Tracks
- Done uses the shared page action footer

The data model records this distinction as track selection plus a separate confirmation state (`tracksVerified`); older preview data without the field normalizes safely to unverified rather than inventing completion.

## Project management sheets

The project-actions sheet does not repeat the song title or add explanatory chrome. It contains only useful management actions:

- Edit
- Reset (Cover only)
- Delete
- Cancel

The action group remains concise. Standalone Cancel uses the shared quiet filled secondary treatment and spans the same sheet content width as the management-action group rather than becoming a small centered control. Paired Cancel + Save/Create/confirm actions remain paired.

Edit opens the compact grouped Title/Artist form above. Reset and Delete are uncommon destructive actions and require a short confirmation step because G7 does not provide a real undo path. The first action menu stays terse; confirmation is where consequence/context belongs.

## Sheets / keyboard / scrolling

- sheets are concise create/edit/manage surfaces, not hidden navigation pages
- do not show a grabber/drag indicator on custom sheets that cannot actually drag, resize, or dismiss through that affordance
- visible sheet headings are conditional: omit them when the source action already makes the temporary surface unambiguous; keep them when they add consequence or necessary context (for example `Reset progress?` and `Delete project?`)
- primary/secondary/destructive actions reuse the shared sheet button geometry; secondary actions remain visually pressable without competing with the primary action
- sheet composition uses intentional major-group vs related-control vs action spacing; content count/flex wrapping must not accidentally decide layout
- obvious multi-field forms use logical keyboard progression; Title Return/Next advances to Artist
- numeric-only fields reject nonnumeric characters rather than merely showing a numeric-looking keyboard
- opening a selection/manage sheet does not automatically summon a keyboard
- controls remain reachable above the iOS software keyboard
- background scrolling locks only while the modal sheet is open
- phone may use the bottom sheet while regular-width iPad uses the centered dialog presentation; semantics/action hierarchy stay identical
- no VisualViewport root-scroll machinery
- normal document height decides whether a page scrolls

## Acceptance gate before FIRE Core breadboard

G7 is not frozen until physical review says generic UI fundamentals are coherent enough to stop redesigning them.

This approval is **shell approval only**. It must not be recorded as approval of Setup/Structure/Tracks as FIRE Core's final Map, of exactly three checkpoints, or of the current fixture interactions as final musical workflow.

Review for:

- stable title position/scale across Projects → Project → work
- toolbar Back/`+`/`•••` feels visually related to the title rather than detached above it
- trailing `+`/`•••` feels like an intentional control in the shared toolbar slot without breaking Back/title alignment
- Cover naming feels natural
- New Project no longer changes shape when type changes
- Original/Cover is clearly separated from grouped Title/Artist by the major-group rhythm, while Title/Artist → actions stays intentionally tighter
- Title/Artist focus preserves one clean rounded group outline with no clipped corners
- compact New/Edit project forms remain obvious without redundant visible headings/labels
- Title/Artist fields keep stable semantics, mobile word capitalization, and logical Return/Next progression
- `•••` feels like one control everywhere and project-row actions do not mutate active-project state
- project rows open cleanly without redundant chevrons; the separate `•••` still reads as management
- project action wording is terse; standalone Cancel uses the full action-group width and reads as a real button; destructive actions do not execute accidentally
- recent-first Projects order feels useful without category clutter
- Project Home reads as one calm progression rather than a current-task card plus a second system
- Project Home state marks are sufficient without redundant chevrons and label typography does not grow/shrink when state changes
- **Setup / Structure / Tracks** fixtures feel concise and natural enough to prove the shell without being mistaken for frozen Core architecture
- grouped page rows across Projects, Project Home, Setup, Structure, and verification share the 64px rhythm without visually jumping between screens
- Setup and Structure primary labels share one left anchor/typography role
- Setup / Structure / Tracks first content starts at the same vertical position
- Setup uses Reference / Tempo / Meter / Grid / Listen without helper-copy noise; Tempo and Meter share one coherent trailing-value grammar
- work-page Continue/Done actions share one lower page-action region without becoming sticky browser-bar competitors
- visible Back retraces Setup → Structure → Tracks when that is the real path, while direct entry safely returns to Project Home
- browser/history Back agrees with visible Back
- Done from Tracks returns Home without a Home → Back → Tracks loop
- Structure rows keep honest Structure-specific controls, no visible ordinal column, and no fake completion marks
- Structure order remains understandable and explicit in accessible control labels
- Structure Add Section is discoverable from the toolbar `+`
- Structure builder is fast, predictable, and uses semantic major/related/action grouping rather than a compressed stack
- Add Section/Tracks/Original-Cover selections have parent-owned rounded geometry with no nested selected rectangle
- 4 / 8 / 12 / 16 / Custom reads as one segmented bar-length control; custom bars only accepts positive integer digits
- adding a section does not add redundant success/helper copy
- **Accurate** reads naturally as Structure verification without a special tint
- reorder feels direct on device; Edit remains compact
- Tracks toolbar `+` is a clean/discoverable Add Track affordance and no `Other` card is needed
- Tracks selection remains clear using fill without redundant checks
- Tracks grid adapts its final row to item count/viewport without filler-looking empty slots
- Tracks completion reflects explicit confirmation rather than merely having one selected track
- redundant sheet headings are gone while consequence-bearing confirmation titles remain
- no mandatory learning-flavored route blocks a quick Cover
- custom sheets do not advertise dead drag/resize behavior
- centered iPad dialogs preserve the same modal semantics as phone sheets
- natural scrolling/sheets remain reliable at 390 / 440 / 820
- V6 production data remains untouched

Approval question:

> **Can Babel move through the shell without wondering what kind of UI is going to happen next?**

If yes, stop broad shell polishing.

## After approval

Sequence:

**physical G7 shell approval → FIRE Core breadboard → thin end-to-end FIRE Core spine → real-project validation**

Breadboard Original + Recreation/Cover end to end using places / affordances / connections. For every phase define the entering problem, what FIRE asks the musician to notice, the decision, the Logic action/experiment, evaluation, done criteria, evidence retained, and carry-forward context.

For each actual checkpoint/workspace, choose interaction from the musical mental model rather than from G7 fixture precedent: selection, drag/reorder, connect/group, mark/draw, compare, toggle, direct manipulation, or another interaction is valid when it best represents the decision. Few visible destinations are desirable, but exact checkpoint count is earned by the work rather than fixed at three.

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
