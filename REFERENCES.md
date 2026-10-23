# Babel FIRE — Reference Registry

This file keeps external references, transferable patterns, and inspiration in one place so FIRE can learn from strong systems without accidentally copying them or confusing inspiration with product doctrine.

**Rule:** references are evidence and inspiration, not authority. `FIRE_CORE.md`, `START_HERE.md`, `V7_DRAFT.md`, and the active product specs remain authoritative for FIRE decisions.

## Product / interaction references

### Apple Human Interface Guidelines
Use for:
- calm hierarchy and clear primary actions
- familiar platform behavior on iPhone/iPad
- progressive disclosure and restraint
- accessibility, motion restraint, and system-native expectations

Do not use as a reason to make FIRE generic, sterile, or visually indistinguishable from Apple apps.

### Duolingo
Use as a **logic reference**, especially for:
- one obvious next action
- understandable progression
- visible movement through a journey
- completed work remaining accessible

Do not import XP, streak pressure, cartoon lesson paths, fake progress percentages, or unnecessary hard locks.

### Google / Material Design
Use for:
- design-system thinking across many surfaces
- reusable components and shared semantics
- consistency without requiring every product to look identical
- motion that communicates state/meaning
- iterative design-system maintenance and QA rather than “set it and forget it”

Useful official references:
- https://design.google/about
- https://design.google/library/material-design-eras
- https://design.google/library/rhythms-appear
- https://design.google/library/figma-comments-material-ux-euphrates-dahout

### Figma
Use for:
- components, variables, styles, and libraries as reusable primitives
- shared design tokens across products while preserving product-specific composition
- promoting proven patterns into a library after they earn reuse
- keeping design and implementation semantics aligned

Important Babel lesson: **do not build a giant speculative universal Babel component library before multiple products exist.** Extract and share what FIRE proves first.

Useful official references:
- https://help.figma.com/hc/en-us/articles/360041051154-Guide-to-libraries-in-Figma
- https://help.figma.com/hc/en-us/articles/15339657135383-Guide-to-variables-in-Figma
- https://www.figma.com/design-systems/

## Learning / interoperability references

### xAPI 2.0
xAPI (Experience API) is a standard for recording and exchanging structured learning/activity evidence between different technologies.

Babel should **borrow the architecture idea, not adopt the whole enterprise learning stack**.

Most useful transferable ideas:
- store meaningful evidence/events first; derive skill state from that evidence later
- give concepts stable semantic IDs instead of relying on display labels
- preserve provenance/context with evidence: source app, project, mode, guidance depth, time, and schema/version
- keep history rather than silently overwriting the past
- use controlled domain vocabularies/templates so multiple apps describe the same capability consistently
- let richer conclusions emerge from multiple evidence events instead of pretending one action proves mastery

xAPI Profiles are especially relevant to the future **Babel Learning Contract** because they formalize domain-specific vocabulary and statement patterns.

Useful references:
- https://opensource.ieee.org/xapi/xapi-base-standard-documentation
- https://github.com/adlnet/xapi-profiles

### Open Badges 3.0
Open Badges packages a visual achievement with metadata such as the achievement identity, issuer, criteria, evidence, and context.

Babel should borrow the principle that a badge should have an inspectable meaning rather than being decoration with no truth behind it.

Useful reference:
- https://www.1edtech.org/standards/open-badges

## Babel World hypotheses

### Shared skill identity + source marks
A future Babel World could show one shared skill identity while small visual source marks indicate which Babel apps have contributed credible evidence to it.

Example concept:

**Balance & Hierarchy**
- FIRE source mark
- future learning-app source mark
- future third-app source mark

Recommendations:
- show each contributing app once, not one icon for every evidence event
- tapping/expanding can reveal the actual evidence history and source contexts
- the shared skill remains the primary identity; app marks are provenance
- multiple app marks can visually accumulate around a skill without creating a fake global level

### Source marks vs achievement badges
Keep two semantics separate even if both use badge-like visual language:

1. **Source/origin marks** — small provenance indicators showing which app(s) contributed evidence to a skill.
2. **Achievement badges** — larger collectible recognitions for meaningful accomplishments, milestones, discoveries, or cross-app achievements.

This prevents a tiny “came from FIRE” marker from being confused with “you earned a major achievement.”

Possible later idea: a cross-app achievement can intentionally combine multiple app source marks when the accomplishment genuinely required evidence across contexts.

## FIRE visual references

### Minecraft
Use for:
- love of readable pixel structure
- modular/systemic visual logic
- simple elements creating a larger living world
- nostalgic game-world warmth without copying Minecraft assets, blocks, UI, textures, or iconography

### OG Pokémon / classic pixel-era creature games
Use for:
- charming limited-resolution pixel art
- strong silhouettes and recognizable states
- small frame-by-frame animation that feels alive
- collectible identity and progression communicated visually

Do not imitate specific Pokémon sprites, characters, palettes, UI, or copyrighted assets.

### Pixel-art Fire hypothesis
A future version of the user’s Fire could be deliberately pixelated rather than smooth/vector-based.

Why it is interesting:
- gives FIRE a distinctive, personal visual language tied to Gabriel’s genuine taste
- small sprite states can make progression feel collectible and alive
- frame-by-frame flame movement, embers, sparks, palette shifts, and silhouette changes can communicate growth without requiring photorealistic effects
- crisp integer-scale rendering could adapt from tiny profile marks to larger dedicated Fire views
- motion can remain lightweight, and Reduce Motion can fall back to a static sprite/state

Guardrails:
- this is a **later personality prototype**, not current Shell Freeze work
- test whether pixel art feels intentional beside FIRE’s calm modern UI rather than pasted on top of it
- draw an original Babel visual grammar; inspiration must not become imitation
- accessibility and legibility remain more important than nostalgia

## Reference-maintenance rule

When a new external product, standard, game, visual language, or design system materially influences FIRE:
1. record **what specific lesson we want from it**
2. record **what we explicitly do not want to copy**
3. keep product decisions in the authoritative FIRE docs rather than treating the reference itself as a requirement
4. revisit references when research or real product evidence contradicts the initial lesson
