from pathlib import Path

path = Path('app.js')
s = path.read_text()
old = '''  function refreshMapProgress() {
    if (ui.route !== "map") return;
    const p = project(), state = canonicalState(p), done = mapCheckpointCount(p);
    const destinations = ["structure", "tracks", sectionStudyCoreDone(p) ? "map-summary" : "section-study"];
    const completed = [state.structure, state.palette, state.study];
    app.querySelectorAll(".phase-checkpoints .group-card.list > .list-row").forEach((row, i) => {
      const html = checkpointRow(["Structure", "Tracks", "Section Study"][i],
        ["Map the form.", "Identify what plays.", "Map each section in time."][i],
        destinations[i], completed[i], !!state.eligible[destinations[i]]);
      row.outerHTML = html;
    });
    const count = app.querySelector(".checkpoint-count");
    if (count) count.textContent = `${done} of 3`;
    queueViewportFit();
  }
'''
new = '''  function refreshMapProgress() {
    if (ui.route !== "map") return;
    const p = project(), state = canonicalState(p), done = mapCheckpointCount(p),
      list = app.querySelector(".phase-checkpoints .group-card.list");
    if (!list) return;
    const destinations = ["structure", "tracks", sectionStudyCoreDone(p) ? "map-summary" : "section-study"],
      completed = [state.structure, state.palette, state.study],
      rows = () => ["Structure", "Tracks", "Section Study"].map((title, i) =>
        checkpointRow(title,
          ["Map the form.", "Identify what plays.", "Map each section in time."][i],
          destinations[i], completed[i], !!state.eligible[destinations[i]]),
      ).join("");
    if (!state.setup) {
      if (!list.querySelector(".checkpoint-locked-message"))
        list.innerHTML = `<div class="list-row static no-status checkpoint-locked-message"><div><div class="title">Available after Song Setup</div></div></div>`;
    } else if (list.querySelector(".checkpoint-locked-message") || list.children.length !== 3) {
      list.innerHTML = rows();
    } else {
      [...list.children].forEach((row, i) => {
        row.outerHTML = checkpointRow(["Structure", "Tracks", "Section Study"][i],
          ["Map the form.", "Identify what plays.", "Map each section in time."][i],
          destinations[i], completed[i], !!state.eligible[destinations[i]]);
      });
    }
    const count = app.querySelector(".checkpoint-count");
    if (count) count.textContent = `${done} of 3`;
    queueViewportFit();
  }
'''
if old not in s:
    raise SystemExit('refreshMapProgress anchor not found')
path.write_text(s.replace(old, new, 1))
