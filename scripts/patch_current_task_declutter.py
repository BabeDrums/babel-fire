from pathlib import Path
import re

app = Path("app.js")
s = app.read_text()

# Project home: keep the current phase dominant and remove redundant Next/Project labels.
pattern = r'    const body = `<div class="project-overview"><section class="project-current">.*?</section></div>`;\n    app.innerHTML ='
replacement = '''    const body = `<div class="project-overview"><section class="project-current"><button class="hero-card project-open" style="border-radius:var(--radius-card);height:auto" data-action="go" data-route="${phase.route}" aria-label="Open ${esc(phase.title)}"><div class="phase-line"><div><h3>${esc(phase.title)}</h3></div><div class="phase-num">Phase ${phaseIndex + 1} of 7</div></div><p class="sub">${esc(phase.desc)}</p><div class="foot"><span>${esc(phaseProgress)}</span><span aria-hidden="true">›</span></div></button></section><section class="project-support"><div class="quick-grid"><button class="quick-card" data-action="go" data-route="roadmap"><strong>Roadmap</strong><span>Seven phases to a finished rebuild.</span></button><button class="quick-card" data-action="go" data-route="notes"><strong>Notes</strong><span>Questions and takeaways.</span></button></div></section></div>`;
    app.innerHTML ='''
s, n = re.subn(pattern, replacement, s, count=1, flags=re.S)
if n != 1:
    raise SystemExit(f"project home replacement count: {n}")

# New Project: remove the redundant section label and keep the commit action compact.
old = '<div class="section-kicker project-field-label">Project</div>'
if old not in s:
    raise SystemExit("new project label not found")
s = s.replace(old, "", 1)
old = '<div class="spacer-24"></div><button class="primary full" data-action="create-project">Create Project</button>'
new = '<button class="primary create-project-action" data-action="create-project">Create Project</button>'
if old not in s:
    raise SystemExit("new project action not found")
s = s.replace(old, new, 1)

# Map: before setup is valid, show one quiet prerequisite summary instead of three dead rows.
old = '    const checkpoints =\n      checkpointRow('
if old not in s:
    raise SystemExit("map checkpoints declaration not found")
s = s.replace(old, '    let checkpoints =\n      checkpointRow(', 1)
anchor = '''        studyUnlocked,
      );
    app.innerHTML = workflowPhaseHome(0, done, 3, checkpoints, setup);'''
replacement = '''        studyUnlocked,
      );
    if (!setupDone)
      checkpoints = `<div class="list-row static no-status checkpoint-locked-message"><div><div class="title">Available after Song Setup</div></div></div>`;
    app.innerHTML = workflowPhaseHome(0, done, 3, checkpoints, setup);'''
if anchor not in s:
    raise SystemExit("map checkpoints anchor not found")
s = s.replace(anchor, replacement, 1)

# Structure: remove labels that repeat the page/task and only reveal continuation when valid.
old = 'const body = `<div class="section-kicker">Structure</div><div class="structure-list"'
if old not in s:
    raise SystemExit("structure duplicate heading not found")
s = s.replace(old, 'const body = `<div class="structure-list"', 1)
old = '<div class="structure-ready-label">Finish structure</div>'
if old not in s:
    raise SystemExit("finish structure label not found")
s = s.replace(old, "", 1)
old = '<div class="structure-next-wrap"><button class="primary structure-next" data-action="go" data-route="tracks" ${done ? "" : "disabled"}>Next</button></div>'
new = '${done ? `<div class="structure-next-wrap"><button class="primary structure-next" data-action="go" data-route="tracks">Next</button></div>` : ""}'
if old not in s:
    raise SystemExit("structure next control not found")
s = s.replace(old, new, 1)

# Tracks: unavailable continuation should not occupy visual space.
old = '<div class="spacer-24"></div><button class="primary full" data-action="start-section-study" ${tracksDone(p) ? "" : "disabled"}>Next</button>'
new = '${tracksDone(p) ? `<div class="tracks-next-wrap"><button class="primary" data-action="start-section-study">Next</button></div>` : ""}'
if old not in s:
    raise SystemExit("tracks next control not found")
s = s.replace(old, new, 1)

app.write_text(s)

css = Path("styles.css")
c = css.read_text()

# Keep the 44pt hit target while making the Projects add affordance visually quiet.
old = '''  border: 1px solid var(--line);
  background: var(--surface-2);
  font-size: 24px;'''
new = '''  border: 0;
  background: transparent;
  font-size: 24px;'''
if old not in c:
    raise SystemExit("top icon style anchor not found")
c = c.replace(old, new, 1)

insert_after = '''.project-field-label {
  margin-top: 18px;
  margin-bottom: 8px;
  font-size: 12px;
  font-weight: 650;
  letter-spacing: 0;
  text-transform: none;
  color: var(--muted);
}
'''
additions = insert_after + '''#app[data-route="new-project"] .project-type-control + .field {
  margin-top: 18px;
}
.create-project-action {
  min-width: 170px;
  margin-top: 18px;
}
.checkpoint-locked-message {
  min-height: 52px;
  color: var(--muted);
}
.checkpoint-locked-message .title {
  color: var(--muted);
  font-weight: 560;
}
'''
if insert_after not in c:
    raise SystemExit("project field label style anchor not found")
c = c.replace(insert_after, additions, 1)

old = '''.structure-verify .action-card {
  background: var(--surface);
}
'''
new = '''.structure-verify {
  margin-top: 24px;
}
.structure-verify .action-card {
  background: var(--surface);
}
.tracks-next-wrap {
  display: flex;
  justify-content: flex-end;
  margin-top: 18px;
}
'''
if old not in c:
    raise SystemExit("structure verify style anchor not found")
c = c.replace(old, new, 1)

old = '''.structure-next-wrap {
  display: flex;
  justify-content: flex-end;
  margin-top: 24px;
}
'''
new = '''.structure-next-wrap {
  display: flex;
  justify-content: flex-end;
  margin-top: 18px;
}
'''
if old not in c:
    raise SystemExit("structure next style anchor not found")
c = c.replace(old, new, 1)

phone_anchor = '''  #app[data-route="roadmap"] .road-phase {
    padding: 11px 14px;
  }
'''
phone_replacement = phone_anchor + '''  #app[data-route="roadmap"] .road-phase.unimplemented {
    padding-top: 8px;
    padding-bottom: 8px;
  }
'''
if phone_anchor not in c:
    raise SystemExit("roadmap phone style anchor not found")
c = c.replace(phone_anchor, phone_replacement, 1)
css.write_text(c)

start = Path("START_HERE.md")
d = start.read_text()
anchor = '- **Adaptive composition is now a shared rule:** current/incomplete work stays expanded and visually dominant; completed work compresses into an editable summary that remains one tap away; future work stays quiet. The Map collapses completed Song Setup, Project makes the current-phase surface the action, and Roadmap reserves full detail for the current phase.\n'
addition = anchor + '- **Unavailable work-screen continuation controls should not occupy visual space.** Keep future journey destinations visible where they help orientation, but hide disabled Next-style actions until they can actually be used; remove headings that merely repeat the page or task.\n'
if anchor not in d:
    raise SystemExit("START_HERE adaptive rule anchor not found")
d = d.replace(anchor, addition, 1)
start.write_text(d)
