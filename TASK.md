# TASK — active work

What's actively being worked on right now, for whoever (human or agent)
picks this up next. This file should almost always describe *one* current
task, not a backlog — see `TODO.md` for the backlog and `PLAN.md` for the
roadmap this is drawn from.

## Current

**Status:** planning/design phase complete; about to start chapter
drafting.

Both background agents (character-development, plot-research) finished and
their output has been reconciled — see `PLAN.md`'s "naming conflict" note
for what that involved. `scenes/plot-map.md` is now the ground truth for
the mystery, all six `characters/*.md` files are fully fleshed out and
consistent with it, and `manuscript/outline.md`'s 26 chapter summaries
have been enriched with the concrete plot facts.

**Next task to pick up:** rewrite the old Chapter 1 draft, split into the
new Chapters 1-2, per `docs/workflows/scene-planning.md` and
`docs/workflows/chapter-drafting.md`. Ground it in `scenes/plot-map.md`'s
Introduction-tier rule: establish each character's private discomfort
without naming the mystery yet.

## History

- 2026-09-14 — Repo reorganized; tracking files (`TODO.md`, `IDEA.md`,
  `PLAN.md`, `TASK.md`) and `AGENTS.md` created.
- 2026-09-14 — Expanded goal to 26 chapters/~200 pages. Resolved the three
  blocking story decisions. Expanded `manuscript/outline.md` to 26
  chapters. Designed and documented core workflows in `docs/workflows/`.
  Built `tests/test_manuscript.py`. Launched background agents for craft
  research, character development, and plot research.
- 2026-09-14 — Added `manuscript/style-guide.md`, synthesized from craft
  research.
- 2026-09-14/15 — Character-development and plot-research agents finished.
  Reconciled a naming conflict between their independent output (Hale vs.
  Whitfield, Daniel Voss vs. Daniel Cole) and a genuine backstory
  contradiction on Sarah's family; folded plot-map facts into all six
  character files' open questions and into the outline's chapter
  summaries; added a regression test guarding against this drift.
