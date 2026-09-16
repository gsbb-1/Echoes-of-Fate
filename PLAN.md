# PLAN — Echoes of Fate

_Last reviewed: 2026-09-16_

## Goal

Expand "Echoes of Fate" from its original 13-chapter/~50-page draft to a
full **26-chapter, ~200-page novel**. See `manuscript/outline.md` for the
current chapter-by-chapter structure.

## Where the project stands

The book was seeded through ChatGPT brainstorming sessions (archived in
`archive/chatgpt-sessions/`), not written directly. As of this review, all
planning/design work is done and the project is ready for chapter drafting:

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
- **Prose:** Chapters 1-18 drafted. Chs. 1-2 (the old ~470-word montage
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
  the last thing he touched). The climax is complete. 2 chapters remain
  undrafted. This is the critical path — everything upstream of it is
  done.

## Working loop

Per `AGENTS.md`, work proceeds as: design → implement → test → update
`TODO.md`/`PLAN.md` → commit, picking up 1-2 `TODO.md` items per pass. For
chapter-writing passes specifically, "design" means scene planning
(`docs/workflows/scene-planning.md`) grounded in `scenes/plot-map.md` and
the relevant `characters/*.md` file, and "test" means both
`tests/test_manuscript.py` and the manual checklist in
`docs/workflows/chapter-drafting.md`.

## Next steps (in order)

1. Draft Chapters 25-26, the resolution pair — "What's Left Standing"
   (Ensemble — fallout; each character's own reckoning, distinct from the
   shared reveal, per `research/subplot-weaving.md`: Olivia's relationship
   with Liam and her own self-forgiveness; Emma's choice about the company
   and her father's memory now that hiding is no longer possible; Sarah
   reckoning with a family history she was never told; Jack finally
   closing the file; Michael and Sarah past the mystery that brought them
   together) and "Echoes of Fate" (Ensemble — resolution and reflection
   on fate, choice, and interconnectedness; final image). No reveal
   remains to spend; this pair is each character's internal aftermath
   plus the closing image.
2. Continue chapter-by-chapter per `manuscript/outline.md`, in roughly
   outline order, running `tests/test_manuscript.py` and committing after
   each pass (or small batch of chapters).
3. Sync `docs/` (GitHub Pages) once a handful of chapters are in a
   publishable state — not on every draft.

## Non-goals for now

- No need for heavier tooling/automation beyond the stdlib test suite —
  this is a small, single-author manuscript repo.
- Not rewriting the 6-part thematic shape — the 26-chapter structure maps
  onto it cleanly.
