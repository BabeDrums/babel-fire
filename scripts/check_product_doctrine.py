"""Protect durable FIRE/Babel authority wiring and known stale definitions.

This guard checks stable markers and explicit stale contradictions. It intentionally does
not encode temporary merge SHAs, but it does require the current shell-routing/gate language.
"""
from pathlib import Path

REQUIRED = {
    "BABEL_TRUTH.md": [
        "BabeDrums/babel-truth",
        "Last reconciled Truth commit",
        "Babel Continuity Buffer",
        "stale divergence",
        "potential upstream improvement",
        "app-local exception",
    ],
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
    "AGENTS.md": [
        "BABEL_TRUTH.md",
        "Babel Continuity Buffer",
        "CONTINUITY_INBOX.md` is retired",
        "production-projects-v1",
        "production-projects-v1-v7-preview",
        "No Codex for FIRE",
        "Inline",
        "Sheet",
        "Navigation",
    ],
    "START_HERE.md": [
        "BABEL_TRUTH.md",
        "G7 Shell Certification active",
        "PR **#66",
        "PR **#67",
        "G7 is not approved/frozen",
        "Babel Truth Issue #1",
        "Inline = choose/toggle/classify/confirm/evaluate",
        "Sheet = create/edit/manage a discrete thing",
        "G7** owns coordinated FIRE shell implementation",
        "Lab is evidence, never authority",
        "10/10 categories Locked",
    ],
    "BABEL_START_HERE.md": [
        "BABEL_TRUTH.md",
        "Product need earns an app",
        "Dedicated learning product — not currently earned",
        "Visual Identity product — promising candidate, deliberately underdefined",
        "Babel World — optional future hub hypothesis",
        "Babel Lab boundary",
        "Shared evidence, local identity",
        "Babel Truth Issue #1",
        "WATER is not currently the learning app",
    ],
    "CONTINUITY_INBOX.md": [
        "Retired Local Continuity Inbox",
        "Do not add new continuity items here",
        "BabeDrums/babel-truth",
        "Babel Continuity Buffer",
    ],
    "BABEL_APPS.md": [
        "# Babel — App Concept Ledger",
        "Product need earns an app",
        "Dedicated learning product — not currently earned",
        "Visual Identity product — promising candidate, deliberately underdefined",
        "Babel World — optional future hub hypothesis",
        "Shared evidence, local identity",
    ],
    "BABEL_PLATFORM.md": [
        "# Babel Platform — Future Hypotheses",
        "Prepare the joints where future products can connect",
        "Shared evidence, local identity",
        "Evidence first, interpretation second",
        "Babel Learning Contract",
    ],
    "V7_DRAFT.md": [
        "`FIRE_CORE.md` governs cross-generation product doctrine",
        "Delete before styling.",
        "## Interaction grammar",
        "## Physical rhythm and visual grammar primitives",
        "## State and accessory grammar",
        "## Navigation and Back behavior",
        "Shared row-content grid",
        "Selection surface",
        "Segmented control",
        "Page action footer",
        "Accurate",
        "does **not** add redundant checkmarks",
        "Visible ordinal numbers are removed",
    ],
}

FORBIDDEN = {
    "AGENTS.md": [
        "Continuity capture buffer",
        "Do **not** update it for every message",
    ],
    "START_HERE.md": [
        "PR **#59** is the last merged/deployed G7 baseline",
        "Latest physical-device review after #59",
        "Current rhythm/navigation refinement contract",
        "Tracks still shows redundant selection checkmarks in the current implementation",
        "visible Structure ordinal numbers push section names",
        "Pause further exploratory shell styling in the product while Lab develops a candidate",
    ],
    "BABEL_START_HERE.md": [
        "`CONTINUITY_INBOX.md` is a low-authority capture buffer",
        "FIRE = making the music.\nThe learning app = studying.",
        "WATER = learning",
        "World = universal source of truth",
    ],
    "CONTINUITY_INBOX.md": [
        "## Pending FIRE deltas",
        "## Pending ecosystem deltas",
    ],
    "CONTEXT.md": [
        "### Recreation — SECONDARY / LEARNING MODE",
        "Project Home owns **Continue + Journey + Notes**",
    ],
    "V7_DRAFT.md": [
        "current Cover shell work remains **Song Setup → Structure → Tracks**",
        "`Matches the song` is a separate grouped verification surface",
        "`Other` belongs to the same selection surface",
        "Tracks is the multi-select variant and adds visible checks to selected choices",
        "- index\n- section name",
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
        print("FIRE/Babel product doctrine consistency check failed:")
        for failure in failures:
            print(f"  - {failure}")
        return 1
    print("FIRE/Babel product doctrine consistency check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
