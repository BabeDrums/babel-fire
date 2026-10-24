from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_real_g7_and_shell_test_load_same_primitive_layer():
    preview = read("v7-preview/index.html")
    shell_test = read("v7-preview/shell-test.html")
    for html in (preview, shell_test):
        assert './styles.css' in html
        assert './shell-primitives.css' in html


def test_shell_test_is_disposable_certification_surface_not_fire_flow():
    js = read("v7-preview/shell-test.js")
    assert "intentionally not a FIRE workflow" in js
    assert "Rows · accessories" in js
    assert "Controls · states" in js
    assert "Temporary UI" in js
    assert "Composition · density" in js


def test_pass_one_removes_project_management_divider_and_canonicalizes_accessories():
    css = read("v7-preview/shell-primitives.css")
    assert ".project-card-actions" in css
    assert "border-left: 0" in css
    assert "--accessory-box" in css
    assert ".journey-mark" in css
    assert ".completion-ring" in css
    assert ".chevron" in css
    assert ".reorder-handle" in css


def test_status_remains_unfrozen_until_physical_review():
    status = read("G7_SHELL_CERTIFICATION_STATUS.md")
    assert status.count("| Candidate |") == 10
    assert "0 / 10 Locked" in status
    assert "G7 NOT FROZEN" in status
    assert "physical" in status.lower()
