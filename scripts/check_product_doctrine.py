"""Protect FIRE/Babel authority wiring and known stale definitions.

This guard intentionally checks only durable markers/known contradictions. It does not
prove natural-language semantic consistency; human/product review remains required.
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
        "Git history is the canonical archive for retired implementation generations",
    ],
    "AGENTS.md": [
        "FIRE_CORE.md",
        "BABEL_START_HERE.md",
        "BABEL_APPS.md",
        "Git history is the archive",
        "Inline",
        "Sheet",
        "Navigation",
    ],
    "START_HERE.md": [
        "FIRE_CORE.md",
        "BABEL_START_HERE.md",
        "BABEL_APPS.md",
        "Generation-spec retention",
        "Shell Freeze was NOT approved",
        "Inline = choose/toggle/classify/confirm/evaluate",
        "Sheet = create/edit/manage a discrete thing",
    ],
    "BABEL_START_HERE.md": [
        "# Babel Ecosystem — Start Here",
        "Product need earns an app",
        "BABEL_APPS.md",
        "Recreation is **not** merely a learning mode",
        "Dedicated learning product — not currently earned",
        "Visual Identity product — promising candidate, deliberately underdefined",
        "Babel World — optional hub hypothesis",
        "WATER is **not** currently the learning app",
        "Shared evidence, local identity",
        "The collection earns its shape",
        "Anti-drift rules for new chats",
    ],
    "BABEL_APPS.md": [
        "# Babel — App Concept Ledger",
        "Product need earns an app",
        "Dedicated learning product — not currently earned",
        "Visual Identity product — promising candidate, deliberately underdefined",
        "Babel World — optional future hub hypothesis",
        "WATER has been floated historically",
        "Shared evidence, local identity",
        "Cross-app object sharing is intentionally open",
        "Source marks, achievements, and pixel badge language",
        "The collection earns its shape",
    ],
    "BABEL_PLATFORM.md": [
        "# Babel Platform — Future Hypotheses",
        "Prepare the joints where future products can connect",
        "Shared evidence, local identity",
        "Evidence first, interpretation second",
        "Babel Learning Contract",
        "Source/origin marks",
        "achievement badges",
        "Pixel-art Fire hypothesis",
        "Desire, not deprivation",
    ],
    "REFERENCES.md": [
        "# Babel FIRE — Reference Registry",
        "GitHub / Primer",
        "ChatGPT",
        "Open Badges 3.0",
        "Pixel-art Fire + badge language hypothesis",
    ],
    "CONTEXT.md": [
        "# Babel FIRE — Durable Supporting Context",
        "standalone cover/reconstruction workflow",
        "Do not infer sibling apps from this file",
    ],
    "V7_DRAFT.md": [
        "`FIRE_CORE.md` governs cross-generation product doctrine",
        "Delete before styling.",
        "## Interaction grammar",
        "**Inline**",
        "**Sheet**",
        "Original",
        "Recreation",
    ],
}

FORBIDDEN = {
    "CONTEXT.md": [
        "### Recreation — SECONDARY / LEARNING MODE",
        "**Recreation:** sequential forward, flexible backward",
        "Current redesign progression and navigation direction — LOCKED FOR V7 SHELL",
        "Project Home owns **Continue + Journey + Notes**",
    ],
    "AGENTS.md": [
        "The current approved next step is a global FIRE Design System foundation pass",
        "Historical/versioned specifications are a library of generation-specific truth",
        "Project Home owns **Continue + Journey + Notes**",
        "The current design objective is **V7 Shell Freeze**",
    ],
    "START_HERE.md": [
        "`V5.md` is historical",
    ],
    "BABEL_START_HERE.md": [
        "FIRE = making the music.\nThe learning app = studying.",
        "WATER = learning",
        "WATER = the learning app",
        "AIR = app",
        "EARTH = app",
        "World = universal source of truth",
    ],
    "BABEL_APPS.md": [
        "FIRE = making the music.\nThe learning app = studying.",
        "WATER = learning",
        "WATER = the learning app",
        "AIR = app",
        "EARTH = app",
        "Babel World = universal database",
    ],
    "BABEL_PLATFORM.md": [
        "Current FIRE work remains: **G7 Shell Freeze",
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