"""Fail a Babel/FIRE pull request when the relevant zero-context handoff is stale.

Usage:
    python3 scripts/check_handoff.py <base_sha> <head_sha>

FIRE product/runtime/spec work refreshes START_HERE.md.
Wider Babel ecosystem/app/platform doctrine refreshes BABEL_START_HERE.md.
Shared routing/authority files refresh both.
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
    "CONTEXT.md",
    "AGENTS.md",
    "BABEL_TRUTH.md",
}
FIRE_WATCHED_PREFIXES = ("v7-preview/",)
FIRE_HANDOFF_PATH = "START_HERE.md"

ECOSYSTEM_WATCHED_PATHS = {
    "BABEL_APPS.md",
    "BABEL_PLATFORM.md",
    "FIRE_CORE.md",
    "AGENTS.md",
    "BABEL_TRUTH.md",
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
            "FIRE handoff is stale. FIRE product/durable files changed without "
            "refreshing START_HERE.md:\n  - " + "\n  - ".join(fire_relevant),
            file=sys.stderr,
        )
        print(
            "Update START_HERE.md so a fresh FIRE chat sees the current state/next step.",
            file=sys.stderr,
        )
        return 1

    ecosystem_relevant = sorted(path for path in changed if path in ECOSYSTEM_WATCHED_PATHS)
    if ecosystem_relevant and ECOSYSTEM_HANDOFF_PATH not in changed:
        print(
            "Babel ecosystem handoff is stale. Ecosystem/app/platform doctrine changed without "
            "refreshing BABEL_START_HERE.md:\n  - " + "\n  - ".join(ecosystem_relevant),
            file=sys.stderr,
        )
        print(
            "Update BABEL_START_HERE.md so a fresh surrounding-app chat inherits the current boundaries.",
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
