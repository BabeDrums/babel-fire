from pathlib import Path


def replace_once(path: str, old: str, new: str) -> None:
    p = Path(path)
    text = p.read_text(encoding="utf-8")
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{path}: expected one match, found {count}: {old[:80]!r}")
    p.write_text(text.replace(old, new), encoding="utf-8")


replace_once(
    "FIRE_CORE.md",
    "A future optional Skills/Growth/Insights surface may summarize development without being required to finish music.",
    "A future optional Skills/Growth/Insights or Practice surface may summarize development and offer targeted category practice without being required to finish music. A living, shareable visualization of growth (working concept: the user’s **Fire**) is also worth prototyping, but it must represent credible learning evidence rather than raw usage, page completion, or a punitive daily streak. These remain future hypotheses; see `BABEL_PLATFORM.md`.",
)
replace_once(
    "FIRE_CORE.md",
    "- how skill confidence is represented without fake mastery\n",
    "- how skill confidence is represented without fake mastery\n- exact optional Practice/Skills/Growth surface and how project lessons feed targeted practice\n- whether/how the user’s Fire visualizes growth without becoming a fake global producer score\n",
)

replace_once(
    "START_HERE.md",
    "- **Cross-generation product doctrine:** [FIRE_CORE.md](FIRE_CORE.md)\n- **Active production specification:** [V6.md](V6.md)",
    "- **Cross-generation product doctrine:** [FIRE_CORE.md](FIRE_CORE.md)\n- **Future Babel platform hypotheses:** [BABEL_PLATFORM.md](BABEL_PLATFORM.md)\n- **Active production specification:** [V6.md](V6.md)",
)
replace_once(
    "START_HERE.md",
    "3. `FIRE_CORE.md` for current cross-generation product doctrine\n4. `V6.md` for shipped production-generation requirements\n5. `V7_DRAFT.md` for the redesign shell\n6. `CONTEXT.md` for supporting history/detail not superseded above\n7. Current `main`, open PRs, relevant branches, and tests\n8. `CHANGELOG.md` for shipped milestones",
    "3. `FIRE_CORE.md` for current cross-generation product doctrine\n4. `BABEL_PLATFORM.md` only when the task involves future accounts/sync, cross-app ecosystem, monetization/entitlements, the deeper learning/practice surface, the user’s Fire, social sharing, or lore/Easter eggs\n5. `V6.md` for shipped production-generation requirements\n6. `V7_DRAFT.md` for the redesign shell\n7. `CONTEXT.md` for supporting history/detail not superseded above\n8. Current `main`, open PRs, relevant branches, and tests\n9. `CHANGELOG.md` for shipped milestones",
)
replace_once(
    "START_HERE.md",
    "PR #39, **Stabilize V7 Safari scrolling and setup semantics**, is merged and deployed at `d459a4f…`; its exact post-merge regression matrix passed at 390px, 440px, and 820px, Pages deployment #64 succeeded on the same SHA, and physical iPhone Safari review confirmed the scrolling behavior is improved. PR #38 remains the preceding grayscale interaction-fidelity milestone.",
    "PR #40, **Define FIRE Core doctrine and adaptive Recreation learning**, is merged at `9a3935c…`; its PR regression matrix passed at 390px, 440px, and 820px, and Pages deployment #65 succeeded on the same SHA. It establishes `FIRE_CORE.md` as canonical cross-generation doctrine without changing runtime behavior or user data. PR #39 remains the preceding V7 Safari/setup milestone and the latest physical iPhone runtime review.",
)
replace_once(
    "START_HERE.md",
    "- game-like progression mechanics (likely reject most literal forms)",
    "- meaningful optional learning/progression experiments — including a targeted Practice/Skills surface and the user’s evolving Fire; reject fake mastery, mandatory XP/streak pressure, and default global leaderboards",
)
insert_after = "- Historical V6/V7 rules remain useful generation-specific evidence but cannot override current FIRE Core doctrine.\n"
platform_note = "- Future accounts/sync, Babel app harmony, monetization/entitlements, the deeper Practice/Skills surface, the user’s Fire, social sharing, and lore/Easter eggs are preserved as **future hypotheses** in `BABEL_PLATFORM.md`; they do not expand current Shell/Core implementation scope.\n"
replace_once("START_HERE.md", insert_after, insert_after + platform_note)

replace_once(
    "scripts/check_handoff.py",
    '    "FIRE_CORE.md",\n',
    '    "FIRE_CORE.md",\n    "BABEL_PLATFORM.md",\n',
)

replace_once(
    "scripts/check_product_doctrine.py",
    '    "START_HERE.md": ["FIRE_CORE.md", "FIRE Core product doctrine"],\n',
    '    "START_HERE.md": ["FIRE_CORE.md", "FIRE Core product doctrine", "BABEL_PLATFORM.md"],\n    "BABEL_PLATFORM.md": ["# Babel Platform — Future Hypotheses", "The user’s Fire", "entitlements", "Future/platform exploration only"],\n',
)
