# Style Guide

The concrete drafting rules for "Echoes of Fate," assembled from the craft
research in `research/`. Check new chapters against this before marking
them done (see `docs/workflows/chapter-drafting.md`'s checklist).

## POV and tense

- **Close third person, past tense**, one POV character per chapter unless
  the chapter is explicitly marked "Ensemble" or a dual-POV chapter in
  `manuscript/outline.md` (a dual chapter should still be one scene at a
  time — no head-hopping within a scene).
- Free indirect discourse, not "she thought" / "he felt" tags — let word
  choice and rhythm carry the character's interiority. See
  `research/voice-differentiation.md`.

## Chapter length and shape

- Target **~1,900-2,200 words** (~7-8 pages) per chapter; vary with tension
  rather than forcing a fixed count. Full guidance:
  `research/pacing-and-chapter-length.md`.
- One primary scene per chapter, occasionally a short second beat as a
  button on the first. Not a montage of multiple characters' summaries —
  that's the exact failure mode of the original Chapter 1 draft.
- Every chapter needs a want and an obstacle playing out **in the scene**,
  even a small one. End on a turn, not a summary.

## Show, don't tell

- No sentence of the shape "[Character] felt/was [abstract trait]." Externalize
  feeling as a physical/behavioral detail, a concrete object, or an action
  that contradicts stated intention. Full technique + before/after example:
  `research/show-dont-tell.md`.
- Retire all inherited stock description — "deep blue eyes," "dark eyes,"
  "carefully constructed facade" — permanently. Physical description should
  come from what a character notices about *others*, filtered through their
  own attention (see next section), not generic narrator shorthand.

## Voice per character

One-line voice test — before finishing a chapter, check whether its opening
paragraph could be swapped into another character's chapter unnoticed. If
yes, the voice isn't differentiated yet. Full notes:
`research/voice-differentiation.md`.

| Character | Sentence rhythm | Notices first | Metaphor source |
|---|---|---|---|
| Sarah | Long/absorbed, fractures when interrupted | Color, light, composition | Paint, canvas, negative space |
| Michael | Short, withheld, avoids naming his own feeling | Exits, hands, tells on other people | — (deliberately spare) |
| Emma | Precise, controlled, rarely fragments | Status markers: dress, punctuality, eye contact | Figures, ledgers, precision |
| Jack | Procedural, catalogs details like a report | What's out of place | Casework, old files |
| Olivia | Economical, task/time-organized | Cost, time, what her son needs | Household logistics |
| Liam | Sensory, fragmented/run-on, contemporary diction | Sound, social hierarchy, who's watching | Music/lyrics |

## Dialogue

- Dialogue is action (characters doing something to each other), not
  exposition delivery. Avoid on-the-nose emotional statements even more
  strictly than in narration.
- Minimize tags ("said" is nearly invisible); use action beats instead of
  adverbs. Let interruption, silence, and non-answers count as dialogue.
- Full toolkit and the first applied example (Sarah/Michael's first
  meeting): `research/dialogue-craft.md`.

## Structural checks

- No POV character should go dark for more than ~4-5 consecutive chapters
  in the middle third of the book (see `research/multi-pov-structure.md`
  and `research/pacing-and-chapter-length.md`).
- Don't reveal plot information ahead of the reveal order in
  `scenes/plot-map.md` once it exists.
- Run `python3 -m unittest discover -s tests` after drafting — it won't
  catch craft problems, but it will catch structural drift (missing files,
  chapter-count mismatches, encoding regressions).
