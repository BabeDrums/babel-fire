from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REVISION = "{{ site.github.build_revision }}"


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_real_g7_and_shell_test_load_same_deployment_revisioned_primitive_layer():
    preview = read("v7-preview/index.html")
    shell_test = read("v7-preview/shell-test.html")
    for html in (preview, shell_test):
        assert f'./styles.css?v={REVISION}' in html
        assert f'./shell-primitives.css?v={REVISION}' in html
        assert "g7-shell-4" not in html
    assert f'./app.js?v={REVISION}' in preview
    assert f'./shell-test.js?v={REVISION}' in shell_test
    assert f'./model.js?v={REVISION}' in preview


def test_shell_test_is_disposable_certification_surface_not_fire_flow():
    js = read("v7-preview/shell-test.js")
    assert "Rows · accessories" in js
    assert "Controls · states" in js
    assert "Temporary UI" in js
    assert "Composition · density" in js
    assert "intentionally not a FIRE workflow" not in js
    assert 'class="screen-meta build-info"' in js
    assert "G7 · ${commit}" in js


def test_project_management_has_no_divider_and_accessories_are_canonicalized():
    css = read("v7-preview/shell-primitives.css")
    assert ".project-card-actions" in css
    assert "border-left: 0" in css
    assert "--accessory-box" in css
    assert "--accessory-stroke" in css
    assert ".journey-mark" in css
    assert ".completion-ring" in css
    assert ".chevron::before" in css
    assert ".reorder-handle::before" in css


def test_current_state_is_neutral_nested_ring_and_actions_are_not_font_dependent():
    css = read("v7-preview/shell-primitives.css")
    assert ".add-button { font-size: 0; }" in css
    assert ".add-button::before" in css
    assert ".add-button::after" in css
    assert ".more-button::before" in css
    assert "width: 3px" in css
    assert "box-shadow: -7px 0 0 currentColor, 7px 0 0 currentColor" in css
    assert ".journey-mark.current" in css
    assert "border: 2px solid var(--state-current-ring)" in css
    assert "--state-current-ring: #d9d9df" in css
    assert "--state-current-inner: rgba(232,232,237,.22)" in css
    assert ".journey-mark.current::after" in css
    assert "width: 10px" in css
    assert "background: var(--state-current-inner)" in css
    assert "#d8d84f" not in css


def test_shared_modal_spacing_uses_named_tokens():
    css = read("v7-preview/shell-primitives.css")
    assert "--sheet-content-gap: 24px" in css
    assert "--sheet-action-gap: 20px" in css
    assert "margin-top: var(--sheet-content-gap)" in css
    assert "margin-top: var(--sheet-action-gap)" in css


def test_status_remains_unfrozen_until_physical_review():
    status = read("G7_SHELL_CERTIFICATION_STATUS.md")
    assert status.count("| Candidate |") == 10
    assert "0 / 10 Locked" in status
    assert "G7 NOT FROZEN" in status
    assert "physical" in status.lower()
