from pathlib import Path

root = Path(__file__).resolve().parents[1]
path = root / "V7_DRAFT.md"
text = path.read_text(encoding="utf-8")
old = "Avoid redundant labels such as Recommended, In progress, Current, Later, Phase 1 of 7, 2 of 3 complete, or progress bars when the hierarchy is already obvious."
new = "Avoid redundant status labels such as Recommended, In progress, Current, Phase 1 of 7, 2 of 3 complete, or progress bars when the hierarchy is already obvious."
if old not in text:
    raise SystemExit("expected V7 wording not found")
path.write_text(text.replace(old, new, 1), encoding="utf-8")

for temp in [root / "scripts/fix_v7_later_once.py", root / ".github/workflows/fix-v7-later-once.yml"]:
    if temp.exists():
        temp.unlink()

print("V7 Later wording reconciled")
