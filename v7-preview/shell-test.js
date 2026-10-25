const host = document.getElementById("shellTest");
const sheetRoot = document.getElementById("sheetRoot");
let buildCommitPromise = null;

const SYMBOLS = {
  back: '<path d="M15 18 9 12l6-6"/>',
  forward: '<path d="m9 18 6-6-6-6"/>',
  plus: '<path d="M5 12h14M12 5v14"/>',
  check: '<path d="M20 6 9 17l-5-5"/>',
  reorder: '<path d="M4 5h16M4 12h16M4 19h16"/>',
  more: '<circle cx="5" cy="12" r="1.25"/><circle cx="12" cy="12" r="1.25"/><circle cx="19" cy="12" r="1.25"/>'
};

const SYMBOL_LABELS = {
  back: "Back",
  forward: "Forward",
  plus: "Add",
  check: "Complete",
  reorder: "Reorder",
  more: "More"
};

// Physical review found the chevron family visually pulled toward each directional tip even after
// visible-bounds centering. Keep one mirrored family rule: both chevrons move the same small amount
// inward toward the center of the control. Other symbols remain purely geometry-centered.
const CHEVRON_OPTICAL_INSET = 1.2;

const normalizedSymbol = (name) => `
  <svg class="normalized-symbol" data-symbol="${name}" viewBox="0 0 24 24" aria-hidden="true" focusable="false">
    <g class="symbol-art">${SYMBOLS[name]}</g>
  </svg>`;

const symbolButton = (name, variant, variantLabel) => `
  <button class="symbol-button ${variant}" data-symbol-button="${name}" aria-label="${variantLabel} ${SYMBOL_LABELS[name]}">
    ${normalizedSymbol(name)}
  </button>`;

const symbolRow = (variant, label) => `
  <div class="symbol-variant" data-symbol-variant="${variant}">
    <span class="symbol-variant-label">${label}</span>
    <div class="symbol-comparison-row">
      ${Object.keys(SYMBOLS).map((name) => symbolButton(name, variant, label)).join("")}
    </div>
  </div>`;

function normalizeSymbols(root = document) {
  root.querySelectorAll(".normalized-symbol").forEach((svg) => {
    const art = svg.querySelector(".symbol-art");
    if (!art) return;
    art.removeAttribute("transform");
    const bounds = art.getBBox();
    const geometryDx = 12 - (bounds.x + bounds.width / 2);
    const dy = 12 - (bounds.y + bounds.height / 2);
    const opticalDx = svg.dataset.symbol === "back"
      ? CHEVRON_OPTICAL_INSET
      : svg.dataset.symbol === "forward"
        ? -CHEVRON_OPTICAL_INSET
        : 0;
    const dx = geometryDx + opticalDx;
    art.setAttribute("transform", `translate(${dx} ${dy})`);
    svg.dataset.normalized = "true";
    svg.dataset.geometryShiftX = geometryDx.toFixed(3);
    svg.dataset.opticalShiftX = opticalDx.toFixed(3);
    svg.dataset.shiftX = dx.toFixed(3);
    svg.dataset.shiftY = dy.toFixed(3);
  });
}

const toolbarButton = (kind, label) => kind === "add"
  ? `<button class="toolbar-button add-button" aria-label="${label}">+</button>`
  : `<button class="toolbar-button more-button" aria-label="${label}">•••</button>`;

const header = `
  <header class="screen-header">
    <div class="toolbar">
      <div class="toolbar-slot toolbar-leading"><a class="shell-test-link" href="./">← G7</a></div>
      <div class="toolbar-slot toolbar-trailing">${toolbarButton("add", "Example add action")}</div>
    </div>
    <div class="title-block"><h1>Shell Test</h1><p class="screen-meta build-info" aria-label="Preview build">G7 · …</p></div>
  </header>`;

host.innerHTML = `
  <main class="screen shell-test-screen scroll-safe">
    ${header}

    <section class="shell-test-section" aria-labelledby="glyphsHeading">
      <h2 id="glyphsHeading" class="shell-test-heading">Symbol system · container comparison</h2>
      <div class="symbol-comparison-stage" aria-label="Normalized symbol button comparison">
        ${symbolRow("symbol-button-current", "Current")}
        ${symbolRow("symbol-button-circle", "Circle")}
      </div>
      <p class="shell-test-note">Both rows use the same 24×24 vector source and automatic visible-bounds centering. Only the button shape changes; Back and Forward share one mirrored inward optical correction from physical review.</p>
    </section>

    <section class="shell-test-section" aria-labelledby="rowsHeading">
      <h2 id="rowsHeading" class="shell-test-heading">Rows · accessories</h2>
      <div class="group">
        <button class="row"><span class="row-title">Complete</span><span class="checkmark" aria-label="Done">✓</span></button>
        <button class="row"><span class="row-title">Current</span><span class="journey-mark current" aria-label="Current"></span></button>
        <button class="row"><span class="row-title">Incomplete</span><span class="completion-ring" aria-label="Incomplete"></span></button>
        <button class="row"><span><span class="row-title">Navigate</span><span class="row-sub">Secondary metadata</span></span><span class="chevron" aria-hidden="true">›</span></button>
        <div class="arrangement-row"><button class="section-edit-target"><span class="arrangement-name">Reorderable item</span><span class="arrangement-bars">8 bars</span></button><button class="reorder-handle" aria-label="Reorder example"></button></div>
        <div class="project-card"><button class="project-open"><span class="project-copy"><strong>Managed row</strong><span>Metadata · Fixture</span></span></button><button class="project-card-actions more-button" aria-label="Example row actions">•••</button></div>
      </div>
      <p class="shell-test-note">State can carry stronger visual emphasis; navigation and management stay quiet.</p>
    </section>

    <section class="shell-test-section" aria-labelledby="typeHeading">
      <h2 id="typeHeading" class="shell-test-heading">Typography · content stress</h2>
      <div class="group">
        <div class="row"><span><span class="row-title">Short label</span><span class="row-sub">Supporting text</span></span><span class="chevron">›</span></div>
        <div class="row shell-test-row-long"><span><span class="row-title">A deliberately long musical decision name that has to wrap without breaking the row</span><span class="row-sub">Long content should bend the composition, not invent a new visual language.</span></span><span class="chevron">›</span></div>
      </div>
    </section>

    <section class="shell-test-section" aria-labelledby="controlsHeading">
      <h2 id="controlsHeading" class="shell-test-heading">Controls · states</h2>
      <div class="selection-surface choice-grid">
        <button class="choice-tile selection-cell selected" aria-pressed="true">Selected</button>
        <button class="choice-tile selection-cell" aria-pressed="false">Default</button>
        <button class="choice-tile selection-cell shell-test-disabled" disabled>Disabled</button>
        <button class="choice-tile selection-cell" aria-pressed="false">Longer choice</button>
      </div>
      <div class="segmented-control bars-grid shell-test-gap">
        <button class="segment-option selected">4</button><button class="segment-option">8</button><button class="segment-option">12</button><button class="segment-option">16</button><button class="segment-option">Custom</button>
      </div>
      <div class="project-field-group shell-test-gap">
        <div class="project-field-row"><input class="field" placeholder="Name" aria-label="Example name"></div>
        <div class="project-field-row"><input class="field" value="Very long value that can be edited" aria-label="Example value"></div>
      </div>
    </section>

    <section class="shell-test-section" aria-labelledby="actionsHeading">
      <h2 id="actionsHeading" class="shell-test-heading">Actions</h2>
      <div class="shell-test-actions">
        <button class="primary-action">Continue</button>
        <button class="sheet-button sheet-secondary">Cancel</button>
        <button class="sheet-button sheet-danger-button">Delete</button>
        ${toolbarButton("add", "Add")}
        ${toolbarButton("more", "More")}
      </div>
    </section>

    <section class="shell-test-section" aria-labelledby="temporaryHeading">
      <h2 id="temporaryHeading" class="shell-test-heading">Temporary UI</h2>
      <div class="shell-test-actions">
        <button class="primary-action" data-open="selection">Open selection</button>
        <button class="sheet-button sheet-secondary" data-open="confirm">Open confirmation</button>
        <button class="sheet-button sheet-danger-button" data-open="destructive">Open destructive</button>
      </div>
      <p class="shell-test-note">Same semantic primitive: bottom sheet on compact width, centered dialog on regular width.</p>
    </section>

    <section class="shell-test-section" aria-labelledby="densityHeading">
      <h2 id="densityHeading" class="shell-test-heading">Composition · density</h2>
      <div class="shell-test-density">
        <div class="group"><div class="placeholder-state"><p>Sparse state: one quiet piece of content should still feel composed.</p></div></div>
        <div class="group">
          <div class="row"><span class="row-title">Normal one</span><span class="completion-ring"></span></div>
          <div class="row"><span class="row-title">Normal two</span><span class="chevron">›</span></div>
          <div class="row"><span class="row-title">Normal three</span><span class="checkmark">✓</span></div>
        </div>
        <div class="group">
          ${Array.from({length: 8}, (_, i) => `<div class="row"><span><span class="row-title">Dense item ${i + 1}</span><span class="row-sub">Representative metadata</span></span><span class="chevron">›</span></div>`).join("")}
        </div>
      </div>
    </section>
  </main>`;

normalizeSymbols(host);

function showBuildInfo() {
  const targets = document.querySelectorAll(".build-info");
  if (!targets.length) return;
  buildCommitPromise ||= fetch("../build-info.json", { cache: "no-store" })
    .then((response) => {
      if (!response.ok) throw new Error("Build metadata unavailable");
      return response.json();
    })
    .then((info) => /^[0-9a-f]{40}$/i.test(info.commit) ? info.commit.slice(0, 7) : "unavailable")
    .catch(() => "unavailable");
  buildCommitPromise.then((commit) => {
    targets.forEach((target) => {
      if (target.isConnected) target.textContent = `G7 · ${commit}`;
    });
  });
}

showBuildInfo();

function closeSheet() {
  sheetRoot.hidden = true;
  sheetRoot.innerHTML = "";
  document.body.style.overflow = "";
}

function openSheet(kind) {
  let body = "";
  if (kind === "selection") {
    body = `
      <div class="sheet-content-group">
        <div class="selection-surface section-types">
          <button class="selection-cell selected">Intimate</button><button class="selection-cell">Open</button>
          <button class="selection-cell">Distant</button><button class="selection-cell">Aggressive</button>
        </div>
      </div>
      <div class="sheet-content-group">
        <div class="segmented-control bars-grid"><button class="segment-option">A</button><button class="segment-option selected">B</button><button class="segment-option">C</button><button class="segment-option">D</button><button class="segment-option">Custom</button></div>
      </div>
      <div class="sheet-actions"><button class="sheet-button sheet-secondary" data-close>Cancel</button><button class="sheet-button sheet-primary" data-close>Done</button></div>`;
  } else if (kind === "confirm") {
    body = `<h2>Confirm change?</h2><p class="sheet-message">Consequence-bearing temporary UI earns a visible heading and concise context.</p><div class="sheet-actions"><button class="sheet-button sheet-secondary" data-close>Cancel</button><button class="sheet-button sheet-primary" data-close>Confirm</button></div>`;
  } else {
    body = `<h2>Delete item?</h2><p class="sheet-message">This fixture tests destructive hierarchy without becoming product architecture.</p><div class="sheet-actions"><button class="sheet-button sheet-secondary" data-close>Cancel</button><button class="sheet-button sheet-danger-button" data-close>Delete</button></div>`;
  }
  sheetRoot.innerHTML = `<div class="sheet" role="dialog" aria-modal="true" aria-label="Shell Test dialog">${body}</div>`;
  sheetRoot.hidden = false;
  document.body.style.overflow = "hidden";
  sheetRoot.querySelector("button")?.focus();
}

document.addEventListener("click", (event) => {
  const opener = event.target.closest("[data-open]");
  if (opener) openSheet(opener.dataset.open);
  if (event.target.closest("[data-close]")) closeSheet();
  if (event.target === sheetRoot) closeSheet();
});

document.addEventListener("keydown", (event) => {
  if (event.key === "Escape" && !sheetRoot.hidden) closeSheet();
});