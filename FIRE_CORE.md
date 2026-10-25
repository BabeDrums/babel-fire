# Babel FIRE — Core Product Doctrine

**Status:** canonical cross-generation FIRE product doctrine. Generation specs describe implementation behavior; they do not override this file unless doctrine is deliberately changed in the same work.

## Naming

- **V6** = established name of the current production implementation generation.
- **G7** = normal human-facing name for the active successor/shell generation.
- Technical G7 identifiers remain `V7_DRAFT.md`, `/v7-preview/`, and `production-projects-v1-v7-preview` unless a real migration reason appears.
- **FIRE Core** = first complete functional product: idea or reference → finished, release-ready audio with FIRE acting as a useful production companion.
- **FIRE 1.0** = future validated release milestone after FIRE Core proves itself on real projects and is intentionally promoted.
- Do not call FIRE Core “V1” and do not invent an `M1` taxonomy merely to create another label.

## Product promise

FIRE helps a musician answer:

> **What deserves my attention next, why, and what should I try in the DAW?**

FIRE is a production companion, not a DAW replacement, plugin encyclopedia, generic checklist, automatic song generator, or mandatory course.

Success criterion:

> **After a useful FIRE session, the musician should know what to do in the DAW that they did not clearly know before opening FIRE. If they only updated FIRE, FIRE failed.**

FIRE Core ends at a finished, release-ready audio file plus essential delivery checks/basic metadata. Distribution, artwork, marketing, and scheduling remain outside the current Core boundary.

## One FIRE brain, two first-class project types

### Original

Start with any musical material or idea and develop it into a finished record. Original stays creatively flexible; guidance should organize decisions without policing creativity.

### Recreation

Use an existing song to make a faithful cover, reconstruction, interpretation, reimagining, or production study. Recreation is a complete standalone workflow. A person may use FIRE only to make covers quickly and never engage with learning history or Original.

Recreation can also build production judgment that later helps Original work, but learning is a benefit—not a prerequisite for completing it.

## Shared reasoning engine

The FIRE loop is:

1. **Feel** — what do you perceive and what matters?
2. **Identify** — where is the meaningful difference/problem/opportunity?
3. **Reason** — what likely causes it and what kind of decision is this?
4. **Experiment** — make one intentional change/test in the DAW.
5. **Evaluate** — did it move toward the target, teach something useful, or reveal another problem?

Recreation gets its target from the reference plus the musician's chosen relationship to it. Original gets its target from the musician's own intention.

## Knowledge model

FIRE combines:

- **Shared production knowledge** — research-backed principles/tradeoffs.
- **Project knowledge** — what is true about this song: structure, elements, roles, intentions, observations, decisions, experiments, unresolved problems.
- **Musician knowledge** — what this person seems comfortable with, struggles with, repeatedly chooses, or has learned across projects.

Adapt by **domain**, not one global Beginner/Intermediate/Advanced label. A musician may be strong at arrangement and inexperienced at mastering.

## Learning is ambient, optional, and applied

Making the record is always the primary task.

- Teach through real production decisions whenever possible.
- **“I don't know” / “Not sure” is a valid answer.** It should open a small diagnostic/explanation, not block progress.
- Default to concise guidance; offer **Why?** and deeper help progressively.
- Instructional detours must be skippable.
- A quick-cover user must be able to keep moving with minimal explanation.
- FIRE may quietly retain skill evidence, useful lessons, repeated weaknesses, and successful approaches, but learning progress must not become mandatory workflow chrome.
- Do not treat page completion as mastery.
- Duolingo is inspiration for adaptive learning/learn-by-doing, not permission to add XP, streak pressure, cartoon paths, or forced lessons.

A future optional Practice / Skills / Growth surface may summarize development and offer targeted category practice without being required to finish music. A living visualization of growth (working concept: the user's **Fire**) is also worth prototyping later, but it must represent credible evidence rather than raw usage or punitive streaks.

A separate learning product is **not currently required or approved** merely because FIRE teaches. See `BABEL_START_HERE.md`, `BABEL_APPS.md`, and `BABEL_PLATFORM.md` before discussing sibling-app learning concepts.

## Recreation creative intent

Do not create separate giant cover workflows. Use one Recreation engine with mutable creative bias:

- **Match** — approach the reference as faithfully as practical.
- **Interpret** — preserve identity while making meaningful production choices your own.
- **Reimagine** — freely change arrangement, instrumentation, feel, pacing, sound, or other production dimensions.

This bias can change during the project. A Match project may intentionally reinterpret one element without becoming a different project type.

For individual differences, FIRE can treat them as:

- **Match** — reduce this difference.
- **Intentional** — this difference belongs to our version.
- **Explore** — undecided; keep it available for experimentation.

A Recreation can therefore change nothing, one thing, or nearly everything.

## Guidance: firm on problems, open on art

FIRE can be firm when a technical/dependency problem has a clear consequence and open when the decision is artistic.

Useful framing:

- **Recommended** — strongest next move for the current diagnosis.
- **Alternative** — another valid solution with a different tradeoff.
- **Explore** — unconventional direction when breaking convention may create identity.

Every recommendation to add, remove, process, automate, double, widen, or otherwise change something should answer:

> **What job would this change perform, and why might it help this specific production?**

If FIRE cannot explain that, it should not recommend the change.

## Companion boundary

Do not recreate the DAW inside FIRE.

FIRE should mainly retain meaning the DAW does not understand well:

- intention/hierarchy
- what was heard
- diagnosis
- meaningful experiment + result
- accepted decision/difference
- unresolved problem
- reusable lesson
- next useful production decision

Do not require plugin settings, detailed routing, every take/region, every automation value, or every knob movement unless a future feature proves that information is necessary.

Default rhythm:

**FIRE → Logic → FIRE → Logic**

## Track / Element / Role — hypothesis to test

Current breadboarding hypothesis:

- **Track** — represented DAW/recorded part.
- **Element** — perceptual production object that may contain one or several tracks.
- **Role** — job the element performs: focal point, pulse, harmonic support, low-end movement, atmosphere, width, texture, etc.

Purpose: let FIRE reason about listener perception without duplicating Logic's mixer.

Do not lock exact data/UI before real projects prove it.

## Decision sequencing and finishing

FIRE should provide a reliable default order while allowing diagnosis to send the musician backward when an upstream issue is the real cause.

Conceptual order:

**Intent → Arrangement → Performance/source → Balance → Tone/dynamics → Space → Movement → Final comparison → Finish**

This is guidance, not a creative prison.

An **Arrangement Ready** state may be a soft commitment that current ingredients are sufficient to move into production/mixing. It must remain reversible.

Sparse arrangements are valid. Never recommend adding a track simply because a conventional instrument/frequency area is absent; adding something needs a musical job and reason.

Meaningful issues can finish as:

- **Resolved**
- **Accepted**
- **Unresolved**

This prevents perfection loops. Recreation does not require an indistinguishable clone unless faithful matching is actually the goal.

## Design references

Use references as lenses, not templates. `REFERENCES.md` is the registry.

Particularly useful FIRE lenses:

- **Apple** — hierarchy, familiarity, restraint, accessibility, contextual help.
- **Logic / Ableton / DAWs** — music-native mental models, creative flexibility, purposeful expert density.
- **Duolingo** — adaptive learning underneath; reject distracting gamification.
- **Basecamp / Shape Up** — calm organization; breadboard behavior before pixels.
- **GitHub / Primer** — stable vocabulary/hierarchy; naming is interface design.
- **ChatGPT** — layered explanation/presentation depth.
- **Things / Procreate** — substantial capability with restrained chrome.
- **Instagram / TikTok / Snapchat** — immediacy and low-friction interaction without engagement addiction.

## G7 shell vs FIRE Core

- **G7 shell** = current successor implementation/design generation and the reusable FIRE/Babel visual-interaction grammar being certified before product breadboarding.
- **FIRE Core** = complete functional product + shared reasoning/learning system.
- `G7_SHELL_CERTIFICATION.md` defines the G7 shell completion contract: ten categories move **Unresolved → Candidate → Locked**, with representative developer Shell Test coverage, real-G7 composition, physical-device validation, and explicit final approval. `G7_SHELL_CERTIFICATION_STATUS.md` records current category state/evidence.
- The developer Shell Test is G7 infrastructure using actual G7 primitives; it is not product architecture, a second FIRE implementation, or a substitute for physical validation.
- Current Setup → Structure → Tracks is disposable shell fixture content. Its polish does not approve the FIRE Core journey or its exact interactions.
- Do not begin FIRE Core breadboarding until all ten certification categories are Locked, the final physical-device sweep reveals no unresolved systemic contradiction, and Babel explicitly freezes the G7 shell.
- Shell freeze means the foundational grammar is stable enough to build confidently; it does not prohibit deliberate extension when a genuinely new FIRE Core requirement appears. Extend the smallest necessary primitive rather than casually reopening unrelated locked categories.
- After freeze, breadboard Original + Recreation Core end-to-end before deeply designing later phases.
- Understand the whole journey; deeply design only the next area being built.
- Real songs drive depth.

Current G7 route/primitive behavior lives in `V7_DRAFT.md`; certification definitions/freeze criteria live in `G7_SHELL_CERTIFICATION.md`; current category status/evidence lives in `G7_SHELL_CERTIFICATION_STATUS.md`; current review/build state lives in `START_HERE.md`. Do not duplicate moving details here.

## Wider Babel ecosystem boundary

FIRE Core does not define sibling-product jobs.

When discussion moves to surrounding apps, Babel World, a dedicated learning product, Visual Identity, WATER, badges/pixel language, or cross-app architecture, use:

1. `BABEL_START_HERE.md`
2. `BABEL_APPS.md`
3. `BABEL_PLATFORM.md`

Core ecosystem rule:

> **Product need earns an app. Naming/metaphor follows the job.**

Do not broaden FIRE or invent sibling products merely to complete an ecosystem diagram.

## Documentation authority and conflict policy

Git history is the canonical archive for retired implementation generations.

Keep the **current production generation specification + active successor/preview specification** in working documentation by default. Older generation specs remain only when a concrete maintenance, migration, compatibility, or recovery need still depends on them.

### FIRE authority

1. `AGENTS.md` — repository/process rules.
2. `FIRE_CORE.md` — current cross-generation product doctrine.
3. active production spec (`V6.md` today) — behavior shipped in that generation.
4. `V7_DRAFT.md` — G7 shell behavior where Core-compatible.
5. `G7_SHELL_CERTIFICATION.md` — active G7 shell completion/certification contract.
6. `G7_SHELL_CERTIFICATION_STATUS.md` — mutable category state/evidence.
7. `START_HERE.md` — current verified state/next step.
8. `CONTEXT.md` — durable supporting context not superseded above.
9. code/tests — implementation evidence, not product authority.

### Wider ecosystem authority

1. `AGENTS.md`
2. `BABEL_START_HERE.md`
3. `BABEL_APPS.md`
4. `BABEL_PLATFORM.md`
5. `FIRE_CORE.md` where FIRE semantics matter
6. `REFERENCES.md`
7. older prototypes/history

When durable FIRE doctrine changes, the same work must scan/reconcile affected `CONTEXT.md`, `START_HERE.md`, `AGENTS.md`, relevant generation specs, shell-certification authority/status, and ecosystem docs when cross-app semantics are affected.

Automated guards can catch known stale phrases/authority wiring, but no script can prove natural-language semantic consistency. Human/product consistency review remains required.

## Open hypotheses for FIRE Core breadboarding

Do not prematurely lock:

- exact Track → Element → Role data/UI
- whether coaching depth needs explicit control or remains contextual
- how skill confidence is represented without fake mastery
- exact optional Practice / Skills / Growth surface
- how project lessons feed targeted practice
- exact Fire visualization/growth mapping
- exact Recreation intent copy and whether chosen/inferred/edited later
- which later phases truly need which earlier information
- future audio-aware analysis; FIRE Core does not require it today

Sibling-app questions are intentionally not listed here; keep them in `BABEL_APPS.md`/`BABEL_PLATFORM.md` so FIRE doctrine remains focused.
