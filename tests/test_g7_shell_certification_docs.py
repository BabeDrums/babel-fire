from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_shell_certification_is_routed_from_active_authority():
    agents = read("AGENTS.md")
    start = read("START_HERE.md")
    core = read("FIRE_CORE.md")
    spec = read("V7_DRAFT.md")

    for text in (agents, start, core, spec):
        assert "G7_SHELL_CERTIFICATION.md" in text


def test_shell_certification_keeps_fire_core_blocked_until_explicit_freeze():
    cert = read("G7_SHELL_CERTIFICATION.md")
    start = read("START_HERE.md")

    assert "Unresolved" in cert
    assert "Candidate" in cert
    assert "Locked" in cert
    assert "all 10 categories" in cert
    assert "explicit" in cert.lower()
    assert "FIRE Core breadboarding has not started" in start


def test_shell_test_is_not_a_second_fire_or_product_destination():
    cert = read("G7_SHELL_CERTIFICATION.md")
    assert "actual G7 primitives" in cert
    assert "not a second FIRE implementation" in cert
    assert "not a FIRE Core destination" in cert


def test_current_workspaces_are_explicitly_fixtures():
    cert = read("G7_SHELL_CERTIFICATION.md")
    spec = read("V7_DRAFT.md")

    assert "Setup → Structure → Tracks" in cert
    assert "disposable" in cert
    assert "Setup → Structure → Tracks" in spec
    assert "disposable" in spec
