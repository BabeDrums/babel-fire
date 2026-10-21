export const SOURCE_KEY = "production-projects-v1";
export const PREVIEW_KEY = "production-projects-v1-v7-preview";

export const COMMON_TRACKS = [
  "Vocal",
  "Drums",
  "Bass",
  "Ukulele",
  "Guitar",
  "Piano",
  "Synth",
  "Backing vocals",
  "Percussion",
  "FX",
];

export const SECTION_TYPES = [
  "Intro",
  "Verse",
  "Pre-Chorus",
  "Chorus",
  "Bridge",
  "Instrumental",
  "Outro",
];

export const WORK = {
  setup: { title: "Song Setup", copy: "Prepare the reference before studying it." },
  structure: { title: "Structure", copy: "Build the song one section at a time." },
  tracks: { title: "Tracks", copy: "Choose everything you hear in the song." },
  "section-study": { title: "Section Study", copy: "Study what changes from section to section." },
  "review-map": { title: "Review Map", copy: "Review the song map before rebuilding it." },
};

const clean = (value) => String(value ?? "").trim();
const uid = () => crypto?.randomUUID?.() || `preview-${Date.now()}-${Math.random().toString(36).slice(2)}`;
const deepCopy = (value) => JSON.parse(JSON.stringify(value));

function seedDb() {
  const project = {
    id: "preview-creep",
    type: "study",
    schemaVersion: 5,
    title: "Creep",
    artist: "Radiohead",
    createdAt: Date.now(),
    notes: [],
    map: {
      setup: { reference: false, tempo: "", meter: "4/4", grid: false, firstListen: false },
      sections: [],
      structureVerified: false,
      tracks: [],
      timeline: { presence: [], events: [] },
      sectionData: {},
      mapVerified: false,
      teachBack: false,
      phaseParking: "",
      phaseTakeaway: "",
    },
    skeleton: {
      session: { tracks: {}, markers: {} },
      draft: { parts: {} },
      bounce: { exported: false, listened: false },
    },
  };
  return { version: 5, currentProjectId: project.id, projects: [project] };
}

function normalizeProject(project) {
  project.title = clean(project.title) || "Untitled";
  project.artist = clean(project.artist || "");
  project.notes = Array.isArray(project.notes) ? project.notes : [];
  if (project.type !== "study") return project;

  project.map = project.map || {};
  project.map.setup = {
    reference: !!project.map.setup?.reference,
    tempo: String(project.map.setup?.tempo || ""),
    meter: project.map.setup?.meter || "4/4",
    grid: !!project.map.setup?.grid,
    firstListen: !!project.map.setup?.firstListen,
  };
  project.map.sections = (Array.isArray(project.map.sections) ? project.map.sections : []).map((section) => ({
    id: section?.id || uid(),
    name: clean(section?.name) || "Section",
    lengthBars: Number(section?.lengthBars) || 8,
  }));
  project.map.structureVerified = !!project.map.structureVerified;
  project.map.tracks = (Array.isArray(project.map.tracks) ? project.map.tracks : [])
    .map((track) => typeof track === "string"
      ? { id: uid(), name: track }
      : { id: track?.id || uid(), name: clean(track?.name) })
    .filter((track) => track.name);
  project.map.timeline = project.map.timeline || { presence: [], events: [] };
  project.map.sectionData = project.map.sectionData || {};
  project.skeleton = project.skeleton || {
    session: { tracks: {}, markers: {} },
    draft: { parts: {} },
    bounce: { exported: false, listened: false },
  };
  return project;
}

function normalizeDb(candidate) {
  const db = candidate && Array.isArray(candidate.projects) ? candidate : seedDb();
  db.version = 5;
  db.projects = db.projects.map(normalizeProject);
  if (!db.projects.some((project) => project.id === db.currentProjectId)) {
    db.currentProjectId = db.projects[0]?.id || null;
  }
  return db;
}

export function cloneProductionDb() {
  try {
    const source = JSON.parse(localStorage.getItem(SOURCE_KEY));
    if (source && Array.isArray(source.projects) && source.projects.length) {
      return normalizeDb(deepCopy(source));
    }
  } catch (error) {}
  return seedDb();
}

export function loadDb() {
  if (new URLSearchParams(location.search).get("reset") === "1") {
    const fresh = cloneProductionDb();
    localStorage.setItem(PREVIEW_KEY, JSON.stringify(fresh));
    return fresh;
  }
  try {
    const saved = JSON.parse(localStorage.getItem(PREVIEW_KEY));
    if (saved && Array.isArray(saved.projects)) return normalizeDb(saved);
  } catch (error) {}
  const fresh = cloneProductionDb();
  localStorage.setItem(PREVIEW_KEY, JSON.stringify(fresh));
  return fresh;
}

export function saveDb(db) {
  localStorage.setItem(PREVIEW_KEY, JSON.stringify(db));
}

export function currentProject(db) {
  return db.projects.find((item) => item.id === db.currentProjectId) || null;
}

export function setupComplete(item) {
  if (item?.type !== "study") return false;
  const setup = item.map.setup;
  return !!setup.reference && Number(setup.tempo) > 0 && !!setup.meter && !!setup.grid && !!setup.firstListen;
}

export function structureComplete(item) {
  return !!item?.map?.structureVerified && (item?.map?.sections?.length || 0) > 0;
}

export function tracksComplete(item) {
  return (item?.map?.tracks?.length || 0) > 0;
}

export function recommendedWork(item) {
  if (!setupComplete(item)) return "setup";
  if (!structureComplete(item)) return "structure";
  if (!tracksComplete(item)) return "tracks";
  return "section-study";
}

export function workDone(item, route) {
  if (route === "setup") return setupComplete(item);
  if (route === "structure") return structureComplete(item);
  if (route === "tracks") return tracksComplete(item);
  return false;
}

export function projectMeta(item) {
  return item.type === "study"
    ? `${item.artist || "Unknown artist"} · Recreation`
    : `${item.artist || "Original"} · Original`;
}

export function resetPreviewProject(item) {
  if (item.type !== "study") return;
  const notes = deepCopy(item.notes || []);
  item.map = {
    setup: { reference: false, tempo: "", meter: "4/4", grid: false, firstListen: false },
    sections: [],
    structureVerified: false,
    tracks: [],
    timeline: { presence: [], events: [] },
    sectionData: {},
    mapVerified: false,
    teachBack: false,
    phaseParking: "",
    phaseTakeaway: "",
  };
  item.skeleton = {
    session: { tracks: {}, markers: {} },
    draft: { parts: {} },
    bounce: { exported: false, listened: false },
  };
  item.notes = notes;
}

export const helpers = { clean, uid, deepCopy };
