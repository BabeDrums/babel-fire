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
11. **Same meaning uses the same visual grammar.** If two controls perform the same kind of choice/action, reuse the same component family instead of inventing near-duplicates.
12. **Different meaning may use different accessories.** Visual unity does not justify fake chevrons, menus, completion marks, or reorder affordances.
13. **Physical rhythm is a system, not a page decision.** Repeated row/control geometry comes from shared tokens rather than one-off heights and gaps.
14. **Back means where the musician actually came from.** Visible Back and browser/history Back must agree whenever G7 has a usable in-app route history.

## Interaction grammar

- **Inline** — choose, toggle, classify, confirm, or evaluate something already in the current task.
- **Sheet** — create/edit/manage a discrete thing while staying in context.
- **Navigation** — enter another meaningful workspace.
- **Menu / secondary affordance** — utilities that should not compete with musical work.

Consistency comes from semantic meaning, not from forcing every interaction into one container.

## Physical rhythm and visual grammar primitives

G7 should not accumulate one-off versions of the same control. Reuse these families and geometry rules:

- **Grouped surface** — one material/radius/separator language for Projects, Project Home progression, Setup, Structure arrangement, verification, and other row-based collections. The canonical grouped page-row height is **64px**; accessories may differ by function.
- **Selection surface** — one connected outer rounded container with internal hairline dividers for direct option sets. Section types and Tracks share this family. Canonical selection-cell height is **52px**. Section type is single-select; Tracks is multi-select and may add checks.
- **Segmented control** — compact mutually exclusive choices such as **Original / Cover** and **4 / 8 / 12 / 16 / Custom** bars. The segments share one outer container instead of becoming five independent rounded buttons.
- **Page action footer** — the final non-sticky region of a work page for Continue/Done. Short pages use flexible document space so the action naturally occupies a stable lower region; long pages push it below the content and scroll normally.
- **Sheet action hierarchy** — primary actions are filled; secondary/cancel actions remain quieter but retain a discernible button shape; destructive actions use the same geometry with danger treatment.
- **Spacing scale** — prefer the shared 4 / 8 / 12 / 16 / 20 / 24 rhythm rather than arbitrary page-specific gaps.

Do not visually clone unrelated controls just to make screenshots symmetrical.

## State and accessory grammar

Use visual marks only when their meaning is true:

- `○` = incomplete/upcoming progression state
- `→` = current/recommended progression state
- `✓` = completed progression state or explicitly selected multi-select choice, according to context
- selected fill = chosen option
- drag handle = reorderable object
- chevron = navigation deeper
- `•••` = management/actions
- `+` = create/add the primary discrete object for the current view

A Structure section row is an arrangement object, not a completed task, so merely existing does **not** earn a checkmark.

## Header and title scaffold

Every G7 screen uses the same structural scaffold:

- a stable 44px-equivalent toolbar region first
- Back occupies the leading slot when applicable
- `+` or `•••` occupies the trailing slot when applicable
- toolbar and title are one visual system with a tight, shared vertical relationship rather than a detached action floating high above the title
- the page title begins at the same vertical location across Projects, Project Home, and work pages
- one coherent page-title scale on phone instead of a 40 → 34 → 30 staircase
- project metadata may sit quietly below the project title

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
- project rows use the shared 64px grouped-row rhythm
- per-card `•••` visually belongs to the card and remains a 44px-equivalent target
- opening a card's action menu must not silently change the active/current project
- build trace remains quiet bottom-center review metadata only

Projects is a reference for the shared grouped-row material and vertical rhythm, not a mandate that other row types copy its chevron/ellipsis accessories.

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
- text/name inputs request word capitalization from the mobile keyboard with `autocapitalize="words"`
- do not programmatically force title casing; intentional stylization must remain possible
- avoid aggressive autocorrection for song/artist/section/track names
- opening the sheet itself should not summon a keyboard
- Cancel is a real secondary button, not floating label-like text

This compact placeholder-only treatment is specific to the simple project form; do not remove labels from more complex forms merely for visual minimalism.

## Project Home

Project Home answers: what project is this, and what deserves attention next?

- title + quiet metadata
- current Cover shell work is **Setup → Structure → Tracks**
- all current mapping steps live in **one coherent progression group** rather than splitting the recommended step into a separate card
- progression rows use the same 64px grouped-row rhythm as the other page-level groups
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

- Setup
- Structure
- Tracks

All use the shared header/title scaffold. Default helper copy is removed when the controls are self-explanatory. When a work page exposes a final Continue/Done action, it uses the shared non-sticky page action footer and flexible document layout rather than inventing page-specific placement.

### Setup

One grouped surface using the shared 64px row rhythm:

- Reference
- Tempo
- Meter
- Grid
- Listen

Tempo remains an inline value field with 16px+ input behavior and an integrated focus treatment. Continue appears only when canonical setup requirements are satisfied and uses the shared page action footer.

The data field may remain named `firstListen` internally for compatibility; the musician-facing row is simply **Listen**.

### Structure

Structure is an ordered arrangement, not a two-step create-then-fix workflow.

Arrangement rows use the same 64px grouped-row physical rhythm as Projects while retaining Structure-specific accessories. They show:

- index
- section name
- bar length
- permanent reorder handle

Do **not** add a project-style chevron, `•••`, or completion check merely for visual similarity. Row tap/edit and reorder remain distinct actions.

**Add Section** lives in the trailing Structure toolbar `+` and opens one builder sheet:

- choose Intro / Verse / Pre-Chorus / Chorus / Bridge / Instrumental / Outro / Custom
- section types live in one connected two-column Selection Surface rather than eight independent rounded cards
- choose **4 / 8 / 12 / 16 / Custom** bars before insertion using one five-segment control
- tapping a section type alone does not create anything
- Add commits one valid section
- the builder stays open after Add so repeated arrangement entry is fast
- retain the chosen bar length, clear/re-arm section type, and show concise inline confirmation
- Done closes the builder
- Custom type/length reveal only their required fields
- the visible `Add Section` sheet heading is omitted because the toolbar action already supplies context; the dialog keeps an accessible name

**Edit Section** edits name and bar length only, plus Duplicate/Delete utilities. It reuses the same bar segmented control. Reordering does not live in Edit. The visible `Edit Section` sheet heading may be omitted when the tapped section already supplies enough context; the dialog remains accessibly named.

Reordering belongs to the visible row handle:

- direct pointer/touch drag path
- keyboard Arrow Up/Down alternative on the handle
- roughly 44px target
- reordering invalidates Structure verification but preserves section identity/data

**Accurate** is the one-word verification row below the arrangement. It is a separate grouped surface using the same 64px row/material system rather than a special tint. It means “the current Structure is accurate to the song.” Continue appears only after current Structure completion and uses the shared page action footer.

### Tracks

Tracks remains a fast musician-facing multi-select surface, not a generic settings list.

- common tracks remain direct inline multi-select
- phone choices use one connected two-column **Selection Surface** rather than a collection of individually rounded cards
- selection cells use the same 52px geometry as Structure section-type choices
- Tracks is the multi-select variant and adds visible checks to selected choices
- selected state should be clear without turning every choice into a heavy slab
- **Add Track** moves to the trailing toolbar `+`; there is no special `Other` tile mixed into the selection surface
- toolbar `+` opens the compact named-track sheet; its visible heading may remain omitted because the source action already supplies context
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

The action group remains concise; Cancel uses the shared secondary button treatment so it reads as tappable without competing with the management actions.

Edit opens the compact grouped Title/Artist form above. Reset and Delete are uncommon destructive actions and require a short confirmation step because G7 does not provide a real undo path. The first action menu stays terse; confirmation is where consequence/context belongs.

## Sheets / keyboard / scrolling

- sheets are concise create/edit/manage surfaces, not hidden navigation pages
- do not show a grabber/drag indicator on custom sheets that cannot actually drag, resize, or dismiss through that affordance
- visible sheet headings are conditional: omit them when the source action already makes the temporary surface unambiguous; keep them when they add consequence or necessary context (for example `Reset progress?` and `Delete project?`)
- primary/secondary/destructive actions reuse the shared sheet button geometry
- opening a selection/manage sheet does not automatically summon a keyboard
- controls remain reachable above the iOS software keyboard
- background scrolling locks only while the modal sheet is open
- no VisualViewport root-scroll machinery
- normal document height decides whether a page scrolls

## Acceptance gate before FIRE Core breadboard

G7 is not frozen until physical review says generic UI fundamentals are coherent enough to stop redesigning them.

Review for:

- stable title position/scale across Projects → Project → work
- toolbar Back/`+`/`•••` feels visually related to the title rather than detached above it
- Cover naming feels natural
- New Project no longer changes shape when type changes
- Original/Cover and grouped Title/Artist have one clear spacing rhythm
- Title/Artist focus preserves one clean rounded group outline with no clipped corners
- compact New/Edit project forms remain obvious without redundant visible headings/labels
- Title/Artist fields keep stable semantics and mobile word capitalization
- `•••` feels like one control everywhere and card actions do not mutate active-project state
- project action wording is terse; Cancel reads as a real secondary button; destructive actions do not execute accidentally
- recent-first Projects order feels useful without category clutter
- Project Home reads as one calm progression rather than a current-task card plus a second system
- **Setup / Structure / Tracks** feels concise and natural
- grouped page rows across Projects, Project Home, Setup, Structure, and verification share the 64px rhythm without visually jumping between screens
- Setup uses Reference / Tempo / Meter / Grid / Listen without helper-copy noise
- work-page Continue/Done actions share one lower page-action region without becoming sticky browser-bar competitors
- visible Back retraces Setup → Structure → Tracks when that is the real path, while direct entry safely returns to Project Home
- browser/history Back agrees with visible Back
- Done from Tracks returns Home without a Home → Back → Tracks loop
- Structure rows keep honest Structure-specific controls and no fake completion marks
- Structure Add Section is discoverable from the toolbar `+`
- Structure builder is fast, predictable, and uses a connected section-selection surface rather than button soup
- 4 / 8 / 12 / 16 / Custom reads as one segmented bar-length control
- **Accurate** reads naturally as Structure verification without a special tint
- reorder feels direct on device; Edit remains compact
- Add Section and Tracks visibly belong to the same connected Selection Surface family
- Tracks toolbar `+` is a clean/discoverable Add Track affordance and no `Other` card is needed
- Tracks completion reflects explicit confirmation rather than merely having one selected track
- redundant sheet headings are gone while consequence-bearing confirmation titles remain
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
