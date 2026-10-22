from pathlib import Path


def replace_once(path: str, old: str, new: str) -> None:
    p = Path(path)
    text = p.read_text(encoding="utf-8")
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{path}: expected one match, found {count}: {old[:90]!r}")
    p.write_text(text.replace(old, new), encoding="utf-8")


# AGENTS: current doctrine authority and stale process guidance.
replace_once(
    "AGENTS.md",
    """1. **AGENTS.md** — repository workflow, engineering, maintenance, review, and documentation rules.\n2. **Active version specification, currently V6.md** — approved requirements for the active product generation; supersedes older UI/product descriptions where they conflict.\n3. **CONTEXT.md** — durable product philosophy, architecture, learning/workflow context, and decisions intended to survive across versions.\n4. **Current code and tests** — implementation evidence; they do not override explicit approved product requirements.\n\nIf a genuine conflict remains after applying this hierarchy, ask rather than guessing.""",
    """1. **AGENTS.md** — repository workflow, engineering, maintenance, review, and documentation rules.\n2. **FIRE_CORE.md** — current cross-generation product doctrine: purpose, shared reasoning/learning model, project-type semantics, and product boundaries.\n3. **Active production specification, currently V6.md** — approved requirements for behavior that ships in the active production generation. Generation-specific rules do not override FIRE Core doctrine unless the doctrine is deliberately changed in the same work.\n4. **V7_DRAFT.md** — experimental V7 shell behavior and interaction direction, scoped to that generation.\n5. **CONTEXT.md** — durable supporting history, detailed learning/workflow context, and decisions not superseded above.\n6. **Current code and tests** — implementation evidence; they do not override explicit approved product requirements.\n\nHistorical/versioned specifications are a library of generation-specific truth, not current universal doctrine. If a genuine conflict remains after applying this hierarchy, reconcile the durable product documents rather than silently choosing one.""",
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
    "- `FIRE_CORE.md` is the canonical current cross-generation product doctrine. A durable doctrine change must update it and reconcile affected guidance in `CONTEXT.md`, `START_HERE.md`, `AGENTS.md`, and relevant generation specs in the same PR.\n- `CONTEXT.md` is not a changelog. It stores durable supporting history, detailed workflow knowledge, and decisions that remain valid under FIRE Core. Preserve useful historical evidence, but scope it clearly when superseded so it cannot compete with current doctrine.",
)

# CONTEXT: reconcile active product semantics while preserving history.
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

# V7 scope boundary.
replace_once(
    "V7_DRAFT.md",
    "**Status:** Isolated V7 shell preview is live from `main` under `/v7-preview/`. V6 remains the production app and active production specification until the V7 shell passes physical iPhone review and is deliberately promoted.",
    "**Status:** Isolated V7 shell preview is live from `main` under `/v7-preview/`. V6 remains the production app and active production specification until the V7 shell passes physical review and is deliberately promoted. `FIRE_CORE.md` governs cross-generation product doctrine; this file governs the V7 shell and must not redefine Recreation, learning, or Original semantics in conflict with FIRE Core.",
)

# START_HERE authority and current state.
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
start = Path("START_HERE.md")
text = start.read_text(encoding="utf-8")
anchor = "Always distinguish shipped production work from experimental V7 preview work.\n"
if "## FIRE Core product doctrine" not in text:
    block = """\n## FIRE Core product doctrine\n\n`FIRE_CORE.md` is the canonical current product doctrine. Key direction:\n\n- FIRE is a **production companion that teaches through use**, not a mandatory learning course.\n- Original and Recreation are both first-class project types. Recreation must work standalone for someone who only wants to make a cover quickly.\n- Learning is ambient and adaptive: concise action by default, optional `Why?` / deeper help, domain-specific growth, and `I don't know` as a valid path.\n- Recreation can **Match, Interpret, or Reimagine** a reference; individual differences can be matched, intentional, or explored.\n- One shared FIRE reasoning engine serves both modes: **Feel → Identify → Reason → Experiment → Evaluate**.\n- Historical V6/V7 rules remain useful generation-specific evidence but cannot override current FIRE Core doctrine.\n\n"""
    if anchor not in text:
        raise RuntimeError("START_HERE doctrine insertion anchor missing")
    start.write_text(text.replace(anchor, anchor + block, 1), encoding="utf-8")

# Existing handoff CI now also protects product-doctrine wiring.
replace_once(
    "scripts/check_handoff.py",
    '    "V7_DRAFT.md",\n    "CONTEXT.md",',
    '    "V7_DRAFT.md",\n    "FIRE_CORE.md",\n    "CONTEXT.md",',
)
replace_once(
    "scripts/check_handoff.py",
    '    print("FIRE handoff freshness check passed.")\n    return 0\n',
    '    print("FIRE handoff freshness check passed.")\n    doctrine = subprocess.run([sys.executable, "scripts/check_product_doctrine.py"], check=False)\n    if doctrine.returncode:\n        return doctrine.returncode\n    return 0\n',
)
