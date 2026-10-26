export const CORE_KEY = "production-projects-v1-v7-core-proof";

const now = () => Date.now();
const clean = (value) => String(value ?? "").trim();
const deepCopy = (value) => JSON.parse(JSON.stringify(value));

const COVER_SEQUENCE = [
  {
    domain: "Arrangement & Roles",
    title: "Prove the verse → chorus lift before matching tone",
    why: "The reference gets much of its impact from a change in role, density, and energy. Chasing exact guitar tone before that contrast exists would be downstream work.",
    experiment: "In Logic, rough in one verse and the first chorus with placeholder or fast-to-build sounds. Match the major roles and the density change first. Keep levels rough and do not chase plugins. Listen straight through once.",
    alternate: "Strip the rough to vocal, drums, bass, and the main guitar role. Rebuild only the parts that clearly increase the chorus lift. Ignore tone matching until the contrast is obvious.",
  },
  {
    domain: "Source & Performance",
    title: "Make the chorus source carry the lift before processing it",
    why: "Now that the section contrast exists, the next leverage is whether the actual source and performance create the weight and aggression the chorus needs without relying on mix rescue.",
    experiment: "Choose one chorus guitar part and test two source/performance versions with minimal processing: one closer to the verse behavior and one intentionally heavier or more forceful. Level-match them and keep the version that creates the stronger lift in context.",
    alternate: "Before adding processing, change only the performance/source variables you can control—attack, register, voicing, doubling, or source choice—and compare them at the same loudness.",
  },
  {
    domain: "Balance & Hierarchy",
    title: "Make the chorus hierarchy obvious before deeper mix work",
    why: "The important parts now exist. FIRE needs the listener to understand what is foreground, what supports it, and how the guitar weight relates to the vocal before tone and space become the highest-value work.",
    experiment: "Reset the chorus to a simple static balance. With no new processing, set vocal, drums, bass, and guitars so the focal hierarchy reads clearly at low monitoring level. Pan only where it helps the roles separate.",
    alternate: "Turn the monitor level down until the mix is barely audible. Adjust only faders and pan until the vocal and section lift remain obvious without one support element swallowing the rest.",
  },
  {
    domain: "Tone & Dynamics",
    title: "Shape only the behavior the rough balance still cannot solve",
    why: "Arrangement, source, and hierarchy are now doing their jobs. Processing is justified only for problems that remain after those upstream decisions are carrying their share.",
    experiment: "Pick the single most distracting tonal or dynamic mismatch against the reference. Make one targeted processing move whose job you can name, then level-match before/after and keep it only if the relationship improves in context.",
    alternate: "Bypass the processing on the element you are about to change. Describe the one behavior that still blocks the target, then use the smallest EQ/compression/saturation move that addresses only that behavior.",
  },
];

const EVEN_SEQUENCE = [
  {
    domain: "Arrangement & Roles",
    title: "Prove the emotional escalation before polishing sounds",
    why: "Even is supposed to begin playful and slightly off-balance, then expose frustration and vulnerability until the record feels like a real plea to be heard. The production should prove that arc before detailed sound polish.",
    experiment: "In Logic, make the roughest playable skeleton that lets you hear the Verse → Pre-Chorus → Chorus and one later high-energy moment such as the Rap or Reprise. Use existing parts or placeholders. Make the change in density, urgency, and focal roles readable without chasing mix quality.",
    alternate: "Mute everything nonessential and rebuild those sections using only the parts required to communicate playful → urgent. Add one role at a time only when it strengthens that emotional turn.",
  },
  {
    domain: "Source & Performance",
    title: "Keep the intimate core while the record opens up",
    why: "The arrangement arc is present. The next risk is that added production makes the song bigger by replacing its intimate ukulele-rooted identity instead of expanding around it.",
    experiment: "Choose one section where the production opens up. Keep the core ukulele/vocal relationship intact, then audition one supporting source or performance choice at a time. Keep only additions that increase urgency without making the song feel emotionally farther away.",
    alternate: "Solo the intimate core, then add the supporting elements back one by one. For each addition, ask whether it increases urgency, support, or contrast. Remove anything whose job is unclear.",
  },
  {
    domain: "Balance & Hierarchy",
    title: "Let urgency grow without burying the plea",
    why: "The record can get bigger without letting the emotional focal point disappear. Balance should preserve the sense that the vocal is becoming more exposed, not merely surrounded by louder production.",
    experiment: "Build a static balance across one earlier section and one later urgent section. Do not add new processing. Make the later section feel larger while keeping the vocal emotionally forward enough that the lyric still reads as the reason the production is growing.",
    alternate: "Turn the mix down and compare the early and late sections. Use only faders and pan until the later section gains scale without the vocal losing its place as the emotional center.",
  },
  {
    domain: "Space & Movement",
    title: "Use movement to reveal vulnerability, not decorate it",
    why: "The core hierarchy is working. Space and automation can now help the song move from playful imbalance toward urgency without becoming generic production motion.",
    experiment: "Choose one transition into a more vulnerable or urgent section. Test one spatial or automation move with a named job—pull the vocal closer, open width, change ambience, or create a brief drop—then keep it only if the emotional turn becomes clearer.",
    alternate: "Remove one existing spatial/movement idea from the transition, listen once, then add back only the single motion that most clearly strengthens the emotional change.",
  },
];

const GENERIC_ORIGINAL_SEQUENCE = [
  {
    domain: "Material & Form",
    title: "Make enough of the song real to expose the next production decision",
    why: "FIRE does not need a perfect brief. It needs enough real musical evidence to stop guessing about what deserves attention next.",
    experiment: "In Logic, build the roughest 60–90 second version that contains the material you actually care about. Use placeholders freely. Do not polish; make the idea audible enough to reveal what is missing or fighting.",
    alternate: "Reduce the idea to the smallest playable version that still feels like the song, then add only one missing role at a time until the next production problem becomes obvious.",
  },
  ...EVEN_SEQUENCE.slice(0, 3),
];

const GENERIC_COVER_SEQUENCE = [
  {
    domain: "Material & Form",
    title: "Map enough of the reference to stop guessing",
    why: "Before matching sound, FIRE needs a usable picture of the song's form and the moments that create its identity.",
    experiment: "In Logic, mark the main sections and rough tempo, then build one representative section transition with placeholders. Capture the musical skeleton and major role changes before chasing sound.",
    alternate: "Ignore individual tones. Listen to the reference once for only section boundaries and major entries/exits, then reproduce that skeleton with the fastest available sounds.",
  },
  ...COVER_SEQUENCE.slice(0, 3),
];

function coreState(target = "", firstDomain = "Material & Form") {
  return {
    target: clean(target),
    stage: 0,
    lastOutcome: "",
    revealedNote: "",
    history: [],
    mapState: { [firstDomain]: "active" },
  };
}

function projectSeed({ id, type, title, artist, target, referenceBias = "" }) {
  const timestamp = now();
  const sequence = type === "study" ? COVER_SEQUENCE : EVEN_SEQUENCE;
  return {
    id,
    type,
    title,
    artist,
    referenceBias,
    createdAt: timestamp,
    lastActivityAt: timestamp,
    core: coreState(target, sequence[0].domain),
  };
}

export function seedDb() {
  const creep = projectSeed({
    id: "core-creep",
    type: "study",
    title: "Creep",
    artist: "Radiohead",
    referenceBias: "Match",
    target: "Recreate the reference closely enough that its defining verse-to-chorus contrast and major production relationships feel convincing before chasing exact sonic details.",
  });
  const even = projectSeed({
    id: "core-even",
    type: "original",
    title: "Even",
    artist: "Babel",
    target: "Start playful and slightly off-balance, then reveal frustration and vulnerability until the record feels like a genuine plea to be heard. Keep the intimate ukulele-rooted core while the production grows more urgent.",
  });
  return { version: 1, currentProjectId: creep.id, projects: [creep, even] };
}

function sequenceFor(project) {
  if (project?.id === "core-creep") return COVER_SEQUENCE;
  if (project?.id === "core-even") return EVEN_SEQUENCE;
  return project?.type === "study" ? GENERIC_COVER_SEQUENCE : GENERIC_ORIGINAL_SEQUENCE;
}

function normalizeProject(project) {
  project.type = project.type === "study" ? "study" : "original";
  project.title = clean(project.title) || "Untitled";
  project.artist = clean(project.artist);
  project.referenceBias = clean(project.referenceBias);
  project.createdAt = Number(project.createdAt) || now();
  project.lastActivityAt = Number(project.lastActivityAt) || project.createdAt;
  const sequence = sequenceFor(project);
  project.core = project.core && typeof project.core === "object" ? project.core : coreState("", sequence[0].domain);
  project.core.target = clean(project.core.target);
  project.core.stage = Math.max(0, Math.min(Number(project.core.stage) || 0, sequence.length - 1));
  project.core.lastOutcome = clean(project.core.lastOutcome);
  project.core.revealedNote = clean(project.core.revealedNote);
  project.core.history = Array.isArray(project.core.history) ? project.core.history : [];
  project.core.mapState = project.core.mapState && typeof project.core.mapState === "object" ? project.core.mapState : {};
  if (!Object.keys(project.core.mapState).length) project.core.mapState[sequence[project.core.stage].domain] = "active";
  return project;
}

function normalizeDb(candidate) {
  const db = candidate && Array.isArray(candidate.projects) ? candidate : seedDb();
  db.version = 1;
  db.projects = db.projects.map(normalizeProject);
  if (!db.projects.some((project) => project.id === db.currentProjectId)) db.currentProjectId = db.projects[0]?.id || null;
  return db;
}

export function loadDb() {
  const params = new URLSearchParams(location.search);
  if (params.get("reset") === "1") {
    const fresh = seedDb();
    localStorage.setItem(CORE_KEY, JSON.stringify(fresh));
    return fresh;
  }
  try {
    const saved = JSON.parse(localStorage.getItem(CORE_KEY));
    if (saved && Array.isArray(saved.projects)) return normalizeDb(saved);
  } catch (error) {}
  const fresh = seedDb();
  localStorage.setItem(CORE_KEY, JSON.stringify(fresh));
  return fresh;
}

export function saveDb(db) {
  localStorage.setItem(CORE_KEY, JSON.stringify(db));
}

export function currentProject(db) {
  return db.projects.find((project) => project.id === db.currentProjectId) || null;
}

export function projectMeta(project) {
  if (project.type === "study") {
    const label = project.artist ? `${project.artist} · Cover` : "Cover";
    return project.referenceBias ? `${label} · ${project.referenceBias}` : label;
  }
  return project.artist ? `${project.artist} · Original` : "Original";
}

export function deriveActiveFocus(project) {
  const sequence = sequenceFor(project);
  const index = Math.max(0, Math.min(project.core.stage, sequence.length - 1));
  const base = sequence[index];
  if (project.core.revealedNote) {
    return {
      domain: base.domain,
      title: "Follow the new evidence before continuing the route",
      why: `Your last experiment revealed: ${project.core.revealedNote} New evidence outranks the planned next step, so FIRE should investigate the smallest decision that could explain it before investing farther downstream.`,
      experiment: "In Logic, isolate the revealed issue with the fewest elements possible. Change only one upstream variable that could plausibly cause it, then return with what changed.",
      state: "reopened",
    };
  }
  const retry = project.core.lastOutcome === "didnt-help";
  return {
    ...base,
    why: retry ? `The first experiment did not move this enough. That does not automatically mean the domain is wrong; it means FIRE needs a cheaper alternate test before escalating. ${base.why}` : base.why,
    experiment: retry ? base.alternate : base.experiment,
    state: project.core.mapState[base.domain] || "active",
  };
}

export function applyEvaluation(project, outcome, note = "") {
  const allowed = new Set(["helped", "didnt-help", "revealed"]);
  if (!project || !allowed.has(outcome)) return false;
  const sequence = sequenceFor(project);
  const focus = deriveActiveFocus(project);
  const timestamp = now();
  project.core.history.push({
    id: `result-${timestamp}-${Math.random().toString(36).slice(2, 8)}`,
    at: timestamp,
    domain: focus.domain,
    title: focus.title,
    experiment: focus.experiment,
    outcome,
    note: clean(note),
  });

  if (outcome === "helped") {
    project.core.mapState[focus.domain] = "provisionally-stable";
    project.core.revealedNote = "";
    project.core.lastOutcome = "helped";
    if (project.core.stage < sequence.length - 1) project.core.stage += 1;
    const next = sequence[project.core.stage];
    if (next && project.core.mapState[next.domain] !== "provisionally-stable") project.core.mapState[next.domain] = "active";
  } else if (outcome === "didnt-help") {
    project.core.mapState[focus.domain] = "active";
    project.core.revealedNote = "";
    project.core.lastOutcome = "didnt-help";
  } else {
    project.core.mapState[focus.domain] = "reopened";
    project.core.revealedNote = clean(note) || "The experiment exposed a different issue that needs diagnosis first.";
    project.core.lastOutcome = "revealed";
  }

  project.lastActivityAt = timestamp;
  return true;
}

export function resetCoreProject(project) {
  if (!project) return;
  const original = seedDb().projects.find((candidate) => candidate.id === project.id);
  const sequence = sequenceFor(project);
  project.core = original ? deepCopy(original.core) : coreState(project.core?.target || "", sequence[0].domain);
  project.lastActivityAt = now();
}

export function stateLabel(value) {
  if (value === "provisionally-stable") return "Stable for now";
  if (value === "reopened") return "Reopened";
  if (value === "active") return "Active";
  return "Not assessed";
}
