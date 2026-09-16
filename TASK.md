# TASK — active work

What's actively being worked on right now, for whoever (human or agent)
picks this up next. This file should almost always describe *one* current
task, not a backlog — see `TODO.md` for the backlog and `PLAN.md` for the
roadmap this is drawn from.

## Current

**Status: 10 of 26 chapters drafted as of 2026-09-16.** Chapters 9-10
(Olivia/Liam) drafted and committed: "Two Jobs, One Boy" (Olivia's diner +
night-cleaning grind, the week-old sight of Jack with a stranger, and
Liam's archive talk about the missing man brushing against the fragment she
never names — she absorbs it and stays silent) and "The Notebook" (Liam
re-logs the search-line photo, gets a half-minted blessing from Jack, and
finds his mother as a teenager in the same orchard — he feels the two
images align without grasping what either is; logs both, posts nothing).
The loud-and-quiet mismatch (Liam will post in Ch. 20; Olivia has been
silent ~18 years) is now set up from both sides. Working tree clean, all
tests passing. Chapter drafting is a steady loop: scene plan
(`scenes/chapter-NN.md`) → draft (`manuscript/chapters/chapter-NN.md`) →
`tests/test_manuscript.py` → update `TODO.md` → commit — repeat per
`AGENTS.md`.

**Next task to pick up:** Chapters 11-12 — "Six Crossings" (ensemble:
each character faces a first real decision point) and "Paths That Shouldn't
Cross" (Sarah). These end Part II and pull the six threads toward first
actual crossings; keep the reveal discipline from `research/mystery-plotting.md`
(no folder contents to others, no Olivia interpretation, Colby's departure
stays the Ch. 13 red herring). See `manuscript/outline.md` and
`scenes/plot-map.md`.

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
