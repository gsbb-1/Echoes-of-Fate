# TASK — active work

What's actively being worked on right now, for whoever (human or agent)
picks this up next. This file should almost always describe *one* current
task, not a backlog — see `TODO.md` for the backlog and `PLAN.md` for the
roadmap this is drawn from.

## Current

**Status:** two background agents in flight; main thread work for this
cycle is done and committed.

- A character-development agent is deepening `characters/*.md` (backstory,
  voice, physical detail, flaws, cross-relationships).
- A plot-research agent is writing `scenes/plot-map.md` (detailed
  beat-by-beat mystery design) and two craft-research files
  (`research/mystery-plotting.md`, `research/subplot-weaving.md`).

**Next task to pick up (once both agents report back):** reconcile their
output — check for contradictions between `scenes/plot-map.md` and the
character files, resolve any newly-flagged open questions in
`characters/README.md`, and fold answers into the remaining open items
(Sarah's painting, Jack's present-day case). Then move to drafting: rewrite
Chapter 1 (split into new Ch. 1-2) per `docs/workflows/scene-planning.md`
and `docs/workflows/chapter-drafting.md`.

## History

- 2026-09-14 — Repo reorganized; tracking files (`TODO.md`, `IDEA.md`,
  `PLAN.md`, `TASK.md`) and `AGENTS.md` created.
- 2026-09-14 — Expanded goal to 26 chapters/~200 pages. Resolved the three
  blocking story decisions (Liam/Olivia relationship, connective
  mechanism, timeframe). Expanded `manuscript/outline.md` to 26 chapters.
  Designed and documented core workflows in `docs/workflows/`. Built
  `tests/test_manuscript.py` (15 checks, passing). Launched background
  agents for craft research, character development, and plot research.
