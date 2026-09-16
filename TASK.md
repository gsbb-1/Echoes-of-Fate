# TASK — active work

What's actively being worked on right now, for whoever (human or agent)
picks this up next. This file should almost always describe *one* current
task, not a backlog — see `TODO.md` for the backlog and `PLAN.md` for the
roadmap this is drawn from.

## Current

**Status: 24 of 26 chapters drafted as of 2026-09-16.** The climax pair,
Chapters 23-24, is drafted and committed: "The Gathering Storm" (the
weeks between carry the storm in — dental takes its time but the town
knows, the society's page climbs, the Harvest Festival finds the square
already full of weather; the night before it, Emma takes her father's
folder out of the locked drawer and carries it to Jack's kitchen table
herself, and the written half of the cover-up settles against Colby's
spoken account; festival morning assembles all six — the archive tent
with the two photographs, Sarah's ground painting in the loan corner,
Liam at the accession table, Olivia at the edge, Emma's booth, Michael
and Jack passing the same ground; the county investigator draws Liam
aside about the post, and Olivia crosses the tent floor and stops it
herself, the eighteen-year wall coming down all at once) and "Reckoning"
(Olivia confesses believing she is confessing to the aftermath of a
murder; Jack sets her account against the folder with Colby's admission
already in hand — an accident, a bank a report had already condemned, a
company that buried it and paid the silence — and the wrong shape of
eighteen years comes apart in her hands; afterwards Jack walks the
recovered effects to Michael, and the engraved pocket watch — the nine
words *to Daniel: the road is long* — brings the pale glint in Sarah's
painting level at last with the last thing his brother touched; Michael
lets the town hold him). The three confirmations converged exactly per
`scenes/plot-map.md`; the watch payoff landed on-page as planned. Working
tree clean, all tests passing. Chapter drafting remains a steady loop:
scene plan (`scenes/chapter-NN.md`) → draft
(`manuscript/chapters/chapter-NN.md`) → `tests/test_manuscript.py` →
update `TODO.md` → commit — repeat per `AGENTS.md`.

**Next task to pick up:** Chapters 25-26, the resolution pair — "What's
Left Standing" (Ensemble — fallout; each character's own reckoning,
distinct from the shared reveal, per `research/subplot-weaving.md`:
Olivia's relationship with Liam and her own self-forgiveness; Emma's
choice about the company and her father's memory now that hiding is no
longer possible; Sarah reckoning with a family history she was never
told; Jack finally closing the file; Michael and Sarah past the mystery
that brought them together) and "Echoes of Fate" (Ensemble — resolution
and reflection on fate, choice, and interconnectedness; final image).
No reveal remains to spend; this pair is each character's internal
aftermath plus the closing image. See `manuscript/outline.md`,
`research/subplot-weaving.md`, and `characters/*.md`.

## History

- 2026-09-14 — Repo reorganized; tracking files and `AGENTS.md` created.
- 2026-09-14 — Expanded goal to 26 chapters/~200 pages; resolved the three
  blocking story decisions; expanded the outline; documented workflows;
  built the test suite; launched background research/character/plot agents.
- 2026-09-14 — Added `manuscript/style-guide.md`.
- 2026-09-14/15 — Reconciled the character-development and plot-research
  agents' output (fixed a naming conflict and a Sarah backstory
  contradiction); `scenes/plot-map.md` is now the mystery's ground truth.
- 2026-09-15 — Drafted Chapters 1-2 (six real scenes replacing the old
  montage draft), added per-chapter word-count and stock-phrase regression
  tests.
- 2026-09-15 — Drafted Chapters 3-4 (Sarah and Michael's first meeting,
  first dialogue-heavy chapter). Session paused here for the user to read
  Ch. 1-4 before more chapters are drafted.
- 2026-09-16 — Drafted Chapters 5-6 (Emma: the ledger reconciliation the
  night before the groundbreaking; the near-tell with Priya at the
  ceremony). Reworded the outline's Ch. 16 beat ("groundbreaking is
  announced") so it stays consistent with Ch. 2's week-one groundbreaking.
  Working tree clean, all tests passing.
- 2026-09-16 — Drafted Chapters 7-8 (Jack: Michael brings the postcard —
  full text, including the orchard line — and the case reopens informally;
  Jack's old regrade note finally rhymes with the Hale line). Working tree
  clean, all tests passing.
- 2026-09-16 — Drafted Chapters 9-10 (Olivia/Liam: the two last POVs get
  their own chapters — Olivia's grind against the fragment she never names;
  Liam holding two images that don't yet mean anything). Patched a
  typo'd "Ma'am" ('course) out of the Ch. 10 draft. Working tree clean, all
  tests passing.
- 2026-09-16 — Drafted Chapters 11-12 (Six Crossings — all six make a
  first active decision; Paths That Shouldn't Cross — Sarah finds the
  place is real, Michael stays name-and-mission concealed so the reader
  holds the irony). Part II (Character Development) now complete.
  Working tree clean, all tests passing.
- 2026-09-16 — Drafted Chapters 13-14 (Digging Deeper — unpermitted
  regrade confirmed, Colby red herring planted with the confrontation
  deferred to ~Ch. 19; What the File Says — Jack's questions reach the
  company, the ledger stays the one near-miss). Part III (Rising Action)
  opened. Working tree clean, all tests passing.
- 2026-09-16 — Drafted Chapters 15-16 (Closer — the Voss leak lands in
  parts and becomes theirs; the finished canvas shows Michael his
  brother's ground and the unresolved glint; The Line Olivia Won't Cross —
  the grading schedule reaches the pond notch "week of," Olivia stands at
  the fence and does not cross, the near-ask with Liam stays unasked).
  Removed a stale duplicate Ch. 11-14 block from TODO. Working tree clean,
  all tests passing.
- 2026-09-16 — Drafted Chapters 17-18 (What Sarah Finds Out — the
  identification lands via the café hung piece, the fragment is said
  aloud, and the mother confrontation opens the Hollis sale at last;
  The Weight of It — the midpoint escalation, remains in the old bank,
  Emma stalls at her own tape line holding the folder, Jack's case
  reopens and he takes the news to the motel). Midpoint reached.
  Working tree clean, all tests passing.
- 2026-09-16 — Drafted Chapters 19-20 (Webs — the Colby confrontation,
  accident-and-cover-up shape given up in the light, Sarah hands Michael
  the Hollis ground, Michael resolves to ask Emma; Liam's Reckoning —
  the two-photo post goes live on the society's account and the man at
  the edge of his mother's photograph is named; he can't take it back).
  The scheduled Colby resolution is written. Working tree clean, all
  tests passing.
- 2026-09-16 — Drafted Chapters 21-22 (Alliances — the post reaches
  Michael, Jack names the girl, the Emma ask and the diner approach;
  Fault Lines — the town's version first, Liam's confession and the
  sliver, the Emma-Olivia crossing in the corner office). The planned
  Ch. 22 Emma crossing is written; the wall holds, the crack has run.
  22 of 26. Working tree clean, all tests passing.
- 2026-09-16 — Drafted Chapters 23-24, the climax pair (The Gathering
  Storm — Emma carries the folder to Jack herself; the festival
  assembles all six; Olivia stops the questioning on her own; Reckoning —
  Olivia's confession set against the folder and Colby's account reveal
  the accident; the pocket watch meets the glint in Sarah's painting).
  The three confirmations converged and the watch payoff landed, per
  `scenes/plot-map.md`; Ch. 24 trimmed to the ceiling (2593 words).
  24 of 26. Working tree clean, all tests passing.
