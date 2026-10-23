"""Protect FIRE product-doctrine authority wiring and known stale definitions.

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
        "Git history is the canonical archive for retired implementation generations",
    ],
    "AGENTS.md": ["FIRE_CORE.md"],
    "START_HERE.md": [
        "FIRE_CORE.md",
        "FIRE Core doctrine",
        "BABEL_PLATFORM.md",
        "REFERENCES.md",
        "Generation-spec retention",
        "Shell Freeze was NOT approved",
        "Inline = choose/toggle/classify/confirm/evaluate",
        "Sheet = create/edit/manage a discrete thing",
    ],
    "BABEL_PLATFORM.md": [
        "# Babel Platform — Future Hypotheses",
        "Future/platform exploration only",
        "shared evidence, local identity",
        "Evidence first, interpretation second",
        "Source/origin marks",
        "Achievement badges",
        "Pixel-art Fire hypothesis",
        "entitlements",
    ],
    "REFERENCES.md": [
        "# Babel FIRE — Reference Registry",
        "GitHub / Primer",
        "ChatGPT",
        "Open Badges 3.0",
        "Pixel-art Fire + badge language hypothesis",
    ],
    "CONTEXT.md": ["FIRE_CORE.md", "standalone cover/reconstruction workflow"],
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
    ],
    "AGENTS.md": [
        "The current approved next step is a global FIRE Design System foundation pass",
    ],
    "START_HERE.md": [
        "`V5.md` is historical",
        "awaiting Babel's physical-device approval. Do not begin the FIRE Core breadboard until that review is complete.",
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
