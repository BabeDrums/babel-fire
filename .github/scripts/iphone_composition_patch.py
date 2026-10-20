from pathlib import Path

path = Path("styles.css")
text = path.read_text(encoding="utf-8")

old = '''@media (max-width: 430px) {
  .project-page .page-heading,
  .workflow-page .page-heading {
    margin-bottom: 20px;
  }
  .project-page .page-heading h1,
  .workflow-page .page-heading h1 {
    font-size: 34px;
    line-height: 1.04;
  }
  .project-open {
    padding-left: 16px;
    min-height: 102px;
  }

  /* Phone screens keep one stable top alignment; density changes only when content needs it. */
  #app[data-route="map"] .setup-row {
    min-height: 56px;
    padding-inline: 14px;
  }
  #app[data-route="map"] .phase-setup > .spacer-18 {
    height: 10px;
  }
  #app[data-route="map"] .phase-setup .action-card {
    min-height: 58px;
  }'''

new = '''@media (max-width: 430px) {
  .app-shell {
    /* Let intrinsic content decide whether the page scrolls; do not reserve a fake toolbar-height tail. */
    padding-bottom: calc(24px + env(safe-area-inset-bottom));
  }
  .project-page .page-heading,
  .workflow-page .page-heading {
    margin-bottom: 20px;
  }
  .project-page .page-heading h1,
  .workflow-page .page-heading h1 {
    font-size: 34px;
    line-height: 1.04;
  }
  .project-open {
    padding-left: 16px;
    min-height: 102px;
  }

  /* Phone screens keep one stable top alignment; density changes only when content needs it. */
  #app[data-route="map"] .setup-row {
    min-height: 58px;
    padding-inline: 14px;
  }
  #app[data-route="map"] .setup-value,
  #app[data-route="map"] .state-control {
    min-height: 44px;
    background: transparent;
    border-color: transparent;
    padding-right: 0;
  }
  #app[data-route="map"] .state-control.on {
    background: transparent;
    border-color: transparent;
  }
  #app[data-route="map"] .phase-setup > .spacer-18 {
    height: 0;
  }
  #app[data-route="map"] .phase-setup .setup-panel {
    border-radius: var(--radius-card) var(--radius-card) 0 0;
    border-bottom: 0;
  }
  #app[data-route="map"] .phase-setup .action-card {
    min-height: 56px;
    padding: 10px 14px;
    border-radius: 0 0 var(--radius-card) var(--radius-card);
  }
  #app[data-route="map"] .phase-checkpoints {
    margin-top: 18px;
  }'''

if old not in text:
    raise SystemExit("phone composition anchor not found")

path.write_text(text.replace(old, new, 1), encoding="utf-8")
