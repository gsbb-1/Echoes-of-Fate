# AGENTS.md

Instructions for AI agents/assistants working in this repository.

## What this project is

"Echoes of Fate" is a long-form, AI-assisted novel-writing project: a
contemporary fiction novel about six interconnected lives in a small
mountain town. It is early-stage — see `PLAN.md` for exactly where it
stands. Treat this as a creative writing project first: prose quality and
story coherence matter more than engineering polish.

## Repository layout

- `manuscript/` — the book itself
  - `outline.md` — canonical outline (theme, structure, chapter-by-chapter
    breakdown)
  - `chapters/chapter-NN.md` — finished/drafted chapter prose, one file per
    chapter, numbered
- `characters/` — one profile file per character (want, obstacle, voice,
  arc, relationships); `characters/README.md` indexes them and tracks
  cross-character open questions
- `scenes/` — setting/background notes and per-scene planning that supports
  the manuscript but isn't prose itself
- `research/` — notes on writing styles/techniques worth drawing on,
  including craft problems identified in the existing draft
- `archive/chatgpt-sessions/` — raw transcripts from the ChatGPT sessions
  that originally seeded this project. Historical reference only — do not
  edit these, and do not treat them as canon if they conflict with
  `manuscript/outline.md` or `characters/*.md`, which supersede them.
- `docs/` — the GitHub Pages site that republishes the manuscript as static
  HTML. Update it deliberately (see `TODO.md`), not automatically on every
  prose change.

## Progress-tracking files — keep these current

This project uses four tracking files at the repo root. **Any agent doing
non-trivial work in this repo should read them at the start of a session
and update them before finishing:**

- **`PLAN.md`** — the roadmap and analysis of where the project stands.
  Update when the overall direction changes or a phase completes; this is
  the "why" document, not a checklist.
- **`TODO.md`** — the concrete backlog, as checkboxes, grouped by area
  (story decisions, writing, craft, publishing). Add items here when new
  work is identified; check items off as they're completed.
- **`TASK.md`** — the single active task, for continuity between sessions.
  Overwrite the "Current" section when starting or finishing a task rather
  than letting it go stale; append a one-line entry to the "History"
  section when a task completes.
- **`IDEA.md`** — a scratchpad for creative options that haven't been
  decided yet (alternate plot mechanisms, character possibilities). When an
  idea is decided, move the decision into the relevant canon file
  (`manuscript/outline.md`, `characters/*.md`, `scenes/*.md`) and remove it
  from `IDEA.md`.

Keep these terse and current rather than exhaustive — stale tracking files
are worse than none.

## Working conventions

- Story canon lives in `manuscript/outline.md` and `characters/*.md`. If a
  scene contradicts them, either the scene or the canon needs to change —
  don't let them silently drift apart.
- Before drafting a new chapter, check `TODO.md` for open story decisions
  that block it (e.g. undefined relationships or plot mechanisms) — resolve
  those in the relevant canon file first rather than drafting around the
  ambiguity.
- Chapter files are numbered (`chapter-01.md`, `chapter-02.md`, ...) and
  contain only finished prose — planning material belongs in `scenes/`.
- When you finish a piece of work, update `TASK.md` and check off the
  relevant `TODO.md` item(s) in the same session, not as a follow-up.
