#!/usr/bin/env python3
"""Regenerate docs/ (chNN.html + index.html) from manuscript/chapters/.

One-shot converter for the GitHub Pages site, run deliberately after a
chapter is worth publishing (see docs/workflows/publishing.md). Stdlib only.
"""

from html import escape
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CHAPTERS = ROOT / "manuscript" / "chapters"
DOCS = ROOT / "docs"

TITLE = "Echoes of Fate"
BLURB = (
    "Six lives in Willow Creek, a small town in the mountains, circle the "
    "same eighteen-year-old disappearance — an artist who keeps painting "
    "a place she has never been, a stranger looking for his missing "
    "brother, and four others who have each kept some piece of the truth "
    "to themselves. A contemporary novel about fate, choice, and how one "
    "person's decisions ripple into the lives of everyone around them."
)

PAGE_STYLE = """
  <style>
    body { font-family: Georgia, "Times New Roman", serif; color: #222;
           background: #fdfcf8; margin: 0; }
    main { max-width: 38em; margin: 0 auto; padding: 3em 1.5em 5em; }
    h1 { font-size: 1.5em; line-height: 1.3; font-weight: normal;
         margin: 0 0 1.5em; }
    p { line-height: 1.7; text-align: justify; margin: 0 0 1.1em; }
    hr.scene { border: 0; text-align: center; margin: 2em 0; }
    hr.scene:after { content: "* * *"; color: #888; font-size: 0.8em;
                     letter-spacing: 0.4em; }
    nav.chapters { text-align: center; font-size: 0.9em;
                   margin-top: 3em; color: #555; }
    nav.chapters a { color: #7a5a1e; text-decoration: none; padding: 0 0.6em; }
    nav.chapters a:hover { text-decoration: underline; }
    ul.contents { list-style: none; padding: 0; }
    ul.contents li { margin: 0.45em 0; }
    ul.contents a { color: #7a5a1e; text-decoration: none; }
    ul.contents a:hover { text-decoration: underline; }
    .tagline { font-style: italic; color: #666; }
  </style>
"""


def split_paragraphs(text):
    blocks = []
    for raw in text.split("\n\n"):
        lines = [l.strip() for l in raw.strip().splitlines()]
        if not any(lines):
            continue
        blocks.append(" ".join(lines))
    return blocks


def inline(core):
    core = escape(core)
    core = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", core)
    return core


def page(title, body_html, chapter_num=None, count=26):
    prev = ""
    nxt = ""
    if chapter_num is not None:
        if chapter_num > 1:
            prev = f'<a href="ch{chapter_num-1:02d}.html">&larr; Previous</a>'
        if chapter_num < count:
            nxt = f'<a href="ch{chapter_num+1:02d}.html">Next &rarr;</a>'
    nav = f'<nav class="chapters">{prev}<a href="index.html">Contents</a>{nxt}</nav>' if prev or nxt else ""
    return (
        "<!DOCTYPE html>\n<html><head>\n"
        "<meta charset=\"utf-8\">\n"
        f"<title>{escape(title)} — {escape(TITLE)}</title>\n"
        f"{PAGE_STYLE}\n</head><body>\n<main>\n"
        f"<h1>{escape(title)}</h1>\n"
        f"{body_html}\n"
        f"{nav}\n"
        "</main></body></html>\n"
    )


def chapter_html(path):
    blocks = split_paragraphs(path.read_text())
    title = blocks[0].lstrip("#").strip() if blocks else path.stem
    sub = re.sub(r"^Chapter \d+:\s*", "", title) or title
    body = []
    for block in blocks[1:]:
        if block == "---":
            body.append('<hr class="scene">')
        else:
            body.append(f"<p>{inline(block)}</p>")
    return title, sub, "\n".join(body)


def index_html(chapters):
    rows = "".join(
        f"<li><a href=\"ch{i:02d}.html\">Chapter {i} — {escape(t)}</a></li>"
        for i, (t, _) in enumerate(chapters, start=1)
    )
    return (
        "<!DOCTYPE html>\n<html><head>\n"
        "<meta charset=\"utf-8\">\n"
        f"<title>{escape(TITLE)}</title>\n"
        f"{PAGE_STYLE}\n</head><body>\n<main>\n"
        f"<h1>{escape(TITLE)}</h1>\n"
        f"<p>{BLURB}</p>\n"
        "<ul class=\"contents\">\n"
        f"{rows}\n"
        "</ul>\n"
        "</main></body></html>\n"
    )


def main():
    files = sorted(CHAPTERS.glob("chapter-*.md"))
    chapters = []
    for i, path in enumerate(files, start=1):
        title, sub, body = chapter_html(path)
        chapters.append((sub, body))
        (DOCS / f"ch{i:02d}.html").write_text(
            page(title, body, i, len(files)))
    (DOCS / "index.html").write_text(index_html(chapters))
    print(f"wrote {len(chapters)} chapters + index to {DOCS}")


if __name__ == "__main__":
    main()