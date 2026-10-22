# Babel FIRE — Core Product Doctrine

**Status:** Canonical cross-generation product doctrine. Version specs describe implementation generations; they do not override this file unless the doctrine is deliberately changed in the same work.

## Naming

- **V6 / V7 / future Vx** = implementation, shell, and interaction generations.
- **FIRE Core** = the first complete functional product: idea or reference → finished, release-ready audio file with FIRE acting as a useful production companion.
- **FIRE 1.0** = a future release milestone after FIRE Core is validated on real projects and intentionally promoted.
- Do not call FIRE Core “V1.”

## Product promise

FIRE helps a musician answer:

> **What deserves my attention next, why, and what should I try in the DAW?**

FIRE is a production companion, not a DAW replacement, plugin encyclopedia, generic checklist, automatic song generator, or mandatory course.

Success criterion:

> **After a useful FIRE session, the musician should know what to do in the DAW that they did not clearly know before opening FIRE. If they only updated FIRE, FIRE failed.**

FIRE Core ends at a finished, release-ready audio file plus essential delivery checks/basic metadata. Distribution, artwork, marketing, and scheduling are outside the current Core boundary.

## One FIRE brain, two first-class project types

### Original

Start with any musical material or idea and develop it into a finished record. Original stays creatively flexible; guidance should organize decisions without policing creativity.

### Recreation

Use an existing song to make a faithful cover, reconstruction, interpretation, reimagining, or production study. Recreation is a complete standalone workflow. A person may use FIRE only to make covers quickly and never engage with learning history or Original mode.

Recreation can also build production judgment that later helps Original work, but learning is a benefit of the workflow, not a prerequisite for completing it.

## Shared reasoning engine

The FIRE loop is:

1. **Feel** — what do you perceive and what matters?
2. **Identify** — where is the meaningful difference/problem/opportunity?
3. **Reason** — what likely causes it and what kind of decision is this?
4. **Experiment** — make one intentional change or test in the DAW.
5. **Evaluate** — did it move toward the target, teach something useful, or reveal another problem?

Recreation gets its target from the reference plus the musician’s chosen relationship to it. Original gets its target from the musician’s own intention.

## Knowledge model

FIRE combines:

- **Shared production knowledge** — research-backed principles and tradeoffs.
- **Project knowledge** — what is true about this song: structure, tracks/elements, roles, intentions, observations, decisions, experiments, unresolved problems.
- **Musician knowledge** — what this person seems comfortable with, struggles with, repeatedly chooses, or has learned across projects.

Adapt by **domain**, not one global Beginner/Intermediate/Advanced label. A musician can be strong at arrangement and inexperienced at mastering.

## Learning is ambient, optional, and applied

Making the record is always the primary task.

- Teach through real production decisions whenever possible.
- **“I don’t know” / “Not sure” is a valid answer.** It should open a small diagnostic or explanation, not block progress.
- Default to concise guidance; offer **Why?** and deeper help progressively.
- Any instructional detour must be skippable.
- A quick-cover user should be able to keep moving with minimal explanation.
- FIRE may quietly track skills practiced, useful lessons, repeated weaknesses, and successful approaches, but learning progress must not become mandatory workflow chrome.
- Do not treat page completion as mastery.
- Duolingo is inspiration for adaptive learning and learn-by-doing, not a requirement to add XP, streaks, cartoon paths, or forced lessons.

A future optional Skills/Growth/Insights or Practice surface may summarize development and offer targeted category practice without being required to finish music. A living, shareable visualization of growth (working concept: the user’s **Fire**) is also worth prototyping, but it must represent credible learning evidence rather than raw usage, page completion, or a punitive daily streak. These remain future hypotheses; see `BABEL_PLATFORM.md`.

## Recreation creative intent

Do not create separate giant cover workflows. Use one Recreation engine with a mutable creative bias:

- **Match** — approach the reference as faithfully as practical.
- **Interpret** — preserve the song’s identity while making meaningful production choices your own.
- **Reimagine** — freely change arrangement, instrumentation, feel, pacing, sound, or other production dimensions.

This bias can change during the project. A Match project may intentionally reinterpret one element without becoming a different project type.

For individual differences, FIRE can treat them as:

- **Match** — reduce this difference.
- **Intentional** — this difference belongs to our version.
- **Explore** — undecided; keep it available for experimentation.

A Recreation can therefore change nothing, one thing, or nearly everything.

## Guidance: firm on problems, open on art

FIRE can be firm when a technical/dependency problem has a clear consequence and open when the decision is artistic.

Useful recommendation framing:

- **Recommended** — strongest next move for the current diagnosis.
- **Alternative** — another valid solution with a different tradeoff.
- **Explore** — an unconventional direction when breaking convention may create identity.

Every recommendation to add, remove, process, automate, double, widen, or otherwise change something should answer:

> **What job would this change perform, and why might it help this specific production?**

If FIRE cannot explain that, it should not recommend the change.

## Companion boundary

Do not recreate the DAW inside FIRE.

FIRE should mainly retain meaning the DAW does not understand well:

- intention and hierarchy
- what was heard
- diagnosis
- meaningful experiment and result
- accepted decision/difference
- unresolved problem
- reusable lesson
- next useful production decision

Do not require plugin settings, detailed routing, every take/region, every automation value, or every knob movement unless a future feature proves that information is necessary.

## Track / Element / Role — hypothesis to test

Current breadboarding hypothesis:

- **Track** — a represented DAW/recorded part.
- **Element** — one perceptual production object that may contain one or several tracks.
- **Role** — the job that element performs, such as focal point, pulse, harmonic support, low-end movement, atmosphere, width, or texture.

This exists to let FIRE reason about what the listener perceives without duplicating Logic’s mixer. Do not lock the exact data model before real projects prove it.

## Decision sequencing and finishing

FIRE should provide a reliable default order of operations while allowing diagnosis to send the musician backward when an upstream issue is the real cause.

Conceptual order:

**Intent → Arrangement → Performance/source → Balance → Tone/dynamics → Space → Movement → Final comparison → Finish**

This is guidance, not a creative prison.

An **Arrangement Ready** state may be a soft commitment that the current ingredients are sufficient to move into production/mixing. It must remain reversible.

Sparse arrangements are valid. Never recommend adding a track simply because a conventional instrument or frequency area is absent; adding something needs a musical job and a reason.

Meaningful issues can finish as:

- **Resolved**
- **Accepted**
- **Unresolved**

This prevents perfection loops. Recreation does not require an indistinguishable clone unless faithful matching is actually the goal.

## Design references

Use references as lenses, not templates:

- **Apple** — hierarchy, familiarity, restraint, accessibility, optional/contextual guidance.
- **Logic Pro / other DAWs** — music-native mental models, grouping, creative flexibility, professional density when needed.
- **Duolingo** — adaptive learning, learn-by-doing, personal progress; reject distracting gamification.
- **Basecamp** — lots of content/actions with calm organization; breadboard behavior before pixel polish.
- **GitHub** — history, reversibility, progressive disclosure.
- **ChatGPT** — layered explanation depth.
- **Instagram / TikTok / Snapchat** — immediacy and low-friction capture/action, not engagement addiction.

Additional references can change over time. Current useful candidates include Ableton Live, Things, Linear, and Figma.

## Shell vs Core

- **V7 Shell** = current implementation/design generation.
- **FIRE Core** = complete functional product and shared reasoning/learning system.
- Finish the Shell once: shared headers, typography, spacing/rhythm, grouping, states, sheets, natural scrolling, adaptive presentation, and declutter rules should become reusable defaults instead of being re-debated route by route.
- Then breadboard the complete Original + Recreation Core end-to-end before deeply designing later phases.
- Understand the whole journey; deeply design only the next area being built. Real songs drive depth.

## Documentation authority and conflict policy

Historical/versioned specs remain useful library material and must not be erased merely because a newer generation exists. Their rules are scoped to the generation they describe.

Authority order:

1. `AGENTS.md` — repository/workflow/documentation process.
2. `FIRE_CORE.md` — current cross-generation product doctrine.
3. Active production spec (`V6.md` today) — behavior actually shipped in that generation.
4. `V7_DRAFT.md` — V7 shell behavior where compatible with FIRE Core.
5. `CONTEXT.md` — supporting history/details not superseded above.
6. Current code/tests — implementation evidence, not product authority.

When a durable idea changes FIRE Core doctrine, the same PR must update this file, scan/reconcile affected guidance in `CONTEXT.md`, `START_HERE.md`, `AGENTS.md`, and relevant specs, and clearly scope historical behavior instead of letting contradictory live rules accumulate.

Automated guards may catch known stale phrases and authority wiring, but no script can prove natural-language product documents are semantically contradiction-free. Human consistency review remains required.

## Open hypotheses for breadboarding

Do not prematurely lock:

- exact Track → Element → Role data/UI
- whether coaching depth needs an explicit control or remains contextual
- how skill confidence is represented without fake mastery
- exact optional Practice/Skills/Growth surface and how project lessons feed targeted practice
- whether/how the user’s Fire visualizes growth without becoming a fake global producer score
- exact Recreation intent copy and whether it is chosen, inferred, or edited later
- which later phases truly need which earlier information
- future audio-aware analysis; FIRE Core does not require it today
