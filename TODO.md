# TODO — Echoes of Fate

Concrete, actionable work items. Check items off as they're done; move
finished large items into commit history rather than leaving them checked
here forever. See `PLAN.md` for the reasoning behind these, `TASK.md` for
what's actively being worked on right now.

Goal: expand from the original 13-chapter/~50-page draft to **26
chapters, ~200 pages** (see `manuscript/outline.md`).

**26 of 26 chapters drafted (Ch. 1-26) as of 2026-09-16.** Manuscript
first-draft complete. All
planning/design infrastructure below is done; only the "Writing" section
has open items. See `TASK.md` for the exact resume point and `PLAN.md`
for the full state of the project.

## Story decisions (were blocking further chapter writing)

- [x] Decide whether Liam is Olivia's son — confirmed, yes
- [x] Define the concrete mechanism that connects all six characters — the
      cold case of Michael's brother Daniel's disappearance (see
      `characters/README.md`)
- [x] Set the story's timeframe — six weeks, early autumn, culminating at
      the Harvest Festival

## Project infrastructure

- [x] Reorganize repo into `manuscript/`, `characters/`, `scenes/`,
      `research/`, `archive/`
- [x] Write `AGENTS.md`, `PLAN.md`, `TODO.md`, `IDEA.md`, `TASK.md`
- [x] Expand `manuscript/outline.md` to the 26-chapter/~200-page structure
- [x] Design and document core workflows in `docs/workflows/`
- [x] Build `tests/test_manuscript.py` automated consistency checks and get
      them passing (23 checks, all green —
      `python3 -m unittest discover -s tests`)
- [x] Reconcile the character-development agent's and plot-research agent's
      output — found and fixed a real naming conflict (the plot-research
      agent independently invented "Whitfield/Gerald"/"Daniel Cole"; renamed
      to match the character files' established "Hale/Warren"/"Daniel Voss"),
      plus a genuine backstory conflict on Sarah's family (merged into one
      consistent version). Updated all `characters/*.md` open-question notes,
      `characters/README.md`, and enriched `manuscript/outline.md`'s chapter
      summaries with the concrete plot-map facts. Added a regression test
      (`TestPlotMap`) so this class of drift gets caught automatically next
      time.
- [x] Resolve any new open questions those two agents raise in
      `characters/README.md` — all four resolved (Jack's case, what Olivia
      saw, Sarah's fragment, Daniel's land-dispute rumor)

## Craft / research (ongoing)

- [x] Research literary styles/techniques relevant to this draft's known
      problems (`research/show-dont-tell.md`,
      `research/multi-pov-structure.md`, `research/voice-differentiation.md`,
      `research/pacing-and-chapter-length.md`, `research/dialogue-craft.md`)
- [x] Research mystery-plotting and subplot-weaving technique —
      `research/mystery-plotting.md`, `research/subplot-weaving.md`
- [x] Write a short style guide (POV, tense, target chapter length) —
      `manuscript/style-guide.md`, assembled from the `research/` notes
- [x] Deepen `characters/*.md` (backstory, voice, physical detail, flaw,
      internal vs. external want, cross-character relationships) — done
      for all six characters
- [x] Design the mystery's beat-by-beat plot map — `scenes/plot-map.md`
      (what happened to Daniel, the evidence, the reveal order, one red
      herring, one foreshadowing plant)

## Writing — 26 chapters (see `manuscript/outline.md` for POV/summary per chapter)

- [x] Ch. 1 — "Six Lives, One Town" (rewritten as three real scenes —
      Sarah, Jack, Olivia — replacing the old six-paragraph montage)
- [x] Ch. 2 — "What the Morning Hides" (Michael, Emma, Liam)
- [x] Ch. 3 — "The Artist and the Stranger"
- [x] Ch. 4 — "A Name Across the Room" (first dialogue-heavy chapter)
- [x] Ch. 5 — "The Ledger"
- [x] Ch. 6 — "What Emma Won't Say"
- [x] Ch. 7 — "Cold Case"
- [x] Ch. 8 — "Echoes of the Unsolved"
- [x] Ch. 9 — "Two Jobs, One Boy" (last POV, Olivia, to get her own chapter)
- [x] Ch. 10 — "The Notebook" (Liam holds two images that don't yet mean anything to him)
- [x] Ch. 11 — "Six Crossings" (ensemble: all six make a first active decision)
- [x] Ch. 12 — "Paths That Shouldn't Cross" (coincidence resolves into choice at the parcel gate)
- [x] Ch. 13 — "Digging Deeper" (Jack: unpermitted regrade confirmed; Colby red herring planted; confrontation reserved)
- [x] Ch. 14 — "What the File Says" (Emma: Jack's questions reach the company; the ledger stays the one near-miss)
- [x] Ch. 15 — "Closer" (Sarah & Michael: the Voss leak; the pact; the painted ground deferred to Ch. 17)
- [x] Ch. 16 — "The Line Olivia Won't Cross" (Olivia: site work staged to the pond notch; she stands at the line and does not cross)
- [x] Ch. 17 — "What Sarah Finds Out" (Sarah: painting = Hollis ground sold to Hale the same autumn; the cabin fragment settles as a leaving)
- [x] Ch. 18 — "The Weight of It" (Emma & Jack: remains found in the old bank; Emma holds the folder, Jack reopens the case)
- [x] Ch. 19 — "Webs" (Jack: the Colby confrontation — accident-and-cover-up shape given up in the light; Sarah hands Michael the Hollis ground)
- [x] Ch. 20 — "Liam's Reckoning" (Liam: the two-photo post goes live; the edge man is named; it's already moving)
- [x] Ch. 21 — "Alliances" (Michael: the post within a day; Jack names the girl; the Emma ask and the Olivia approach)
- [x] Ch. 22 — "Fault Lines" (Olivia: the town's version first; Liam's confession, the sliver; the Emma crossing in the corner office)
- [x] Ch. 23 — "The Gathering Storm" (Emma carries the folder to Jack; the festival assembles all six; Olivia answers for the photograph)
- [x] Ch. 24 — "Reckoning" (Olivia's confession; the folder + her account reveal the accident; the watch payoff)
- [x] Ch. 25 — "What's Left Standing" (each character's own gain: Jack files the case, Emma gives the ground back, Sarah and Diane's first true sentence, Michael's last phone call, Liam and Olivia's whole version)
- [x] Ch. 26 — "Echoes of Fate" (the same six, same tracks, carrying less; the deliberate glint; *it's home*)

## Revision / continuity pass (begun 2026-09-16)

- [x] Olivia's age: Ch. 8 file transcript said "sixteen"; canon is
      seventeen (she was seventeen the autumn Daniel vanished — Chs. 22/24,
      `characters/olivia.md`). Fixed.
- [x] Reconcile `characters/*.md` with the drafted book: Introduced points
      fixed (Michael/Emma/Liam are introduced in Ch. 2, not Ch. 1; Jack's
      Ch. 1 scene is the diner + the box, not the park bench); Liam's
      climax beat renumbered to Ch. 23 (where the investigator draws him
      aside); Daniel's age fixed to twenty-two (Ch. 15's draft text, the
      only on-page age); `characters/README.md` status updated for a
      complete book.
- [x] Liam's archive count: Ch. 2 said "eleven boxes left of sixty-two" but
      he's on box 41 → corrected to "twenty-one" (Ch. 10 confirms box 41;
      Ch. 26 confirms sixty-two total).
- [x] Postcard loop closed: Ch. 7 left the card in Jack's file; Ch. 25 now
      has Jack set it apart to walk back to Michael, and Ch. 26 has Michael
      carrying it home beside the recovered watch.
- [x] Watch/glint/postcard motifs walked through all 26 chapters —
      consistent (broken digital watch at 4:47 on Michael's wrist; Emma's
      father's watch set down in Ch. 25/26; pocket watch engraving
      "To Daniel. The road is long. — M." recovering in Ch. 24; glint
      resolving in Ch. 24 and painted deliberately in Ch. 26).
- [x] Prose read-through of all 26 chapters for first-draft clunk (six
      parallel review passes, 2026-09-16; fixes applied, not committed yet).
      Real fixes: Ch. 6 "one breathe"→"one breath"; Ch. 23 "owns and
      exits"→"openings and exits", wall metaphor unknotted; Ch. 24
      "fifteen years ago"→"eighteen", "his boy's face on a wall" reworked,
      engraving is **seven** words not nine (Ch. 24/25/outline); Ch. 21
      photo timeline ("that summer", not "the summer after"), "eighteen
      years of witness statements", "stood very still" duplication, closing
      button relabeled "Michael & Olivia" in outline; Ch. 20 photo-order
      comment ("second"→"first"), "remains…they did", "coppers" anachronism;
      duplication/repetition thinning in Chs. 1/2/5/9/10/11/12/15/16/17/18/
      19/20/22/26 ("the whole of it", "for eighteen months", "ordinary",
      "flat, even", "very quiet/still", "cold, fast thing", "in pieces he
      decided the weight of", "the finished thing", "the cataloguing look",
      "bottom drawer" x2, "mis-read" triple, "actual thing" x2, "never once
      mentioned" x2); Ch. 11 POV scene breaks added; Ch. 26 closing sweep
      reworked to include Emma and drop the doubled Sarah beat; Ch. 17
      "painting it his whole life" literal-impossibility fixed. Deliberately
      left: Ch. 4 "told her nothing" (pre-reveal, correct), Ch. 7 "not by a
      long way", Ch. 9 "stung more than it used to", and "the whole of" as a
      book-wide motif. Tests 23/23 passing.
- [ ] Word-count smoothing — the true outliers are Ch. 3 (~800 words) and
      Ch. 4 (~1,150) vs the ~1,900-2,200 band; Ch. 26 runs light (~1,700).
      Decision (2026-09-16): expand Ch. 3-4, the opening pair, in the
      established voice, folding in their flagged local notes (Ch. 3
      "for exactly" x2; Ch. 4 "soft at the edges" self-echo).

## Publishing (`docs/`)

- [ ] Update `docs/ch01.html` (and add `docs/ch02.html`-`ch04.html`) to
      match the drafted chapters — or switch to a generated approach, see
      `docs/workflows/publishing.md`. Not urgent: deliberately left until
      more chapters are drafted, per that workflow's own guidance not to
      republish on every draft.
- [ ] `docs/index.html` is a placeholder landing page — give it real
      content (title, blurb, chapter links) once there are a few chapters
      worth linking to
