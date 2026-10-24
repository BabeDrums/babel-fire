# Babel FIRE changelog

Meaningful product milestones only; Git history records detailed technical changes. Determine shipped/unmerged state from `main` and open pull requests.

## G7

- Rhythm + navigation consolidation candidate after physical review: musician-facing Song Setup / First Listen / Matches the song become Setup / Listen / Accurate; Projects, Project Home, Setup, Structure, and verification share one 64px grouped-row rhythm; section types and Tracks become connected 52px Selection Surfaces; bar length becomes one segmented 4 / 8 / 12 / 16 / Custom control; Tracks custom creation moves to the toolbar `+`; Title/Artist focus moves to the outer grouped field surface; toolbar/title spacing tightens; Continue now preserves real work history so visible/browser Back can retrace Setup → Structure → Tracks, while Tracks Done returns Home without a back loop. Tests/spec/handoff/continuity/doctrine guard are reconciled in the same pass. Physical iPhone review is still required before shell freeze.
- Visual-grammar consolidation candidate after physical review: New/Edit Project group Title + Artist into one field surface beneath Original/Cover; secondary/Cancel actions gain a discernible button shape; Song Setup/Structure/Tracks share one non-sticky page-action footer; Structure moves Add Section to the toolbar, aligns arrangement-row rhythm with Projects without fake accessories, and separates untinted verification from arrangement editing; Add Section, Tracks, and bar choices now share one Choice Tile family with semantic variants; redundant Add/Edit Section and Add Track sheet headings are removed while consequence-bearing Reset/Delete headings remain. Physical iPhone review is still required before shell freeze.
- Shell refinement candidate after physical review: compact New/Edit project sheets remove redundant visible headings/labels while preserving semantic Title/Artist inputs; fake sheet grabbers are removed; project actions become Edit/Reset/Delete with destructive confirmation and no active-project side effect; Cover Home becomes one coherent mapping progression without a separate completion card; Tracks keeps its fast grid but tightens selection styling, integrates Other, and requires explicit Done confirmation before counting complete. Physical iPhone review is still required before shell freeze.
- System correction candidate: public project naming becomes Original + Cover while retaining internal compatibility; Projects sort by meaningful activity; one shared header/title scaffold replaces the root/project/work size staircase; New Project keeps stable Title/Artist fields with word-capitalization hints; project actions/home lose redundant copy; Structure restores choose-type + choose-length-before-insert, direct row reorder, and a compact edit surface; Tracks ends current shell mapping without forcing Section Study. Physical iPhone review is still required before shell freeze.
- Shell simplification correction: physical review rejected the first Shell Freeze as still too text-heavy, visually inconsistent, and interactionally unpredictable. G7 now removes redundant Continue/Journey/work-page copy, restores the preview build trace to a quiet bottom-center review position, gives project cards direct secondary management access, exposes Original + Recreation explicitly at creation, normalizes work-title scale, keeps Structure on one arrangement surface from empty state forward, and defines one interaction grammar: inline for choose/toggle/evaluate, sheets for create/edit/manage, navigation for workspaces, menus for secondary utilities.
- Shell Freeze candidate: Project Home gave the current task one home instead of repeating it, later phases became quieter, empty Notes stopped competing for attention, work-page headers became more compact, Structure verification joined the arrangement group, Tracks became denser, and unfinished Section Study/Review Map states became intentionally quiet. Physical review found this direction structurally better but not yet ready to freeze, leading to the simplification correction above.

## V6

- Phase progression/navigation consolidation: user-facing Checkpoints become ordered Steps with derived done/current/locked state; Map and Skeleton share one Phase Home system; a real center context navigator provides fast project-local jumps while Back remains truthful history; true scrolling pages gain Safari end clearance; dormant Backup/Restore code is removed; and zero-context handoff freshness is CI-enforced.
- Project/Map calmness foundation: unified Edit/Reset/Delete project actions, reset now preserves identity/details and archives workflow notes, Projects/Project overview carry less repeated phase chrome, Song Setup stays permanently editable with First Listen integrated into the same group, and Structure uses the compact continuation action pattern.
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
