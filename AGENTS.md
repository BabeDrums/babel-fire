# Babel FIRE — Codex Repository Instructions

## Product
Babel FIRE is an iPhone/iPad-first music-production workflow app. The current shipped app is a static GitHub Pages app. `FIRE_CONTEXT.md` contains the long-lived product and architecture context.

## Working rules
- For product behavior, workflow, data-model, or UX changes, consult `FIRE_CONTEXT.md`.
- For the current redesign task, `V5_SPEC.md` is the task-specific source of truth and supersedes older UI details where they conflict.
- Preserve existing user data. Do not change the current localStorage key or wipe projects. Any schema change must include a forward migration from the current shipped version.
- Preserve stable IDs for sections, tracks, presence ranges, and changes.
- Keep deployment simple and compatible with GitHub Pages. You may split the monolithic `index.html` into static CSS/JS modules if that materially improves maintainability, but do not add a framework, backend, database, or build pipeline without a clear need.
- Mobile touch quality is a first-class requirement: approximately 44px hit targets, Pointer Events for direct manipulation, no interaction that requires hitting a visually thin line, and no gesture-only essential action.
- Respect reduced-motion preferences.
- Favor direct manipulation, progressive disclosure, and visual hierarchy over forms, helper text, nested menus, and redundant readouts.
- Avoid duplicated state. The timeline model remains the source of truth for arrangement presence and changes.
- Do not preserve an awkward V4 interaction merely for compatibility. Preserve data and product intent; redesign the UI when V5 requires it.
- Keep the app visually neutral and premium. Smithereens is a Recreation project inside FIRE, not FIRE's visual identity.
- Do not add features outside the approved V5 scope unless required for correctness.
- Do not leave debug files, test screenshots, temporary fixtures, or dead CSS/JS in the committed result.

## Verification
Before considering the task complete:
- Validate JavaScript syntax and startup with no console errors.
- Exercise V4 → V5 data migration with representative saved data.
- Test section add/edit/reorder/remove behavior.
- Test open-ended presence continuation across existing and newly added sections.
- Test trimming presence at a section boundary and inside a section.
- Test adding, selecting, trimming, removing, and superseding changes.
- Test section-to-section sliding and collapsed/expanded track states.
- Test at narrow iPhone width and iPad width.
- Verify no required action depends on tapping a thin visual line.
- Update `FIRE_CONTEXT.md` only when the implementation establishes durable product/architecture rules that should survive future tasks.
