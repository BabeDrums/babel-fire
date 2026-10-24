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

PR **#59** is the last merged/deployed G7 baseline before the current rhythm/navigation refinement, merge commit `d357ec634fa62bc9f6473c3cc1aa5df40db396f6`. It consolidated grouped project fields, visible secondary buttons, shared work-page action placement, Structure toolbar add/verification, and the first visual-grammar primitive pass. At the start of the current refinement there were no open PRs. Always re-check current `main` and open PRs rather than assuming this SHA remains latest.

The current refinement is a physical-rhythm + navigation consolidation prompted by the next real iPhone review. Whether it is still on a branch/PR or has already merged when a new chat reads this file, the next product gate remains **physical iPhone review**. G7 is still **not approved/frozen** and FIRE Core breadboarding must not begin until Babel explicitly approves the generic shell fundamentals.

### Latest physical-device review after #59

The latest iPhone review says the shell is close, but the remaining discomfort is now identifiable as **physical rhythm drift** and history behavior rather than broad page architecture:

- Projects and the overall dark visual direction feel solid
- Title/Artist grouped fields have a focus highlight that visually cuts off at the rounded outer corners
- Add Section's option controls still read as a pile of separate buttons rather than one coherent selection control
- `Matches the song`, `Song Setup`, and `First Listen` are wordier than the surrounding shell needs
- page-level grouped rows visibly change physical height from Projects → Project Home → Setup → Structure, making the interface feel like it resizes between screens
- Structure arrangement objects should not receive checkmarks merely for existing; completion/selection marks must remain semantically honest
- Tracks should use the same toolbar `+` creation grammar as Projects and Structure rather than a special `Other` tile
- trailing toolbar `+` feels too detached/high relative to the title; tighten the shared toolbar-to-title relationship rather than nudging only one icon
- current work-page Back behavior is wrong for the visible Back affordance: Setup → Structure → Tracks can dump straight back to Project Home because Continue replaced history and work-page Back was hard-coded to Home
- visible Back and browser/history Back should retrace the actual route when one exists, with Project Home as a safe fallback for direct/deep-linked work pages

### Current rhythm/navigation refinement contract

The active refinement resolves those findings as one shell-level system pass:

- keep Projects architecture, Cover Home progression, project actions, scrolling model, data isolation, and FIRE Core boundaries intact
- rename musician-facing **Song Setup → Setup**, **First Listen → Listen**, and Structure verification **Matches the song → Accurate**; internal compatibility fields such as `firstListen` may remain unchanged
- establish shared geometry tokens instead of page-specific near-duplicates: grouped page row **64px**, connected selection cell **52px**, standard control/button roughly **46px**, toolbar touch area at least **44px**, and shared 4 / 8 / 12 / 16 / 20 / 24 spacing rhythm
- Projects, Project Home, Setup, Structure arrangement, and Structure verification share the same 64px grouped-row rhythm; accessories still follow semantics
- Title/Artist focus moves to the outer grouped field surface so one clean rounded emphasis replaces clipped inner rectangular focus rings
- section type becomes one connected two-column Selection Surface with internal dividers instead of eight individually rounded buttons
- Tracks uses the same connected Selection Surface family as section type; selected Tracks keep checks because Tracks is multi-select
- bar length becomes one segmented **4 / 8 / 12 / 16 / Custom** control; Original / Cover remains the other segmented-control use
- Structure section rows do **not** gain checkmarks, chevrons, or `•••`; they keep index + name + bars + reorder handle
- Tracks moves custom-track creation to the trailing toolbar `+` and removes the special `Other` tile
- Projects / Structure / Tracks now share toolbar `+` semantics: create/add the primary object for that view
- tighten the shared toolbar-to-title gap so Back/`+`/`•••` and the title read as one header system
- Continue from Setup → Structure and Structure → Tracks pushes actual route history rather than replacing it
- visible Back retraces that in-app history when available; browser/history Back agrees; direct/deep-linked work pages fall back safely to Project Home
- Tracks Done remains a completion action: confirm Tracks and return to Project Home without creating a Home → Back → Tracks loop
- keep Continue/Done non-sticky, but short work pages use flexible document space so the shared action footer naturally occupies a consistent lower region; long pages scroll normally
- reconcile tests/spec/handoff/doctrine guard/changelog in the same pass so no stale #58/#59 or old wording remains as current authority

This refinement still does **not** equal physical approval. The next meaningful product action after merge/deploy is another real iPhone review of the changed surfaces.

## G7 interaction grammar

Protect these semantic rules:

- **Inline = choose/toggle/classify/confirm/evaluate** something already in the task.
- **Sheet = create/edit/manage a discrete thing** while staying in context.
- **Navigation = enter another meaningful workspace.**
- menu/secondary affordance = utilities that should not compete with musical work.

Delete before styling. Subtitle/helper text is optional, not default. Same meaning should reuse the same visual grammar; different meaning may use different accessories. Do not compensate for weak fundamentals with signature visual polish.

## Current state/accessory grammar

- `○` = incomplete/upcoming progression
- `→` = current/recommended progression
- `✓` = completed progression or explicitly selected multi-select choice, according to context
- selected fill = chosen option
- drag handle = reorderable object
- chevron = navigation deeper
- `•••` = management/actions
- `+` = create/add the primary discrete object for the current view

Do not add a visual state simply to make two rows look more alike.

## Physical approval checklist

On real iPhone Safari, inspect:

1. Does Projects → project → work keep title position/scale calm and predictable?
2. Do Back/`+`/`•••` feel visually connected to the title rather than floating too high?
3. Does **Cover** read naturally next to Original?
4. Does New Project keep Original/Cover plus grouped Title/Artist visually coherent?
5. Does Title/Artist focus show one clean rounded group emphasis with no cut-off corners?
6. Does Edit Project remain obvious with the same grouped Title/Artist pattern, including after clearing a field?
7. Do Title/Artist keyboard capitalization suggestions behave naturally without forcing casing?
8. Does `•••` feel like the same control in rows and the toolbar, and can a project-card menu open without changing the active project?
9. Are Edit / Reset / Delete / Cancel terse and understandable, with destructive confirmation preventing accidental loss?
10. Does meaningful recent activity ordering still feel useful?
11. Does Cover Home still read as one calm progression with no redundant completion card?
12. Does **Setup → Structure → Tracks** read naturally and concisely?
13. Do page-level grouped rows keep one stable 64px rhythm instead of visibly resizing between screens?
14. Does Setup feel clear as Reference / Tempo / Meter / Grid / Listen, including Tempo focus/keyboard behavior?
15. Do Continue/Done actions feel like one consistent lower page-action region without becoming sticky?
16. If Babel enters Setup → Continue → Structure → Continue → Tracks, does visible Back retrace Tracks → Structure → Setup → Home?
17. If Babel enters Structure or Tracks directly from Home, does Back return directly to Home?
18. Does browser/history Back agree with the visible Back button?
19. After Tracks Done returns Home, does Home Back go to Projects instead of reopening Tracks?
20. Do Structure rows feel like the same grouped-row system as Projects without fake checkmarks/chevrons/ellipsis?
21. Is toolbar `+` a clean/discoverable Add Section affordance?
22. Does Add Section read as one connected section-type selection surface instead of button soup?
23. Does **4 / 8 / 12 / 16 / Custom** read as one coherent segmented bar-length control?
24. Does Structure still allow quick repeated section entry, direct reorder, and compact Edit without regression?
25. Does **Accurate** read naturally as the separate Structure verification step?
26. Does Tracks visibly belong to the same connected Selection Surface family as Add Section while preserving multi-select checks?
27. Is toolbar `+` a clean/discoverable Add Track affordance, with no need for an `Other` tile?
28. Does Tracks remain incomplete until Done explicitly confirms the current non-empty selection, and does editing later invalidate that confirmation?
29. Are redundant sheet headings still gone while Reset/Delete confirmation headings remain useful?
30. Do sheets feel honest without a dead grabber/drag affordance?
31. Does the Cover flow stop cleanly after current mapped shell work without forcing learning chrome?
32. Overall: **can Babel move through the shell without wondering what kind of UI is going to happen next?**

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
