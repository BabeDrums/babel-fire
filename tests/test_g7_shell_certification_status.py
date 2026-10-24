from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_status_board_tracks_all_categories_and_blocks_fire_core_until_locked():
    text = (ROOT / "G7_SHELL_CERTIFICATION_STATUS.md").read_text(encoding="utf-8")
    category_rows = [line for line in text.splitlines() if line.startswith("| ") and line[2:3].isdigit()]
    assert len(category_rows) == 10
    assert all(any(state in row for state in ("Unresolved", "Candidate", "Locked")) for row in category_rows)
    assert "0 / 10 Locked" in text
    assert "G7 NOT FROZEN" in text
    assert "FIRE Core breadboarding blocked" in text
