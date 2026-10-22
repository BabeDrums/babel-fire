from pathlib import Path


def replace_once(path: str, old: str, new: str) -> None:
    p = Path(path)
    text = p.read_text(encoding="utf-8")
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{path}: expected one match, found {count}: {old[:100]!r}")
    p.write_text(text.replace(old, new), encoding="utf-8")


platform_insert = """
### Shared learning architecture — shared evidence, local identity

Future Babel apps should not each invent their own meaning for the same learned capability. When two apps genuinely teach or observe the same skill, they should read and write the same underlying learning evidence through a shared, versioned contract.

Working principle: **shared evidence, local identity.**

- Progress belongs to a real skill/domain, not blindly to the app that happened to generate it.
- A future learning-focused Babel app may contribute evidence to FIRE's production-skill model only when the evidence genuinely measures the same production capability.
- Merely opening, using, or progressing through another Babel app must never grow the user's Fire by association.
- App-specific progression metaphors can remain separate. A future learning app might have its own journey/metaphor while the same credible production evidence can also strengthen the shared production model.
- Do not collapse unrelated domains into one Babel-wide level or score.

Before a second app exists, FIRE should be designed against a **Babel Learning Contract**, not against guessed details of a hypothetical sibling app. The contract should eventually define stable semantic identifiers and meanings for things such as skill/domain, evidence type, source context/app, guidance depth, demonstrated transfer, and confidence/strength. Exact fields are not locked yet; stable meaning and versionability matter more than the first schema.

For overlapping learning surfaces, prefer shared design primitives and information architecture where the meaning is the same: skill status, evidence history, explanation depth, lesson/practice state, and achievement semantics should feel familiar across Babel products. A shared component/token library can later enforce those fundamentals while allowing each app to compose them for its own job and atmosphere. Consistency is for transferable meaning, not for making every app visually identical.

This removes the need to build FIRE and a future learning app simultaneously. Build one validated product at a time, but avoid FIRE-only learning semantics that would be impossible for another Babel product to consume later.

### Dedicated learning-app split — only if earned

Do not create a second learning app merely to complete an elemental naming set. FIRE should keep enough contextual teaching and optional Practice/Growth depth to help a musician make records successfully.

A dedicated learning product becomes justified only if deliberate training grows into a distinct job that would make FIRE worse if kept inside it — for example, a substantial curriculum, ear-training laboratory, structured drills, courses, or other training experiences that no longer depend on an active production project. If that split happens, it should consume the same Babel Learning Contract rather than rebuilding progress from scratch.

### Babel World — optional ecosystem hub hypothesis

A future **Babel World** (working concept/name only) could become a calm hub for cross-app identity, progress, discoveries, entitlements, and handoff between Babel products once enough real apps exist to justify it.

Guardrails:

- Babel World must never be required to use FIRE or another Babel app.
- It should aggregate shared meaning rather than duplicate every app's task UI.
- App-specific progress metaphors can remain native to their apps while Babel World shows a coherent ecosystem-level view.
- Do not create a single global Babel skill score simply because a hub exists.
- Build Babel World only after multiple real products create a clear cross-app job; do not reverse-engineer products to give the hub content.

"""

replace_once(
    "BABEL_PLATFORM.md",
    "Potential name for this concept is still open (`Babel Harmony`, `Babel Link`, `Babel Platform`, etc.). Do not lock naming yet.\n\n## 3. Monetization + entitlements",
    "Potential name for this concept is still open (`Babel Harmony`, `Babel Link`, `Babel Platform`, etc.). Do not lock naming yet.\n\n" + platform_insert + "## 3. Monetization + entitlements",
)

fire_insert = """
### Ambient discovery in FIRE

The Fire should be discoverable without becoming homepage chrome. Strong visual hypothesis for a later personality pass: keep Projects/current work dominant, but let the Fire exist spatially below or beyond the main work surface so a restrained glow or ambient light subtly reaches the home page and invites curiosity.

- The glow is atmosphere, not a notification or required call to action.
- A person who only wants to make music can ignore it indefinitely.
- Do not let Fire color, animation, or decoration reduce readability or compete with project actions.
- Respect Reduce Motion and accessibility; a static light treatment must be sufficient.
- Do not implement this during the current Shell Freeze. First lock the shared shell fundamentals; prototype ambient Fire personality later as optional product evidence.

"""

replace_once(
    "BABEL_PLATFORM.md",
    "A shareable Fire card/profile could let people show off their Fire without claiming that a bigger animation makes someone objectively “better” at production.\n\n## 6. Achievements, cosmetics, and collectibility",
    "A shareable Fire card/profile could let people show off their Fire without claiming that a bigger animation makes someone objectively “better” at production.\n\n" + fire_insert + "## 6. Achievements, cosmetics, and collectibility",
)

replace_once(
    "BABEL_PLATFORM.md",
    "- what cross-app data is genuinely useful enough to justify sharing\n- final ecosystem naming and visual family system",
    "- what cross-app data is genuinely useful enough to justify sharing\n- exact Babel Learning Contract semantics/versioning and which learning UI primitives should be shared across apps\n- whether a dedicated learning product ever earns a separate app boundary\n- whether Babel World ever becomes a real product and what unique cross-app job would justify it\n- final ecosystem naming and visual family system",
)

replace_once(
    "START_HERE.md",
    "PR #40, **Define FIRE Core doctrine and adaptive Recreation learning**, is merged at `9a3935c…`; its PR regression matrix passed at 390px, 440px, and 820px, and Pages deployment #65 succeeded on the same SHA. It establishes `FIRE_CORE.md` as canonical cross-generation doctrine without changing runtime behavior or user data. PR #39 remains the preceding V7 Safari/setup milestone and the latest physical iPhone runtime review.",
    "PR #41, **Capture Babel platform, monetization, and learning-Fire hypotheses**, is merged at `ec5c7a8…`; its PR regression matrix passed at 390px, 440px, and 820px. It preserves future accounts/sync, ecosystem, entitlements, Practice/Growth, the user's Fire, social, and lore ideas without changing runtime behavior or user data. PR #40 remains the FIRE Core doctrine milestone; PR #39 remains the latest physical iPhone runtime review.",
)

replace_once(
    "START_HERE.md",
    "- Future accounts/sync, Babel app harmony, monetization/entitlements, the deeper Practice/Skills surface, the user’s Fire, social sharing, and lore/Easter eggs are preserved as **future hypotheses** in `BABEL_PLATFORM.md`; they do not expand current Shell/Core implementation scope.",
    "- Future accounts/sync, Babel app harmony, monetization/entitlements, the deeper Practice/Skills surface, the user’s Fire, social sharing, and lore/Easter eggs are preserved as **future hypotheses** in `BABEL_PLATFORM.md`; they do not expand current Shell/Core implementation scope.\n- Cross-app learning follows **shared evidence, local identity**: overlapping production skills should eventually use a shared versioned Babel Learning Contract and familiar progress/learning primitives, while app-specific journeys/metaphors stay distinct. A future Babel World is only a hub hypothesis and must never become a dependency or global skill score.",
)
