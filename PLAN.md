# PLAN — Echoes of Fate

_Last reviewed: 2026-09-16_

## Goal

Expand "Echoes of Fate" from its original 13-chapter/~50-page draft to a
full **26-chapter, ~200-page novel**. See `manuscript/outline.md` for the
current chapter-by-chapter structure.

## Where the project stands

The book was seeded through ChatGPT brainstorming sessions (archived in
`archive/chatgpt-sessions/`), not written directly. As of this review, the
plotting, planning, and first draft are complete (26 chapters) and the
project is in revision/publishing; the working loop below applies to
revision passes and docs/routing upkeep:

- **Outline:** expanded to 26 chapters across the original 6-part thematic
  shape (Introduction → Character Development → Rising Action → Midpoint
  Revelations → Climax → Resolution), with POV and a concrete summary per
  chapter. See `manuscript/outline.md`.
- **Central mystery fully designed:** ground truth is `scenes/plot-map.md` —
  Daniel died accidentally, confronting foreman Hank Colby over an unfiled
  safety report at an unstable pond embankment; Warren Hale (Emma's father)
  covered it up. Every character's connection to it, the reveal order, one
  fair-play red herring, and one foreshadowing plant are all fixed. All six
  `characters/*.md` files have full backstory, voice, physical detail,
  flaws, internal/external wants, and cross-character relationships, and
  are reconciled against `scenes/plot-map.md` with no open questions
  remaining.
- **A naming conflict was found and fixed (2026-09-14):** the plot-research
  and character-development agents ran concurrently and invented different
  names for the same facts (Whitfield/Gerald/"Daniel Cole" vs. the
  established Hale/Warren/"Daniel Voss"), plus a genuine contradiction in
  Sarah's family backstory. Both were reconciled by hand; `tests/
  test_manuscript.py`'s `TestPlotMap` now guards against this recurring.
  **Lesson for future parallel agent work:** when two agents can each
  independently invent proper nouns for the same underlying facts, either
  sequence them (one finishes and commits before the next starts) or give
  the later one the earlier one's output as required reading — don't just
  rely on reconciling afterward.
- **Craft research:** notes covering show-vs-tell, multi-POV structure,
  voice differentiation, pacing/chapter length, dialogue, mystery plotting,
  and subplot weaving — see `research/`. Synthesized into
  `manuscript/style-guide.md`.
- **Process design:** the recurring workflows (outline design, character
  development, plot design, scene planning, chapter drafting, continuity
  testing, publishing) are documented with diagrams in `docs/workflows/`.
- **Automated checks:** `tests/test_manuscript.py` (23 checks) validates
  outline structure, character-file consistency, plot-map/character-file
  name consistency, and repo text encoding. All passing.
- **Prose:** Chapters 1-26 drafted. Chs. 1-2 (the old ~470-word montage
  rewritten as six real scenes); Chs. 3-4 (Sarah and Michael's first
  meeting); Chs. 5-6 (Emma: the ledger reconciliation and the groundbreaking
  near-tell — timeline fixed so the groundbreaking is week one and Ch. 18's
  remains discovery is unchanged); Chs. 7-8 (Jack: Michael brings the
  postcard and the case reopens informally); Chs. 9-10 (Olivia/Liam get
  their own chapters — the loud-and-quiet mismatch that Ch. 20 will spring);
  Chs. 11-12 (Six Crossings — all six make a first active decision; Paths
  That Shouldn't Cross — Sarah finds the place is real while Michael stays
  name-and-mission concealed); Chs. 13-14 (Digging Deeper — unpermitted
  regrade confirmed and the Colby red herring planted, with the
  confrontation deferred to ~Ch. 19; What the File Says — Jack's questions
  reach the company and the never-opened 2008 ledger is the one near-miss);
  Chs. 15-16 (Closer — the Voss leak lands in parts and becomes theirs,
  with the painted-ground identification held back; The Line Olivia Won't
  Cross — the grading schedule reaches the pond notch "week of," Olivia
  stands at the fence and does not cross); Chs. 17-18 (What Sarah Finds
  Out — the identification lands, the fragment is said aloud, and the
  Hollis sale is opened at last; The Weight of It — the midpoint
  escalation: remains in the old bank, Emma holds the folder, Jack's case
  reopens and he takes the news to the motel); Chs. 19-20 (Webs — the
  Colby confrontation given up in the light gives Jack and Michael the
  accident-and-cover-up shape ahead of the folder or Olivia's account,
  Sarah hands Michael the Hollis ground, and Michael resolves to ask Emma;
  Liam's Reckoning — the two-photo post goes live and the man at the edge
  of his mother's picture is named, too late to take back); Chs. 21-22
  (Alliances — the post reaches Michael within a day, Jack names the girl
  in the kept photograph, and Michael goes where the ask sends him: the
  Emma denial he reads for its tell, and the diner table where he leaves
  Olivia the truth; Fault Lines — the town's version reaches Olivia first,
  Liam's confession and the sliver, and the long-planned crossing when her
  path finally meets Emma's in the corner office; the wall holds but the
  crack has run, and Olivia knows she will not let it come for her boy);
  Chs. 23-24, the climax pair (The Gathering Storm — Emma carries her
  father's folder to Jack herself the night before the festival, and the
  written half of the cover-up settles against Colby's spoken account;
  festival morning assembles all six, and Olivia stops the county
  man's questioning of Liam on her own, the wall down at last; Reckoning —
  her confession set against the folder and Colby's account reveals the
  accident to everyone at once, and the pocket watch recovered with
  Daniel's remains brings the pale glint in Sarah's painting level with
  the last thing he touched); Chs. 25-26, the resolution pair (What's
  Left Standing — the town wakes the morning after the reckoning, and
  each character's own gain lands separately from the shared reveal:
  Jack files the box for the last time and walks in for the coffee, not
  the case; Emma turns the board call from spin into truth and gives the
  parcel to the town as memorial ground; Sarah and Diane make their first
  real sentence in front of the Hollis ground; Michael puts the last
  phone call's guilt down and calls his mother; Liam and Olivia trade the
  sliver for the whole true version on the apartment steps; Echoes of
  Fate — some weeks later, the same low gold light as the first morning,
  the same six in their same tracks and none the same: Sarah paints the
  glint deliberately for the first time, Olivia opens the bottom drawer
  and puts the bracelet down, Liam finishes the sixty-second box and
  finds the fifth chord, Emma keeps her own time, and Michael stands at
  the lakefront ground with his brother's watch and decides to stay — the
  road's not long anymore, it's home). **The full 26-chapter first draft
  is complete as of 2026-09-16**; the climax and resolution per
  `scenes/plot-map.md` and `research/subplot-weaving.md` landed as
  designed. Drafting is over; the critical path moves to revision and
  publishing.

## Working loop

Per `AGENTS.md`, work proceeds as: design → implement → test → update
`TODO.md`/`PLAN.md` → commit, picking up 1-2 `TODO.md` items per pass. For
chapter-writing passes specifically, "design" means scene planning
(`docs/workflows/scene-planning.md`) grounded in `scenes/plot-map.md` and
the relevant `characters/*.md` file, and "test" means both
`tests/test_manuscript.py` and the manual checklist in
`docs/workflows/chapter-drafting.md`.

## Next steps (in order)

1. ~~Continuity/revision pass over the full draft~~ — **done 2026-09-16.**
   Batch 1 fixed the Olivia age mismatch, reconciled `characters/*.md`
   front-matter to the completed book, walked the watch/glint/postcard
   motifs, and closed the postcard loop (Chs. 25-26). The read-through
   then went all 26 chapters (six parallel passes): applied real fixes —
   typos, the Ch. 21 photo-timeline slips, Ch. 24 "eighteen years ago",
   the lost-watch engraving is **seven** words not nine (Chs. 24/25 +
   outline), the Ch. 20 photo-order comment, Ch. 11 POV scene breaks, Ch.
   21 relabeled "Michael & Olivia" for its closing button, and repetition
   thinning across ~20 chapters (Ch. 26's closing sweep reworked to
   include Emma). Deliberately left: Ch. 4 "told her nothing" (correct);
   "the whole of" kept as a book-wide motif.
2. ~~Word-count smoothing~~ — **done 2026-09-16.** The outliers were Ch. 3
   (~800) and Ch. 4 (~1,150), reopened and expanded in the established
   voice up to the ~1,900-2,200 band (1,870 / 1,867). Ch. 26 (~1,740)
   runs slightly light but is within the test-enforced range and fits a
   quiet closer; not padding it.
3. ~~Publish `docs/` (GitHub Pages)~~ — **done 2026-09-16.** Added
   `tools/build_docs.py` (stdlib converter generating `docs/chNN.html` +
   `docs/index.html` from `manuscript/chapters/`), regenerated all 26
   chapters with a real landing page (title, blurb, chapter list), and
   pointed GitHub Pages at `main` `/docs`. Live at
   https://gsbb-1.github.io/Echoes-of-Fate/
4. Keep polishing/beta-read as an ongoing activity once continuity is
   clean.

## Non-goals for now

- No need for heavier tooling/automation beyond the stdlib test suite —
  this is a small, single-author manuscript repo.
- Not rewriting the 6-part thematic shape — the 26-chapter structure maps
  onto it cleanly.
