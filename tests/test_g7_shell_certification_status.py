from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_status_board_tracks_all_categories_and_records_completed_freeze():
    text = (ROOT / "G7_SHELL_CERTIFICATION_STATUS.md").read_text(encoding="utf-8")
    category_rows = [line for line in text.splitlines() if line.startswith("| ") and line[2:3].isdigit()]
    assert len(category_rows) == 10
    assert all("Locked" in row for row in category_rows)
    assert "10 / 10 Locked" in text
    assert "G7 SHELL FROZEN" in text
    assert "FIRE Core breadboarding unblocked" in text
    assert "4a258c5170dd1d96dcbc0f2b0a9c35b283cec489" in text
