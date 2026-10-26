# Babel FIRE — Core Product Doctrine

**Status:** canonical cross-generation FIRE product doctrine. Generation specs describe implementation behavior; they do not override this file unless doctrine is deliberately changed in the same work.

## Naming

- **V6** — current production implementation generation.
- **G7** — frozen successor shell generation. Technical identifiers remain `V7_DRAFT.md`, `/v7-preview/`, and `production-projects-v1-v7-preview` unless a real migration reason appears.
- **FIRE Core** — first complete functional product: idea or reference → finished, release-ready audio with FIRE acting as a useful production companion.
- **FIRE 1.0** — future validated release milestone after FIRE Core proves itself on real projects and is intentionally promoted.

## Product promise

FIRE helps a musician answer:

> **What deserves my attention next, why, and what should I try in the DAW?**

FIRE is a production companion / decision engine, not a DAW replacement, plugin encyclopedia, generic checklist, automatic song generator, or mandatory course.

Success criterion:

> **After a useful FIRE session, the musician should know what to do in the DAW that they did not clearly know before opening FIRE. If they only updated FIRE, FIRE failed.**

FIRE Core ends at a finished, release-ready audio file plus essential delivery checks/basic metadata. Distribution, artwork, marketing, and scheduling remain outside the current Core boundary.

FIRE must remain useful as a standalone specialist. A musician should be able to open FIRE, make or finish a record, and leave satisfied without first creating a World profile, defining a career plan, or entering the wider Babel ecosystem.

## One FIRE brain, two first-class project types

### Original
Start with musical material or an idea and develop it into a finished record. The musician's intention defines the target. Guidance should organize decisions without policing creativity.

### Recreation / Cover
Use an existing song to make a faithful cover, reconstruction, interpretation, reimagining, or production study. Recreation is a complete standalone workflow, not a secondary learning mode and not dependent on Original.

One Recreation engine can carry a mutable creative bias:
- **Match** — approach the reference as faithfully as practical
- **Interpret** — preserve identity while making meaningful choices your own
- **Reimagine** — freely change arrangement, instrumentation, feel, pacing, sound, or other production dimensions

For an individual difference, FIRE may classify it as:
- **Match** — reduce the difference
- **Intentional** — the difference belongs to this version
- **Explore** — unresolved; keep it available for experimentation

## Shared reasoning engine

The FIRE loop is:

1. **Feel** — what do you perceive and what matters?
2. **Identify** — where is the meaningful difference/problem/opportunity?
3. **Reason** — what likely causes it and what kind of decision is this?
4. **Experiment** — make one intentional change/test in the DAW.
5. **Evaluate** — did it move toward the target, teach something useful, or reveal another problem?

Recreation gets its target from the reference plus the musician's chosen relationship to it. Original gets its target from the musician's intention.

## FIRE Knowledge model

FIRE combines three local knowledge layers:

- **Shared production knowledge** — research-backed production principles, dependencies, tradeoffs, failure modes, and useful experiments.
- **Project knowledge** — structure, elements, roles, intentions, observations, decisions, experiments, accepted choices, unresolved problems, and current production state.
- **Musician knowledge** — domain-specific evidence about what the person understands, struggles with, repeatedly chooses, prefers, rejects, or has learned across projects.

The knowledge system exists to support real production decisions, not to create a profile for its own sake.

For every meaningful Core step, breadboarding should ask:
- what production knowledge is relevant here?
- what project information must already exist?
- what can FIRE know from earlier work instead of asking again?
- what question is actually necessary to choose a useful next move?
- what musician preference/skill evidence materially changes the guidance?
- what recommendation can FIRE explain confidently?
- what should be preserved after the decision or experiment?

Adapt by **domain**, not one global Beginner/Intermediate/Advanced label. Do not front-load a large musician questionnaire. Learn progressively through work and timely clarification.

## Learning is ambient, optional, and applied

Making the record is always the primary task.

- teach through real production decisions whenever possible
- **“I don't know” / “Not sure” is valid** and should open a small diagnostic/explanation rather than block progress
- default to concise guidance; reveal deeper **Why?** progressively
- instructional detours must be skippable
- a quick-cover user must be able to move with minimal explanation
- FIRE may quietly retain skill evidence, lessons, repeated weaknesses, successful approaches, and explicit preferences
- page completion is not mastery

A future optional Practice / Skills / Growth surface may summarize development, but learning progress must not become mandatory workflow chrome. A separate learning product is not earned merely because FIRE teaches; wider product questions belong to Babel Truth/Lab, not FIRE doctrine.

## Guidance: firm on problems, open on art

FIRE can be firm when a technical/dependency problem has a clear consequence and open when the decision is artistic.

Useful framing:
- **Recommended** — strongest next move for the current diagnosis and context
- **Alternative** — another valid solution with a different tradeoff
- **Explore** — unconventional direction when breaking convention may create identity

Recommendations should be allowed to be opinionated when the evidence supports one strongest current move. User agency remains explicit: a recommendation can be rejected, deferred, or replaced by another valid direction, and that decision may become useful musician/project knowledge.

Every recommendation to add, remove, process, automate, double, widen, or otherwise change something should answer:

> **What job would this change perform, and why might it help this specific production?**

If FIRE cannot explain that, it should not recommend the change.

## Companion boundary

Do not recreate the DAW inside FIRE.

FIRE should mainly retain meaning the DAW usually does not understand well:
- intention/hierarchy
- what was heard
- diagnosis
- meaningful experiment + result
- accepted decision/difference
- unresolved problem
- reusable lesson
- next useful production decision

Do not require detailed routing, plugin settings, every take/region, every automation value, or every knob movement unless a future feature proves that information necessary.

Default rhythm:

**FIRE → Logic → FIRE → Logic**

## Sequencing is a dependency map, not a course

Current default production order:

**Intent → Arrangement → Performance/source → Balance → Tone/dynamics → Space → Movement → Final comparison → Finish**

Treat that order as a strong breadboarding hypothesis, not a locked linear curriculum. FIRE should understand dependency direction well enough to reopen upstream work when downstream symptoms reveal the real problem. A mix problem may actually be arrangement; a tone problem may actually be source/performance; a finishing problem may expose an unresolved intention.

The goal is not to make every user complete every production topic. The goal is to surface the production area that currently has the highest useful leverage for this record.

An **Arrangement Ready** state may be a reversible soft commitment that current ingredients are sufficient to move forward.

Meaningful issues can finish as:
- **Resolved**
- **Accepted**
- **Unresolved**

This helps prevent perfection loops. Recreation does not require an indistinguishable clone unless faithful matching is actually the goal.

## Track → Element → Role — hypothesis

Current breadboarding hypothesis:
- **Track** — represented DAW/recorded part
- **Element** — perceptual production object that may contain one or several tracks
- **Role** — job the element performs: focal point, pulse, harmonic support, low-end movement, atmosphere, width, texture, etc.

Purpose: reason at listener-perception level without duplicating Logic's mixer. Do not lock exact data/UI before real projects prove it.

## Cross-app boundary

Babel Truth ADR 0005 governs cross-app context. FIRE owns detailed production knowledge and should not expose its entire internal reasoning model merely because another Babel product exists.

If a FIRE fact genuinely matters outside FIRE, expose only the smallest meaningful projection needed by the destination. Candidate examples to prove through real use include:
- stable song/record identity and type
- explicit intent relevant outside production
- relationship to a larger body of work
- high-level production state or continuation point
- meaningful accepted decisions another product should not re-ask
- provenance indicating FIRE owns the production source state
- a destination/return context for continuing production

Do not lock a universal schema from these examples. Prove the fields through real FIRE → World → FIRE or future specialist flows first.

FIRE should not advertise World mechanically after every project. The specialist must provide value first. An optional “take this further” invitation is appropriate only when the user's work creates a genuinely new broader possibility, and it should not repeat once that possibility has already been accepted, declined, or established elsewhere.

Likewise, when another Babel product sends a user into FIRE with valid context, FIRE should use that context rather than starting from a blank onboarding question.

## Larger bodies of work — active hypothesis

FIRE currently treats Original and Recreation/Cover as production workflows for a record/song. A larger body of work such as a single, EP, or album is a different dimension and should not be added as a third peer project type beside Original/Cover without evidence.

Breadboarding should test whether FIRE needs a lightweight relationship above individual song projects so multiple FIRE records can belong to one larger music project while FIRE owns only the production facet. Album-level production capabilities such as sequencing, transitions, cohesion, and delivery consistency must be earned through real project use rather than invented as a suite up front.

World or another future product may understand a broader album context, but FIRE must still support larger music work independently if that production job is proven useful.

## G7 shell vs FIRE Core

- **G7 shell** = frozen successor implementation/design generation and reusable shell grammar.
- **FIRE Core** = complete functional production companion + reasoning/learning system.
- Current `Setup → Structure → Tracks` is disposable shell fixture content. Its polish does not approve the FIRE Core journey, Map architecture, checkpoint count, or exact future interactions.
- `G7_SHELL_CERTIFICATION.md` is the completed finite shell contract; `G7_SHELL_CERTIFICATION_STATUS.md` records **10 / 10 Locked** and the freeze evidence.
- The approved shell runtime anchor is `4a258c5170dd1d96dcbc0f2b0a9c35b283cec489`.
- Shell Test is G7 developer infrastructure using actual G7 primitives; it is not product architecture, a second FIRE implementation, or a substitute for physical validation.
- **FIRE Core breadboarding may now begin.** The shell freeze gate has been satisfied and Babel explicitly approved the final physical-review result.
- Shell freeze means the foundational grammar is stable enough to build confidently; it does not prohibit a deliberate minimal extension when FIRE Core proves a genuinely new primitive is needed.
- Do not casually reopen locked shell categories because Core content differs from fixtures. Reopen only when new evidence shows the foundation itself is wrong.
- Breadboard Original + Recreation Core end-to-end before deeply designing later phases.
- Understand the whole journey; deeply design only the next area being built.
- Real songs drive depth.

Current route/primitive behavior lives in `V7_DRAFT.md`; current build/next-step state lives in `START_HERE.md`.

## Documentation authority and conflict policy

Shared cross-app process/design rules come from the immutable Babel Truth commit pinned in `BABEL_TRUTH.md`.

FIRE-local authority is:
1. `FIRE_CORE.md` — doctrine
2. `V6.md` — shipped production behavior
3. `V7_DRAFT.md` — frozen successor shell behavior
4. `G7_SHELL_CERTIFICATION.md` — completed shell certification/freeze contract
5. `G7_SHELL_CERTIFICATION_STATUS.md` — completed certification evidence/status
6. `START_HERE.md` — exact current verified state/next gate
7. code/tests — implementation evidence

Git/PR history is the archive. Do not create parallel ecosystem ledgers, supporting-context catchalls, or changelog-as-authority files in FIRE.

When doctrine changes, reconcile affected active FIRE authority/tests/handoff in the same work. Wider ecosystem/product exploration belongs to Babel Truth/Lab until a real owning product exists.

## Open hypotheses for FIRE Core breadboarding

These are now active breadboarding questions, not shell blockers. Do not prematurely lock:
- exact Track → Element → Role data/UI
- exact dependency/curriculum graph behind the current production-order hypothesis
- what evidence is required before FIRE can recommend one production move over another
- whether coaching depth needs explicit control or remains contextual
- how skill confidence is represented without fake mastery
- exact optional Practice / Skills / Growth surface
- how project lessons feed targeted practice
- exact Fire visualization/growth mapping
- exact Recreation intent copy and whether chosen/inferred/edited later
- which later phases truly need which earlier information
- whether/how standalone song projects relate to a larger single/EP/album container
- exact minimal cross-app projection fields; prove them before standardizing
- future audio-aware analysis; FIRE Core does not require it today
