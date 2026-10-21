# Babel FIRE — Repository Instructions

Babel FIRE is an iPhone/iPad-first music-production workflow app. Production runs on GitHub Pages from `main`. Resume through `START_HERE.md`; do not ask the user to re-explain documented FIRE decisions.

## Source-of-truth order

Apply this hierarchy when sources conflict:

1. **AGENTS.md** — repository workflow, engineering, maintenance, review, and documentation rules.
2. **Active version specification, currently V6.md** — approved requirements for the active product generation; supersedes older UI/product descriptions where they conflict.
3. **CONTEXT.md** — durable product philosophy, architecture, learning/workflow context, and decisions intended to survive across versions.
4. **Current code and tests** — implementation evidence; they do not override explicit approved product requirements.

If a genuine conflict remains after applying this hierarchy, ask rather than guessing. Inspect `main`, open PRs, relevant branches, and the working tree to distinguish shipped, unmerged, and planned work. Never mistake a local implementation or a passing test for a production release.

## Git and review workflow

- Never perform implementation work directly on `main`.
- Begin implementation tasks from the latest appropriate production state on a dedicated task branch. An isolated cloud checkout is sufficient; do not create a worktree unless explicitly requested.
- Inspect and preserve unfinished local work before syncing or switching branches. Never reset, overwrite, or discard work to obtain a clean tree. Existing unfinished work takes priority over syncing first.
- Commit and push completed task work, then open a pull request against `main`.
- PRs are the review checkpoint before production. Include the PR link in the completion report; if access prevents opening it, report that blocker and do not claim completion.
- The user has granted standing permission to merge FIRE PRs once the diff is reviewed and required checks are green. Stop instead of merging when tests fail, data safety is uncertain, the change is risky/destructive, or a genuine product decision remains unresolved.
- Preserve Git history. Do not erase old versions simply because a newer version exists.

Normal sequence: task branch → implementation → tests → commit → push → PR → review/checks → merge under standing permission → Pages deploy → physical-device approval when visual/interaction work is involved.

## Default product/design iteration protocol

The user should not need to repeatedly request research, project review, file cleanup, or handoff maintenance. For every nontrivial FIRE product/design pass, treat those activities as implied when they materially improve the work.

User ideas and examples are **inputs and hypotheses, not locked requirements**, unless the user explicitly says to lock, approve, or require them. Evaluate suggestions against the product goal, platform guidance, current evidence, and project architecture. Improve, reinterpret, defer, or reject an idea when that produces a better FIRE.

Use a lightweight FIRE adaptation of established divergent/convergent and iterative design practice:

1. **Discover** — review physical-device feedback, current app behavior, relevant repo state, and current external/platform references when useful.
2. **Define** — state the actual problem and success condition before changing UI. Distinguish architecture, usability, correctness, polish, and delight problems so a visual symptom is not mistaken for the root cause.
3. **Develop** — consider more than one plausible solution when the problem is open-ended. Prefer the smallest coherent approach that removes complexity rather than adding compensating UI.
4. **Deliver** — prototype or implement the chosen approach in the safest appropriate surface (currently the isolated V7 preview for experimental shell work), then run relevant static/browser tests.
5. **Verify + consolidate** — use physical-device evidence for visual work, remove superseded UI/code, reconcile documentation, and refresh the zero-context handoff before treating a pass as complete.

Do not make the process bureaucratic. The framework exists to make iteration faster and prevent solving the wrong problem; it does not replace creative exploration or judgment.

### Page necessity audit

Before adding or polishing a screen, explicitly ask what job the page performs. For each visible element, classify it as one of:

- essential to the page’s primary task,
- necessary context or navigation,
- conditional/advanced information that can be progressively disclosed,
- duplicated/system-explanation content that should be removed or moved elsewhere.

Every focused work page should have a clear primary task, the minimum information needed to perform it, an obvious continuation or exit when appropriate, and no redundant workflow explanation. Also ask whether the page needs to exist at all or can be merged into a more natural surface.

### Fundamentals before signature polish

Stabilize information architecture, navigation, page purpose, scrolling/viewport behavior, spacing, interaction states, and consistency before adding decorative or brand-signature behavior. Distinctive Babel/FIRE touches are welcome after the fundamentals work, but prototype them as optional product evidence rather than letting personality compensate for structural problems.

## Engineering and product rules

- Read `CONTEXT.md`, the active specification, and relevant code/tests before product work. The active approved implementation scope is **V6**.
- Preserve existing user data and the localStorage key `production-projects-v1`. Schema changes require a tested forward migration; never wipe projects.
- Preserve stable section, track, presence-range, and change IDs. When a genuine split/merge needs new identities, retain surviving identities wherever possible.
- The continuous timeline is the source of truth. Do not recreate duplicate Parts / Enters / Leaves state. Preserve downstream Skeleton Session → Draft → Bounce dependencies and browser-history behavior.
- Keep GitHub Pages deployment simple: `index.html`, `app.js`, and `styles.css` are plain static files deployed together. Do not add a framework, backend, database, build pipeline, or runtime dependency without a clear approved need.
- Approximately 44px touch targets, Pointer Events, whole-bar snapping, reduced-motion support, and tap-based alternatives are required. No essential action may depend on a skinny line or an undiscoverable gesture.
- Favor direct manipulation, progressive disclosure, and visual hierarchy over forms, redundant readouts, nested menus, and unnecessary modals. Do not retain awkward V4 UI merely for compatibility.
- Keep FIRE neutral and premium. Smithereens is a Recreation inside FIRE, not its visual identity.
- Do not introduce features outside the active approved scope unless required for correctness.
- Remove replaced/dead interactions. Do not commit screenshots, temporary/debug fixtures, browser artifacts, caches, or environment-only files. Permanent regression tests and their representative test data belong in `tests/`.

## Progression and navigation model — October 2026

- User-facing workflow hierarchy is **Project → Phase → Step → Musical content**.
- **Checkpoint** is historical/internal terminology only. Do not present phase navigation as manual checklist controls; completion is automatically derived from canonical project state.
- Phase homes show ordered **Steps** with clear done/current/locked state. Completed Steps remain navigable for editing; locked Steps remain visible when they help orientation.
- **Back = browser/history navigation.** It should truthfully reflect where the user came from rather than pretending to be a hierarchy jump.
- **Center context title = fast in-project navigation.** A quiet interactive context title may occupy the center toolbar when it opens real navigation to useful destinations such as Project Overview, Roadmap, Notes, the current Phase, and available Steps.
- **Roadmap = whole journey.** Do not turn the context navigator into a duplicate seven-phase Roadmap.
- Passive center labels/pills are prohibited. If a center element looks interactive, it must perform navigation.
- A future Projects/Notes tab bar or iPad sidebar is allowed only when Notes becomes a genuine app-level destination; do not add persistent app-level chrome before the product earns it.

## FIRE design-system operating rules — October 2026

- **No Codex for FIRE.** Use the normal ChatGPT GitHub connector/direct repository tools for implementation and repository maintenance.
- Projects + New Project are the current visual reference implementation. Extract their rules; do not copy one layout blindly onto every screen.
- The current approved next step is a global FIRE Design System foundation pass. Do not continue route-by-route cosmetic micro-polish without first fixing shared typography, spacing, surfaces, controls, states, and adaptive presentation.
- Use one coherent hierarchy for page title, subtitle, section title, row title, supporting text, and metadata/status. Remove redundant labels and excessive tracked uppercase when layout already communicates hierarchy.
- Use one coherent interaction-state system: normal, hover (fine pointer only), pressed, selected, focus-visible, disabled, destructive, and completed. Geometry must not change between states.
- Selection and completion are distinct semantics. Do not use completion checkmarks as generic selection decoration.
- Prefer grouped rows/lists for structured text-heavy workflows; reserve cards for meaningful conceptual groups.
- Primary actions should fit the composition. Do not default to giant full-width light slabs on iPad/desktop.
- Leading toolbar = navigation; trailing toolbar = contextual action. The center toolbar is normally quiet but may host the approved interactive context navigator described above.
- iPad task sheets should prefer compact centered form/page-style presentation when appropriate; narrow phone layouts may use bottom-oriented sheets.
- Short phone pages that fit within the visual viewport must not create unnecessary root scrolling or rubber-band drift. Use dynamic viewport sizing/overscroll containment while preserving natural scrolling when content genuinely exceeds the viewport.
- Pages that genuinely scroll on iOS Safari must provide enough scroll-end clearance for the final interactive row to rise fully above dynamic browser chrome; short pages must not reserve that clearance and become fake-scroll pages.
- Dense narrow-phone layouts should reduce redundant secondary copy and compact non-current states before shrinking controls. Preserve ~44px touch targets and progression/state clarity.
- Do not imitate Liquid Glass decoratively. FIRE remains a near-black creative tool with restrained surfaces and clear functional hierarchy.
- Do not add overlay polish files or MutationObserver visual rewrites. Modify core shared components and `styles.css` directly.
- Visual work is not complete merely because CI is green. Physical iPhone/iPad Safari approval is required before locking a visual chunk.
- Update `START_HERE.md`, `AGENTS.md`, `CONTEXT.md`, `V6.md`, and `CHANGELOG.md` whenever a durable design-system rule or major shipped milestone changes, so a new chat can resume without reconstructing decisions.

## Product versioning

- Major approved product/interaction generations increment the whole version: V5 → V6.
- Meaningful approved refinements within the same generation may use a minor version: V6 → V6.1.
- Tiny bug fixes normally do not require a FIRE product-version bump.
- Git commit history is independent of FIRE product-version numbers. Never silently invent or increment a product version; a new version must represent an actual approved product milestone.
- When the active generation changes, update its specification, `START_HERE.md`, and `CHANGELOG.md` together. Committing the current work does not create V5.1 or V6.

## Documentation hygiene and automatic handoff

- `CONTEXT.md` is not a changelog. It stores durable product decisions, architecture principles, and reusable interaction rules. Preserve valid durable V5 additions; change it only when those rules change.
- Task-specific implementation details, validation results, and review findings belong in the PR/completion report.
- `START_HERE.md` is the canonical zero-context handoff entry point, not a second context document. Keep its active-specification reference, current shipped/approved direction, physical-device review state, and next approved chunk current.
- Every product/runtime or durable-rule PR that changes `app.js`, `styles.css`, `index.html`, `V6.md`, `CONTEXT.md`, or `AGENTS.md` must also refresh `START_HERE.md`. `scripts/check_handoff.py` and the CI **Handoff freshness** job enforce this automatically.
- The user should never need to remember to request a handoff update. Handoff maintenance is part of FIRE's definition of done.
- A brand-new chat should be able to continue after being pointed at `BabeDrums/babel-fire` by reading `README.md` → `START_HERE.md` and following this file's source-of-truth order.
- `CHANGELOG.md` records meaningful product milestones, not every technical commit. Do not fabricate unverifiable history; Git contains detailed technical history.
- Changelog milestone text describes the product milestone itself; avoid temporary PR-state wording that automatically becomes false on merge. Determine shipped/unmerged state from `main` and open PRs.
- Avoid duplicating large bodies of information across files. Remove obsolete filenames and contradictory guidance rather than retaining duplicate context/specification files.

## Verification and definition of done

An implementation task is not complete until:

- Requested behavior is implemented and reviewed against the active specification.
- Existing user data is preserved or has a tested forward migration, including imported legacy data.
- Relevant regression tests pass; startup/JavaScript is clean with no known application console errors.
- Touch interaction is checked at representative iPhone and iPad viewport widths.
- Replaced/dead interaction code and temporary/debug artifacts are removed.
- Documentation is updated only when durable rules changed, with milestones recorded in the changelog when appropriate.
- `START_HERE.md` passes the handoff freshness check whenever the product/runtime or durable rules changed.
- Remaining risks are explicitly stated, and completed work is committed, pushed, and opened as a PR for review.

For V6, verify section add/edit/reorder/remove; open presence through existing and newly added sections; boundary/internal trimming; change creation/selection/trimming/removal/supersession; section slides; collapsed/expanded track states; forgiving hit targets; migration/data safety; history; and downstream invalidation.

Serve the checkout with `python3 scripts/serve.py`. Run `node --check app.js` and `python3 -B -m unittest discover -s tests -v`; repeat the browser suite with `FIRE_TEST_WIDTH=820`. Test tools require Python Playwright and Chromium (`CHROMIUM_PATH` can override the executable); they are not application dependencies.

Testing reports must distinguish **automated tests**, **responsive viewport testing**, **browser interaction testing**, and **physical-device Safari testing**. Chromium touch injection and iPhone/iPad-sized viewports are simulated/browser tests, not physical-device evidence. Never claim physical iPhone/iPad Safari verification unless it actually occurred on physical hardware. Physical iOS Safari verification must be reported separately.
