"""Protect the small active FIRE authority set from stale/duplicate doctrine drift."""
from pathlib import Path

REQUIRED = {
    "BABEL_TRUTH.md": [
        "BabeDrums/babel-truth",
        "Last reconciled Truth commit",
        "FOUNDATIONS.md",
        "Babel Continuity Buffer",
    ],
    "AGENTS.md": [
        "BABEL_TRUTH.md",
        "START_HERE.md",
        "FIRE_CORE.md",
        "production-projects-v1",
        "production-projects-v1-v7-preview",
        "No Codex for FIRE",
        "G7_SHELL_CERTIFICATION_STATUS.md",
        "active FIRE documentation set",
    ],
    "START_HERE.md": [
        "G7 Shell",
        "0 / 10 Locked",
        "G7 is NOT FROZEN",
        "PR **#89",
        "d93729ff7a734035f25a6835323d19706f15186d",
        "physical review",
        "Babel Truth Issue #1",
    ],
    "FIRE_CORE.md": [
        "# Babel FIRE — Core Product Doctrine",
        "production companion",
        "Feel",
        "Identify",
        "Reason",
        "Experiment",
        "Evaluate",
        "Match",
        "Interpret",
        "Reimagine",
        "Documentation authority and conflict policy",
        "G7 shell vs FIRE Core",
        "G7_SHELL_CERTIFICATION_STATUS.md",
    ],
    "V7_DRAFT.md": [
        "`FIRE_CORE.md` governs cross-generation product doctrine",
        "G7_SHELL_CERTIFICATION_STATUS.md",
        "## Interaction grammar",
        "## Canonical icon/accessory grammar",
        "## Navigation and Back behavior",
    ],
    "G7_SHELL_CERTIFICATION.md": [
        "# Babel FIRE — G7 Shell Certification",
        "G7_SHELL_CERTIFICATION_STATUS.md",
        "Developer Shell Test",
        "all 10 categories are **Locked**",
        "Babel explicitly approves/freezes the shell",
    ],
    "G7_SHELL_CERTIFICATION_STATUS.md": [
        "# G7 Shell Certification — Status Board",
        "0 / 10 Locked",
        "G7 NOT FROZEN",
    ],
}

RETIRED_ACTIVE_DOCS = {
    "BABEL_APPS.md",
    "BABEL_PLATFORM.md",
    "BABEL_START_HERE.md",
    "CHANGELOG.md",
    "CONTEXT.md",
    "CONTINUITY_INBOX.md",
    "REFERENCES.md",
}

FORBIDDEN_TEXT = {
    "AGENTS.md": ["BABEL_START_HERE.md", "CONTINUITY_INBOX.md", "CONTEXT.md"],
    "FIRE_CORE.md": ["BABEL_APPS.md", "BABEL_PLATFORM.md", "BABEL_START_HERE.md", "CONTEXT.md", "REFERENCES.md"],
    "START_HERE.md": ["CONTINUITY_INBOX.md", "BABEL_START_HERE.md"],
}


def main() -> int:
    failures: list[str] = []

    for path, needles in REQUIRED.items():
        p = Path(path)
        if not p.exists():
            failures.append(f"missing active authority file: {path}")
            continue
        text = p.read_text(encoding="utf-8")
        for needle in needles:
            if needle not in text:
                failures.append(f"{path}: missing required marker: {needle!r}")

    for path in sorted(RETIRED_ACTIVE_DOCS):
        if Path(path).exists():
            failures.append(f"retired duplicate documentation still active: {path}")

    for path, needles in FORBIDDEN_TEXT.items():
        text = Path(path).read_text(encoding="utf-8")
        for needle in needles:
            if needle in text:
                failures.append(f"{path}: stale reference to retired authority: {needle!r}")

    if failures:
        print("FIRE authority consistency check failed:")
        for failure in failures:
            print(f"  - {failure}")
        return 1

    print("FIRE authority consistency check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
