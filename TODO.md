# TODO — Echoes of Fate

Concrete, actionable work items. Check items off as they're done; move
finished large items into commit history rather than leaving them checked
here forever. See `PLAN.md` for the reasoning behind these, `TASK.md` for
what's actively being worked on right now.

Goal: expand from the original 13-chapter/~50-page draft to **26
chapters, ~200 pages** (see `manuscript/outline.md`).

## Story decisions (were blocking further chapter writing)

- [x] Decide whether Liam is Olivia's son — confirmed, yes
- [x] Define the concrete mechanism that connects all six characters — the
      cold case of Michael's brother Daniel's disappearance (see
      `characters/README.md`)
- [x] Set the story's timeframe — six weeks, early autumn, culminating at
      the Harvest Festival

## Project infrastructure

- [x] Reorganize repo into `manuscript/`, `characters/`, `scenes/`,
      `research/`, `archive/`
- [x] Write `AGENTS.md`, `PLAN.md`, `TODO.md`, `IDEA.md`, `TASK.md`
- [x] Expand `manuscript/outline.md` to the 26-chapter/~200-page structure
- [x] Design and document core workflows in `docs/workflows/`
- [x] Build `tests/test_manuscript.py` automated consistency checks and get
      them passing (15 checks, all green —
      `python3 -m unittest discover -s tests`)
- [ ] Reconcile the character-development agent's and plot-research agent's
      output into `characters/*.md`, `scenes/plot-map.md`, and
      `manuscript/outline.md` once both finish (check for contradictions)
- [ ] Resolve any new open questions those two agents raise in
      `characters/README.md`

## Craft / research (ongoing)

- [x] Research literary styles/techniques relevant to this draft's known
      problems (`research/show-dont-tell.md`,
      `research/multi-pov-structure.md`, `research/voice-differentiation.md`,
      `research/pacing-and-chapter-length.md`, `research/dialogue-craft.md`)
- [ ] Research mystery-plotting and subplot-weaving technique
      (`research/mystery-plotting.md`, `research/subplot-weaving.md` — in
      progress via plot-research agent)
- [x] Write a short style guide (POV, tense, target chapter length) —
      `manuscript/style-guide.md`, assembled from the `research/` notes
- [ ] Deepen `characters/*.md` (backstory, voice, physical detail, flaw,
      internal vs. external want) — in progress via character-development
      agent

## Writing — 26 chapters (see `manuscript/outline.md` for POV/summary per chapter)

- [ ] Ch. 1 — "Six Lives, One Town" (rewrite existing draft — see below)
- [ ] Ch. 2 — "What the Morning Hides"
- [ ] Ch. 3 — "The Artist and the Stranger"
- [ ] Ch. 4 — "A Name Across the Room"
- [ ] Ch. 5 — "The Ledger"
- [ ] Ch. 6 — "What Emma Won't Say"
- [ ] Ch. 7 — "Cold Case"
- [ ] Ch. 8 — "Echoes of the Unsolved"
- [ ] Ch. 9 — "Two Jobs, One Boy"
- [ ] Ch. 10 — "The Notebook"
- [ ] Ch. 11 — "Six Crossings"
- [ ] Ch. 12 — "Paths That Shouldn't Cross"
- [ ] Ch. 13 — "Digging Deeper"
- [ ] Ch. 14 — "What the File Says"
- [ ] Ch. 15 — "Closer"
- [ ] Ch. 16 — "The Line Olivia Won't Cross"
- [ ] Ch. 17 — "What Sarah Finds Out"
- [ ] Ch. 18 — "The Weight of It"
- [ ] Ch. 19 — "Webs"
- [ ] Ch. 20 — "Liam's Reckoning"
- [ ] Ch. 21 — "Alliances"
- [ ] Ch. 22 — "Fault Lines"
- [ ] Ch. 23 — "The Gathering Storm"
- [ ] Ch. 24 — "Reckoning"
- [ ] Ch. 25 — "What's Left Standing"
- [ ] Ch. 26 — "Echoes of Fate"

Old Chapter 1 draft (`manuscript/chapters/chapter-01.md`) is a
six-paragraph introduction montage covering what's now split across
Chapters 1-2 — it needs a full rewrite/split, not just a copy, per
`docs/workflows/chapter-drafting.md`.

## Publishing (`docs/`)

- [ ] Once Chapter 1 is rewritten, update `docs/ch01.html` to match (or
      switch to a generated approach — see `docs/workflows/publishing.md`)
- [ ] `docs/index.html` is a placeholder landing page — give it real
      content (title, blurb, chapter links) once there are a few chapters
      worth linking to
