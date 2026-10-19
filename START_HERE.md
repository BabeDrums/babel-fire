# Babel FIRE

- **Repository:** BabeDrums/babel-fire
- **Production branch:** `main`
- **Current active product generation/specification:** [V6.md](V6.md)

When a new ChatGPT/Codex conversation begins with or clearly refers to **Babel FIRE**, resume this project; do not ask the user to explain FIRE again.

Before substantive product or implementation guidance:

1. Inspect `BabeDrums/babel-fire` and preserve any unfinished local work.
2. Read `START_HERE.md`, then [AGENTS.md](AGENTS.md), [CONTEXT.md](CONTEXT.md), and the active version specification.
3. Inspect current `main` without overwriting local work.
4. Check open pull requests and relevant active branches.
5. Distinguish shipped work on `main`, unmerged PR work, and planned/unimplemented work. State any access limitation instead of assuming remote state.
6. Resume from the latest **verified** project state. Do not make the user repeat documented decisions.

Follow the source-of-truth hierarchy and task-branch/PR workflow in `AGENTS.md`. Code on a task branch is not shipped until the reviewed PR is explicitly approved and merged. Physical iPhone/iPad Safari testing must be separately verified.

Fallback continuation phrase:

> Babel FIRE — continue from GitHub repo BabeDrums/babel-fire. Read START_HERE.md.

V6 implementation uses the approved specification on a dedicated branch. Determine shipped state from `main` and PR review; activation of this entry point does not authorize a merge. Use `python3 scripts/serve.py` for local development and asset revision handling.
