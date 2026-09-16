# TASK — active work

What's actively being worked on right now, for whoever (human or agent)
picks this up next. This file should almost always describe *one* current
task, not a backlog — see `TODO.md` for the backlog and `PLAN.md` for the
roadmap this is drawn from.

## Current

**Status: 8 of 26 chapters drafted as of 2026-09-16.** Chapters 7-8 (Jack)
drafted and committed: "Cold Case" (Michael brings Jack the full postcard —
including the orchard line quoted in Ch. 2 — and the case reopens
informally) and "Echoes of the Unsolved" (the no-work-order pond-bank
regrade in Jack's old notes rhymed with the postcard's Hale line; he writes
the first "Reopened" entry in six years). Procedural, cataloguing voice.
Working tree otherwise clean, all tests passing. Chapter drafting is a
steady loop now: scene plan (`scenes/chapter-NN.md`) → draft
(`manuscript/chapters/chapter-NN.md`) → `tests/test_manuscript.py` →
update `TODO.md` → commit — repeat per `AGENTS.md`.

**Next task to pick up:** Chapters 9-10 (Olivia/Liam) — "Two Jobs, One
Boy" (Olivia's grinding routine; friction with Liam, who has started
digitizing old newspaper archives for community service) and "The
Notebook" (Liam, between the archive work and a box of his mother's old
photos, turns up two things about Daniel that don't yet mean anything to
him). Olivia and Liam are the last two POVs to get their own chapters;
remember the loud-and-quiet mismatch (Liam posts; Olivia stays silent ~18
years) and that neither knows what he/she is holding. See `characters/`
and `scenes/plot-map.md` for what Liam "finds" without grasping.

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
