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


def test_completed_certification_status_has_one_documented_owner():
    status = "G7_SHELL_CERTIFICATION_STATUS.md"
    agents = read("AGENTS.md")
    start = read("START_HERE.md")
    core = read("FIRE_CORE.md")
    cert = read("G7_SHELL_CERTIFICATION.md")

    for text in (agents, start, core, cert):
        assert status in text
    assert "completed certification evidence/status" in agents
    assert "completed evidence board" in start
    assert "records **10 / 10 Locked**" in core
    assert "completed mutable category/evidence record" in cert


def test_shell_certification_records_explicit_completed_freeze():
    cert = read("G7_SHELL_CERTIFICATION.md")
    start = read("START_HERE.md")
    core = read("FIRE_CORE.md")

    assert "Unresolved" in cert
    assert "Candidate" in cert
    assert "Locked" in cert
    assert "all 10 categories" in cert
    assert "explicit Babel approval" in cert
    assert "G7 SHELL IS FROZEN" in start
    assert "FIRE Core breadboarding is now unblocked" in start
    assert "FIRE Core breadboarding may now begin" in core


def test_shell_test_is_not_a_second_fire_or_product_destination():
    cert = read("G7_SHELL_CERTIFICATION.md")
    assert "actual G7 primitive families" in cert
    assert "not FIRE product architecture" in cert
    assert "not a FIRE Core destination" in cert


def test_current_workspaces_are_explicitly_fixtures():
    cert = read("G7_SHELL_CERTIFICATION.md")
    spec = read("V7_DRAFT.md")

    assert "Setup → Structure → Tracks" in cert
    assert "disposable" in cert
    assert "Setup → Structure → Tracks" in spec
    assert "disposable" in spec
