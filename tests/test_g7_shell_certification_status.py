from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_status_board_starts_unfrozen_and_blocks_fire_core():
    text = (ROOT / "G7_SHELL_CERTIFICATION_STATUS.md").read_text(encoding="utf-8")
    assert text.count("| Unresolved |") == 10
    assert "0 / 10 Locked" in text
    assert "G7 NOT FROZEN" in text
    assert "FIRE Core breadboarding blocked" in text
