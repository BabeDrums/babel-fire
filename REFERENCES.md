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
- concise language and consistent visual/interaction semantics

Do not use as a reason to make FIRE generic, sterile, or visually indistinguishable from Apple apps.

### Duolingo
Use as a **logic reference**, especially for:
- one obvious next action
- understandable progression
- visible movement through a journey
- completed work remaining accessible
- adaptive help/practice that responds to demonstrated need

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

### GitHub / Primer
Use for:
- organizing an enormous amount of information without flattening everything into one screen
- stable, concise vocabulary that makes complex concepts learnable (`branch`, `merge`, `pull request`, etc.)
- breadcrumbs, hierarchy, and wayfinding that help people understand where they are
- familiar reusable metaphors/components across many product areas
- responsive design foundations that let dense tools remain coherent across sizes

Babel lesson: **naming is interface design.** Prefer short, durable, meaningful nouns/verbs when one word can carry the concept cleanly.

Do not copy developer-centric density, terminology, or GitHub's exact navigation patterns where a musician would need simpler language.

Useful official references:
- https://primer.style/
- https://primer.style/product/getting-started/
- https://primer.style/product/ui-patterns/navigation/
- https://github.blog/news-insights/product-news/exploring-github-with-the-redesigned-navigation-now-in-public-beta/

### ChatGPT
Use for:
- a calm shell that can expose very different capabilities without making every capability permanently visible
- choosing the presentation that fits the task rather than forcing one UI format everywhere
- allowing simple text/content to remain simple when richer interaction is unnecessary
- progressive, contextual capability discovery
- conversation/history as continuity without requiring the user to manually reconstruct context

Do not make FIRE conversational merely because ChatGPT is; FIRE should use the interaction model that best serves production decisions.

Useful official references:
- https://help.openai.com/en/articles/20001598-intelligent-ui-in-chatgpt
- https://developers.openai.com/plugins/concepts/ui-guidelines

### Basecamp / Shape Up
Use for:
- calm organization of substantial work
- keeping actions/content intentional even when a product supports many jobs
- **breadboarding**: define places, affordances, and connections before debating visual treatment
- solving the product at the right abstraction level before polishing the enclosure

Do not copy Basecamp's information architecture literally; FIRE has a different creative workflow and needs music-native structures.

Useful official reference:
- https://basecamp.com/shapeup/1.3-chapter-04

### Things
Use for:
- a simple surface that remains powerful for people who want depth
- hiding optional detail until it is actually needed
- clear content structure, quiet hierarchy, and polished interaction
- making functionality feel deliberate instead of configurable for configuration's sake

Do not copy Things' task-management metaphors into music-production work.

Useful official references:
- https://culturedcode.com/things/features/
- https://culturedcode.com/things/

### Instagram / TikTok / Snapchat
Use primarily as **observational interaction references**, not as doctrine.

Useful qualities to study:
- immediate entry into the primary content/job
- low-chrome, content-first presentation
- repeated interaction patterns that become muscle memory quickly
- strong creation/discovery affordances with very little explanatory UI
- personalization and identity expressed without making every screen visually noisy
- Snapchat's willingness to simplify navigation around a smaller set of core jobs

Important guardrail: FIRE should **not** import engagement-maximizing dark patterns, infinite-feed pressure, social comparison loops, notification pressure, or attention capture that conflicts with making music.

Useful official Snapchat reference:
- https://newsroom.snap.com/sps-2024-simple-snapchat

Instagram and TikTok can remain live-product observation references when official design-system material is not public enough to justify treating them as authoritative sources.

### Logic Pro / Ableton / other DAWs
Use for:
- domain-native musical vocabulary and mental models
- accepting purposeful density where expert work genuinely needs it
- track/group/stack abstractions and progressive detail
- preserving creative flexibility rather than forcing one “correct” production workflow
- understanding that beginning, progressing, and finishing are different creative problems

FIRE must remain a **companion**, not a second DAW. Borrow production mental models where they reduce translation cost; do not reproduce plugin/routing/session data merely because the DAW has it.

Useful references:
- Logic Pro / Apple documentation for current DAW behavior
- https://makingmusic.ableton.com/

### Pokémon GO
Use as a collection/progress reference for:
- medals with inspectable progress
- a profile that gathers many different progression artifacts without requiring them all to mean the same thing
- the idea that a badge collection can have both list/gallery and spatial/map presentations
- optional world/progression discovery around a primary experience

Do not copy XP ladders, medal tiers, map styling, Pokémon branding, or reward structures. Babel World should earn its own collection language from the apps/achievements that eventually exist.

Useful references:
- https://niantic.helpshift.com/hc/en/6-pokemon-go/faq/101-how-do-i-level-up-and-earn-medals/
- https://niantic.helpshift.com/hc/en/6-pokemon-go/faq/2409-collecting-gym-badges/

### Additional references worth watching, not locking

These are useful comparison products when a specific problem calls for them, but they do not need to become permanent doctrine merely because they are strong products:

- **Notion** — flexible information organization; can be minimal or powerful depending on need
- **Spotify** — library/discovery/playback hierarchy and personalization
- **Linear** — focused, fast information-dense work surfaces
- **Pinterest** — visual discovery/collection patterns when future mood/reference workflows need them

Add them to durable doctrine only if a specific transferable lesson becomes important to FIRE.

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

The eventual collection surface could be a gallery, trophy-like display, spatial map/neighborhood/park, or something more original. Do not choose the container before real Babel apps and badges give it content.

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

### Pixel-art Fire + badge language hypothesis
A future version of the user’s Fire — and potentially Babel achievement/source marks — could use one original pixel visual grammar rather than smooth/vector-only artwork.

Why it is interesting:
- gives FIRE/Babel a distinctive, personal visual language tied to Gabriel’s genuine taste
- small sprite states can make progression feel collectible and alive
- frame-by-frame flame movement, embers, sparks, palette shifts, silhouette changes, and badge details can communicate growth without requiring photorealistic effects
- crisp integer-scale rendering could adapt from tiny source marks/profile badges to larger dedicated Fire views
- motion can remain lightweight, and Reduce Motion can fall back to a static sprite/state

Guardrails:
- this is a **later personality prototype**, not current Shell Freeze work
- test whether pixel art feels intentional beside FIRE’s calm modern UI rather than pasted on top of it
- draw an original Babel visual grammar; inspiration must not become imitation
- accessibility and legibility remain more important than nostalgia
- do not lock pixel dimensions, palette, or sprite complexity before prototyping at actual UI sizes

## Reference-maintenance rule

When a new external product, standard, game, visual language, or design system materially influences FIRE:
1. record **what specific lesson we want from it**
2. record **what we explicitly do not want to copy**
3. keep product decisions in the authoritative FIRE docs rather than treating the reference itself as a requirement
4. revisit references when research or real product evidence contradicts the initial lesson
