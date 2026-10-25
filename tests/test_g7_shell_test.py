from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REVISION = "{{ site.github.build_revision }}"


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_real_g7_and_shell_test_load_same_deployment_revisioned_primitive_layers():
    preview = read("v7-preview/index.html")
    shell_test = read("v7-preview/shell-test.html")
    for html in (preview, shell_test):
        assert f'./styles.css?v={REVISION}' in html
        assert f'./shell-primitives.css?v={REVISION}' in html
        assert f'./state-primitives.css?v={REVISION}' in html
        assert "g7-shell-4" not in html
    assert f'./app.js?v={REVISION}' in preview
    assert f'./shell-test.js?v={REVISION}' in shell_test
    assert f'./shell-test-experiments.css?v={REVISION}' in shell_test
    assert "shell-test-experiments.css" not in preview
    assert f'./model.js?v={REVISION}' in preview


def test_shell_test_is_disposable_certification_surface_not_fire_flow():
    js = read("v7-preview/shell-test.js")
    assert "Symbol system · container comparison" in js
    assert "Rows · accessories" in js
    assert "Controls · states" in js
    assert "Temporary UI" in js
    assert "Composition · density" in js
    assert "intentionally not a FIRE workflow" not in js
    assert 'class="screen-meta build-info"' in js
    assert "G7 · ${commit}" in js
    assert 'symbolRow("symbol-button-current", "Current")' in js
    assert 'symbolRow("symbol-button-circle", "Circle")' in js
    assert "symbol-button-glass" not in js
    assert "Liquid Glass" not in js


def test_project_management_has_no_divider_and_accessories_use_canonical_icon_variables():
    css = read("v7-preview/shell-primitives.css")
    assert ".project-card-actions" in css
    assert "border-left: 0" in css
    assert "--accessory-box: 28px" in css
    assert "--accessory-glyph: 20px" in css
    for token in ("--icon-check", "--icon-chevron-right", "--icon-plus", "--icon-ellipsis", "--icon-menu"):
        assert token in css
    assert ".journey-mark" in css
    assert ".completion-ring" in css
    assert ".reorder-handle::before" in css


def test_accessory_family_uses_canonical_masks():
    css = read("v7-preview/shell-primitives.css")

    assert ".add-button::before" in css
    assert ".more-button::before" in css
    assert "mask-image: var(--icon-plus)" in css
    assert "mask-image: var(--icon-ellipsis)" in css

    assert ".checkmark::before" in css
    assert ".journey-mark.done::before" in css
    assert "mask: var(--icon-check) center / contain no-repeat" in css
    assert 'content: "✓"' not in css

    assert "--icon-chevron-right" in css
    assert "stroke-linecap='round'" in css
    assert "stroke-linejoin='round'" in css
    assert ".chevron::before," in css
    assert ".back-glyph::before," in css
    assert ".shell-test-link::before" in css
    assert "scaleX(-1)" in css
    assert ".chevron::after," in css


def test_state_language_is_non_circular_and_current_is_not_a_selected_row():
    css = read("v7-preview/state-primitives.css")
    assert ".journey-row.current { background: transparent; }" in css
    assert "--state-mark-box: 24px" in css
    assert "--state-mark-visual: 18px" in css
    assert "--state-current-width: var(--state-mark-visual)" in css
    assert "--state-current-height: 3px" in css
    assert "--state-upcoming-width: var(--state-mark-visual)" in css
    assert "--state-upcoming-height: 2px" in css
    assert ".journey-mark.done," in css
    assert ".checkmark" in css
    assert "border-radius: 50%" not in css
    assert ".journey-mark.current::before" in css
    assert ".journey-mark.upcoming::before," in css
    assert ".completion-ring::before" in css


def test_visible_glyph_artwork_uses_one_downward_optical_baseline_without_moving_layout():
    css = read("v7-preview/shell-primitives.css")
    state_css = read("v7-preview/state-primitives.css")
    assert "--symbol-optical-y: 1px" in css
    assert "padding-right: var(--accessory-edge-inset)" in css
    assert "grid-template-columns: minmax(0, 1fr) var(--touch)" in css
    assert "transform: translateY(var(--symbol-optical-y))" in css
    assert "translate(1px, var(--symbol-optical-y))" in css
    assert "translate(-1px, var(--symbol-optical-y)) scaleX(-1)" in css
    assert "top: calc(50% + var(--symbol-optical-y))" in css
    assert state_css.count("transform: translateY(var(--symbol-optical-y))") == 3
    assert "translateY(-.25px)" not in state_css


def test_shell_test_comparison_normalizes_vector_geometry_with_one_mirrored_chevron_correction():
    js = read("v7-preview/shell-test.js")
    css = read("v7-preview/shell-test-experiments.css")

    assert "const bounds = art.getBBox()" in js
    assert "12 - (bounds.x + bounds.width / 2)" in js
    assert "12 - (bounds.y + bounds.height / 2)" in js
    assert 'svg.dataset.normalized = "true"' in js
    assert 'viewBox="0 0 24 24"' in js
    for glyph in ("back", "forward", "plus", "check", "reorder", "more"):
        assert f"{glyph}:" in js

    assert "const CHEVRON_OPTICAL_INSET = 1.2" in js
    assert 'svg.dataset.symbol === "back"' in js
    assert 'svg.dataset.symbol === "forward"' in js
    assert "? CHEVRON_OPTICAL_INSET" in js
    assert "? -CHEVRON_OPTICAL_INSET" in js
    assert 'svg.dataset.opticalShiftX = opticalDx.toFixed(3)' in js

    assert "--symbol-optical-y" not in css
    assert ".symbol-button-current" in css
    assert ".symbol-button-circle" in css
    assert ".symbol-button-glass" not in css
    assert "backdrop-filter" not in css
    assert "radial-gradient" not in css
    assert "background: var(--surface)" in css
    assert "border-radius: var(--group-radius)" in css
    assert "border-radius: 50%" in css
    assert "width: var(--touch)" in css
    assert "height: var(--touch)" in css


def test_header_action_alignment_is_owned_by_shared_primitive_layer():
    css = read("v7-preview/shell-primitives.css")
    assert "--header-action-offset: 44px" in css
    assert ".toolbar-trailing { transform: translateY(var(--header-action-offset)); }" in css


def test_shared_accessory_lane_keeps_hit_target_separate_from_visible_marker_mass():
    css = read("v7-preview/shell-primitives.css")
    state_css = read("v7-preview/state-primitives.css")
    assert ".row,\n.form-row" not in css
    assert ".row > :last-child,\n.form-row > :last-child" not in css
    assert ".row {\n  grid-template-columns: minmax(0, 1fr) var(--touch);" in css
    assert ".journey-mark,\n.checkmark,\n.completion-ring" in state_css
    assert "width: var(--state-mark-box)" in state_css
    assert "height: var(--state-mark-box)" in state_css


def test_shell_test_comparison_is_bounded_and_does_not_become_product_chrome():
    css = read("v7-preview/shell-test-experiments.css")
    html = read("v7-preview/shell-test.html")
    preview = read("v7-preview/index.html")
    assert "Shell Test-only experiments" in css
    assert "must never redefine real G7 production primitives" in css
    assert "shell-test-experiments.css" in html
    assert "shell-test-experiments.css" not in preview


def test_shared_modal_spacing_uses_named_tokens_without_added_hairlines():
    css = read("v7-preview/shell-primitives.css")
    assert "--sheet-content-gap: 24px" in css
    assert "--sheet-action-gap: 20px" in css
    assert "margin-top: var(--sheet-content-gap)" in css
    assert "margin-top: var(--sheet-action-gap)" in css
    assert "padding-top: 0" in css
    assert "border-top: 0" in css
    assert "inset 0 1px 0" not in css


def test_status_remains_unfrozen_until_physical_review():
    status = read("G7_SHELL_CERTIFICATION_STATUS.md")
    assert status.count("| Candidate |") == 10
    assert "0 / 10 Locked" in status
    assert "G7 NOT FROZEN" in status
    assert "physical" in status.lower()