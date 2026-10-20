# Babel FIRE changelog

Meaningful product milestones only; Git history records detailed technical changes. Determine shipped/unmerged state from `main` and open pull requests.

## V6

- iPhone composition refinement: narrow-phone pages now let intrinsic content decide whether scrolling is needed instead of reserving a fake toolbar-height tail; The Map also uses a quieter grouped setup surface with less nested control chrome and a visually integrated First Listen row.
- iPhone scroll/density refinement: short routes now use the dynamic visual viewport without unnecessary root bounce, while dense phone screens compact secondary detail instead of shrinking controls; Map checkpoints and Roadmap progression receive phone-specific density treatment and the Add Sections sheet wastes less vertical space.
- FIRE Design System foundation consolidation: the temporary second visual-override layer was folded back into the core component rules; section hierarchy is calmer, primary actions are compact/dark rather than width-driven light slabs, selected options no longer borrow completion checks, Structure and Roadmap use coherent grouped-list language, passive center pills are visually retired, and responsive regression coverage now includes narrow/large iPhone plus iPad widths.
- First FIRE Design System foundation batch: calmer type hierarchy, grouped progression/list surfaces, selection separated from completion, compact workflow actions, centered iPad task sheets, and shared styling across representative Map/Structure/Tracks/Roadmap/Skeleton screens.
- Projects + New Project now establish a useful visual reference: stable shared page shell, aligned toolbar/title/subtitle/content guides, persistent Song title + Artist fields, restrained navigation, and geometry-stable transitions. They are not immutable templates; shared-system improvements may refine them too.
- Workflow shell continuity was extended through Project → The Map → Structure → Tracks; passive center pills were removed from those routes and page hierarchy was normalized.
- Structure received an interim hierarchy/interaction cleanup while preserving rapid repeated section entry, bar persistence, row editing, delete + Undo, reorder, verification, and downstream gating.
- FIRE's approved visual target is roughly 70% calm Apple-like app hierarchy / 30% focused creative-tool density, with density reserved for genuinely musical workspaces.

- Coherent shared shapes and states, rapid repeated section entry, separate row delete/Undo, and direct musical blocks with drag, tap-boundary/tap-destination and keyboard edits. Aligned changes and horizontal dense-section navigation replace separate timing editors.

- Shared stable controls and sheets, intentional text focus, tonal selection, and reduced-motion support.
- Current canonical prerequisites govern completion, progress, route entry, and restored browser history.
- Back follows eligible history; hierarchical navigation and Roadmap remain distinct concepts while passive center labels are retired from the visual language.
- Musical Stop/Start placement, real boundaries, open continuation, direct accessible boundary movement, and Undo preserve the continuous timeline engine.
- Inline Draft disclosures and whole-song coverage retain Session → Draft → Bounce and honestly lead onward to Roadmap.
- Revisioned static assets and the retained FIRE V6 DEV stamp identify deployed builds without a new runtime dependency or build pipeline.
- Storage schema 5 and `production-projects-v1` remain compatible with existing projects and migrations.

## V5

- One cohesive section builder with section/name and bar-length selection before insertion.
- Direct presence/change editing with whole-bar handles, tap-based timing controls, large selectors, and contextual gap editing.
- Common changes available in one sheet, immediate creation, coherent state supersession, and Undo for routine timeline edits/removal.
- Restrained collapsed timeline visuals, quiet Mix controls, and preserved section slides and downstream workflow.
- Existing storage key retained; forward migration preserves V4 projects, stable identities, fractional timing, notes, and valid progress. Existing legacy cues remain readable while new Transition cue creation is removed.
- Plain static HTML/CSS/JavaScript separation, plus browser regressions for migration, touch interaction, history, and responsive layouts.
- Repository continuity entry point, source-of-truth hierarchy, and task-branch/PR review workflow.

Automated Chromium/browser tests at iPhone and iPad viewport widths do not establish physical iOS Safari verification; that testing remains unverified.
