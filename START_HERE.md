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

PR **#57** merged the previous G7 system correction to `main` at `38a33779faff6aae9ae3dad596bba3b021bea12b`. At the start of the latest physical-review refinement there were no open PRs. Always re-check current `main` and open PRs rather than assuming this SHA remains latest.

The G7 shell is still **not approved/frozen**. Do not begin FIRE Core breadboarding until Babel physically approves the generic shell fundamentals.

### Latest physical-device review after #57

The latest iPhone review narrowed the remaining problems instead of reopening the whole shell:

- Projects itself feels solid and should stay stable unless a real issue appears
- compact New Project / Edit Project sheets still carry redundant visible headings and field labels; the two-field context is clear enough to let Title/Artist placeholders do the visual work while semantic labels remain accessible
- project actions should read simply **Edit / Reset / Delete / Cancel**
- custom sheets show a grabber even though they cannot drag/resize, advertising behavior that does not exist
- Reset/Delete currently execute immediately and need a short confirmation because there is no undo path
- card `•••` should not silently change `currentProjectId` merely to open another project's management sheet
- Cover Home still feels split because the recommended step lives in one card while the other mapping steps live in another group
- completed Cover Home redundantly adds a `Song map complete.` card above three checked rows
- Tracks' two-column grid is worth keeping; the problem is its heavy selected slabs, detached `Other`, and completion semantics rather than the grid itself
- Tracks currently counts as complete as soon as one track exists even though `Done` visually implies confirmation; this is not truthful progress

### Current refinement contract

The active refinement resolves those findings as one shell-level cleanup:

- keep Projects layout/header/project-card behavior otherwise unchanged
- New Project keeps **Original / Cover** plus stable Title/Artist inputs, but removes redundant visible sheet heading and visible Title/Artist labels; placeholders and accessible labels remain
- Edit Project uses the same compact Title/Artist pattern without a redundant heading
- remove fake grabbers from custom sheets rather than implementing drag merely to justify the affordance
- project management becomes **Edit / Reset / Delete / Cancel** with no unnecessary chevron or repeated title
- Reset and Delete require small confirmation sheets before changing data
- per-card project actions target that project through sheet state without changing the globally active project
- Project Home becomes one coherent **Song Setup → Structure → Tracks** progression group; current/completed/upcoming are states of the same system
- remove the separate `Song map complete.` card; three completed rows are already truthful completion evidence
- keep Tracks as a compact multi-select grid, tighten tile weight, use a subtle selected state + check, and integrate `Other` into the same selection surface
- selecting/editing tracks invalidates track confirmation; **Done** explicitly confirms a non-empty selection and only then counts Tracks complete
- preserve all #57 Structure, header, Cover naming, recent-ordering, scrolling, and V6-isolation behavior

This refinement still does **not** equal physical approval. The next meaningful product action after merge/deploy is another real iPhone review of the changed surfaces.

## G7 interaction grammar

Protect these semantic rules:

- **Inline = choose/toggle/classify/confirm/evaluate** something already in the task.
- **Sheet = create/edit/manage a discrete thing** while staying in context.
- **Navigation = enter another meaningful workspace.**
- menu/secondary affordance = utilities that should not compete with musical work.

Delete before styling. Subtitle/helper text is optional, not default. Do not compensate for weak fundamentals with signature visual polish.

## Physical approval checklist

On real iPhone Safari, inspect:

1. Does Projects → project → work keep title position/scale calm and predictable?
2. Does **Cover** read naturally next to Original?
3. Does New Project feel complete immediately and stay understandable without a redundant visible heading/field labels?
4. Does Edit Project remain obvious with the same compact Title/Artist pattern, including after clearing a field?
5. Do Title/Artist keyboard capitalization suggestions behave naturally without forcing casing?
6. Does `•••` feel like the same control in rows and the toolbar, and can a project-card menu open without changing the active project?
7. Are Edit / Reset / Delete / Cancel terse and understandable, with Reset/Delete confirmation preventing accidental loss?
8. Does meaningful recent activity ordering still feel useful?
9. Does Cover Home now read as one calm progression instead of two competing hierarchy systems?
10. When all three mapping steps are complete, do the checked rows communicate completion without another status card?
11. Is Song Setup still clear, including Tempo focus/keyboard behavior?
12. Does Structure still allow quick repeated section entry, direct reorder, and compact Edit without regression?
13. Does Tracks still feel fast as a grid while selected state, Other, and Done feel like one coherent surface?
14. Does Tracks remain incomplete until Done explicitly confirms the current non-empty selection, and does editing later invalidate that confirmation?
15. Do sheets feel honest without a dead grabber/drag affordance?
16. Does the Cover flow stop cleanly after current mapped shell work without forcing learning chrome?
17. Overall: **can Babel move through the shell without wondering what kind of UI is going to happen next?**

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
