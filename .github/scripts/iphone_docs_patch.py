from pathlib import Path


def replace(path, old, new):
    p = Path(path)
    text = p.read_text(encoding="utf-8")
    if old not in text:
        raise SystemExit(f"anchor not found in {path}")
    p.write_text(text.replace(old, new, 1), encoding="utf-8")

replace(
    "START_HERE.md",
    "- On iPad, task sheets such as Add Sections should use compact centered form/page-style presentation where practical; narrow iPhone layouts may remain bottom-oriented.\n",
    "- On iPad, task sheets such as Add Sections should use compact centered form/page-style presentation where practical; narrow iPhone layouts may remain bottom-oriented.\n- Physical iPhone review after the foundation consolidation established two phone-specific rules: short routes that fit the visual viewport must not create root scroll/bounce, and dense routes should compact redundant secondary information before shrinking touch targets.\n- On narrow phones, Roadmap should prioritize full detail for the current phase and compact non-current phases; The Map may collapse redundant checkpoint descriptions while preserving titles, state, and progression.\n",
)

replace(
    "AGENTS.md",
    "- iPad task sheets should prefer compact centered form/page-style presentation when appropriate; narrow phone layouts may use bottom-oriented sheets.\n",
    "- iPad task sheets should prefer compact centered form/page-style presentation when appropriate; narrow phone layouts may use bottom-oriented sheets.\n- Short phone pages that fit within the visual viewport must not create unnecessary root scrolling or rubber-band drift. Use dynamic viewport sizing/overscroll containment while preserving natural scrolling when content genuinely exceeds the viewport.\n- Dense narrow-phone layouts should reduce redundant secondary copy and compact non-current states before shrinking controls. Preserve ~44px touch targets and progression/state clarity.\n",
)

replace(
    "V6.md",
    "12. No `polish.css`, `polish.js`, or MutationObserver rewrite architecture. Implement in core `app.js`, `styles.css`, and shared components.\n",
    "12. No `polish.css`, `polish.js`, or MutationObserver rewrite architecture. Implement in core `app.js`, `styles.css`, and shared components.\n13. On narrow phones, routes that fit inside the visual viewport should remain stationary instead of creating unnecessary page scroll/rubber-band drift; use dynamic viewport sizing while retaining natural scroll for genuinely long content.\n14. Dense phone layouts should compact redundant supporting detail and non-current states before shrinking controls. Roadmap gives the current phase full detail and may collapse secondary detail for non-current phases; Map may suppress redundant checkpoint descriptions while keeping titles/state/progress clear.\n",
)

replace(
    "CONTEXT.md",
    "Mouse, touch, and normal keyboard accessibility are first-class. Keep important controls visible without hover, provide stable non-geometric hover/press feedback and visible focus, and preserve native scrolling, Tab/Shift+Tab, Enter/Space activation, and safe Escape dismissal. Custom productivity shortcuts remain outside the current scope.\n",
    "Mouse, touch, and normal keyboard accessibility are first-class. Keep important controls visible without hover, provide stable non-geometric hover/press feedback and visible focus, and preserve native scrolling, Tab/Shift+Tab, Enter/Space activation, and safe Escape dismissal. Custom productivity shortcuts remain outside the current scope.\n\nOn narrow iPhone layouts, a route that already fits the visual viewport should not gain fake root scroll or rubber-band drift; keeping the page shell stationary preserves alignment when moving between screens. When a phone route is genuinely dense, first remove redundant supporting copy or compact non-current states before shrinking touch targets. Roadmap should emphasize the current phase and compress future/completed phase detail; Map checkpoint descriptions may collapse when the titles and state already communicate the task.\n",
)

replace(
    "CHANGELOG.md",
    "## V6\n\n",
    "## V6\n\n- iPhone scroll/density refinement: short routes now use the dynamic visual viewport without unnecessary root bounce, while dense phone screens compact secondary detail instead of shrinking controls; Map checkpoints and Roadmap progression receive phone-specific density treatment and the Add Sections sheet wastes less vertical space.\n",
)
