# Babel FIRE — G7 Shell Specification (Frozen)

**Status:** G7 is the frozen isolated successor shell under `/v7-preview/`; V6 remains production. `FIRE_CORE.md` governs cross-generation product doctrine. This file governs the frozen G7 shell behavior/primitive grammar. `G7_SHELL_CERTIFICATION.md` is the completed freeze contract; `G7_SHELL_CERTIFICATION_STATUS.md` records **10 / 10 Locked** and the evidence.

Approved shell runtime anchor: `4a258c5170dd1d96dcbc0f2b0a9c35b283cec489` (PR #96).

G7 uses **Cover** as the musician-facing label for the canonical FIRE Core **Recreation** workflow. Internal compatibility may continue using the legacy `study` project type; public naming does not require a storage migration.

## Why G7 exists

G7 establishes a reusable visual/interaction grammar that can disappear behind the music.

The shell is not a collection of final FIRE screens. It is the page frame, typography, spacing/alignment, surfaces, actions, icons/accessories, controls/states, temporary UI, responsive behavior, accessibility, and motion rules from which future FIRE interfaces can be composed.

A future screen, section, modal, menu, form, or workspace should begin from solved fundamentals and already feel like Babel. New product-specific UI may extend the grammar deliberately when genuinely needed; shell freeze does not mean no new primitive can ever be added.

The current **Setup → Structure → Tracks** flow is disposable **shell/workspace fixture content**. It exercises useful primitive families but is not a frozen definition of The Map, a promise of exactly three checkpoints, or proof that FIRE Core should keep these interactions. FIRE Core breadboarding now reconsiders the musical journey from first principles.

## Frozen-state boundary

Certification is complete:

- all ten categories are **Locked**
- representative primitive/state families are exercised in Shell Test where applicable
- the same primitives compose coherently in real G7
- compact and regular-width automated regressions pass
- accumulated physical iPhone/iPad review plus explicit Babel approval closed the real-device gate
- transferable shell rules were promoted into Babel Truth
- **FIRE Core breadboarding is unblocked**

Locked does not mean immutable. When Core exposes a new requirement, first determine whether it is product-specific composition or a genuinely missing primitive. Extend the smallest necessary primitive; reopen a locked category only when new evidence shows the frozen foundation itself is wrong.

## Developer Shell Test

G7 contains a developer-only Shell Test that renders the **actual G7 primitives/tokens/styles** side by side under deliberately varied fixture states.

It exists to expose systemic defects and stress sparse/normal/dense, short/long, selected/custom/disabled/focused/error states where applicable. It is not a replica of FIRE, not Babel Lab, not a user-facing product destination, and not a substitute for real-G7 or physical-device review.

## Frozen shell rules

1. **Delete before styling.** If removing a label/subtitle/helper sentence does not make the next action harder to understand, remove it rather than making it smaller.
2. One obvious current action; do not duplicate it elsewhere.
3. One stable page scaffold across root, project, and work pages.
4. Subtitle/helper text is exceptional, not default.
5. Progress is inferred from musical state where practical; when FIRE cannot truthfully infer completion, use an explicit lightweight confirmation.
6. Project Home is a hub, not a dashboard.
7. One product across iPhone/iPad; presentation adapts, semantics do not.
8. Natural document scrolling; sparse pages should not scroll accidentally and dense pages should scroll naturally.
9. Learning remains ambient and optional. A Cover must not require a learning-flavored waypoint merely to keep moving.
10. **Same meaning uses the same visual grammar.** Reuse the same component/glyph family instead of inventing near-duplicates.
11. **Different meaning may use different accessories.** Unity does not justify fake chevrons, menus, completion marks, or reorder affordances.
12. **Physical rhythm is a system, not a page decision.** Repeated row/control geometry comes from shared primitives/tokens rather than one-off heights and gaps.
13. **Back means where the musician actually came from.** Visible Back and browser/history Back agree whenever G7 has usable in-app history.
14. **State must not move the object.** Repeated labels keep stable typography/anchors; state uses semantic emphasis/accessories.
15. **Fixtures do not become product architecture by polish.** A fixture may prove a primitive without freezing FIRE Core workflow.
16. **Quiet until important.** Most chrome recedes; attention is earned by a real decision/state.
17. **Tactile, not decorative.** Character comes from composition, proportion, material, motion, and interaction rather than gratuitous gradients/glow/borders.
18. **Familiar first, signature second.** Commodity controls should be excellent and platform-legible; originality is spent where it improves the musical job.

## Interaction grammar

- **Inline** — choose, toggle, classify, confirm, or evaluate something already in the current task.
- **Sheet** — create/edit/manage a discrete thing while staying in context.
- **Navigation** — enter another meaningful workspace.
- **Menu / secondary affordance** — utilities that should not compete with musical work.

Consistency comes from semantic meaning, not forcing every interaction into one container.

## Physical rhythm and visual grammar primitives

G7 does not maintain one-off versions of the same control.

- **Grouped surface** — one material/radius/separator language for row-based collections. Current canonical grouped page-row height is **64px**.
- **Shared row-content grid** — stable leading label anchor plus predictable metadata/accessory slots. Accessories do not push the label around.
- **Trailing value control** — editable/value rows share compact geometry/material/alignment/focus behavior while preserving correct input semantics.
- **Selection surface** — parent owns outer border/radius; child options communicate selection through fill/contrast rather than nested outlines. Current canonical selection-cell height is **52px**.
- **Segmented control** — compact mutually exclusive choices; parent owns outer geometry.
- **Page action footer** — final non-sticky region for a page's primary completion/continue action; short pages compose without accidental scrolling and long pages flow naturally.
- **Sheet action hierarchy** — primary actions filled; secondary/cancel quieter but unmistakably actionable; destructive actions share geometry with danger treatment.
- **Sheet spacing grammar** — tightly related disclosure/control groups use **12px** separation; major conceptual groups and task-content-to-footer separation use **24px**. These sit inside the shared 4 / 8 / 12 / 16 / 20 / 24 vocabulary with deliberate optical exceptions.
- **Split-action row feedback** — the parent row owns the pressed surface; child action targets preserve distinct semantics but do not paint competing pressed rectangles.

Do not visually clone unrelated controls merely to make screenshots symmetrical.

## Canonical icon/accessory grammar

Recurring glyphs come from one coherent accessory system: fixed accessory slots, canonical icon boxes, optical weight, size/alignment, and semantic meaning.

Placement model:

**geometry baseline → optional intrinsic per-symbol optical metric → container placement**

- incomplete/upcoming progression state = canonical quieter short bar
- current/recommended progression state = canonical stronger short bar
- completed progression/state = canonical completion mark where completion is actually true
- selected fill = chosen option where selection itself is sufficient
- drag handle = reorderable object
- chevron = navigation deeper only when a navigation cue is actually useful
- `•••` = management/actions
- `+` = create/add the primary discrete object for the current view

Plus / More / Reorder use normal centered placement. Check may own its small intrinsic optical correction. Back / Forward own mirrored outward optical side bearings. Symbol alignment belongs to the symbol primitive, never page-specific CSS.

Do not stack redundant navigation indicators. Structure arrangement objects do not earn completion checks merely by existing. Track selections do not need redundant completion checks when selected fill already communicates selection.

## Header and title scaffold

Every G7 screen uses the same structural scaffold:

- stable toolbar region
- Back in the leading slot when applicable
- contextual add/manage action in the trailing slot when applicable
- roughly 44px interaction target with quieter visible material where appropriate
- toolbar and title compose as one system rather than detached glyphs floating at page edges
- the page title begins from a stable anchor
- one coherent title hierarchy across root/project/work pages
- project metadata may sit quietly below project identity
- action glyphs are optically centered inside their control surfaces

The trailing slot is part of the scaffold and is not nudged independently per page.

## Navigation and Back behavior

- entering a work page from Project Home creates a real history step
- visible Back retraces actual in-app path when available
- browser/history Back resolves to the same previous work page
- direct/deep-linked work entry safely falls back to Project Home
- Project Home Back returns to Projects; direct/deep-linked Project Home safely falls back to Projects

Fixture-specific Continue/Done routing remains evidence, not promised FIRE Core architecture.

## Projects fixture

Projects exists to stress root-page composition, grouped rows, project identity, open/create, and management actions.

- public project types are **Original** and **Cover**
- project title primary; artist + type secondary
- whole main row area opens the project
- `•••` is a roughly 44px management target that belongs visually to the row
- no decorative divider separates `•••` from the row
- opening row management does not silently change active project

## New/Edit Project fixture

This fixture stresses segmented choice, grouped fields, focus/keyboard behavior, and paired actions.

- Original / Cover visible immediately
- Title and Artist remain stable fields
- Original requires Title; Cover requires Title + Artist
- Title Return/Next advances to Artist
- opening the sheet does not summon the keyboard
- ordinary text fields keep normal platform correction/spelling/predictive assistance
- specialized input modes elsewhere remain value-appropriate
- Cancel is a real secondary action
- compact placeholder-only treatment is local to this simple form; it is not a universal label-removal rule

## Project Home fixture

- title + quiet metadata
- Setup / Structure / Tracks is temporary fixture content
- state changes do not move/resize the row label
- state accessories use the canonical icon/accessory system
- no redundant chevron when state mark plus fully tappable row already communicates the interaction
- saved Notes may appear as a separate utility group; empty Notes stays hidden

## Work-page fixtures

Setup, Structure, and Tracks prove transferable mechanics. They may be changed or replaced during Core breadboarding.

### Setup
Stresses grouped rows, trailing values, focus/input semantics, completion/state accessories, and page action footer.

### Structure
Stresses ordered rows, reordering, create/edit sheets, selection surfaces, segmented values, custom fields, confirmation state, split-action feedback, and adaptive temporary UI.

The current verification wording (including **Accurate**) is disposable fixture copy. Do not promote it into shell doctrine.

### Tracks
Stresses multi-selection, adaptive collections, custom creation, density, and explicit confirmation. The current Tracks UI is **not** a product-design target. Do not infer FIRE Core Track/Element/Role UI from it.

## Temporary UI / modal composition

- compact iPhone presents an edge-attached bottom sheet where appropriate
- regular-width/iPad presents a centered card/dialog where appropriate
- semantic content/action hierarchy remains the same
- composition establishes clear conceptual groups rather than giving every control equal visual authority
- primary/secondary/destructive actions follow shared hierarchy
- custom/revealed controls remain attached to the control that caused them
- dialogs/sheets have accessible names even when redundant visible headings are omitted

Babel character comes through hierarchy, rhythm, material, tactile grouping, restraint, and deliberate motion—not decorative FIRE theming.

## Responsive / accessibility baseline

- one product logic across iPhone/iPad
- roughly 44px+ interactive targets
- safe areas respected
- long content/wrapping tested
- focus/keyboard behavior tested on physical iPhone where relevant
- keyboard alternatives for nontrivial pointer interactions such as reorder
- reduced-motion support where motion exists
- no essential skinny-line or gesture-only actions

## Data safety

- V6 production key: `production-projects-v1`
- G7 preview key: `production-projects-v1-v7-preview`
- G7 must never mutate/wipe V6 data
- schema changes require tested migration

## After freeze

The shell is complete enough to stop being the project.

Current sequence:

**FIRE Core breadboarding → thin FIRE Core spine → real-project validation → deliberate product/runtime promotion only when earned.**

Transferable shell principles already live in the Babel Truth commit pinned by `BABEL_TRUTH.md`. Lab reconciliation is a separate parallel ecosystem task and does not block FIRE Core.
