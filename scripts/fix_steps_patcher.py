from pathlib import Path

path = Path(__file__).with_name("apply_steps_navigation.py")
text = path.read_text(encoding="utf-8")
old = """css = replace_once(
    css,
    '.change-marker {\\n  position: absolute;',
    '.change-marker {\\n  position: absolute;\\n  z-index: 7;',
    \"change marker z-index\",
)"""
new = """css = replace_once(
    css,
    '.change-marker {\\n  z-index: 3;\\n  position: absolute;',
    '.change-marker {\\n  z-index: 7;\\n  position: absolute;',
    \"change marker z-index\",
)"""
if old not in text:
    raise SystemExit("target patcher block not found")
path.write_text(text.replace(old, new, 1), encoding="utf-8")
