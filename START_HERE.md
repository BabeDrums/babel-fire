# Babel FIRE — Start Here

Use **Babel** as the project-facing name.

This is the canonical zero-context FIRE handoff. For FIRE implementation/product work, read in this order:

1. `START_HERE.md`
2. `AGENTS.md`
3. `FIRE_CORE.md`
4. `V6.md` for production behavior
5. `V7_DRAFT.md` for G7 shell behavior
6. relevant unresolved items in `CONTINUITY_INBOX.md`
7. code/tests as implementation evidence

For wider ecosystem/surrounding-app work instead, route through `BABEL_START_HERE.md`, `BABEL_APPS.md`, and `BABEL_PLATFORM.md`. Do not let ecosystem brainstorming rewrite active FIRE runtime/spec behavior.

## Current verified continuity — G7 shell is live but NOT frozen

Production remains V6. G7 remains the isolated successor preview at `/v7-preview/` using `production-projects-v1-v7-preview`; it must never mutate V6 `production-projects-v1` data.

PR **#58** is the current merged/deployed G7 baseline on `main`, merge commit `bbcfed804b76076a03b43b6c427a487dc9084592`. It refined compact project sheets, project actions/destructive confirmation, one coherent Cover Home progression, and truthful Tracks completion after explicit Done. At the start of the current visual-grammar refinement there were no open PRs. Always re-check current `main` and open PRs rather than assuming this SHA remains latest.

The G7 shell is still **not approved/frozen**. Do not begin FIRE Core breadboarding until Babel physically approves the generic shell fundamentals.

### Latest physical-device review after #58

The latest iPhone review says the shell is substantially cleaner but still exposes design-system drift rather than one coherent visual grammar:

- Projects itself looks strong and should remain stable unless a real issue appears
- project management actions are functionally right but the action sheet still feels visually under-resolved; Cancel reads too much like floating text instead of a button
- New Project's Original/Cover selector and separate Title/Artist boxes do not share one clear spacing rhythm; Title + Artist should read as one grouped field surface beneath the segmented project-type decision
- Edit Project already feels clean and should inherit the same grouped Title/Artist treatment without adding chrome
- Cover Home now feels clean and should stay stable
- Song Setup feels solid and should not be visually churned merely to prove a design system exists
- Continue/Done actions should share one stable final-page action region rather than page-specific placement; this should remain a normal non-sticky footer in document flow, not a viewport-fixed control
- Structure still needs consolidation: Add Section should move to a toolbar `+`; arrangement rows should share Projects' grouped-list material/rhythm without copying irrelevant chevrons/ellipsis; `Matches the song` should become a separate verification card using the same surface material instead of a special tint
- Add Section and Tracks are semantically similar direct-choice grids but currently use slightly different borders/fills/gaps/radii; they should share one Choice Tile family, with Tracks as multi-select + checks and bar length as a compact variant
- visible Add Section / Edit Section / Add Track sheet headings are redundant when the source action already supplies context; Reset/Delete confirmation headings are not redundant because they communicate consequence
- secondary actions such as Cancel/Done/Duplicate should be quieter than primary actions but still visibly tappable

### Current visual-grammar refinement contract

The active refinement resolves those findings as one shell-level consolidation:

- keep Projects, Cover Home, Song Setup behavior, title/header scaffold, Cover naming, recent ordering, scrolling, and V6 isolation intact
- introduce reusable visual grammar primitives in G7 rather than one-off near-duplicates: grouped surfaces, Choice Tiles, segmented choice, non-sticky page action footer, and primary/secondary/destructive sheet buttons
- New Project keeps Original / Cover as a segmented decision and groups Title + Artist into one rounded field surface with one internal divider
- Edit Project uses the same grouped Title/Artist surface
- Cancel/secondary actions receive a discernible button shape while remaining visually subordinate to primary actions
- Song Setup Continue, Structure Continue, and Tracks Done use one shared page-action-footer grammar at the end of page content; do not introduce a sticky footer
- Structure moves Add Section to the trailing toolbar `+`
- Structure arrangement rows reuse the same grouped-list material/rhythm as Projects while keeping Structure-specific index, bar metadata, and reorder handle; do not add fake `•••`/chevron accessories
- `Matches the song` becomes a separate grouped verification surface below the arrangement and drops its one-off tint
- Add Section section-type choices and Tracks choices share one Choice Tile family; 4/8/12/16/Custom bars use the compact variant
- omit visible headings from Add Section, Edit Section, and Add Track when their source action already makes context obvious; keep accessible dialog names
- retain visible confirmation headings for Reset/Delete because they communicate consequence
- reconcile tests/spec/handoff/doctrine guard/changelog so #58 is baseline truth and no guard hardcodes the obsolete “after #57” checkpoint

This refinement still does **not** equal physical approval. The next meaningful product action after merge/deploy is another real iPhone review of the changed surfaces.

## G7 interaction grammar

Protect these semantic rules:

- **Inline = choose/toggle/classify/confirm/evaluate** something already in the task.
- **Sheet = create/edit/manage a discrete thing** while staying in context.
- **Navigation = enter another meaningful workspace.**
- menu/secondary affordance = utilities that should not compete with musical work.

Delete before styling. Subtitle/helper text is optional, not default. Same meaning should reuse the same visual grammar; different meaning may use different accessories. Do not compensate for weak fundamentals with signature visual polish.

## Physical approval checklist

On real iPhone Safari, inspect:

1. Does Projects → project → work keep title position/scale calm and predictable?
2. Does **Cover** read naturally next to Original?
3. Does New Project feel complete immediately and keep Original/Cover plus grouped Title/Artist visually coherent?
4. Does Edit Project remain obvious with the same grouped Title/Artist pattern, including after clearing a field?
5. Do Title/Artist keyboard capitalization suggestions behave naturally without forcing casing?
6. Does `•••` feel like the same control in rows and the toolbar, and can a project-card menu open without changing the active project?
7. Are Edit / Reset / Delete / Cancel terse and understandable, with Cancel visibly tappable and Reset/Delete confirmation preventing accidental loss?
8. Does meaningful recent activity ordering still feel useful?
9. Does Cover Home still read as one calm progression with no redundant completion card?
10. Is Song Setup still clear, including Tempo focus/keyboard behavior, without unnecessary redesign?
11. Do Continue/Done actions feel like one consistent final-page action region without becoming a sticky browser-bar competitor?
12. Do Structure rows feel like the same grouped-list system as Projects while keeping honest Structure-specific controls?
13. Is toolbar `+` a clean/discoverable Add Section affordance?
14. Does Structure still allow quick repeated section entry, direct reorder, and compact Edit without regression?
15. Does `Matches the song` read as a distinct verification step without a weird one-off tint?
16. Do Add Section and Tracks visibly belong to the same Choice Tile family, with bar choices as the compact variant?
17. Does Tracks still feel fast as a grid while selected state, Other, and Done feel integrated?
18. Does Tracks remain incomplete until Done explicitly confirms the current non-empty selection, and does editing later invalidate that confirmation?
19. Are redundant sheet headings gone while Reset/Delete confirmation headings remain useful?
20. Do sheets feel honest without a dead grabber/drag affordance?
21. Does the Cover flow stop cleanly after current mapped shell work without forcing learning chrome?
22. Overall: **can Babel move through the shell without wondering what kind of UI is going to happen next?**

If yes, explicitly record approval and stop broad shell polishing. Small later animation/personality/microinteraction improvements remain allowed after the product logic proves itself.

## After shell approval

Sequence:

**physical G7 shell approval → FIRE Core breadboard → thin end-to-end FIRE Core spine → real-project validation**

The breadboard is behavior-first, not pixel-first. Map Original + Recreation/Cover end to end and define, for every phase:

- entering problem
- what FIRE asks the musician to notice
- decision being made
- Logic action/experiment
- evaluation
- done criteria
- evidence retained
- carry-forward context

The breadboard must make a believable path from a Cover reference to finished release-ready audio and from Original material to finished release-ready audio. If a phase devolves into “then somehow mix it,” the product logic is not ready.

The thin FIRE Core should then implement the smallest real walking spine across that entire journey and validate it on real music before deep polish.

## Generation-spec retention

Git history is the archive. Keep the current production spec (`V6.md`) plus the active successor spec (`V7_DRAFT.md`) in the working tree by default. Do not resurrect retired generation specs as competing authority unless maintenance/migration/recovery genuinely requires them.

## Parallel-chat ownership

Babel may keep multiple chats open.

- FIRE build lane owns active runtime/spec implementation and follows this file + `AGENTS.md`.
- Ecosystem brainstorm lane follows `BABEL_START_HERE.md` + `BABEL_APPS.md` + `BABEL_PLATFORM.md`, is read-mostly toward FIRE runtime while a build is active, and must re-read latest `main`/open PRs before any durable write.
- an old branch without an open PR/current handoff reference is historical working state, not product authority.

## Normal workflow / standing permission

For FIRE implementation:

**branch → implement → test → reconcile docs → PR → checks → merge → Pages deploy → verify → physical-device approval when relevant**

Babel has standing permission to merge FIRE PRs once the diff is reviewed, required checks are green, production-data safety is clear, and no genuine product decision remains unresolved. Do not merge when tests fail, behavior is destructive/risky, data safety is uncertain, or a real decision is still unresolved.
