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
- **Automated checks:** `tests/test_manuscript.py` (21 checks) validates
  outline structure, character-file consistency, plot-map/character-file
  name consistency, and repo text encoding. All passing.
- **Prose:** Chapters 1-6 drafted. Chs. 1-2 (the old ~470-word montage
  rewritten as six real scenes, ~1,950 words each); Chs. 3-4 (Sarah and
  Michael's first meeting, first dialogue-heavy chapters); Chs. 5-6 (Emma:
  the ledger reconciliation the night before the groundbreaking, and the
  near-tell at the ceremony — her controlled voice against the folder).
  20 chapters remain undrafted. This is the critical path — everything
  upstream of it is done. Note: Ch. 2 establishes the groundbreaking
  happening in week one; the outline's Ch. 16 beat was reworded
  accordingly (site work advancing toward the pond section) so it no
  longer claims the groundbreaking "is announced" — Ch. 18's remains
  discovery is unchanged.

## Working loop

Per `AGENTS.md`, work proceeds as: design → implement → test → update
`TODO.md`/`PLAN.md` → commit, picking up 1-2 `TODO.md` items per pass. For
chapter-writing passes specifically, "design" means scene planning
(`docs/workflows/scene-planning.md`) grounded in `scenes/plot-map.md` and
the relevant `characters/*.md` file, and "test" means both
`tests/test_manuscript.py` and the manual checklist in
`docs/workflows/chapter-drafting.md`.

## Next steps (in order)

1. Draft Chapters 7-8 (Jack) — "Cold Case" and "Echoes of the Unsolved":
   Michael brings Jack the postcard Daniel mailed home days before he
   vanished; the case reopens informally. First chapters in Jack's
   procedural, cataloguing voice.
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
