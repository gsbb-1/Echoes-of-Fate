# PLAN — Echoes of Fate

_Last reviewed: 2026-09-14_

## Goal

Expand "Echoes of Fate" from its original 13-chapter/~50-page draft to a
full **26-chapter, ~200-page novel**. See `manuscript/outline.md` for the
current chapter-by-chapter structure.

## Where the project stands

The book was seeded through ChatGPT brainstorming sessions (archived in
`archive/chatgpt-sessions/`), not written directly. As of this review:

- **Outline:** expanded to 26 chapters across the original 6-part thematic
  shape (Introduction → Character Development → Rising Action → Midpoint
  Revelations → Climax → Resolution). See `manuscript/outline.md`.
- **Central mystery decided:** the connective mechanism blocking further
  writing has been resolved — Michael's brother Daniel disappeared from
  Willow Creek eighteen years ago; Jack never solved it; Emma's father
  buried evidence tied to it; Olivia was a teenage witness who stayed
  silent; Liam (confirmed as Olivia's son) unknowingly surfaces the
  connection; Sarah has been unconsciously painting the place Daniel was
  last seen. Story spans six weeks in early autumn, climaxing at the town's
  Harvest Festival. Full detail in `characters/README.md`,
  `scenes/willow-creek.md`, and each `characters/*.md` file.
- **Character depth:** in progress. A character-development agent is
  deepening backstory/voice/physical detail/flaws in `characters/*.md`,
  and a plot-research agent is writing `scenes/plot-map.md` (the detailed
  beat-by-beat mystery design) plus mystery-plotting/subplot-weaving craft
  notes in `research/`. Their output needs reconciling once both finish
  (check `TODO.md`).
- **Craft research:** five notes written covering show-vs-tell, multi-POV
  structure, voice differentiation, pacing/chapter length, and dialogue —
  see `research/`.
- **Process design:** the recurring workflows (outline design, character
  development, plot design, scene planning, chapter drafting, continuity
  testing, publishing) are documented with diagrams in `docs/workflows/`.
- **Automated checks:** `tests/test_manuscript.py` (15 checks) validates
  outline structure, character-file consistency, and repo text encoding.
  All passing.
- **Prose:** still only one chapter exists — the original ~470-word
  Chapter 1 draft, now mapped to the new Chapters 1-2 and needing a full
  rewrite/split rather than a copy. 25-26 chapters remain undrafted.

**Bottom line:** planning and design infrastructure for the 26-chapter
expansion is in place; almost all of the actual prose still needs to be
written.

## Working loop

Per `AGENTS.md`, work proceeds as: design → implement → test → update
`TODO.md`/`PLAN.md` → commit, picking up 1-2 `TODO.md` items per pass. For
chapter-writing passes specifically, "design" means scene planning
(`docs/workflows/scene-planning.md`) grounded in `scenes/plot-map.md` and
the relevant `characters/*.md` file, and "test" means both
`tests/test_manuscript.py` and the manual checklist in
`docs/workflows/chapter-drafting.md`.

## Next steps (in order)

1. Reconcile the character-development and plot-research agents' output
   once they finish — resolve any contradictions, fold plot-map answers
   into the character files' remaining open questions (Sarah's painting,
   Jack's present-day case).
2. Assemble a short style guide from the existing `research/` notes.
3. Rewrite/split Chapter 1 into the new Chapters 1-2 (scene plan first, per
   `docs/workflows/scene-planning.md`).
4. Draft Chapters 3-4 (Sarah/Michael's meeting) — first chapters needing
   real scene-writing and dialogue.
5. Continue chapter-by-chapter per `manuscript/outline.md`, in roughly
   outline order, running `tests/test_manuscript.py` and committing after
   each pass.
6. Sync `docs/` (GitHub Pages) once a handful of chapters are in a
   publishable state — not on every draft.

## Non-goals for now

- No need for heavier tooling/automation beyond the stdlib test suite —
  this is a small, single-author manuscript repo.
- Not rewriting the 6-part thematic shape — the 26-chapter structure maps
  onto it cleanly.
