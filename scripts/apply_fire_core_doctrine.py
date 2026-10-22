from pathlib import Path


def replace_once(path: str, old: str, new: str) -> None:
    p = Path(path)
    text = p.read_text(encoding="utf-8")
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{path}: expected one match, found {count}: {old[:80]!r}")
    p.write_text(text.replace(old, new), encoding="utf-8")


FIRE_CORE = r'''# Babel FIRE — Core Product Doctrine

**Status:** Current cross-generation product doctrine. This file defines what FIRE is trying to accomplish regardless of which implementation generation is active. `V6.md` and `V7_DRAFT.md` describe generation-specific behavior; they do not override this doctrine unless a deliberate product-doctrine change updates this file in the same change.

## Naming

Keep implementation generations separate from product milestones:

- **V6 / V7 / future Vx** = implementation, shell, and interaction generations.
- **FIRE Core** = the first complete functional product definition: a musician can use FIRE as a useful companion from an idea or reference through a finished, release-ready audio file.
- **FIRE 1.0** = a future release milestone only after FIRE Core has been validated on real projects and is intentionally promoted as a releasable product.

Do not call FIRE Core “V1.” That collides with implementation-generation numbering.

## Product promise

FIRE helps a musician answer:

> **What deserves my attention next, why, and what should I try in the DAW?**

FIRE is a production companion, not a DAW replacement, plugin encyclopedia, generic checklist, automatic song generator, or mandatory course.

Success criterion:

> **After a useful FIRE session, the musician should know what to do in the DAW that they did not clearly know before opening FIRE. If they only updated FIRE, FIRE failed.**

The product should support the path from a simple idea or reference to a finished, release-ready audio file. Distribution, artwork, marketing, and release scheduling are outside FIRE Core unless a later product decision expands the boundary.

## One FIRE brain, two first-class project types

### Original

Start with any musical material or idea and develop it into a finished record. Original is FIRE's primary long-term creative workflow, but it must remain creatively flexible rather than policing a fixed sequence.

### Recreation

Use an existing song as a reference to make a cover, reconstruction, interpretation, reimagining, or production study. Recreation is a complete standalone workflow. A musician may use Recreation only to make covers and never use Original or the learning history; that is a fully valid FIRE use case.

Recreation can also develop production judgment that later helps Original work, but learning is a benefit of using the workflow, not a prerequisite for completing it.

Both project types share the same reasoning engine and production knowledge while differing in what defines the target.

## Shared reasoning engine

The FIRE acronym remains the core problem-solving loop:

1. **Feel** — what do you perceive and what matters?
2. **Identify** — where is the meaningful difference/problem/opportunity?
3. **Reason** — what likely causes it and what category of decision is this?
4. **Experiment** — make one intentional change or test in the DAW.
5. **Evaluate** — did it move the production toward the target, teach something useful, or reveal a different problem?

The app may use simpler user-facing language when appropriate. The internal reasoning should prefer the smallest useful next decision rather than blindly advancing a checklist.

For Recreation, the target is anchored by the reference plus the musician's chosen relationship to it. For Original, the target is the musician's intention for the record.

## Knowledge model

FIRE guidance combines three layers:

### Shared production knowledge

Research-backed and practice-tested concepts such as hierarchy, arrangement, performance/source quality, masking, balance, dynamics, depth, width, movement, contrast, and finishing. This knowledge explains options and tradeoffs; it does not dictate artistic taste.

### Project knowledge

What FIRE knows about the current song: sections, tracks/elements, roles, focal points, intentions, observations, unresolved problems, accepted decisions, meaningful experiments, and downstream dependencies.

### Musician knowledge

What this musician appears comfortable with, struggles with, repeatedly chooses, has already learned, or has consciously rejected across projects. This should adapt by **domain**, not assign one global Beginner/Intermediate/Advanced label.

A musician can be strong at arrangement and inexperienced at mastering, or technically experienced but new to a particular workflow. FIRE must support those mixed profiles.

## Learning model: ambient, optional, and applied

FIRE can become a powerful production-learning system without turning every project into a lesson.

Rules:

- **Making the record is always the primary task.** Learning content supports the task rather than interrupting it.
- Teach through the musician's real project and real decision whenever possible.
- **“I don't know” / “Not sure” is a first-class answer.** It should open a small diagnostic or explanation instead of blocking the workflow.
- Provide layered depth: concise next action by default, a short **Why?** when useful, and deeper explanation/practice only when requested or clearly beneficial.
- Any instructional detour should be skippable. A musician who wants to make a quick cover should be able to keep moving with minimal explanation.
- FIRE may quietly record skills practiced, useful lessons, repeated weaknesses, and successful approaches, but learning progress must not become mandatory workflow chrome.
- Do not equate button taps or completed pages with mastery. Skill confidence requires evidence from real decisions over time.
- Avoid importing Duolingo's XP, streak pressure, cartoon path, or forced lesson cadence unless later evidence proves a specific mechanic improves music-making rather than distracts from it.

A future optional **Skills / Growth / Insights** surface may summarize development across production domains. It is not required to complete a project.

## Coaching depth

Do not force a permanent “learning mode” vs “quick mode” split unless real use proves that explicit modes are necessary.

Default behavior should adapt in place:

- **Do it** — concise mission and necessary context.
- **Why?** — simple rationale and what to listen for.
- **Go deeper** — richer explanation, alternatives, diagnostic help, or practice.

The musician can always skip educational detail and continue producing. FIRE can gradually reduce explanations in domains where the musician consistently demonstrates confidence and offer more scaffolding where they repeatedly choose `Not sure`, ask for help, or struggle.

## Recreation creative intent

Recreation must support both faithful covers and radical reinterpretations without creating separate giant workflows.

A project's **relationship to the reference** is a mutable creative bias, not a hard gate:

- **Match** — approach the reference as faithfully as practical.
- **Interpret** — preserve the song's identity while making meaningful production choices your own.
- **Reimagine** — use the reference as creative source material and freely change arrangement, instrumentation, feel, pacing, sound, or other production dimensions.

The relationship can change during the project. A Match project may intentionally reinterpret one element without becoming a different project type.

For individual reference differences, FIRE should support states such as:

- **Match** — this difference is something we want to reduce.
- **Intentional** — this difference is part of our version and should not be treated as a defect.
- **Explore** — we have not decided yet; keep it available for experimentation.

Therefore a Recreation can change nothing, one thing, or nearly everything while still using the same production reasoning system.

## Production guidance: firm on problems, open on art

FIRE should be firmer when a technical or dependency problem has a clear consequence and more open when the decision is artistic.

Examples:

- Clipping, broken prerequisites, or an unintelligible focal element can justify strong guidance.
- Whether a chorus should feel huge or intimate is an artistic target; FIRE should offer valid directions and tradeoffs rather than choose taste for the musician.

A useful recommendation pattern is:

- **Recommended** — strongest next move for the current diagnosis.
- **Alternative** — another legitimate solution with a different tradeoff.
- **Explore** — a deliberately unconventional direction when breaking convention may produce identity.

Every recommendation to add, remove, process, automate, double, widen, reverberate, or otherwise change something should be able to answer:

> **What job would this change perform, and why might it help this specific production?**

If FIRE cannot explain that, it should not recommend the change.

## Track, Element, and Role — current modeling hypothesis

Do not assume one DAW track equals one perceptual production object.

Current hypothesis to test during FIRE Core breadboarding:

- **Track** — an actual recorded/DAW part the musician chooses to represent in FIRE.
- **Element** — one perceptual production object that may contain one or several Tracks, such as a multi-layer Synth Bed.
- **Role** — the musical/production job an Element performs, such as focal point, harmonic support, pulse, low-end movement, atmosphere, width, transition, or texture.

This model exists to reduce duplication and let FIRE reason about how the listener perceives the record. It must not require the musician to recreate Logic's mixer, routing, plugins, or every region inside FIRE.

Treat this as a hypothesis until real projects prove the exact data model and UI.

## Companion boundary: store meaning, not DAW bureaucracy

FIRE generally should not duplicate information Logic already owns well, such as plugin settings, detailed automation values, exact routing, every take, every region, or every knob movement.

FIRE should preferentially retain the meaning Logic does not understand:

- intention
- role / hierarchy
- what was heard
- what felt wrong or promising
- diagnosis
- meaningful experiment
- result of the experiment
- accepted decision / accepted difference
- unresolved problem
- what should be revisited next
- reusable production lesson

Meaningful experiment history should preserve what was learned, not become a forensic log of every setting change.

## Decision sequencing and arrangement readiness

FIRE should provide a reliable default order of operations while allowing diagnosis to send the musician backward when an upstream issue is the real cause.

A useful conceptual progression is:

**Intent → Arrangement → Performance/source → Balance → Tone/dynamics → Space → Movement → Final comparison → Finish**

This is a reasoning order, not a prohibition on creative exploration.

An **Arrangement Ready** state may act as a soft commitment: the current musical ingredients appear sufficient to move into production/mixing. It must not permanently lock arrangement. If later diagnosis reveals an arrangement problem, FIRE can deliberately reopen it.

Sparse arrangements are valid. FIRE must never recommend adding a track simply because a conventional instrument or frequency region is absent. Adding something needs a musical job and a reason.

## Project outcomes and accepted decisions

FIRE must prevent perfection loops.

A meaningful issue/difference can resolve as:

- **Resolved** — the musician changed something and considers the issue addressed.
- **Accepted** — the difference/choice is understood and intentionally left as-is.
- **Unresolved** — it remains worth revisiting.

For Recreation, success does not require an indistinguishable clone. For Original, success does not require exhausting every possible idea. Finishing means the important remaining choices are understood and intentionally committed.

## Design doctrine

FIRE should support substantial capability without making the musician think about FIRE's organization.

Use these references as **lenses, not visual templates**:

- **Apple** — hierarchy, familiarity, accessibility, restrained defaults, optional/contextual guidance.
- **Logic Pro and other DAWs** — music-native mental models, grouping, hierarchy, creative flexibility, professional density where the task requires it.
- **Duolingo** — learn by doing, adaptive challenge, personal progress, and reinforcing weak skills; reject gamification that distracts from making music.
- **Basecamp** — large information/action capacity with calm organization; breadboard behavior before pixel-polishing it.
- **GitHub** — history, reversible changes, progressive disclosure, powerful capability without requiring every detail at once.
- **ChatGPT** — layered explanations and guidance depth that can adapt to the person's question.
- **Instagram / TikTok / Snapchat** — immediacy, low-friction capture/action, content-first presentation; do not import addictive engagement mechanics into production work.

Additional useful references can change over time. Current candidates include Ableton Live for creative workflow education, Things for calm task hierarchy, Linear for dense-but-fast professional interaction, and Figma for progressive disclosure in a powerful creative tool.

No reference is authoritative by brand name. Adopt only patterns that improve FIRE's actual job.

## Shell vs Core

- **V7 Shell** is the current implementation/design generation being refined and frozen around Projects → Project Home → focused work.
- **FIRE Core** defines the complete functional product and the shared reasoning/learning system.
- Finish the Shell once: shared headers, typography, spacing/rhythm, grouping, states, sheets, natural scrolling, adaptive presentation, and declutter rules should become reusable defaults rather than being re-debated route by route.
- Then breadboard the complete FIRE Core end-to-end before deeply designing later phases.
- Understand the whole journey, but deeply design only the next area being built. Real songs drive depth.

## Documentation authority and conflict policy

This file is the canonical source for current cross-generation product doctrine.

Historical/versioned implementation documents remain valuable evidence and must not be erased simply because a newer generation exists. Their rules are scoped to the generation they describe.

When sources appear to conflict:

1. `AGENTS.md` governs repository workflow, engineering, and documentation process.
2. `FIRE_CORE.md` governs current cross-generation product purpose, shared reasoning, learning philosophy, project-type semantics, and product boundaries.
3. The active production implementation spec (`V6.md` today) governs behavior that actually ships in that generation.
4. `V7_DRAFT.md` governs the experimental V7 shell where it does not conflict with FIRE Core doctrine.
5. `CONTEXT.md` preserves durable supporting history, detailed workflow knowledge, and decisions not superseded above.
6. Current code/tests are implementation evidence, not product authority.

If a new durable idea changes FIRE Core doctrine, the same pull request must:

- update `FIRE_CORE.md`,
- scan/reconcile `CONTEXT.md`, `START_HERE.md`, `AGENTS.md`, and any affected active/experimental spec,
- clearly scope historical behavior instead of deleting useful history,
- update regression/doc guards when a known stale phrase or authority rule could reintroduce a conflict.

Automated checks can catch known authority markers and stale phrases, but no script can prove that natural-language product documents are semantically contradiction-free. The required human consistency audit remains part of product-definition work.

## Current open hypotheses for breadboarding

Do not prematurely lock these before real project evidence:

- the exact UI/data model for Track → Element → Role
- whether coaching depth needs an explicit control or can remain entirely contextual
- how skill confidence is represented without fake mastery or gamification
- how Original and Recreation share phase engines while preserving different creative targets
- exact Recreation intent copy and whether it is chosen up front or inferred/edited later
- which information later phases truly need from earlier phases
- whether future audio-aware analysis earns its complexity; FIRE Core does not require it today

The next product-definition artifact should breadboard the full Original and Recreation journeys at the level of places, decisions, carried-forward knowledge, DAW actions, and definitions of done before deep visual design of later phases.
'''

Path("FIRE_CORE.md").write_text(FIRE_CORE, encoding="utf-8")

# AGENTS: make cross-generation product doctrine authoritative and remove stale next-step language.
replace_once(
    "AGENTS.md",
    """1. **AGENTS.md** — repository workflow, engineering, maintenance, review, and documentation rules.\n2. **Active version specification, currently V6.md** — approved requirements for the active product generation; supersedes older UI/product descriptions where they conflict.\n3. **CONTEXT.md** — durable product philosophy, architecture, learning/workflow context, and decisions intended to survive across versions.\n4. **Current code and tests** — implementation evidence; they do not override explicit approved product requirements.\n\nIf a genuine conflict remains after applying this hierarchy, ask rather than guessing.""",
    """1. **AGENTS.md** — repository workflow, engineering, maintenance, review, and documentation rules.\n2. **FIRE_CORE.md** — current cross-generation product doctrine: purpose, shared reasoning/learning model, project-type semantics, and product boundaries.\n3. **Active production specification, currently V6.md** — approved requirements for the behavior that ships in the active production generation. Generation-specific rules do not override FIRE Core doctrine unless the doctrine is deliberately changed in the same work.\n4. **V7_DRAFT.md** — experimental V7 shell behavior and interaction direction, scoped to that generation.\n5. **CONTEXT.md** — durable supporting history, detailed learning/workflow context, and decisions not superseded above.\n6. **Current code and tests** — implementation evidence; they do not override explicit approved product requirements.\n\nHistorical/versioned specifications are a library of generation-specific truth, not current universal doctrine. If a genuine conflict remains after applying this hierarchy, reconcile the durable product documents rather than silently choosing one.""",
)
replace_once(
    "AGENTS.md",
    "- Read `CONTEXT.md`, the active specification, and relevant code/tests before product work. The active approved implementation scope is **V6**.",
    "- Read `FIRE_CORE.md`, `CONTEXT.md`, the relevant generation specification, and relevant code/tests before product work. The active shipped implementation scope is **V6**; V7 remains an isolated preview until deliberately promoted.",
)
replace_once(
    "AGENTS.md",
    "- The current approved next step is a global FIRE Design System foundation pass. Do not continue route-by-route cosmetic micro-polish without first fixing shared typography, spacing, surfaces, controls, states, and adaptive presentation.",
    "- The current design objective is **V7 Shell Freeze**: one deliberate declutter/system pass should lock reusable header archetypes, typography, spacing/rhythm, grouping, states, sheets, natural scrolling, and adaptive presentation. After that, stop broad shell churn and breadboard FIRE Core end-to-end before deeply designing later phases.",
)
replace_once(
    "AGENTS.md",
    "- Short phone pages that fit within the visual viewport must not create unnecessary root scrolling or rubber-band drift. Use dynamic viewport sizing/overscroll containment while preserving natural scrolling when content genuinely exceeds the viewport.\n- Pages that genuinely scroll on iOS Safari must provide enough scroll-end clearance for the final interactive row to rise fully above dynamic browser chrome; short pages must not reserve that clearance and become fake-scroll pages.",
    "- Document height determines page scrolling. Never switch root overflow based on live `VisualViewport` measurements while Safari chrome moves; short pages remain naturally short and genuinely tall pages scroll normally.\n- Tall iOS Safari pages may use modest CSS-only end clearance so final controls can rise above browser chrome. Short pages must not reserve a fake-scroll tail. Modal sheets may temporarily lock background scrolling while open.",
)
replace_once(
    "AGENTS.md",
    "- Major approved product/interaction generations increment the whole version: V5 → V6.",
    "- **V6 / V7 / future Vx** are implementation/product-interaction generations. **FIRE Core** is the first complete functional product definition, not `V1`. **FIRE 1.0** is reserved for a future validated release milestone.\n- Major approved product/interaction generations increment the whole version: V5 → V6.",
)
replace_once(
    "AGENTS.md",
    "- `CONTEXT.md` is not a changelog. It stores durable product decisions, architecture principles, and reusable interaction rules. Preserve valid durable V5 additions; change it only when those rules change.",
    "- `FIRE_CORE.md` is the canonical current cross-generation product doctrine. A durable doctrine change must update it and reconcile affected guidance in `CONTEXT.md`, `START_HERE.md`, `AGENTS.md`, and relevant generation specs in the same PR.\n- `CONTEXT.md` is not a changelog. It stores durable supporting history, detailed workflow knowledge, and decisions that remain valid under FIRE Core. Preserve useful historical/version-specific evidence, but scope it clearly when superseded so it cannot compete with current doctrine.",
)

# CONTEXT: remove active contradictions and point current doctrine to FIRE_CORE.
replace_once(
    "CONTEXT.md",
    "This is the durable product/design context for Babel FIRE, not a changelog or a report of what has shipped. Begin continuations with `START_HERE.md` and follow the source-of-truth order in `AGENTS.md`: repository rules, active version specification (currently `V6.md`), this context, then current code/tests. The active specification supersedes older product/UI descriptions here where they conflict.",
    "This is durable supporting product/design context for Babel FIRE, not a changelog or a report of what has shipped. Begin continuations with `START_HERE.md` and follow the source-of-truth order in `AGENTS.md`. `FIRE_CORE.md` is the canonical current cross-generation product doctrine; version specs describe generation-specific behavior, and this file preserves deeper workflow/history that remains valid under that doctrine.",
)
replace_once(
    "CONTEXT.md",
    "- This file is the source of truth for **why FIRE works the way it does**, the user's production-learning profile, and decisions that must survive future chats.",
    "- `FIRE_CORE.md` is the source of truth for current cross-generation product doctrine. This file preserves supporting workflow/history, the reference user's design-relevant production profile, and detailed decisions that remain compatible with FIRE Core.",
)
replace_once(
    "CONTEXT.md",
    """### Original Song — PRIMARY\nThe main long-term product.\nGoal: start with anything → finish a record.\n\n### Recreation — SECONDARY / LEARNING MODE\nTake an existing record apart, reconstruct it, and learn production decisions by doing.\n\n**Smithereens by Twenty One Pilots is the first preloaded Recreation.**""",
    """### Original Song\nThe main long-term creative workflow.\nGoal: start with anything → finish a record.\n\n### Recreation\nA first-class standalone cover/reconstruction workflow that can range from faithful Match to Interpretation or full Reimagination. Recreation can develop production judgment through use, but learning is optional and must never be a prerequisite for someone who simply wants to complete a cover efficiently.\n\n**Smithereens by Twenty One Pilots is the first preloaded Recreation.**""",
)
replace_once(
    "CONTEXT.md",
    "- Assume the user is an experienced musician/creator with working familiarity with common production concepts; do not teach from absolute zero unless asked.",
    "- The reference user has strong musical experience but uneven production confidence by domain. FIRE itself must not require prior production knowledge: adapt guidance by domain, let `I don't know` be a valid answer, and avoid one global Beginner/Intermediate/Advanced assumption.",
)
replace_once(
    "CONTEXT.md",
    "FIRE should emphasize structured listening, diagnosis, intentional experimentation, and finishing. It should not behave like a beginner course, a plugin encyclopedia, or an automatic song generator.",
    "FIRE should emphasize structured listening, diagnosis, intentional experimentation, and finishing. It should behave as a production companion that can teach through real work, not a mandatory beginner course, plugin encyclopedia, or automatic song generator. Concise production flow remains available even when the musician does not want educational depth.",
)
replace_once(
    "CONTEXT.md",
    """### Goal of a Recreation\nThe target is a **complete finished reconstruction** taken as far as the user’s current ability allows.\n\nSuccess does **not** require being indistinguishable from the commercial master.""",
    """### Goal of a Recreation\nThe target is a **complete finished cover/recreation** whose relationship to the reference is intentionally chosen rather than assumed. A project may begin as **Match**, **Interpret**, or **Reimagine**, and that bias may change during the work. Individual differences may be matched, intentionally kept, or explored.\n\nA musician can use Recreation purely to make a cover quickly; learning/progress tracking must remain optional and ambient. Success does **not** require being indistinguishable from the commercial master unless faithful matching is the musician's actual goal.""",
)
replace_once(
    "CONTEXT.md",
    """Original projects should be **more flexible** than Recreation.\n\nImportant distinction:\n- **Recreation:** sequential forward, flexible backward\n- **Original Song:** progress should guide, not police creativity\n\nDo not impose strict gating on Original mode just because Study mode uses it.""",
    """Original projects should remain creatively flexible, but Recreation is no longer defined as a rigid learning sequence either. Both project types use strong default guidance with minimal hard gating.\n\nImportant distinction:\n- **Recreation:** the reference helps define the target, while Match / Interpret / Reimagine and intentional differences control how closely it is followed.\n- **Original Song:** the musician's own intention defines the target.\n\nBoth modes share the FIRE reasoning engine. Guidance may recommend an order of operations, but creative exploration stays reversible and hard gates exist only when a task literally cannot function without required context.""",
)

# V7_DRAFT: make scope boundary explicit.
replace_once(
    "V7_DRAFT.md",
    "**Status:** Isolated V7 shell preview is live from `main` under `/v7-preview/`. V6 remains the production app and active production specification until the V7 shell passes physical iPhone review and is deliberately promoted.",
    "**Status:** Isolated V7 shell preview is live from `main` under `/v7-preview/`. V6 remains the production app and active production specification until the V7 shell passes physical review and is deliberately promoted. `FIRE_CORE.md` governs cross-generation product doctrine; this file governs the V7 shell and must not redefine Recreation, learning, or Original semantics in conflict with FIRE Core.",
)

# START_HERE: update authority, shipped continuity, and next direction.
replace_once(
    "START_HERE.md",
    "- **Active production specification:** [V6.md](V6.md)\n- **Experimental next-shell direction:** [V7_DRAFT.md](V7_DRAFT.md)",
    "- **Cross-generation product doctrine:** [FIRE_CORE.md](FIRE_CORE.md)\n- **Active production specification:** [V6.md](V6.md)\n- **Experimental next-shell direction:** [V7_DRAFT.md](V7_DRAFT.md)",
)
replace_once(
    "START_HERE.md",
    """1. `START_HERE.md`\n2. `AGENTS.md`\n3. `V6.md` for current production requirements\n4. `V7_DRAFT.md` for the redesign preview\n5. `CONTEXT.md`\n6. Current `main`, open PRs, relevant branches, and tests\n7. `CHANGELOG.md` for shipped milestones""",
    """1. `START_HERE.md`\n2. `AGENTS.md`\n3. `FIRE_CORE.md` for current cross-generation product doctrine\n4. `V6.md` for shipped production-generation requirements\n5. `V7_DRAFT.md` for the redesign shell\n6. `CONTEXT.md` for supporting history/detail not superseded above\n7. Current `main`, open PRs, relevant branches, and tests\n8. `CHANGELOG.md` for shipped milestones""",
)
replace_once(
    "START_HERE.md",
    "PR #38, **Refine V7 grayscale interaction fidelity**, is merged and deployed at `c7aa0c4…`; its PR and post-merge regression matrices passed at 390px, 440px, and 820px, and Pages deployment #63 succeeded. Physical iPhone Safari review then exposed two conceptual/runtime defects that the current corrective pass addresses: Reference should be a setup attestation rather than a file picker, and VisualViewport-driven root scroll locking can glitch as Safari browser chrome changes height. PR #37 remains the preceding visual-semantics milestone.",
    "PR #39, **Stabilize V7 Safari scrolling and setup semantics**, is merged and deployed at `d459a4f…`; its exact post-merge regression matrix passed at 390px, 440px, and 820px, Pages deployment #64 succeeded on the same SHA, and physical iPhone Safari review confirmed the scrolling behavior is improved. PR #38 remains the preceding grayscale interaction-fidelity milestone.",
)
replace_once(
    "START_HERE.md",
    "The current corrective direction is **Safari stability + setup semantics**: preserve the grayscale interaction foundation, treat Reference as a setup completion requirement rather than file ownership, use natural document scrolling instead of runtime root-scroll locking, keep upcoming Journey destinations visibly tappable, and remove internal V6/approval language from preview placeholders.",
    "The current direction is **V7 Shell Freeze + FIRE Core shaping**: perform one deliberate declutter/system pass so headers, typography, spacing/rhythm, grouping, states, sheets, natural scrolling, and adaptive presentation stop being re-litigated route by route; then breadboard the complete FIRE Core Original + Recreation journeys before deeply designing later phases.",
)
insert_after = "Always distinguish shipped production work from experimental V7 preview work.\n"
start = Path("START_HERE.md")
text = start.read_text(encoding="utf-8")
if "## FIRE Core product doctrine" not in text:
    doctrine = """\n## FIRE Core product doctrine\n\n`FIRE_CORE.md` is now the canonical current product doctrine. Key direction:\n\n- FIRE is a **production companion that teaches through use**, not a mandatory learning course.\n- Original and Recreation are both first-class project types. Recreation must work standalone for someone who only wants to make a cover quickly.\n- Learning is ambient and adaptive: concise action by default, optional `Why?` / deeper help, domain-specific skill growth, and `I don't know` as a valid path.\n- Recreation can **Match, Interpret, or Reimagine** a reference; individual differences can be matched, intentional, or explored.\n- One shared FIRE reasoning engine serves both modes: **Feel → Identify → Reason → Experiment → Evaluate**.\n- Historical V6/V7 rules remain useful generation-specific evidence but cannot override current FIRE Core doctrine.\n\n"""
    if insert_after not in text:
        raise RuntimeError("START_HERE insertion anchor missing")
    start.write_text(text.replace(insert_after, insert_after + doctrine, 1), encoding="utf-8")

# Handoff freshness: FIRE_CORE changes must refresh START_HERE.
replace_once(
    "scripts/check_handoff.py",
    '    "V7_DRAFT.md",\n    "CONTEXT.md",',
    '    "V7_DRAFT.md",\n    "FIRE_CORE.md",\n    "CONTEXT.md",',
)

# Add a lightweight doctrine consistency guard. It cannot prove semantic consistency,
# but it protects authority wiring and known stale definitions from regressing.
Path("scripts/check_product_doctrine.py").write_text(r'''"""Protect FIRE's product-doctrine authority wiring and known stale definitions.

This is intentionally a small guard, not an attempt to prove semantic consistency in
natural-language product documents. Human doctrine review remains required.
"""
from pathlib import Path


REQUIRED = {
    "FIRE_CORE.md": [
        "# Babel FIRE — Core Product Doctrine",
        "production companion",
        "Match",
        "Interpret",
        "Reimagine",
        "Feel",
        "Identify",
        "Reason",
        "Experiment",
        "Evaluate",
        "Documentation authority and conflict policy",
    ],
    "AGENTS.md": ["FIRE_CORE.md", "Historical/versioned specifications are a library"],
    "START_HERE.md": ["FIRE_CORE.md", "FIRE Core product doctrine"],
    "CONTEXT.md": ["FIRE_CORE.md", "standalone cover/reconstruction workflow"],
    "V7_DRAFT.md": ["`FIRE_CORE.md` governs cross-generation product doctrine"],
}

FORBIDDEN = {
    "CONTEXT.md": [
        "### Recreation — SECONDARY / LEARNING MODE",
        "**Recreation:** sequential forward, flexible backward",
    ],
    "AGENTS.md": [
        "The current approved next step is a global FIRE Design System foundation pass",
    ],
}


def main() -> int:
    failures: list[str] = []
    for path, needles in REQUIRED.items():
        text = Path(path).read_text(encoding="utf-8")
        for needle in needles:
            if needle not in text:
                failures.append(f"{path}: missing required doctrine marker: {needle!r}")
    for path, needles in FORBIDDEN.items():
        text = Path(path).read_text(encoding="utf-8")
        for needle in needles:
            if needle in text:
                failures.append(f"{path}: stale/conflicting doctrine remains: {needle!r}")
    if failures:
        print("FIRE product doctrine consistency check failed:")
        for failure in failures:
            print(f"  - {failure}")
        return 1
    print("FIRE product doctrine consistency check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
''', encoding="utf-8")

# Run the doctrine guard in the existing static CI job.
replace_once(
    ".github/workflows/v6-regression.yml",
    """      - name: Check whitespace\n        run: |\n          if [ \"${{ github.event_name }}\" = \"pull_request\" ]; then\n            git diff --check \"${{ github.event.pull_request.base.sha }}...${{ github.sha }}\"\n          else\n            git diff --check HEAD^\n          fi\n""",
    """      - name: Check whitespace\n        run: |\n          if [ \"${{ github.event_name }}\" = \"pull_request\" ]; then\n            git diff --check \"${{ github.event.pull_request.base.sha }}...${{ github.sha }}\"\n          else\n            git diff --check HEAD^\n          fi\n      - name: Check FIRE product doctrine consistency\n        run: python3 scripts/check_product_doctrine.py\n""",
)

# Self-clean the one-shot reconciler and workflow that invokes it.
Path("scripts/apply_fire_core_doctrine.py").unlink()
Path(".github/workflows/apply-fire-core-doctrine.yml").unlink()
