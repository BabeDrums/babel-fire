# Babel FIRE — Repository Instructions

Babel FIRE is an iPhone/iPad-first music-production workflow app. Production runs on GitHub Pages from `main`. Resume through `START_HERE.md`; do not ask the user to re-explain documented FIRE decisions.

## Source-of-truth order

Apply this hierarchy when sources conflict:

1. **AGENTS.md** — repository workflow, engineering, maintenance, review, and documentation rules.
2. **Active version specification, currently V5.md** — approved requirements for the active product generation; supersedes older UI/product descriptions where they conflict.
3. **CONTEXT.md** — durable product philosophy, architecture, learning/workflow context, and decisions intended to survive across versions.
4. **Current code and tests** — implementation evidence; they do not override explicit approved product requirements.

If a genuine conflict remains after applying this hierarchy, ask rather than guessing. Inspect `main`, open PRs, relevant branches, and the working tree to distinguish shipped, unmerged, and planned work. Never mistake a local implementation or a passing test for a production release.

## Git and review workflow

- Never perform implementation work directly on `main`.
- Begin implementation tasks from the latest appropriate production state on a dedicated task branch. An isolated cloud checkout is sufficient; do not create a worktree unless explicitly requested.
- Inspect and preserve unfinished local work before syncing or switching branches. Never reset, overwrite, or discard work to obtain a clean tree. Existing unfinished work takes priority over syncing first.
- Commit and push completed task work, then open a pull request against `main`.
- PRs are the review checkpoint before production. Include the PR link in the completion report; if access prevents opening it, report that blocker and do not claim completion.
- Do not merge a PR or deploy production without explicit user approval. Stop after opening the PR for external/user review unless further action is explicitly authorized.
- Preserve Git history. Do not erase old versions simply because a newer version exists.

Normal sequence: task branch → implementation → tests → commit → push → PR → external/user review → explicit approval → merge to `main`.

## Engineering and product rules

- Read `CONTEXT.md`, the active specification, and relevant code/tests before product work. This task remains **V5**.
- Preserve existing user data and the localStorage key `production-projects-v1`. Schema changes require a tested forward migration; never wipe projects.
- Preserve stable section, track, presence-range, and change IDs. When a genuine split/merge needs new identities, retain surviving identities wherever possible.
- The continuous timeline is the source of truth. Do not recreate duplicate Parts / Enters / Leaves state. Preserve downstream Skeleton Session → Draft → Bounce dependencies and browser-history behavior.
- Keep GitHub Pages deployment simple: `index.html`, `app.js`, and `styles.css` are plain static files deployed together. Do not add a framework, backend, database, build pipeline, or runtime dependency without a clear approved need.
- Approximately 44px touch targets, Pointer Events, whole-bar snapping, reduced-motion support, and tap-based alternatives are required. No essential action may depend on a skinny line or an undiscoverable gesture.
- Favor direct manipulation, progressive disclosure, and visual hierarchy over forms, redundant readouts, nested menus, and unnecessary modals. Do not retain awkward V4 UI merely for compatibility.
- Keep FIRE neutral and premium. Smithereens is a Recreation inside FIRE, not its visual identity.
- Do not introduce features outside the active approved scope unless required for correctness.
- Remove replaced/dead interactions. Do not commit screenshots, temporary/debug fixtures, browser artifacts, caches, or environment-only files. Permanent regression tests and their representative test data belong in `tests/`.

## Product versioning

- Major approved product/interaction generations increment the whole version: V5 → V6.
- Meaningful approved refinements within the same generation may use a minor version: V6 → V6.1.
- Tiny bug fixes normally do not require a FIRE product-version bump.
- Git commit history is independent of FIRE product-version numbers. Never silently invent or increment a product version; a new version must represent an actual approved product milestone.
- When the active generation changes, update its specification, `START_HERE.md`, and `CHANGELOG.md` together. Committing the current work does not create V5.1 or V6.

## Documentation hygiene

- `CONTEXT.md` is not a changelog. It stores durable product decisions, architecture principles, and reusable interaction rules. Preserve valid durable V5 additions; change it only when those rules change.
- Task-specific implementation details, validation results, and review findings belong in the PR/completion report.
- `START_HERE.md` is a short entry point, not a second context document. Keep its active-specification reference current.
- `CHANGELOG.md` records meaningful product milestones, not every technical commit. Do not fabricate unverifiable history; Git contains detailed technical history.
- Changelog milestone text describes the product milestone itself; avoid temporary PR-state wording that automatically becomes false on merge. Determine shipped/unmerged state from `main` and open PRs.
- Avoid duplicating large bodies of information across files. Remove obsolete filenames and contradictory guidance rather than retaining duplicate context/specification files.

## Verification and definition of done

An implementation task is not complete until:

- Requested behavior is implemented and reviewed against the active specification.
- Existing user data is preserved or has a tested forward migration, including imported backups.
- Relevant regression tests pass; startup/JavaScript is clean with no known application console errors.
- Touch interaction is checked at representative iPhone and iPad viewport widths.
- Replaced/dead interaction code and temporary/debug artifacts are removed.
- Documentation is updated only when durable rules changed, with milestones recorded in the changelog when appropriate.
- Remaining risks are explicitly stated, and completed work is committed, pushed, and opened as a PR for review.

For V5, verify section add/edit/reorder/remove; open presence through existing and newly added sections; boundary/internal trimming; change creation/selection/trimming/removal/supersession; section slides; collapsed/expanded track states; forgiving hit targets; migration/data safety; history; and downstream invalidation.

Serve the checkout with `python3 -m http.server 8000 --bind 127.0.0.1`. Run `node --check app.js` and `python3 -B -m unittest discover -s tests -v`; repeat the browser suite with `FIRE_TEST_WIDTH=820`. Test tools require Python Playwright and Chromium (`CHROMIUM_PATH` can override the executable); they are not application dependencies.

Testing reports must distinguish **automated tests**, **responsive viewport testing**, **browser interaction testing**, and **physical-device Safari testing**. Chromium touch injection and iPhone/iPad-sized viewports are simulated/browser tests, not physical-device evidence. Never claim physical iPhone/iPad Safari verification unless it actually occurred on physical hardware. Physical iOS Safari remains unverified for this V5 work.
