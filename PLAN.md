# PLAN — Echoes of Fate

_Last reviewed: 2026-09-14_

## Where the project stands

The book was seeded through a series of ChatGPT brainstorming sessions (now
archived in `archive/chatgpt-sessions/`), not written directly. What exists:

- A high-level 6-part story outline (theme, character list, plot beats,
  climax, resolution) — see `manuscript/outline.md`.
- A 13-chapter breakdown with a one-line summary per chapter — folded into
  `manuscript/outline.md`.
- **One chapter drafted: Chapter 1** (`manuscript/chapters/chapter-01.md`),
  ~470 words. It was originally requested as "6 pages long" but the draft
  received is far short of that — it's a rapid scene-setting montage that
  introduces all six characters in six short paragraphs, with no dialogue,
  no scene-level conflict, and no distinct prose voice per character.
- A GitHub Pages site (`docs/`) that republishes the homepage and Chapter 1
  as static HTML, using default w3.css styling with no real design.

**Bottom line: this is still at the concept/outline stage.** 12 of 13
chapters are unwritten, and the one existing chapter is a summary-length
placeholder rather than a scene.

## Structural gaps to resolve before writing more chapters

These are outline-level holes that will cause rework if chapters are
written before they're settled (tracked individually in `TODO.md`):

1. **Liam/Olivia relationship is ambiguous.** Chapter 4's summary implies
   Liam is Olivia's son, but the character list introduces them as
   unrelated. This needs to be decided and stated explicitly, since it
   changes Chapter 1 onward.
2. **No concrete connective mechanism.** The outline asserts the six
   character's fates "become intertwined" and "converge" at the climax, but
   never specifies *how* — a shared event, a shared location, a shared past,
   a shared secret. Six independent character studies won't converge on
   their own; the connection has to be designed.
3. **No chapter-1 conflict or scene.** Chapter 1 as drafted is introduction
   only — nobody wants anything on-page, nothing happens. It needs at least
   one scene with a concrete want/obstacle to actually open the story.
4. **Prose is generic/cliché** ("deep blue eyes... brow furrowed",
   "carefully constructed facade") and every character is described in the
   same distant, tell-don't-show register. A style pass or rewrite is
   needed before this reads as a real chapter rather than an outline in
   prose form.
5. **Timeframe is unset.** Days, weeks, or a season — affects pacing across
   13 chapters.

## Proposed next steps (in order)

1. Resolve the open story questions above (Liam/Olivia relationship, the
   connective mechanism, timeframe) — these are creative decisions, not
   writing tasks, and should happen in `characters/`, `scenes/`, and
   `manuscript/outline.md` before more prose is written.
2. Do a pass of craft research (`research/`) on show-vs-tell and
   differentiating POV voice — directly relevant to the prose problems in
   the current Chapter 1 draft.
3. Plan Chapter 1 scene-by-scene in `scenes/` (goal, conflict, POV
   character, outcome per scene) before rewriting it as prose — the
   current draft is an introduction montage, not a scene.
4. Rewrite Chapter 1 in `manuscript/chapters/` as an actual scene (or split
   it into per-character scenes) rather than a six-paragraph introduction —
   pick one or two characters to open on rather than all six at once.
5. Draft Chapter 2 ("The Artist and the Stranger") — first chapter that
   needs actual scene-writing (a meeting, dialogue) rather than
   introduction.
6. Establish a lightweight style guide (POV rules, tense, target
   chapter length) so chapters stay consistent as more get written.
7. Keep `docs/` in sync only once chapters are in a state worth publishing —
   no need to republish placeholder text on every draft.

## Non-goals for now

- No need to build tooling/automation for this project; it's a small,
  single-author manuscript repo.
- Not rewriting the whole outline from scratch — the existing 13-chapter
  shape is usable once the gaps above are patched.
