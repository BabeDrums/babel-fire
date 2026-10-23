# Babel FIRE

Babel FIRE is an iPhone/iPad-first music-production workflow app.

- **Live app:** https://babedrums.github.io/babel-fire/
- **Production branch:** `main`
- **Active product generation:** V6
- **External references / inspiration registry:** [`REFERENCES.md`](REFERENCES.md)

## Continue the project

Start with [`START_HERE.md`](START_HERE.md). It is the canonical zero-context handoff entry point for a new ChatGPT conversation or collaborator. Follow the source-of-truth order defined in [`AGENTS.md`](AGENTS.md), then inspect current `main`, open PRs, relevant branches, and tests before making changes.

FIRE's pull-request checks enforce handoff freshness when core product/runtime or durable-rule files change, so merged states stay resumable without a separate manual handoff step.

For substantive FIRE product work, also perform a **consistency sweep** across the current doctrine, active generation docs, platform hypotheses, handoff state, and implementation. Fix clear stale/duplicate contradictions as part of the task. Do not silently auto-resolve a genuine product conflict when two sources represent materially different decisions; surface and reconcile that conflict using the documented authority order and product judgment. CI catches known markers and stale handoff wiring, but semantic consistency still requires this review step.

Do not ask the user to reconstruct decisions that are already documented in the repository.
