# Babel FIRE — Project Continuity / Handoff Context

## Purpose of this file
This is durable supporting product/design context for Babel FIRE, not a changelog or a report of what has shipped. Begin continuations with `START_HERE.md` and follow the source-of-truth order in `AGENTS.md`. `FIRE_CORE.md` is the canonical current cross-generation product doctrine; version specs describe generation-specific behavior, and this file preserves deeper workflow/history that remains valid under that doctrine.

Inspect current `main`, open PRs, relevant branches, and local changes without overwriting unfinished work. Distinguish shipped, unmerged, and planned work; continue from the latest verified state rather than asking the user to repeat documented decisions.

## Continuity maintenance rule
`CONTEXT.md` is a **living product specification**, not a one-time handoff.

- Keep **one canonical copy** in the root of `BabeDrums/babel-fire`.
- Update it whenever a **locked product decision, learning-framework decision, architecture rule, or important user preference changes**.
- Pure visual tweaks and bug fixes do not need a context rewrite unless they establish a new reusable rule.
- The production branch records shipped implementation; task branches and PRs may contain newer, unmerged work. Code/tests describe implementation state without overriding approved requirements.
- `FIRE_CORE.md` is the source of truth for current cross-generation product doctrine. This file preserves supporting workflow/history, the reference user's design-relevant production profile, and detailed decisions that remain compatible with FIRE Core.
- A new chat should inspect both the current repo and this file before proposing changes.
- Do not make the user repeat the original production assessment or previously settled FIRE decisions.

---

# 1. Product identity

## Name
**Public/product family name:** `Babel FIRE`  
**Inside the app:** usually just `FIRE`  
**GitHub repo:** `babel-fire`

The naming logic is similar to product families like Google Docs / Google Sheets or Adobe Illustrator:
- **Babel** = parent creative ecosystem / family
- **FIRE** = this specific product
- FIRE is intentionally uppercase because it is an acronym

Possible future Babel apps may use the same naming convention (e.g. Babel WATER), but FIRE is the only app in scope right now.

## FIRE acronym
**F — Feel**  
**I — Identify**  
**R — Reason**  
**E — Experiment**

FIRE is a universal production problem-solving loop, not merely a Smithereens-specific feature.

---

# 2. What FIRE is actually for

The **primary purpose** of FIRE is to help someone take **any original musical idea** and turn it into a **finished record**.

The user might begin with:
- a beat
- lyric
- melody
- chord progression
- drum pattern
- instrumental riff
- sound/texture
- voice memo
- title
- concept
- anything else worth keeping

The product should help expand that spark into a complete, intentional song.

## Two project types
FIRE is one app with two project modes:

### Original Song
The main long-term creative workflow.
Goal: start with anything → finish a record.

### Recreation
A first-class standalone cover/reconstruction workflow that can range from faithful Match to Interpretation or full Reimagination. Recreation can develop production judgment through use, but learning is optional and must never be a prerequisite for someone who simply wants to complete a cover efficiently.

**Smithereens by Twenty One Pilots is the first preloaded Recreation.**


### Internal data compatibility
The public project-type name is **Recreation**. Existing stored projects may continue to use the internal type/key `study` for backward compatibility; do not migrate or break saved projects just to rename the UI.

The Smithereens reconstruction started as a way to apply production lessons in practice. The app must not become a procrastination substitute for making music.

**Important rule:** build only what a real music session needs. Actual use should drive development.

---

# 3. User / workflow context relevant to FIRE

The user is a serious independent musician / multi-instrumentalist working under the broader Babel creative identity.

He uses Logic Pro (Mac + iPad) and wants:
- manager-style structure
- clear next steps
- minimal clutter
- credible production logic
- a workflow that develops production judgment rather than just teaching plugins/tools

He already understands basics such as:
- headroom
- reference level matching
- basic EQ/compression ideas
- masking
- panning
- automation
- reverb/delay basics
- direct vs ambient sound
- static mix = volume + pan

Do **not** repeatedly reteach those basics unless they become relevant to a specific decision.

The real development goal is stronger **diagnostic production judgment**:
- hearing source character
- arrangement
- relative balance
- punch
- width/depth
- space
- movement
- why a professional reference feels different

The user also wants to make music **now**, so app development should remain efficient.

## Design-relevant user preferences — preserve this across chats

Keep this section limited to information that directly affects FIRE's product design. Do not include private biography, embarrassing skill gaps, health/relationship/financial details, or anything a collaborator/developer would not need to know.

### Learning / interaction preferences
- The reference user has strong musical experience but uneven production confidence by domain. FIRE itself must not require prior production knowledge: adapt guidance by domain, let `I don't know` be a valid answer, and avoid one global Beginner/Intermediate/Advanced assumption.
- Prefer concise, manager-like direction with one clear next action at a time.
- Keep the interface simple, but make the underlying logic rigorous.
- Favor applied learning on real songs over detached theory.
- Explain **why** a production decision matters when that improves judgment.
- Use credible research/sources when production principles materially affect the workflow.
- Avoid unnecessary bureaucracy, repetitive instructions, and over-explaining.
- Preserve the user's creative authorship: FIRE should guide decisions and learning, not make the artistic decisions for them.

### Product implication
FIRE should emphasize structured listening, diagnosis, intentional experimentation, and finishing. It should behave as a production companion that can teach through real work, not a mandatory beginner course, plugin encyclopedia, or automatic song generator. Concise production flow remains available even when the musician does not want educational depth.


---

# 4. Long-term app architecture

## Recreation — 7 phases
These phase names are currently the core Recreation framework:

1. **The Map** — understand the reference
2. **The Skeleton** — build the complete rough song
3. **The Sounds** — match sources, performances, and tone
4. **The Balance** — establish hierarchy through volume + pan
5. **The Shape** — EQ, dynamics, transients, saturation/character
6. **The World** — depth, width, reverb, delay, automation, movement
7. **The Finish** — compare, revise, polish, complete

Earlier versions described three checkpoints per phase / 21 checkpoints total. V6 later exposed ordered work as Steps. That vocabulary and its Phase-home shell are **production-generation behavior, not universal FIRE architecture**.

### Current redesign progression and navigation direction — LOCKED FOR V7 SHELL

The V7 shell uses **Projects → Project Home → direct musical work**.

- Project Home owns **Continue + Journey + Notes**.
- Continue recommends one next destination.
- Journey shows the project path, supports direct revisiting, and groups work by Phase without requiring a Phase intermediary screen.
- The Map remains the first Recreation phase, but its work (Song Setup, Structure, Tracks, Section Study, Review Map) is directly reachable from Journey.
- Completed work remains revisitable. Upcoming work remains visible when useful for orientation. Hard gates exist only when a destination cannot function without required context.
- V7 has no center context navigator and no separate Roadmap destination.
- The future Projects/Notes top-level navigation surface remains deferred until Notes is a genuine app-level destination.

The shipped V6 Phase/Step/Roadmap/center-navigator model remains documented in `V6.md` and later V6-specific sections of this file for production maintenance only.

### Goal of a Recreation
The target is a **complete finished cover/recreation** whose relationship to the reference is intentionally chosen rather than assumed. A project may begin as **Match**, **Interpret**, or **Reimagine**, and that bias may change during the work. Individual differences may be matched, intentionally kept, or explored.

A musician can use Recreation purely to make a cover quickly; learning/progress tracking must remain optional and ambient. Success does **not** require being indistinguishable from the commercial master unless faithful matching is the musician's actual goal.

A strong outcome is:
> Every meaningful remaining difference is either understood or consciously accepted.

The study should transform:
> “Theirs just sounds more professional.”

into:
> “Here is exactly why ours differs and what caused it.”

---

# 5. Original Song mode — conceptual architecture

Original Song is the most important long-term mode.

Current conceptual workflow:

1. **The Spark**
   - capture the raw idea
   - protect what made it worth keeping
2. **The Direction**
   - mood, energy, intent, references if useful
3. **The Skeleton**
   - rough complete song from beginning to end
4. **The Production**
   - arrangement, transitions, layers, textures, production identity
5. **The Recording**
   - replace placeholders with intentional performances
6. **The Mix**
   - Balance → Shape → World as mix sub-steps
7. **The Finish**
   - reference, revise, final mix/master/commit

Original projects should remain creatively flexible, but Recreation is no longer defined as a rigid learning sequence either. Both project types use strong default guidance with minimal hard gating.

Important distinction:
- **Recreation:** the reference helps define the target, while Match / Interpret / Reimagine and intentional differences control how closely it is followed.
- **Original Song:** the musician's own intention defines the target.

Both modes share the FIRE reasoning engine. Guidance may recommend an order of operations, but creative exploration stays reversible and hard gates exist only when a task literally cannot function without required context.

---

# 6. Product philosophy

## The app is a structured production notebook — but smarter
A notebook can record notes.
FIRE should:
- organize observations
- reuse them downstream
- turn previous analysis into later tasks
- keep unresolved questions
- generate summaries / briefs
- reduce re-entry of information

Core principle:
> **Enter information once; reuse it intelligently later.**

Another important principle:
> **Each phase should make the next phase smarter.**

Another:
> **If a field does not improve the current decision or make a later phase easier, delete it.**

The app should never become bureaucracy.

---

# 7. Recreation — The Map (most developed phase)

The Map should answer:
> What is this record doing before we try to recreate how it was made?

It should produce a reliable blueprint of:
- form
- global track/part palette
- what is active per section
- major changes
- overall section feel
- focal point
- unresolved questions
- takeaways

It should **not** prematurely solve detailed sound design/mixing questions that belong in later phases.

## Map listening workflow

### Song Setup / First Listen
One uninterrupted orientation listen.

**First Listen** is an actionable completion card:
> Play the full song once without stopping.

It should be visually consistent with other completion/action cards.

Song Setup includes:
- Reference
- Tempo (with BPM suffix)
- Meter
- Grid
- First Listen action state

**V6 production behavior (superseded by V7 shell direction):** V6 keeps Song Setup controls on The Map phase home. In V7, **Song Setup is a dedicated focused work page** reached directly from Project Home/Journey; do not recreate the V6 Map-home shell in the redesign.

### Structure
Instruction style:
> Play through the record. Add a section when the form changes. Pause and rewind freely.

Common sections:
- Intro
- Verse
- Pre-Chorus
- Chorus
- Bridge
- Instrumental
- Outro
- Custom

Repeated names auto-number:
- Verse 1
- Verse 2
- Chorus 1
- Chorus 2

**Stable section IDs are required.**
Notes/analysis must stay attached if sections are reordered.

Each Structure section also has a **bar length**. Use quick values such as 4 / 8 / 12 / 16 plus custom whole-bar entry. Do not silently assume a length that was never identified. Structure Verified confirms order, lengths, and boundaries.

**V6 interaction:** Structure has one **+ Add section** action opening one cohesive sheet with section type and bar-length segmented controls. Custom fields appear only for Custom. Each Add commits one valid section and keeps the builder open, retains the selected bar length, and shows inline confirmation; Done closes it. A deliberate new choice/input re-arms Add to prevent duplicate submissions. A selected length control is sufficient confirmation; do not repeat its value in another field. Repeated types may prefill their last used length. Permanent row handles reorder by drag or focused Up/Down arrows. Edit is name/type/length only; a separate restrained 44px trash target deletes immediately with Undo. Add/Edit sheets contain no deletion.

#### Structure row interaction — LOCKED direction
Permanent drag handle is visible at all times.

Desired behavior:
- row body → edit name/type/length; trailing trash → immediate deletion with Undo
- drag only from handle → reorder
- page scroll should not fight drag
- no separate Reorder / Done mode
- drag should feel fluid and iOS-like

Do not reintroduce old `↑ ↓ ×` buttons.

### Structure Verified
A dedicated completion/action card.

Meaning:
> Play through once and confirm section boundaries/order.

It is different from the final Map Verified action.

### Tracks
The separate **Unidentified** area has been removed.

Use a single section called:
**Tracks**

Common options can include:
- Vocal
- Drums
- Bass
- Ukulele
- Guitar
- Piano
- Synth
- Backing vocals
- Percussion
- FX
- custom items

Custom input placeholder:
**Other...**

Custom entries should become normal pills in the same Tracks list immediately.

Unknown/mystery sounds can simply be named descriptively and added as a custom Track.

Do **not** re-add a separate “Unidentified” section.

### Logic tracks created
This was deliberately removed from The Map.
Creating DAW placeholder tracks belongs in **The Skeleton**.

---

# 8. Section Study — LOCKED name

Step 3 of The Map is:
## **Section Study**

Do not rename it back to “Production.”

Section Study is no longer a Parts/Changes form. It is a **focused viewport into one continuous song timeline**.

The app still walks through Structure sections in exact order and keeps the horizontal section navigator. Moving Verse → Chorus should use a subtle horizontal slide so it feels like moving forward through one song, not loading an unrelated form. Direct section-tab jumps use the same mental model.

Only the current section is the primary editing surface, but ranges are allowed to continue across section boundaries.

---

# 9. Section Study — timeline model — LOCKED

The timeline is the source of truth for arrangement state. Do not maintain a parallel Parts/Enters/Leaves state machine.

## Stable identity
Use stable IDs for:
- sections
- tracks
- presence ranges
- change events/ranges

Renaming or reordering must not detach data.

## Section length / timing
Every section has a whole-number bar length.

The current timeline UI snaps to **whole bars** by default. The internal model remains capable of fractional bar offsets later so beat/subdivision precision can be added without another schema rewrite.

Do not add beat-level controls until real use proves they are necessary.

## Presence ranges
A track's presence is represented visually by one or more ranges.

**Open-ended presence / continuity rule:** adding a track starts presence at that musical position and assumes it **continues indefinitely through every later section until explicitly cut**. Internally, an open presence range has no fixed end. Adding new sections later automatically extends that open presence into them. FIRE should ask the user to document the exception — where something stops — instead of repeatedly asking whether it continues.

In V6, block bodies only select. Empty space starts/resumes at a whole-bar boundary. Actual boundaries drag, or select an edge then tap its destination in the same lane; focused Left/Right arrows move one valid boundary. Escape/click-away cancels. Open continuation uses a distinct arrow grip for placing a stop, never a false stop cap. No separate timing editor, modal, slider, Earlier/Later or Stop/Continue machinery remains. During drag, preserve the mounted DOM and canonical music; move a disposable visual candidate, then commit once on release. Reject crossing/inverted boundaries. Cancel on scrolling/capture loss/Escape/route/viewport/layout interruption. Routine edits offer Undo. Long sections scroll horizontally at a usable bar scale while short sections fit naturally.

Visual grammar:
- uninterrupted block = continuous presence
- `|` end cap = the part actually stops there
- `|` start cap = the part actually begins there
- no cap at a section boundary when the part continues across it
- an actual gap in sound is represented by separate ranges with empty space between them

If one presence range ends at the exact instant another begins, merge them automatically. With no period of absence, presence is continuous; a new phrase/performance at that instant should be represented as a change, not as fake stop/restart presence.

Presence ranges may cross section boundaries. A Synth that begins in Verse bar 5 and ends in Chorus bar 4 is one range, not duplicated Verse/Chorus data.

## Changes
Changes live on a Track or on Mix.

Use two underlying kinds:
- **Duration/state range** — e.g. Widens, Narrows, Doubles, Louder/Softer, Effect shift.
- **Moment marker** — e.g. Pattern shift and Register shift; older saved data may also contain Transition cue.

Do not expose Duration/Moment classification. In V5, **+ Change** opens one sheet with all standard actions visible under small headings: Width (Widens/Narrows), Level (Louder/Softer), Performance (Doubles/Pattern shift/Register shift), and Sound (Effect shift). Choosing an action creates it immediately across the selected/current visible presence and closes the sheet. Refine timing directly on the timeline. Transition cue is no longer offered; existing saved cues and custom changes remain preserved and editable.

Known duration/state changes begin at a musical position and, like presence, may remain open-ended until explicitly ended or superseded. If another range in the same underlying property begins later (for example `Widens` followed by `Narrows`), the earlier state should end automatically at the new state's start. Different properties may overlap. A track-level open state naturally cannot outlive the track presence that contains it.

A duration range may cross section boundaries exactly like presence.

A Track change must stay inside that Track's presence. Mix changes are not constrained to a Track presence range.

Entering and leaving are **derived from presence edges**. Do not create separate Enters/Leaves events.

## Progressive disclosure / visual calm
The data may be detailed; the default screen must not look detailed.

Collapsed timeline row:
- **Track name only** — no `1 change`, `Starts bar 3`, `Full section`, or other redundant subtext
- one clean neutral presence rail
- duration changes reflected as restrained colored segments
- moment changes reflected as small colored markers

The visualization should carry the timing information instead of repeating it as text. Color may distinguish semantic change families, but shape must also carry meaning so the system never relies on color alone.

Only one Track expands at a time. Changes are labeled thin bands or point markers directly aligned with presence in the same main-lane coordinate and scroll system. Selection reveals real edges and a small Remove action; + Change keeps the single taxonomy sheet. Do not add a duplicate mini-timeline or editor. Change edges/points share presence dragging, tap-destination, keyboard and cancellation paths. Semantic colors identify only musical change families. Another saved edit replaces the current Undo opportunity. No persistent timing instructions or hover tooltips; transient drag position feedback disappears immediately on finish/cancel.

Mix belongs to the Arrangement header; reveal a global grouping only when expanded or populated. Track lanes keep a fixed vertical order across sections so Verse → Chorus motion feels spatially continuous rather than making instruments jump between rows.

## Current FIRE / timeline visual language
FIRE itself is no longer themed around Smithereens. The product chrome should use a neutral, premium graphite/near-black palette with crisp light type and restrained borders. Smithereens is a project inside FIRE, not FIRE's brand identity.

Reserve color primarily for musical information and interaction state. Current semantic change families may use restrained distinct hues (for example Space, Level, Performance, Sound, Cue) while presence stays neutral. Avoid rainbow clutter, gradients, foggy glass, or decorative effects that reduce precision.

The governing UI principle is:
> **FIRE assumes the music keeps doing what it was doing. You only tell it when something changes.**

The default interface should stay visually simple even when the underlying timeline model is detailed.

## Section-to-section motion
Section Study is one continuous musical model under a focused viewport.

When moving to the next/previous section:
- slide horizontally with restrained motion
- continuous presence/change ranges should visually read as continuing, with no artificial end cap at the boundary
- stopped parts show a real end cap
- newly entering parts show a real start cap
- reset the expanded Track when changing sections so the next section opens cleanly

Respect Reduce Motion.

## Structure edits and timeline safety
Because ranges can cross sections, reorder/removal must never accidentally make a range span unrelated music or delete unaffected data. Retain original IDs on surviving fragments; new fragments get new IDs. Preserve open tails when the resulting coverage reaches the current song end. If a reorder moves an open tail ahead of absent music, close that tail at its actual covered boundary rather than spreading it across unrelated sections.

Before destructive Structure mutation, preserve timeline data as section-local segments; after the mutation, reconcile and merge truly adjacent compatible ranges again. Section IDs remain authoritative.

# 10. “Not sure” policy — LOCKED

The user explicitly decided that Recreation should not use **Not sure** as a completed answer.

Remove / do not reintroduce:
- `Not sure` in Changes
- `Not sure` in Focus
- `?` uncertainty buttons in Feel dimensions

Reason:
The study is meant to train judgment.
If uncertain, make the best judgment or put the question in Parking Lot.

Timeline Changes do not need an explicit **No notable change** answer anymore; no mapped event is already a valid empty state.

### Keep:
**No clear focus**
because that can also be a real observation.

Principle:
> **Ambiguity can be an answer. Uncertainty is unfinished work.**

---

# 11. Feel system — section-level overall impression

Feel refers to the **overall section**, not every individual instrument.

A section may contain both dry and wet instruments while still having an overall spatial impression.

Current intended 3-state dimensions:

### Depth
Close · Mixed · Distant

### Space
Dry · Mixed · Wet

### Width
Narrow · Mixed · Wide

### Density
Sparse · Balanced · Dense

### Energy
Low · Medium · High

These should behave like true mutually exclusive segmented controls.

Do not use the old “Soft / Punchy” pair; those are not reliable opposites and punch belongs more naturally in Shape.

---

# 12. Focus

Focus means:
> what pulls attention in this section?

Multiple tracks may be selectable when attention is genuinely shared.

Keep:
**No clear focus**

Do not keep:
**Not sure**

---

# 13. Notes system

Use consistent naming:
## Notes
Inside:
- **Parking Lot**
- **Takeaway**

Do not switch between “Phase Notes,” “Babel takeaway,” etc. in inconsistent ways.

### Parking Lot
Questions / unresolved production mysteries.

### Takeaway
A lesson worth remembering/applying elsewhere.

Long-term idea:
Parking Lot and Takeaways should aggregate across phases/projects into a personal production library.

Examples:
- “Why does this vocal suddenly feel wider?”
- “Removing bass before a chorus increases impact.”

The app can later surface learned principles in Original Song mode.

---

# 14. Map completion / gating

Recreation is intentionally stricter.

## Core rule
**Forward progress is gated. Backward movement is always allowed.**

The disabled state/checkmarks should normally communicate incompleteness by themselves. Do not place persistent helper/status sentences underneath disabled Next buttons unless the missing requirement would otherwise be genuinely unclear.

### Required Map completion conditions

#### Structure
- at least one section
- every section has a valid bar length
- Structure Verified completed

#### Tracks
- at least one global Track
- before the full Map can finish, every global Track must appear somewhere on the timeline

#### Section Study
Every section has:
- at least one Presence range touching the section, OR explicit `No active tracks`
- all five Feel dimensions completed
- Focus selected, OR `No clear focus`

Changes are **optional observations**, not a required checkbox. No redundant `No notable change` completion state is needed when the absence of timeline events already communicates that nothing was mapped.

#### Final verification
- Map Verified
- Teach It Back

Meaningful Structure/timeline/Feel/Focus edits invalidate Map Verified / Teach It Back. Notes alone do not.

### Map Verified
Final full-song listen with the completed map open; correct anything that does not match.

### Teach It Back
Be able to explain where you are, what exists, what changes, how the section feels, and what matters most.

# 15. Map Summary

Map Summary remains part of The Map, not a separate phase.

It should show:
- Structure + bar lengths
- global Tracks
- section summaries derived from timeline presence / changes
- Feel
- Focus
- Notes
- final verification actions

Section rows are tappable to return to that section for editing.

If a global Track exists but never appears on the timeline, Review may show one concise unused-track warning linking back to Tracks. Do not add a generic yellow “items still open” panel; unchecked actions and disabled continuation are sufficient.

The user previously wanted Map Summary top-button clutter reduced. Navigation should be solved at the phase level instead.

---

# 16. Navigation and progress — V6

Back follows actual eligible browser history. The center pill opens the hierarchical parent: Map work → The Map, Skeleton work → The Skeleton, phase home → Recreation project home. Roadmap is explicitly labeled on the project home. Section movement and inline disclosures do not add route depth. Every route, including restored browser history, rechecks current canonical eligibility.

Progress is contextual: seven-phase journey on Recreation home, valid checkpoint completion on phase homes, quiet checkpoint position on work screens, and local section position in Section Study. Review Map concludes the three-checkpoint Map flow. Retain stored work separately from current valid completion when a prerequisite is temporarily invalid.

---

# 17. Phase homes — V6 production pattern (not V7 architecture)

The Map and Skeleton previously looked too different.

## V6-only phase-home rule
A V6 phase home is an **overview**, not a workspace. This section exists to maintain production V6 and must not override the V7 Project Home + Journey architecture.

Default structure:
- parent phase/project pill
- phase progress
- checkpoint list
- at most one compact utility/details row when the phase genuinely needs it

Do not put full forms, large action cards, long instructional copy, or expanded notes directly on a phase home. Those belong inside the relevant checkpoint/detail screen.

### The Map
The Map home should show:
- progress
- Structure
- Tracks
- Section Study
- optional compact phase-specific utility/preflight content **above** Checkpoints (The Map uses Setup)

For The Map, the full setup controls live directly above Checkpoints because setup is part of starting The Map. Setup must be complete before Structure unlocks. Other phases such as The Skeleton do not need to imitate this because they do not have an equivalent setup stage.

Checkpoint progress belongs visually to the **Checkpoints** section: show `X of Y` beside the Checkpoints label and the thin progress bar directly beneath it. Do not show a redundant percentage on phase homes.

When Section Study is already complete, opening its checkpoint can lead to the Map Summary/verification screen, which still provides access back into individual sections for editing.

### The Skeleton
The Skeleton home should show:
- progress
- Session
- Draft
- Bounce

No extra explanatory dashboard content is needed.

The same visual grammar should eventually serve:
- Map
- Skeleton
- Sounds
- Balance
- Shape
- World
- Finish

Only checkpoint content changes.

Do not independently design every phase home.

---

# 18. Skeleton — current conceptual structure

The Skeleton consumes The Map automatically. Do not ask the user to re-enter arrangement information.

Current checkpoints are locked as:

### Session
Create the DAW scaffolding one item at a time:
- one completion row per mapped Track
- one completion row per Structure section marker

Tracks and Markers use the same left-aligned circular completion language.

### Draft
Build the complete rough arrangement.

Draft is one page with whole-song coverage. Each section discloses its mapped Track checks inline and shows automatic completion; routine checks never need a separate detail route.

Inside a Draft section:
- check each required Track individually
- show concise read-only timing/change cues from The Map
- the section check turns on automatically when every required Track is complete
- never ask the user to manually declare the whole section complete
- a legitimately silent section can complete from its Map state

Draft stays live-linked to The Map. New/changed requirements should invalidate only affected work where practical; preserve unrelated valid completion. Presence edits invalidate only the affected Track/section span. Structure reorders/length changes preserve completed Draft work for unaffected section IDs while resetting any DAW markers whose positions actually moved.

Not every Map change belongs in Draft. Arrangement/performance cues such as **Doubles, Pattern shift, Register shift, and Transition cue** can invalidate the affected Draft Track. Width, level, and effect-space observations belong to later phases and should not force the rough arrangement to be rebuilt.

### Bounce
Two deliberate actions:
- **Export draft bounce**
- **Listen start to finish**

Both are required. Any later Draft/arrangement change invalidates Bounce.

Skeleton goal remains **coverage, not polish**. Detailed source/performance matching belongs in The Sounds.

Backbone and Full Rough are removed. Do not reintroduce them as duplicate checkpoints.

---

# 19. Project dashboard

Main app should open to the **Projects** screen.

Smithereens is preloaded as a Recreation on fresh install.

User can create:
- Original Song
- Recreation

There should be only **one** clean new-project affordance (e.g. top-right `+`).

Do not duplicate “New Project” buttons.

Project menu should support:
- Delete Project
- with deliberate confirmation

Recreation overview order:
1. Current Phase
2. Next
3. Project

Project section belongs at the bottom.

---

# 20. Completion visuals

Use **one completion visual language everywhere**.

Use the same circular action-card check throughout the app, with the neutral V5 interaction accent.

Use the same visual family for:
- First Listen
- Structure Verified
- Map Verified
- Teach It Back
- Roadmap completed phases
- Skeleton checkpoints
- future phase completion states

No random second checkmark style.

---


## UI copy rule — LOCKED
FIRE copy should be concise and action-oriented:
- Page titles should be short and normally omit terminal periods.
- Subtext should be one short sentence only when it adds necessary context.
- Prefer concrete verbs: `Map the form`, `Identify the tracks`, `Build the backbone`, `Review the map`.
- Avoid repeating information already communicated by disabled states, checkmarks, progress bars, or section labels.
- Consistency means shared typography, spacing, cards, navigation, and completion language — not forcing every phase to contain the same content.

---


## Skeleton Session — LOCKED interaction
The Session checkpoint creates DAW elements one-by-one.

- **Tracks:** each mapped track has its own completion row.
- **Markers:** each Structure section has its own marker completion row; do not use one global “Section markers created” toggle.
- Track and marker rows should use the same left-aligned circular completion indicator.
- Draft section rows use the same left-aligned automatic completion indicator.
- Do not show extra Skeleton status/helper callouts beneath the normal gating controls.

---

# 21. Visual design system

## Overall feel
- iPhone-first
- Apple-inspired
- dark
- minimal
- polished
- neutral graphite palette
- restrained neutral interaction accent
- comfortable touch targets
- clean typography
- progressive disclosure
- immediate selection feedback

The user wants the UI to feel native/intentional, not like a web form.

For the current timeline, keep the implementation **crisp rather than foggy/frosted**:
- solid dark surfaces
- sharp readable contrast
- thin precise timeline/grid lines
- restrained radii and separators
- neutral accents reserved for selection, progress, and active editing
- no decorative blur/glow just because Apple-inspired styling is desired

## Shared component geometry

Use one semantic shape/spacing/state system: meaningful cards/dialogs around 18px, standard controls around 12px, small chips/segments around 8–10px, and true capsules only for compact context/status/tag pills. A component retains its silhouette and dimensions through idle, hover, selection, press, focus and disabled states. Shared tokens control padding, spacing, gutters, motion/easing and semantic states; avoid layered conflicting overrides. Cards remain useful for meaningful groups, rows for navigation/list structure, and buttons for actions. Respect reduced motion.

## Adaptive canvas and input

Same FIRE, different canvas: phone, tablet, laptop, and desktop share one workflow and data model. Choose fluid content widths by screen purpose: focused forms/checkpoints, medium project/overview lists, and wider Arrangement/Draft workspaces. Use side-by-side regions only when the content benefits; do not stretch every form or add filler dashboards. Large-screen editing panels may be centered dialogs while compact layouts retain bottom sheets.

Mouse, touch, and normal keyboard accessibility are first-class. Keep important controls visible without hover, provide stable non-geometric hover/press feedback and visible focus, and preserve native scrolling, Tab/Shift+Tab, Enter/Space activation, and safe Escape dismissal. Custom productivity shortcuts remain outside the current scope.

On compact layouts, a route that already fits the visual viewport should not gain fake root scroll or rubber-band drift; keeping the page shell stationary preserves alignment when moving between screens. When a route is genuinely dense, first remove redundant supporting copy or compact non-current states before shrinking touch targets. The same FIRE product logic, hierarchy, and interaction model must survive across phone and tablet; only presentation may adapt to available space. In production V6, Roadmap may compress future/completed phase detail.

## Apple-like rules that have emerged
- avoid unnecessary hairlines
- use spacing/grouping before separators
- related controls should align
- one clear primary action
- 44pt-ish touch targets
- concise copy
- selection when possible instead of typing
- text fields only when custom text is genuinely necessary
- action cards for real “did this” tasks
- no explanatory text when the control explains itself

## User copy preference
Very sensitive to redundant text.

Examples of copy the user has explicitly wanted removed:
- repeated explanations of listening workflow
- “overall section impression” plus another paragraph explaining the same thing
- “what pulls your attention” beside Focus
- “starting state” beside Parts
- “what changed / from last section” when Changes already communicates it
- “mystery sound is useful information...” below an obvious input
- excessive drag/reorder instructions

Rule:
> **If text is not helping the current action, remove it.**

---

# 22. Guided / Minimal — REMOVED

This decision is locked.

There is **no Guided vs Minimal mode**.

Reason:
FIRE should have one experience that is:
- simple
- clear
- effective
- minimally instructional where needed

Do not reintroduce:
- guidance project setting
- CSS classes for guided/minimal
- alternate copy modes
- UI toggle for it

---

# 23. Current refactor direction / code architecture

FIRE retains the **continuous timeline architecture originally introduced in V3**, while **V6 is the active interaction generation**.

FIRE uses three plain static files: `index.html` is the document shell, `styles.css` owns visual styles, and `app.js` owns the application. Deploy all three together from the GitHub Pages root. There is no framework, package installation, bundler, or backend. Within the application, keep concerns separated:
- schema/migration
- timeline math
- mutations + invalidation
- render helpers
- navigation/history
- completion validators

The timeline engine is the musical source of truth. UI text such as “starts,” “continues,” “ends,” active Tracks, and Draft requirements should be derived from timeline ranges rather than separately persisted whenever possible.

Important engineering rules:
- preserve the existing localStorage key
- maintain explicit schema versioning and migrations
- normalize imported backups through the same migration path as normal startup
- initialize browser history with `replaceState`
- history entries carry project ID and previous route label
- in-app Back mirrors real browser Back
- centralize destructive/mutation logic; do not keep duplicate remove/update paths that clean different dependent state
- avoid keeping both the old Parts/Changes editor and the new timeline editor for the same truth

## Legacy data migration
Old data should migrate rather than reset:
- old global ingredient names → stable Track objects/IDs
- old active Parts → Presence ranges
- adjacent active sections → continuous presence where no absence existed
- old Enters/Leaves are not migrated as separate events because Presence now derives them
- other old transition Changes → Moment markers at the destination section start when the old schema had no more precise timing
- old Rough completion → Draft completion where identities can be matched
- old rough bounce → Bounce exported state; listening remains a separate requirement

---

# 24. Data/state requirements

Use stable identifiers for:
- projects
- sections
- tracks
- presence ranges
- change events/ranges

A Recreation project stores:
- Map setup
- ordered sections with `lengthBars`
- Track objects
- section-level Feel / Focus / Notes
- timeline Presence ranges
- timeline Moment/Duration changes
- Skeleton Session / Draft / Bounce state

Timing anchors are section-relative rather than hardcoded absolute song bar numbers. That keeps timeline data attached to musical section identity when earlier section lengths change.

Whole-bar snapping is the current UI precision, while the internal timing representation should remain compatible with fractional offsets later.

Autosave to localStorage. No Save button.

Dependency invalidation must prevent stale “complete” states:
- Structure edits invalidate Structure verification and downstream marker/Draft/Bounce state as appropriate
- meaningful Map analysis edits invalidate Map verification
- affected arrangement/Track changes invalidate affected Draft work where practical
- Draft changes invalidate Bounce
- Notes do not invalidate musical completion

Existing user progress should be preserved whenever it is still logically valid.

---

# 25. Drag/reorder behavior

The current desired approach:
- drag handle is always visible
- no Reorder mode
- handle is the only drag target
- page should continue to scroll normally elsewhere
- touching/dragging handle should prevent page scroll from stealing the gesture
- row should move fluidly, not snap/glitch wildly
- tap row → edit sheet
- drag handle → reorder

This has been a repeated pain point; test it carefully on iPhone/Safari.

---

# 26. Home Screen / PWA

FIRE can be added to iOS Home Screen.

Current web app metadata should support:
- standalone-ish launch
- app title FIRE / Babel FIRE

A custom `apple-touch-icon` is planned, but **deferred** until navigation/logic is stable.

Do not spend current development time on the icon unless the user explicitly returns to it.

---

# 27. Deployment / repo workflow

## GitHub repo
`BabeDrums/babel-fire`

## GitHub Pages live site
`https://babedrums.github.io/babel-fire/`

## Deployment model
- GitHub Pages serves `index.html`, `app.js`, and `styles.css` from the `main` root; deploy the three static files together with no build step.
- Implementation belongs on dedicated task branches. Completed work is tested, committed, pushed, and opened as a PR against `main`.
- PRs are the external/user review checkpoint. Merge and production deployment require explicit approval; opening a PR does not deploy the work.
- Preserve history and unfinished local work before syncing or switching branches. The full workflow and completion-report requirements live in `AGENTS.md`.
- Report the PR link, exact changed files, validation, and remaining risks. Do not substitute manual uploads to production for PR review.

Netlify is no longer required for this project.

---

# 28. Chat vs Codex workflow

Current conclusion:

## This Chat = FIRE product/design brain
Use this conversation to:
- decide UX
- production pedagogy
- workflow
- architecture
- evaluate user testing feedback
- protect project intent

## Codex = repository engineering executor
Codex executes approved engineering work in the repository:
- working directly in repo
- coordinated edits
- tests
- refactors
- multiple files
- commits/pushes

Do **not** throw away this product conversation just because Codex becomes involved.

Collaboration workflow:
> user + ChatGPT decide what FIRE should do → Codex implements on a task branch → tests → commit/push → PR → external/user review → explicit approval → merge → GitHub Pages production

Do not bypass PR review by uploading files directly to production.

---

# 29. Smithereens / collaboration specifics

Smithereens by Twenty One Pilots is the first Recreation.

The original Driver/Detective and later Lead/Six roles were deliberately removed.

Do not reintroduce role assignment.

If multiple people are working together, both can:
- listen
- discuss
- operate Logic
- make decisions

The workflow should work for:
- one person
- two collaborators
- a producer + artist
- a band

---

# 30. Why this project is worth doing

The app is not valuable merely because it digitizes a notebook.

Its value is:
- structure
- consistency
- downstream reuse of observations
- diagnostic production training
- making reference analysis actionable
- turning study lessons into original-production judgment

Estimated conceptual usefulness previously discussed:
roughly **80–90% useful as a learning framework** for this specific type of intermediate musician/producer *if the recreations are actually done*.

The remaining skill comes from real hours:
- listening
- producing
- making mistakes
- recording
- comparing
- revising

If FIRE ever causes more app-design time than music-making time, simplify it.

---

# 31. Important product tension

The user wants to start making music immediately.

Therefore:
- do not design Phases 3–7 in exhaustive detail before they are needed
- finish enough Map/Skeleton to work
- actually use Smithereens
- let real friction determine next changes
- prioritize Original Song development as soon as necessary

Core process:
> **build → use on real music → notice friction → fix → continue producing**

NOT:
> design the perfect app for weeks → someday make music

---

# 32. Latest state / likely next move

The active approved interaction generation is V6, specified in `V6.md`, retaining the continuous timeline engine. An active specification does not imply that its implementation has shipped; verify `main` and open PRs for release status. Stored schema version is 5; the storage key remains `production-projects-v1`. Startup and imported backups share normalization/migration. V4 projects, stable identities, fractional timing, notes, and valid downstream progress survive migration. Legacy cue observations remain stored even though new cues are no longer offered.

Durable interaction and architecture rules:
- Structure sections have bar lengths
- Section Study uses the visual timeline model
- Presence is represented by continuous ranges with clear start/end boundaries
- uninterrupted ranges may cross section boundaries
- timed production changes are ranges or markers internally; those classifications are not exposed in creation UI
- only one Track expands at a time; changes are directly selected on aligned bands/markers
- presence and change editing shares drag, tap-boundary/tap-destination, arrow keys and Undo
- section-to-section navigation slides through the song
- stable Track IDs replace name-as-identity logic
- old Map data migrates into the new model where possible
- Skeleton is `Session → Draft → Bounce`
- Backbone / Full Rough are removed
- browser-history Back behavior is the navigation source of truth
- imported backups pass through migration/normalization

Next product development should come from using this build on the real Smithereens recreation. Do not pre-design Sounds/Balance/Shape/World further until actual use of Map/Skeleton exposes the next meaningful need.

Before future code changes, follow `START_HERE.md` to inspect current production, unmerged work, and local changes. This context does not replace verification of implementation/release state.

---

# 33. New-chat bootstrap instruction

If this file is uploaded into a new conversation, the user should be able to say:

> **Babel FIRE — continue from GitHub repo BabeDrums/babel-fire. Read START_HERE.md.**

The assistant should not make the user repeat the project history.


# 34. Continuity file usage going forward

The safest continuity workflow is intentionally simple:

**One canonical durable product context: `CONTEXT.md`.** `START_HERE.md` is the short entry point; `AGENTS.md` holds repository rules; the active specification holds approved generation requirements; `CHANGELOG.md` records meaningful milestones. Do not duplicate this context across them.

Do not create a new handoff document for every chat.

Instead, keep this file current as the living FIRE specification. When an important locked decision changes, update this file. When only code implementation or small UI polish changes, the repo code itself records that implementation.

A future chat should not need a giant pasted prompt. The user can simply say:
> **Babel FIRE — continue from GitHub repo BabeDrums/babel-fire. Read START_HERE.md.**

That is the intended long-term handoff method.


# 35. Regression workflow

`tests/test_v6.py` is a browser regression suite using Python Playwright and a local Chromium installation. Serve the repository with `python3 scripts/serve.py`, then run `python3 -B -m unittest discover -s tests -v`. `CHROMIUM_PATH`, `FIRE_URL`, and `FIRE_TEST_WIDTH` can override the browser, server, and viewport. Test dependencies are development tools only; the shipped app remains dependency-free. Tests use disposable browser contexts, representative V4/legacy saved data, actual Chromium touch input, and imported backups. Physical iOS Safari verification remains a separate device check.


---

# Current FIRE Design System direction — October 2026

This section records the durable visual/interaction direction established through physical iPad review. It is a product rule, not a temporary screenshot critique.

## North star
Projects and New Project are the current visual reference implementation. They feel cleaner because they use stable page geometry, restrained controls, deliberate whitespace, calmer typography, and fewer decorative containers. Future work should extract those principles into shared components rather than redesigning each route independently.

The goal is not to make every page identical. The goal is for Roadmap, Notes, The Map, Structure, Tracks, Section Study, Review Map, Skeleton Session/Draft/Bounce, Arrangement, Original flows, and future screens to feel like one product designed by one system.

## Global design language
- Stable page anatomy: toolbar → page title → subtitle/status → primary content.
- Leading toolbar area is navigation; trailing toolbar area is contextual action. Passive center pills are not part of the final language.
- One type hierarchy: page title, page subtitle, section title, row title, supporting text, metadata/status.
- Tracked uppercase is not the default section treatment. Use it only when it genuinely improves orientation.
- One spacing/radius/control rhythm across the app. State changes must not alter geometry.
- One action hierarchy: primary, secondary, quiet, destructive. Full-width light slabs are not the universal primary-action pattern.
- One grouped-surface/row language. Prefer structured rows/lists for text-heavy editable information; keep cards only for meaningful conceptual groups.
- One form language for fields and segmented controls.
- One state model: normal, hover for fine pointers, pressed, selected, focus-visible, disabled, destructive, completed.
- Selection and completion are semantically different. Selected tracks/feel choices/etc. should not borrow completion checkmarks by default.
- Completion circles/checkmarks are reserved for actual workflow completion.
- iPad task sheets should use compact centered form/page-style presentation when practical; phone layouts may use bottom-oriented presentation.
- Avoid fake Liquid Glass, decorative gradients, excessive glow, and blur. FIRE remains a near-black creative tool; borrow hierarchy, geometry, restraint, adaptive behavior, and interaction clarity rather than visual imitation.

## Route implications
- Roadmap should read as structured progression, not seven unrelated large cards packed with chips and status decorations.
- Notes should use intentional empty states/layout rather than arbitrary columns of sparse text.
- The Map should reduce competing pill/control treatments and use one coherent grouped-row language.
- Structure should become one coherent editable structure list with integrated add/edit/reorder/delete behavior and downstream verification, not a stack of unrelated bordered widgets.
- Tracks remains multi-select but should become denser/calmer and use the shared selected-state language rather than completion-style checkmarks.
- Review Map should reduce redundant cards and make Structure/Track summaries navigational and coherent.
- Section Study/Arrangement may keep specialized timeline geometry, but its controls, typography, selection, sheets, and spacing must inherit the shared FIRE system.
- Skeleton Session/Draft/Bounce should inherit the same shell and component language; Draft parent rows are derived progress/disclosure, while child parts are the actual completion controls.

## Implementation rule
Build the system globally, validate it locally, then roll it out. Change core shared components and styles, not overlay polish files or MutationObserver rewrites. Automated green tests are necessary but not sufficient; physical iPhone/iPad Safari review determines whether a visual chunk is actually locked.
