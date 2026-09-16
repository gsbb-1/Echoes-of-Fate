# TODO — Echoes of Fate

Concrete, actionable work items. Check items off as they're done; move
finished large items into commit history rather than leaving them checked
here forever. See `PLAN.md` for the reasoning behind these, `TASK.md` for
what's actively being worked on right now.

Goal: expand from the original 13-chapter/~50-page draft to **26
chapters, ~200 pages** (see `manuscript/outline.md`).

**18 of 26 chapters drafted (Ch. 1-18) as of 2026-09-16.** All
planning/design infrastructure below is done; only the "Writing" section
has open items. See `TASK.md` for the exact resume point and `PLAN.md`
for the full state of the project.

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
      them passing (23 checks, all green —
      `python3 -m unittest discover -s tests`)
- [x] Reconcile the character-development agent's and plot-research agent's
      output — found and fixed a real naming conflict (the plot-research
      agent independently invented "Whitfield/Gerald"/"Daniel Cole"; renamed
      to match the character files' established "Hale/Warren"/"Daniel Voss"),
      plus a genuine backstory conflict on Sarah's family (merged into one
      consistent version). Updated all `characters/*.md` open-question notes,
      `characters/README.md`, and enriched `manuscript/outline.md`'s chapter
      summaries with the concrete plot-map facts. Added a regression test
      (`TestPlotMap`) so this class of drift gets caught automatically next
      time.
- [x] Resolve any new open questions those two agents raise in
      `characters/README.md` — all four resolved (Jack's case, what Olivia
      saw, Sarah's fragment, Daniel's land-dispute rumor)

## Craft / research (ongoing)

- [x] Research literary styles/techniques relevant to this draft's known
      problems (`research/show-dont-tell.md`,
      `research/multi-pov-structure.md`, `research/voice-differentiation.md`,
      `research/pacing-and-chapter-length.md`, `research/dialogue-craft.md`)
- [x] Research mystery-plotting and subplot-weaving technique —
      `research/mystery-plotting.md`, `research/subplot-weaving.md`
- [x] Write a short style guide (POV, tense, target chapter length) —
      `manuscript/style-guide.md`, assembled from the `research/` notes
- [x] Deepen `characters/*.md` (backstory, voice, physical detail, flaw,
      internal vs. external want, cross-character relationships) — done
      for all six characters
- [x] Design the mystery's beat-by-beat plot map — `scenes/plot-map.md`
      (what happened to Daniel, the evidence, the reveal order, one red
      herring, one foreshadowing plant)

## Writing — 26 chapters (see `manuscript/outline.md` for POV/summary per chapter)

- [x] Ch. 1 — "Six Lives, One Town" (rewritten as three real scenes —
      Sarah, Jack, Olivia — replacing the old six-paragraph montage)
- [x] Ch. 2 — "What the Morning Hides" (Michael, Emma, Liam)
- [x] Ch. 3 — "The Artist and the Stranger"
- [x] Ch. 4 — "A Name Across the Room" (first dialogue-heavy chapter)
- [x] Ch. 5 — "The Ledger"
- [x] Ch. 6 — "What Emma Won't Say"
- [x] Ch. 7 — "Cold Case"
- [x] Ch. 8 — "Echoes of the Unsolved"
- [x] Ch. 9 — "Two Jobs, One Boy" (last POV, Olivia, to get her own chapter)
- [x] Ch. 10 — "The Notebook" (Liam holds two images that don't yet mean anything to him)
- [x] Ch. 11 — "Six Crossings" (ensemble: all six make a first active decision)
- [x] Ch. 12 — "Paths That Shouldn't Cross" (coincidence resolves into choice at the parcel gate)
- [x] Ch. 13 — "Digging Deeper" (Jack: unpermitted regrade confirmed; Colby red herring planted; confrontation reserved)
- [x] Ch. 14 — "What the File Says" (Emma: Jack's questions reach the company; the ledger stays the one near-miss)
- [x] Ch. 15 — "Closer" (Sarah & Michael: the Voss leak; the pact; the painted ground deferred to Ch. 17)
- [x] Ch. 16 — "The Line Olivia Won't Cross" (Olivia: site work staged to the pond notch; she stands at the line and does not cross)
- [x] Ch. 17 — "What Sarah Finds Out" (Sarah: painting = Hollis ground sold to Hale the same autumn; the cabin fragment settles as a leaving)
- [x] Ch. 18 — "The Weight of It" (Emma & Jack: remains found in the old bank; Emma holds the folder, Jack reopens the case)
- [ ] Ch. 19 — "Webs"
- [ ] Ch. 20 — "Liam's Reckoning"
- [ ] Ch. 21 — "Alliances"
- [ ] Ch. 22 — "Fault Lines"
- [ ] Ch. 23 — "The Gathering Storm"
- [ ] Ch. 24 — "Reckoning"
- [ ] Ch. 25 — "What's Left Standing"
- [ ] Ch. 26 — "Echoes of Fate"

## Publishing (`docs/`)

- [ ] Update `docs/ch01.html` (and add `docs/ch02.html`-`ch04.html`) to
      match the drafted chapters — or switch to a generated approach, see
      `docs/workflows/publishing.md`. Not urgent: deliberately left until
      more chapters are drafted, per that workflow's own guidance not to
      republish on every draft.
- [ ] `docs/index.html` is a placeholder landing page — give it real
      content (title, blurb, chapter links) once there are a few chapters
      worth linking to
