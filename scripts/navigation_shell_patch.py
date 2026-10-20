from pathlib import Path


def replace_once(text, old, new, label):
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"{label}: expected 1 match, found {count}")
    return text.replace(old, new, 1)


app_path = Path("app.js")
app = app_path.read_text()

app = replace_once(
    app,
    '  let saveFlashTimer = null;\n  let sheetClearTimer = null;\n',
    '  let saveFlashTimer = null;\n  let sheetClearTimer = null;\n  let routeMotion = "";\n',
    "route motion state",
)

app = replace_once(
    app,
    '''    const fromRoute = ui.route,\n      fromLabel = routeLabel(fromRoute);\n    ui = { ...ui, ...extra, route };\n''',
    '''    const fromRoute = ui.route,\n      fromLabel = routeLabel(fromRoute);\n    routeMotion =\n      fromRoute === "projects" && route === "new-project"\n        ? "route-forward"\n        : fromRoute === "new-project" && route === "projects"\n          ? "route-back"\n          : "";\n    ui = { ...ui, ...extra, route };\n''',
    "go motion direction",
)

app = replace_once(
    app,
    '''  window.addEventListener("popstate", (e) => {\n    cancelGesture?.();\n    clearBoundarySelection();\n    closeSheet();\n    const st = e.state || {};\n    if (st.projectId && db.projects.some((p) => p.id === st.projectId))\n      db.currentProjectId = st.projectId;\n    ui = { ...ui, ...st, route: st.route || "projects", animating: false };\n    render();\n    window.scrollTo(0, 0);\n  });\n''',
    '''  window.addEventListener("popstate", (e) => {\n    cancelGesture?.();\n    clearBoundarySelection();\n    closeSheet();\n    const st = e.state || {},\n      fromRoute = ui.route,\n      route = st.route || "projects";\n    if (st.projectId && db.projects.some((p) => p.id === st.projectId))\n      db.currentProjectId = st.projectId;\n    routeMotion =\n      fromRoute === "new-project" && route === "projects"\n        ? "route-back"\n        : fromRoute === "projects" && route === "new-project"\n          ? "route-forward"\n          : "";\n    ui = { ...ui, ...st, route, animating: false };\n    render();\n    window.scrollTo(0, 0);\n  });\n''',
    "popstate motion direction",
)

app = replace_once(
    app,
    '''  function topbar(left = "", center = "", right = "") {\n    // Canvas size follows content, not the user's device or input method.\n    app.dataset.route = ui.route;\n    app.dataset.layout = ui.route === "section-study" ? "arrangement"\n      : ui.route === "skeleton-draft" ? "draft"\n      : ["new-project", "original-spark", "skeleton-bounce", "skeleton"].includes(ui.route) ? "focused" : "overview";\n    return `<div class="topbar"><div class="left">${left}</div><div class="center">${center}</div><div class="right">${right}</div></div>`;\n  }\n''',
    '''  function topbar(left = "", center = "", right = "") {\n    // Canvas size follows content, not the user's device or input method.\n    app.dataset.route = ui.route;\n    app.dataset.layout = ui.route === "section-study" ? "arrangement"\n      : ui.route === "skeleton-draft" ? "draft"\n      : ["new-project", "original-spark", "skeleton-bounce", "skeleton"].includes(ui.route) ? "focused" : "overview";\n    return `<div class="topbar"><div class="left">${left}</div><div class="center">${center}</div><div class="right">${right}</div></div>`;\n  }\n  function projectPageMotionClass() {\n    return routeMotion ? ` ${routeMotion}` : "";\n  }\n''',
    "project page motion helper",
)

start = app.index("  function renderProjects() {")
end = app.index("  function renderProject() {", start)
app = app[:start] + '''  function renderProjects() {\n    app.innerHTML =\n      topbar(\n        "",\n        "",\n        `<button class="top-icon-btn" data-action="new-project" aria-label="New project"><span aria-hidden="true">+</span></button>`,\n      ) +\n      `<main class="project-page${projectPageMotionClass()}"><header class="page-heading"><h1>Projects</h1><p class="sub">Original songs and recreations.</p></header><div class="projects-grid">${\n        db.projects.length\n          ? db.projects\n              .map((p) => {\n                const phase =\n                  p.type === "study"\n                    ? STUDY_PHASES[currentStudyPhaseIndex(p)].title\n                    : originalSparkDone(p)\n                      ? "The Direction"\n                      : "The Spark";\n                return `<div class="project-card"><button class="project-open" data-action="open-project" data-id="${p.id}"><div class="type">${p.type === "study" ? "Recreation" : "Original Song"}</div><strong>${esc(p.title)}</strong>${p.artist ? `<div class="artist">${esc(p.artist)}</div>` : ""}<div class="foot"><span>${esc(phase)}</span><span aria-hidden="true">›</span></div></button><button class="project-menu" data-action="project-menu" data-id="${p.id}" aria-label="Project options">…</button></div>`;\n              })\n              .join("")\n          : ""\n      }</div></main><footer id="buildStamp" class="build-stamp">FIRE V6 DEV · …</footer>`;\n    showBuildStamp();\n  }\n''' + app[end:]

start = app.index("  function renderNewProject() {")
end = app.index("\n\n  function checkpointRow", start)
app = app[:start] + '''  function renderNewProject() {\n    app.innerHTML =\n      topbar(backButton("projects", "Projects"), "", "") +\n      `<main class="project-page${projectPageMotionClass()}"><header class="page-heading"><h1>New project</h1><p class="sub">Start original or rebuild a reference.</p></header><div class="project-type-control" role="group" aria-label="Project type"><button class="segment-choice ${ui.newType === "original" ? "selected" : ""}" data-action="set-new-type" data-type="original" aria-pressed="${ui.newType === "original"}">Original</button><button class="segment-choice ${ui.newType === "study" ? "selected" : ""}" data-action="set-new-type" data-type="study" aria-pressed="${ui.newType === "study"}">Recreation</button></div><div class="section-kicker project-field-label">Project</div><input class="field" id="newTitle" aria-label="Song title" enterkeyhint="next" autocomplete="off" autocapitalize="words" placeholder="Song title"><input class="field custom-length" id="newArtist" aria-label="Artist" enterkeyhint="done" autocomplete="off" autocapitalize="words" placeholder="Artist"><div class="spacer-24"></div><button class="primary full" data-action="create-project">Create Project</button></main>`;\n  }\n''' + app[end:]

app_path.write_text(app)

styles_path = Path("styles.css")
styles = styles_path.read_text()

old_shell = '''#app[data-route="projects"] {\n  --canvas-width: 880px;\n}\n.projects-heading {\n  display: flex;\n  align-items: flex-end;\n  justify-content: space-between;\n  gap: var(--space-4);\n  width: 100%;\n  max-width: 760px;\n  margin-bottom: var(--space-5);\n}\n.projects-heading > div {\n  min-width: 0;\n}\n.projects-heading h1 {\n  margin: 0 0 7px;\n}\n.projects-grid {\n  display: grid;\n  grid-template-columns: 1fr;\n  gap: 10px;\n  max-width: 760px;\n}\n.projects-grid > .project-card {\n  margin-bottom: 0;\n}\n'''
new_shell = '''#app[data-route="projects"],\n#app[data-route="new-project"] {\n  --canvas-width: 880px;\n}\n#app[data-route="projects"] > .topbar,\n#app[data-route="new-project"] > .topbar,\n.project-page {\n  width: 100%;\n  max-width: 760px;\n}\n.project-page {\n  min-width: 0;\n}\n.project-page .page-heading {\n  margin: 0 0 var(--space-5);\n}\n.project-page .page-heading h1 {\n  margin: 0 0 7px;\n}\n.projects-grid {\n  display: grid;\n  grid-template-columns: 1fr;\n  gap: 10px;\n  max-width: none;\n}\n.projects-grid > .project-card {\n  margin-bottom: 0;\n}\n.project-page.route-forward {\n  animation: routeForwardIn var(--motion-standard) var(--ease);\n}\n.project-page.route-back {\n  animation: routeBackIn var(--motion-standard) var(--ease);\n}\n'''
styles = replace_once(styles, old_shell, new_shell, "shared navigation shell styles")

styles = replace_once(
    styles,
    '''@keyframes sheetIn {\n''',
    '''@keyframes routeForwardIn {\n  from {\n    opacity: 0.82;\n    transform: translateX(8px);\n  }\n  to {\n    opacity: 1;\n    transform: translateX(0);\n  }\n}\n@keyframes routeBackIn {\n  from {\n    opacity: 0.82;\n    transform: translateX(-8px);\n  }\n  to {\n    opacity: 1;\n    transform: translateX(0);\n  }\n}\n\n@keyframes sheetIn {\n''',
    "route motion keyframes",
)

styles = replace_once(
    styles,
    '''@media (max-width: 430px) {\n  .projects-heading {\n    align-items: center;\n    margin-bottom: 20px;\n  }\n  .projects-heading h1 {\n    font-size: 34px;\n    line-height: 1.04;\n  }\n  .project-open {\n''',
    '''@media (max-width: 430px) {\n  .project-page .page-heading {\n    margin-bottom: 20px;\n  }\n  .project-page .page-heading h1 {\n    font-size: 34px;\n    line-height: 1.04;\n  }\n  .project-open {\n''',
    "mobile shared heading",
)

styles_path.write_text(styles)

tests_path = Path("tests/test_v6.py")
tests = tests_path.read_text()
method_start = tests.index("    def test_projects_foundation_and_new_project_keyboard_flow(self):")
method_end = tests.index("    def test_revisioned_assets_and_development_stamp(self):", method_start)
new_test = '''    def test_projects_navigation_shell_and_new_project_keyboard_flow(self):\n        for width in [320, 390, 430, 820, 1180]:\n            with self.subTest(width=width):\n                self.open('projects', width=width, pointer=width >= 1180)\n                self.assertLessEqual(self.page.evaluate('document.documentElement.scrollWidth'), width)\n                self.assertEqual(self.page.locator('.topbar').count(), 1)\n                self.assertEqual(self.page.locator('.pill-tag').count(), 0)\n                add = self.page.locator('.topbar .right [data-action="new-project"]')\n                box = add.bounding_box()\n                self.assertGreaterEqual(box['width'], 44)\n                self.assertGreaterEqual(box['height'], 44)\n                card = self.page.locator('.project-card').first.bounding_box()\n                shell = self.page.locator('.project-page').bounding_box()\n                toolbar = self.page.locator('.topbar').bounding_box()\n                title = self.page.locator('.page-heading h1').bounding_box()\n                subtitle = self.page.locator('.page-heading .sub').bounding_box()\n                self.assertLessEqual(card['height'], 140)\n                self.assertLess(abs((box['x'] + box['width']) - (card['x'] + card['width'])), 1.1)\n                self.assertLess(abs(shell['x'] - card['x']), 1.1)\n                self.assertLess(abs((shell['x'] + shell['width']) - (card['x'] + card['width'])), 1.1)\n                self.assertLess(abs(toolbar['x'] - shell['x']), 1.1)\n                self.assertLess(abs(toolbar['width'] - shell['width']), 1.1)\n                self.assertEqual(self.page.locator('.project-menu').first.text_content().strip(), '…')\n                self.assertEqual(self.page.locator('.project-open .foot > span:last-child').first.text_content().strip(), '›')\n\n                self.click('new-project')\n                expect(self.page.locator('.page-heading h1')).to_have_text('New project')\n                self.assertEqual(self.page.locator('.topbar .left [data-action="history-back"]').count(), 1)\n                self.assertEqual(self.page.locator('.topbar [data-action="new-project"]').count(), 0)\n                self.assertEqual(self.page.locator('.project-page.route-forward').count(), 1)\n                new_shell = self.page.locator('.project-page').bounding_box()\n                new_toolbar = self.page.locator('.topbar').bounding_box()\n                new_title = self.page.locator('.page-heading h1').bounding_box()\n                new_subtitle = self.page.locator('.page-heading .sub').bounding_box()\n                segmented = self.page.locator('.project-type-control').bounding_box()\n                self.assertLess(abs(new_shell['x'] - shell['x']), 1.1)\n                self.assertLess(abs(new_shell['width'] - shell['width']), 1.1)\n                self.assertLess(abs(new_toolbar['x'] - toolbar['x']), 1.1)\n                self.assertLess(abs(new_toolbar['width'] - toolbar['width']), 1.1)\n                self.assertLess(abs(new_title['y'] - title['y']), 1.1)\n                self.assertLess(abs(new_subtitle['y'] - subtitle['y']), 1.1)\n                self.assertLess(abs(segmented['y'] - card['y']), 1.1)\n                if width >= 1180:\n                    self.assertLessEqual(shell['width'], 760.1)\n                    self.assertLessEqual(card['width'], 760.1)\n\n                self.page.locator('[data-action="history-back"]').click()\n                expect(self.page.locator('.page-heading h1')).to_have_text('Projects')\n                self.assertEqual(self.page.locator('.project-page.route-back').count(), 1)\n                self.context.close()\n\n        self.open('projects', width=390, data={'version':5,'currentProjectId':None,'projects':[]})\n        self.assertEqual(self.page.locator('.empty').count(), 0)\n        self.assertEqual(self.page.get_by_text('No projects yet. Tap + to start one.').count(), 0)\n        self.context.close()\n\n        self.open('projects', width=390)\n        self.click('new-project')\n        self.assertEqual(self.page.locator('.topbar .center .pill-tag').count(), 0)\n        segments = self.page.locator('.project-type-control .segment-choice')\n        self.assertEqual(segments.count(), 2)\n        for i in range(segments.count()):\n            self.assertGreaterEqual(segments.nth(i).bounding_box()['height'], 44)\n        self.assertEqual(self.page.locator('#newTypeDescription').count(), 0)\n        self.assertEqual(self.page.get_by_text('Start with anything worth keeping.').count(), 0)\n        self.click('set-new-type', '[data-type="study"]')\n        self.assertEqual(self.page.get_by_text('Rebuild an existing song to learn how it works.').count(), 0)\n        title = self.page.locator('#newTitle')\n        artist = self.page.locator('#newArtist')\n        self.assertEqual(title.get_attribute('enterkeyhint'), 'next')\n        self.assertEqual(artist.get_attribute('enterkeyhint'), 'done')\n        self.assertEqual(title.get_attribute('autocapitalize'), 'words')\n        self.assertEqual(artist.get_attribute('autocapitalize'), 'words')\n        title.fill('Enter Flow')\n        title.press('Enter')\n        expect(artist).to_be_focused()\n        artist.fill('Babel')\n        artist.press('Enter')\n        expect(self.page.locator('h1')).to_have_text('Enter Flow')\n        saved = self.db()\n        created = next(p for p in saved['projects'] if p['title'] == 'Enter Flow')\n        self.assertEqual(created['artist'], 'Babel')\n        self.assertEqual(created['schemaVersion'], 5)\n\n'''
tests = tests[:method_start] + new_test + tests[method_end:]
tests = replace_once(
    tests,
    "                        if route in ['new-project','skeleton-bounce','skeleton']:\n                            self.assertLessEqual(self.page.locator('#app').bounding_box()['width'],760)\n",
    "                        if route in ['skeleton-bounce','skeleton']:\n                            self.assertLessEqual(self.page.locator('#app').bounding_box()['width'],760)\n                        if route=='new-project':\n                            self.assertLessEqual(self.page.locator('#app').bounding_box()['width'],880)\n",
    "new project canvas width",
)
tests_path.write_text(tests)
