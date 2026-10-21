from pathlib import Path

path = Path(__file__).with_name("apply_steps_navigation.py")
text = path.read_text(encoding="utf-8")

old_marker = """css = replace_once(
    css,
    '.change-marker {\\n  position: absolute;',
    '.change-marker {\\n  position: absolute;\\n  z-index: 7;',
    \"change marker z-index\",
)"""
new_marker = """css = replace_once(
    css,
    '.change-marker {\\n  z-index: 3;\\n  position: absolute;',
    '.change-marker {\\n  z-index: 7;\\n  position: absolute;',
    \"change marker z-index\",
)"""
if old_marker not in text:
    raise SystemExit("target marker patcher block not found")
text = text.replace(old_marker, new_marker, 1)

old_context = """css = replace_once(
    css,
    '.sheet-backdrop {\\n',
    context_css + '.sheet-backdrop {\\n',
    \"context navigator styles\",
)"""
new_context = """if '.sheet-backdrop {\\n' not in css:
    raise RuntimeError(\"context navigator style anchor missing\")
css = css.replace('.sheet-backdrop {\\n', context_css + '.sheet-backdrop {\\n', 1)"""
if old_context not in text:
    raise SystemExit("target context patcher block not found")
text = text.replace(old_context, new_context, 1)

path.write_text(text, encoding="utf-8")
