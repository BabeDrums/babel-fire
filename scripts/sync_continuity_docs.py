from pathlib import Path


def replace_once(path, old, new):
    p = Path(path)
    text = p.read_text()
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"{path}: expected exactly one match for {old[:80]!r}, found {count}")
    p.write_text(text.replace(old, new, 1))


Path("START_HERE.md").write_text("""# Babel FIRE

- **Repository:** BabeDrums/babel-fire
- **Production branch:** `main`
- **Live app:** https://babedrums.github.io/babel-fire/
- **Active product generation/specification:** [V6.md](V6.md)

When a new ChatGPT conversation begins with or clearly refers to **Babel FIRE**, resume this project immediately; do not ask the user to explain FIRE again.

## Read in this order

1. `START_HERE.md`
2. [AGENTS.md](AGENTS.md)
3. [CONTEXT.md](CONTEXT.md)
4. [V6.md](V6.md)
5. Current `main`, open PRs, relevant branches, and tests
6. [CHANGELOG.md](CHANGELOG.md) for shipped product milestones

Always distinguish shipped work on `main`, unmerged work, and planned work. Resume from the latest verified state and do not make the user repeat documented decisions.

## Current verified direction — October 2026

- **Projects + New Project are the visual north star.** Their cleaner page shell, spacing, typography, restrained controls, and stable geometry are the reference for the rest of FIRE.
- The shared workflow shell has been carried through Project → The Map → Structure → Tracks, but the older interior component language still feels inconsistent across Map, Structure, Tracks, Roadmap, Notes, Review Map, Section Study, and Skeleton screens.
- The next approved product pass is a **FIRE Design System foundation pass**, not another isolated Structure polish pass.
- The design-system pass should standardize typography, spacing, radii, grouped surfaces, rows, inputs, segmented controls, selections, completion states, primary/secondary/quiet/destructive actions, navigation placement, hover/pressed/focus/disabled states, and adaptive sheets.
- **Selection is not completion.** Checkmarks/circles are reserved for genuine completion semantics, not generic selected state.
- On iPad, task sheets such as Add Sections should use compact centered form/page-style presentation where practical; narrow iPhone layouts may remain bottom-oriented.
- Huge light full-width CTA slabs are not the default FIRE action pattern. Action prominence should come from hierarchy/style, not simply width.
- Passive center pills are being retired. Leading toolbar = navigation; trailing toolbar = contextual action; page title = current location.
- Typography should use a consistent hierarchy and reduce unnecessary tracked-uppercase labels or redundant copy.
- Meaningful cards stay cards, but text-heavy structured information should prefer coherent grouped rows/lists rather than card soup.
- Arrangement/Section Study may keep specialized geometry, but must inherit the same FIRE control, typography, state, and spacing language.
- Do not add fake Liquid Glass or decorative blur/gradient effects. Borrow Apple-like hierarchy, geometry, restraint, adaptive behavior, and interaction clarity instead.

## Operating workflow

- **No Codex for FIRE.** Use the normal ChatGPT GitHub connector/direct repository tools.
- Work on a task branch, review the diff, run the regression suite, then merge when green under the user's standing merge permission.
- Stop instead of merging when tests fail, data safety is uncertain, the change is risky/destructive, or a genuine product decision is unresolved.
- Automated/browser tests do not establish visual completion. After deployment, physical iPhone/iPad Safari testing by the user is the visual/interaction approval gate.
- Keep implementation in core `app.js` / `styles.css` / shared components. Do not recreate the failed `polish.css` / `polish.js` / MutationObserver override architecture.
- Preserve `production-projects-v1`, schema 5, stable IDs, migrations, timeline semantics, notes, history, and downstream Skeleton behavior.

Fallback continuation phrase:

> Babel FIRE — continue from GitHub repo BabeDrums/babel-fire. Read START_HERE.md and resume the current FIRE Design System work.

`V5.md` is historical. `V6.md` is active. Use `python3 scripts/serve.py` for local development and the existing regression workflow for validation.
""")

replace_once(
    "AGENTS.md",
    "- Do not merge a PR or deploy production without explicit user approval. Stop after opening the PR for external/user review unless further action is explicitly authorized.\n",
    "- The user has granted standing permission to merge FIRE PRs once the diff is reviewed and required checks are green. Stop instead of merging when tests fail, data safety is uncertain, the change is risky/destructive, or a genuine product decision remains unresolved.\n",
)
replace_once(
    "AGENTS.md",
    "Normal sequence: task branch → implementation → tests → commit → push → PR → external/user review → explicit approval → merge to `main`.\n",
    "Normal sequence: task branch → implementation → tests → commit → push → PR → review/checks → merge under standing permission → Pages deploy → physical-device approval when visual/interaction work is involved.\n",
)

agents = Path("AGENTS.md")
text = agents.read_text()
marker = "## FIRE design-system operating rules — October 2026"
if marker not in text:
    insert = """
## FIRE design-system operating rules — October 2026

- **No Codex for FIRE.** Use the normal ChatGPT GitHub connector/direct repository tools for implementation and repository maintenance.
- Projects + New Project are the current visual reference implementation. Extract their rules; do not copy one layout blindly onto every screen.
- The current approved next step is a global FIRE Design System foundation pass. Do not continue route-by-route cosmetic micro-polish without first fixing shared typography, spacing, surfaces, controls, states, and adaptive presentation.
- Use one coherent hierarchy for page title, subtitle, section title, row title, supporting text, and metadata/status. Remove redundant labels and excessive tracked uppercase when layout already communicates hierarchy.
- Use one coherent interaction-state system: normal, hover (fine pointer only), pressed, selected, focus-visible, disabled, destructive, and completed. Geometry must not change between states.
- Selection and completion are distinct semantics. Do not use completion checkmarks as generic selection decoration.
- Prefer grouped rows/lists for structured text-heavy workflows; reserve cards for meaningful conceptual groups.
- Primary actions should fit the composition. Do not default to giant full-width light slabs on iPad/desktop.
- Passive center pills are prohibited. Leading toolbar = navigation; trailing toolbar = contextual action; page title = current location.
- iPad task sheets should prefer compact centered form/page-style presentation when appropriate; narrow phone layouts may use bottom-oriented sheets.
- Do not imitate Liquid Glass decoratively. FIRE remains a near-black creative tool with restrained surfaces and clear functional hierarchy.
- Do not add overlay polish files or MutationObserver visual rewrites. Modify core shared components and `styles.css` directly.
- Visual work is not complete merely because CI is green. Physical iPhone/iPad Safari approval is required before locking a visual chunk.
- Update `START_HERE.md`, `AGENTS.md`, `CONTEXT.md`, `V6.md`, and `CHANGELOG.md` whenever a durable design-system rule or major shipped milestone changes, so a new chat can resume without reconstructing decisions.

"""
    text = text.replace("## Product versioning\n", insert + "## Product versioning\n", 1)
    agents.write_text(text)

changelog = Path("CHANGELOG.md")
text = changelog.read_text()
entry = """- Projects + New Project now establish the visual north star: stable shared page shell, aligned toolbar/title/subtitle/content guides, persistent Song title + Artist fields, restrained navigation, and geometry-stable transitions.\n- Workflow shell continuity was extended through Project → The Map → Structure → Tracks; passive center pills were removed from those routes and page hierarchy was normalized.\n- Structure received an interim hierarchy/interaction cleanup while preserving rapid repeated section entry, bar persistence, row editing, delete + Undo, reorder, verification, and downstream gating.\n- A global FIRE Design System foundation is now the approved next refinement: shared typography, surfaces, rows, actions, selection/completion semantics, adaptive iPad sheets, and app-wide component consistency.\n\n"""
if entry.strip() not in text:
    text = text.replace("## V6\n\n", "## V6\n\n" + entry, 1)
    changelog.write_text(text)

context = Path("CONTEXT.md")
text = context.read_text()
ctx_marker = "# Current FIRE Design System direction — October 2026"
if ctx_marker not in text:
    text += """

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
"""
    context.write_text(text)

v6 = Path("V6.md")
text = v6.read_text()
v6_marker = "# V6 Design System refinement — October 2026"
if v6_marker not in text:
    text += """

---

# V6 Design System refinement — October 2026

This refinement is approved within V6 and does not change the storage/timeline architecture. It supersedes older V6 visual descriptions where they conflict.

## Objective
Make FIRE feel like one coherent focused creative tool across Projects, Project, Roadmap, Notes, The Map, Structure, Tracks, Section Study, Review Map, Skeleton, Session, Draft, Bounce, Original flows, and future screens.

Projects + New Project are the current reference implementation for cleanliness and spatial continuity. Do not merely duplicate their layout; extract their shared rules into reusable components and tokens.

## Required system
1. Stable page shell with fixed toolbar/title/subtitle/content guides.
2. Shared typography hierarchy with reduced redundant uppercase/tracking.
3. Shared spacing, radii, grouped surfaces, rows, fields, segmented controls, and action hierarchy.
4. Shared interaction states with no geometry changes between normal/hover/pressed/selected/focus/disabled/destructive/completed.
5. Selection and completion must be visually and semantically distinct.
6. Passive center pills are removed; navigation and actions occupy predictable toolbar slots.
7. iPad task sheets use compact centered form/page-style presentation when appropriate; narrow phones may use bottom-oriented sheets.
8. Primary actions are composition-aware; giant full-width light CTA slabs are not the default desktop/iPad solution.
9. Structured text-heavy workflows prefer coherent grouped rows/lists instead of excessive card/chip nesting.
10. Specialized musical canvases may retain unique geometry but inherit the same controls, typography, state, sheet, and spacing language.
11. No fake Liquid Glass/decorative blur system. Preserve FIRE's near-black identity and use restraint/hierarchy rather than imitation.
12. No `polish.css`, `polish.js`, or MutationObserver rewrite architecture. Implement in core `app.js`, `styles.css`, and shared components.

## Validation
Apply the foundation first to representative routes (The Map, Structure, Tracks, Roadmap, and at least one Skeleton route), physically review on iPad/phone, then roll the approved primitives across remaining routes. CI/browser tests protect behavior and geometry; physical-device review protects feel.
"""
    v6.write_text(text)

v5 = Path("V5.md")
text = v5.read_text()
archive = "> **Historical specification.** V5 is preserved for product history. V6.md is the active FIRE specification and supersedes V5 where they conflict.\n\n"
if archive not in text:
    text = text.replace("# Babel FIRE V5 — Interaction Redesign Specification\n\n", "# Babel FIRE V5 — Interaction Redesign Specification\n\n" + archive, 1)
    v5.write_text(text)
