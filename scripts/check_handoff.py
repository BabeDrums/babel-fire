"""Fail a Babel/FIRE PR when the zero-context FIRE handoff is stale.

Usage:
    python3 scripts/check_handoff.py <base_sha> <head_sha>
"""
from __future__ import annotations

import subprocess
import sys

WATCHED_PATHS = {
    "app.js",
    "styles.css",
    "index.html",
    "V6.md",
    "V7_DRAFT.md",
    "FIRE_CORE.md",
    "G7_SHELL_CERTIFICATION.md",
    "G7_SHELL_CERTIFICATION_STATUS.md",
    "AGENTS.md",
    "BABEL_TRUTH.md",
}
WATCHED_PREFIXES = ("v7-preview/",)
HANDOFF_PATH = "START_HERE.md"


def changed_files(base: str, head: str) -> set[str]:
    output = subprocess.check_output(
        ["git", "diff", "--name-only", f"{base}...{head}"],
        text=True,
    )
    return {line.strip() for line in output.splitlines() if line.strip()}


def main() -> int:
    if len(sys.argv) != 3:
        print("usage: check_handoff.py <base_sha> <head_sha>", file=sys.stderr)
        return 2

    changed = changed_files(sys.argv[1], sys.argv[2])
    relevant = sorted(
        path for path in changed
        if path in WATCHED_PATHS or path.startswith(WATCHED_PREFIXES)
    )

    if relevant and HANDOFF_PATH not in changed:
        print(
            "FIRE handoff is stale. Durable FIRE files changed without refreshing START_HERE.md:\n  - "
            + "\n  - ".join(relevant),
            file=sys.stderr,
        )
        return 1

    print("Babel/FIRE handoff freshness check passed.")
    doctrine = subprocess.run([sys.executable, "scripts/check_product_doctrine.py"], check=False)
    return doctrine.returncode


if __name__ == "__main__":
    raise SystemExit(main())
