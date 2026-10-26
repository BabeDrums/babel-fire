# Babel FIRE — G7 Shell Certification

**Status:** completed shell-certification contract. **G7 Shell Frozen.** The completed mutable category/evidence record lives in `G7_SHELL_CERTIFICATION_STATUS.md`.

The exact shell runtime that received final explicit Babel approval is `4a258c5170dd1d96dcbc0f2b0a9c35b283cec489` (PR #96). Keep this file as the stable contract that explains what “Locked” and “Frozen” mean; do not turn it into a running changelog.

## Purpose

G7 is not a collection of final FIRE screens. It is the reusable Babel/FIRE visual and interaction grammar that should let a future screen, section, modal, menu, form, or workspace begin from solved fundamentals and already feel like Babel.

Shell certification answered one question:

> If the fixture content changed tomorrow, would the product still compose cleanly from the same underlying grammar and unmistakably feel like Babel?

The current Setup → Structure → Tracks flow is disposable stress-test fixture content. Do not product-design those fixtures beyond what is useful to prove the shell. FIRE Core breadboarding may rename, replace, regroup, or remove them.

## Certification states

Each category used exactly one active state during certification:

- **Unresolved** — known systemic questions or contradictions remain.
- **Candidate** — a coherent solution exists in the real G7 primitives and is ready for/under representative validation.
- **Locked** — the primitive family is coherent, has survived representative Shell Test coverage where applicable, has been exercised in real G7 context, and has passed relevant physical iPhone/iPad review.

A category was never locked merely because one screenshot looked good.

Locking is category-level, not a promise that every future UI need already exists. A later genuinely new product requirement may deliberately extend the shell. Extension should add/revise the smallest necessary primitive without casually reopening unrelated locked categories.

## The ten categories

### 1. Page frame
Must establish safe-area behavior, content width, page/title anchors, top/bottom composition, sparse/normal/dense page behavior, and natural scrolling.

### 2. Typography
Must establish stable roles for page/project/workspace titles, section labels, row labels, body/supporting text, metadata, control values, field text, and action text. State must not arbitrarily move or resize the underlying label.

### 3. Spacing and alignment
Must establish the shared spacing vocabulary, vertical rhythm, leading/trailing anchors, accessory slots, optical centering, and deliberate exceptions. Repeated geometry must come from shared primitives/tokens rather than page patches.

### 4. Surfaces
Must establish background, grouped surfaces, cards/rows, separators, borders, elevation/material relationships, selected/focused treatment, and when a surface should disappear entirely.

### 5. Actions
Must establish primary, secondary, destructive, add (`+`), management (`•••`), Cancel, Done/Continue/Confirm, toolbar actions, and action-footers. Meaning determines hierarchy; visual treatment must remain coherent across contexts.

### 6. Icons and accessories
Must establish one canonical glyph/accessory vocabulary and geometry: icon box, optical weight, alignment, completion/incomplete/current state, chevron, add, ellipsis, drag/reorder, and other recurring accessories. Same meaning uses the same symbol family; different meanings are not forced into fake uniformity.

### 7. Controls and states
Must establish text/name fields, numeric fields, trailing value controls, segmented controls, selection surfaces, toggles/checks where needed, and representative default/selected/custom/disabled/focused/error states. Keyboard/input semantics remain appropriate to the value.

### 8. Temporary UI
Must establish modal/dialog, bottom sheet, menu, confirmation, destructive confirmation, and custom-selection composition. iPhone may use a bottom sheet while iPad/regular width uses a centered dialog; semantics and action hierarchy remain the same.

### 9. Responsive behavior
Must establish one product logic across compact and regular widths, adaptive reflow/density, wrapping, long content, scrolling, safe areas, keyboard/focus behavior, and iPhone/iPad presentation changes without device-specific product logic.

### 10. Accessibility and motion
Must establish approximately 44pt+ interactive targets, semantic labels, contrast/readability, text-scaling/Dynamic-Type strategy appropriate to the web implementation, visible focus, reduced-motion behavior, keyboard alternatives where applicable, and no essential skinny/gesture-only interaction.

## Developer Shell Test

G7 contains a developer-only **Shell Test** that renders the actual G7 primitive families rather than a replica of FIRE.

Purpose:
- compare canonical primitives side by side
- stress sparse / normal / dense composition
- test short / long / wrapping content
- exercise representative states
- exercise actions, rows/accessories, forms/controls, surfaces, modal/sheet/menu/confirmation patterns, typography, spacing, and responsive behavior
- make systemic defects obvious before they become page-specific patches

Rules:
1. Shell Test uses the same underlying primitives/tokens/styles as real G7.
2. Fixing a primitive in Shell Test must fix real G7 where that primitive is used; do not maintain a parallel visual implementation.
3. Shell Test is developer infrastructure, not FIRE product architecture and not a FIRE Core destination.
4. It may use fake/disposable fixture content specifically chosen to stress the shell.
5. It does not replace real-product physical validation.
6. It is not Babel Lab. Babel Lab remains an optional external sandbox for bounded experiments; complete coordinated FIRE shell validation belongs in G7.

## Babel composition principles proven through G7

- **Quiet until important.** Most chrome recedes; attention is earned by a real decision or state.
- **Rhythm is structural.** Spacing, grouping, repetition, and proportion should have deliberate cadence rather than arbitrary consistency.
- **One meaning, one language.** Same semantic job reuses the same component/glyph family.
- **Content before chrome.** The musician's project/work is primary.
- **Tactile, not decorative.** Character comes from composition, material, proportion, motion, and interaction—not gratuitous gradients, glow, borders, or metaphor.
- **Calm surface, expressive moments.** Restraint is the default; distinctive expression is reserved for moments/features that earn it.
- **Familiar first, signature second.** Commodity controls should be excellent and platform-legible. Spend originality on Babel/FIRE experiences where novelty improves the musical job.

The genuinely transferable versions of these principles were promoted into Babel Truth after freeze. FIRE-specific workflow, fixture content, and implementation code remain local.

## Historical adoption baseline

At adoption of this contract, all ten categories were Unresolved. Existing G7 work was evidence, but no category was grandfathered into Locked.

Initial shell findings included:
- remove the project-row `•••` divider and integrate the management control into the row
- optically center recurring action glyphs
- unify recurring check/current/incomplete/chevron/accessory geometry and positioning
- improve shared modal/sheet composition rather than polishing one fixture-specific modal
- treat `Accurate` and the current Tracks interaction/layout as disposable fixture semantics, not shell doctrine
- solve repeated defects at primitive/system level rather than page level

## Freeze record

The final gate required all of the following:
1. all 10 categories **Locked**
2. representative Shell Test coverage
3. real G7 composition using the same primitives
4. final physical-device review across iPhone and iPad/regular-width adaptation
5. no unresolved systemic contradiction in active authority
6. explicit Babel approval

All six conditions are satisfied. `G7_SHELL_CERTIFICATION_STATUS.md` records the evidence and **10 / 10 Locked** state.

Completed sequence:

**G7 Shell Frozen → transferable principles promoted to Babel Truth → FIRE Core breadboarding unblocked → thin FIRE Core spine → real-project validation.**

Shell freeze means the foundation is stable enough to build confidently. It does not prohibit deliberate future extension when FIRE Core discovers a genuinely new UI requirement. Reopen a locked category only when new evidence shows the foundation itself is wrong.
