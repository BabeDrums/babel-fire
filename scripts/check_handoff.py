"""Fail a FIRE pull request when product work leaves START_HERE.md stale.

Usage:
    python3 scripts/check_handoff.py <base_sha> <head_sha>

The check is intentionally simple: if a PR changes the product/runtime, active
or experimental specification, preview runtime, or durable repository rules, it
must also refresh START_HERE.md. That keeps every merged state resumable from a
zero-context chat without asking the user to remember a handoff step.
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
    "CONTEXT.md",
    "AGENTS.md",
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
        path
        for path in changed
        if path in WATCHED_PATHS or path.startswith(WATCHED_PREFIXES)
    )
    if relevant and HANDOFF_PATH not in changed:
        print(
            "FIRE handoff is stale. Product/durable files changed without "
            "refreshing START_HERE.md:\n  - " + "\n  - ".join(relevant),
            file=sys.stderr,
        )
        print(
            "Update START_HERE.md with the current shipped/preview/planned state so "
            "a new chat can resume without reconstructing context.",
            file=sys.stderr,
        )
        return 1

    print("FIRE handoff freshness check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
