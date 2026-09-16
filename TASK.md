# TASK — active work

What's actively being worked on right now, for whoever (human or agent)
picks this up next. This file should almost always describe *one* current
task, not a backlog — see `TODO.md` for the backlog and `PLAN.md` for the
roadmap this is drawn from.

## Current

**Status: 6 of 26 chapters drafted as of 2026-09-16.** Chapters 5-6 (Emma)
drafted and committed: "The Ledger" (the night before the groundbreaking
she reconciles the folder against her father's ledger and finds the buried
pattern) and "What Emma Won't Say" (the near-tell with Priya at the
ceremony; she buries it again). Working tree clean, all tests passing.
Chapter drafting is a steady loop now: scene plan
(`scenes/chapter-NN.md`) → draft (`manuscript/chapters/chapter-NN.md`) →
`tests/test_manuscript.py` → update `TODO.md` → commit — repeat per
`AGENTS.md`.

**Next task to pick up:** Chapters 7-8 (Jack) — "Cold Case" (Michael
brings Jack the postcard Daniel mailed home days before he vanished; the
case reopens informally) and "Echoes of the Unsolved" (Jack pulls his old
case notes; the postcard's line about Hale "not going to like" something
starts to rhyme with old details). First chapters in Jack's procedural,
cataloguing voice; see `characters/jack.md` and `scenes/plot-map.md` for
the two-stage reopening and the suspicion-tier information rules.

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
