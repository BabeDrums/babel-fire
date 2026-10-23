"""Fail a Babel/FIRE pull request when zero-context handoffs are left stale.

Usage:
    python3 scripts/check_handoff.py <base_sha> <head_sha>

FIRE product/runtime/spec work must refresh START_HERE.md.
Cross-app ecosystem doctrine must also refresh BABEL_START_HERE.md.
This keeps merged states resumable without asking Babel to reconstruct context.
"""
from __future__ import annotations

import subprocess
import sys

FIRE_WATCHED_PATHS = {
    "app.js",
    "styles.css",
    "index.html",
    "V6.md",
    "V7_DRAFT.md",
    "FIRE_CORE.md",
    "BABEL_PLATFORM.md",
    "CONTEXT.md",
    "AGENTS.md",
}
FIRE_WATCHED_PREFIXES = ("v7-preview/",)
FIRE_HANDOFF_PATH = "START_HERE.md"

ECOSYSTEM_WATCHED_PATHS = {
    "BABEL_PLATFORM.md",
    "FIRE_CORE.md",
}
ECOSYSTEM_HANDOFF_PATH = "BABEL_START_HERE.md"


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

    fire_relevant = sorted(
        path
        for path in changed
        if path in FIRE_WATCHED_PATHS or path.startswith(FIRE_WATCHED_PREFIXES)
    )
    if fire_relevant and FIRE_HANDOFF_PATH not in changed:
        print(
            "FIRE handoff is stale. Product/durable files changed without "
            "refreshing START_HERE.md:\n  - " + "\n  - ".join(fire_relevant),
            file=sys.stderr,
        )
        print(
            "Update START_HERE.md with the current shipped/preview/planned state so "
            "a new chat can resume without reconstructing context.",
            file=sys.stderr,
        )
        return 1

    ecosystem_relevant = sorted(path for path in changed if path in ECOSYSTEM_WATCHED_PATHS)
    if ecosystem_relevant and ECOSYSTEM_HANDOFF_PATH not in changed:
        print(
            "Babel ecosystem handoff is stale. Cross-app doctrine changed without "
            "refreshing BABEL_START_HERE.md:\n  - " + "\n  - ".join(ecosystem_relevant),
            file=sys.stderr,
        )
        print(
            "Update BABEL_START_HERE.md so a new ecosystem/surrounding-app chat "
            "inherits the current app-concept boundaries instead of reconstructing them from old files.",
            file=sys.stderr,
        )
        return 1

    print("Babel/FIRE handoff freshness check passed.")
    doctrine = subprocess.run([sys.executable, "scripts/check_product_doctrine.py"], check=False)
    if doctrine.returncode:
        return doctrine.returncode
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
