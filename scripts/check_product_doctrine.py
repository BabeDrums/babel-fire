"""Protect the small active FIRE authority set from stale/duplicate doctrine drift."""
from pathlib import Path

REQUIRED = {
    "BABEL_TRUTH.md": [
        "BabeDrums/babel-truth",
        "Last reconciled Truth commit",
        "9b9414ca360035fd76c2b30db5ecbe561bf130fe",
        "FOUNDATIONS.md",
        "ADR 0005",
        "ADR 0006",
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
        "FIRE Core incubation boundary",
        "babel-lab/fire/core/**",
        "Draft FIRE PR #99",
    ],
    "START_HERE.md": [
        "G7 SHELL IS FROZEN",
        "10 / 10 Locked",
        "4a258c5170dd1d96dcbc0f2b0a9c35b283cec489",
        "Target → Production Map → Active Focus → FIRE Loop",
        "FIRE PR #99 is Draft seed material",
        "bounded FIRE Core audition in Lab",
        "babel-lab/fire/core/**",
        "Babel Truth Issue #1",
    ],
    "FIRE_CORE.md": [
        "# Babel FIRE — Core Product Doctrine",
        "production companion",
        "Core operating model",
        "Production Map",
        "Active Focus",
        "provisionally stable under current evidence",
        "Prevent what can reasonably be prevented now",
        "Feel",
        "Identify",
        "Reason",
        "Experiment",
        "Evaluate",
        "Match",
        "Interpret",
        "Reimagine",
        "Recreation reference overlay",
        "Original target development",
        "FIRE Knowledge model",
        "Question rule",
        "Deep model underneath. Minimal burden on the musician.",
        "First FIRE Core interaction audition",
        "babel-lab/fire/core/**",
        "Draft FIRE PR #99",
        "Cross-app boundary",
        "ADR 0006",
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
        "FIRE Core breadboarding is unblocked",
    ],
    "G7_SHELL_CERTIFICATION.md": [
        "# Babel FIRE — G7 Shell Certification",
        "G7_SHELL_CERTIFICATION_STATUS.md",
        "Developer Shell Test",
        "all 10 categories **Locked**",
        "explicit Babel approval",
        "G7 Shell Frozen",
    ],
    "G7_SHELL_CERTIFICATION_STATUS.md": [
        "# G7 Shell Certification — Status Board",
        "10 / 10 Locked",
        "G7 SHELL FROZEN",
        "FIRE Core breadboarding unblocked",
        "4a258c5170dd1d96dcbc0f2b0a9c35b283cec489",
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
    "FIRE_CORE.md": ["BABEL_APPS.md", "BABEL_PLATFORM.md", "BABEL_START_HERE.md", "CONTEXT.md", "REFERENCES.md", "Sequencing is a dependency map, not a course"],
    "START_HERE.md": ["CONTINUITY_INBOX.md", "BABEL_START_HERE.md", "**0 / 10 Locked", "G7 is NOT FROZEN"],
    "G7_SHELL_CERTIFICATION_STATUS.md": ["**0 / 10 Locked", "G7 NOT FROZEN", "FIRE Core breadboarding blocked"],
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
                failures.append(f"{path}: stale reference to retired/superseded authority: {needle!r}")

    if failures:
        print("FIRE authority consistency check failed:")
        for failure in failures:
            print(f"  - {failure}")
        return 1

    print("FIRE authority consistency check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
