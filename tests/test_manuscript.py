"""Automated consistency checks for the Echoes of Fate manuscript project.

This is not a test suite for code — it's a test suite for the *manuscript's
structure and internal consistency*, per docs/workflows/continuity-testing.md.
Run with:

    python3 -m unittest discover -s tests

If a check fails, fix the manuscript/character/outline file it's checking —
don't weaken the check to make it pass, unless the check itself is wrong.
"""

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANUSCRIPT = ROOT / "manuscript"
CHARACTERS = ROOT / "characters"
SCENES = ROOT / "scenes"
DOCS_WORKFLOWS = ROOT / "docs" / "workflows"

CHARACTER_NAMES = ["sarah", "michael", "emma", "jack", "olivia", "liam"]

TARGET_CHAPTER_COUNT = 26


def _outline_text():
    return (MANUSCRIPT / "outline.md").read_text(encoding="utf-8")


class TestOutline(unittest.TestCase):
    def test_outline_file_exists(self):
        self.assertTrue((MANUSCRIPT / "outline.md").exists())

    def test_outline_declares_target_length(self):
        text = _outline_text()
        self.assertIn("200 pages", text)
        self.assertIn("26 chapters", text)

    def test_outline_has_26_chapter_rows(self):
        text = _outline_text()
        rows = re.findall(r"^\|\s*(\d+)\s*\|", text, flags=re.MULTILINE)
        self.assertEqual(
            len(rows),
            TARGET_CHAPTER_COUNT,
            f"expected {TARGET_CHAPTER_COUNT} chapter rows, found {len(rows)}",
        )

    def test_chapter_numbers_are_sequential_from_1(self):
        text = _outline_text()
        rows = [int(n) for n in re.findall(r"^\|\s*(\d+)\s*\|", text, flags=re.MULTILINE)]
        self.assertEqual(rows, list(range(1, TARGET_CHAPTER_COUNT + 1)))


class TestCharacterFiles(unittest.TestCase):
    def test_all_character_files_exist(self):
        for name in CHARACTER_NAMES:
            with self.subTest(character=name):
                self.assertTrue((CHARACTERS / f"{name}.md").exists())

    def test_no_unconfirmed_relationship_markers_remain(self):
        for name in CHARACTER_NAMES:
            text = (CHARACTERS / f"{name}.md").read_text(encoding="utf-8")
            with self.subTest(character=name):
                self.assertNotIn(
                    "unconfirmed",
                    text.lower(),
                    f"{name}.md still has an unresolved relationship marker",
                )

    def test_central_mystery_plot_thread_recorded(self):
        for name in CHARACTER_NAMES:
            text = (CHARACTERS / f"{name}.md").read_text(encoding="utf-8")
            with self.subTest(character=name):
                self.assertIn(
                    "Plot thread",
                    text,
                    f"{name}.md has no recorded connection to the central mystery",
                )

    def test_readme_records_resolved_decisions(self):
        text = (CHARACTERS / "README.md").read_text(encoding="utf-8")
        self.assertIn("Resolved decisions", text)
        self.assertIn("Daniel", text)


class TestSettingFile(unittest.TestCase):
    def test_willow_creek_timeframe_and_venue_resolved(self):
        text = (SCENES / "willow-creek.md").read_text(encoding="utf-8")
        self.assertIn("Harvest Festival", text)
        self.assertIn("six weeks", text.lower())


class TestPlotMap(unittest.TestCase):
    """scenes/plot-map.md is the ground truth for the mystery. It was
    originally written by an agent working concurrently with (and without
    seeing the final output of) the character-development agent, which
    produced a real naming conflict (Whitfield/Gerald/"Daniel Cole" vs. the
    character files' Hale/Warren/"Daniel Voss") — reconciled by hand on
    2026-09-14. Guard against that class of drift recurring."""

    def test_plot_map_exists(self):
        self.assertTrue((SCENES / "plot-map.md").exists())

    def test_no_superseded_placeholder_names(self):
        stale_names = ["Whitfield", "Daniel Cole"]
        for path in [SCENES / "plot-map.md"] + [
            CHARACTERS / f"{n}.md" for n in CHARACTER_NAMES
        ] + [CHARACTERS / "README.md"]:
            text = path.read_text(encoding="utf-8")
            for name in stale_names:
                with self.subTest(file=path.name, name=name):
                    self.assertNotIn(name, text)

    def test_plot_map_uses_established_character_names(self):
        text = (SCENES / "plot-map.md").read_text(encoding="utf-8")
        for name in ("Daniel Voss", "Warren Hale", "Hale Development"):
            with self.subTest(name=name):
                self.assertIn(name, text)


class TestTodoTracking(unittest.TestCase):
    def test_story_decisions_checked_off(self):
        text = (ROOT / "TODO.md").read_text(encoding="utf-8")
        section = text.split("## Story decisions")[1].split("##")[0]
        unchecked = re.findall(r"^-\s*\[ \]", section, flags=re.MULTILINE)
        self.assertEqual(
            unchecked, [], "story decisions section still has unchecked items"
        )

    def test_todo_mentions_26_chapter_goal(self):
        text = (ROOT / "TODO.md").read_text(encoding="utf-8")
        self.assertIn("26", text)
        self.assertIn("200 pages", text)


class TestWorkflowDocs(unittest.TestCase):
    EXPECTED = [
        "README.md",
        "outline-design.md",
        "character-development.md",
        "plot-design.md",
        "scene-planning.md",
        "chapter-drafting.md",
        "continuity-testing.md",
        "publishing.md",
    ]

    def test_all_workflow_docs_exist(self):
        for filename in self.EXPECTED:
            with self.subTest(file=filename):
                self.assertTrue((DOCS_WORKFLOWS / filename).exists())

    def test_workflow_docs_have_diagrams(self):
        for filename in self.EXPECTED:
            if filename == "README.md":
                continue
            text = (DOCS_WORKFLOWS / filename).read_text(encoding="utf-8")
            with self.subTest(file=filename):
                self.assertIn("```mermaid", text)


MIN_CHAPTER_WORDS = 700
MAX_CHAPTER_WORDS = 2600

STOCK_PHRASES = [
    "deep blue eyes",
    "dark eyes",
    "carefully constructed facade",
]


class TestChapterFiles(unittest.TestCase):
    def test_chapter_01_exists(self):
        self.assertTrue((MANUSCRIPT / "chapters" / "chapter-01.md").exists())

    def _chapter_files(self):
        return sorted((MANUSCRIPT / "chapters").glob("chapter-*.md"))

    def test_drafted_chapters_meet_minimum_length(self):
        for path in self._chapter_files():
            word_count = len(path.read_text(encoding="utf-8").split())
            with self.subTest(chapter=path.name):
                self.assertGreaterEqual(
                    word_count,
                    MIN_CHAPTER_WORDS,
                    f"{path.name} is {word_count} words, below the "
                    f"{MIN_CHAPTER_WORDS}-word floor (the original Chapter 1 "
                    "draft was ~470 words and was a summary, not a scene — "
                    "this check exists to catch that regression)",
                )
                self.assertLessEqual(
                    word_count,
                    MAX_CHAPTER_WORDS,
                    f"{path.name} is {word_count} words, above the "
                    f"{MAX_CHAPTER_WORDS}-word ceiling",
                )

    def test_no_stock_phrases_in_drafted_chapters(self):
        for path in self._chapter_files():
            text = path.read_text(encoding="utf-8").lower()
            for phrase in STOCK_PHRASES:
                with self.subTest(chapter=path.name, phrase=phrase):
                    self.assertNotIn(phrase, text)


class TestStyleGuide(unittest.TestCase):
    def test_style_guide_exists(self):
        self.assertTrue((MANUSCRIPT / "style-guide.md").exists())

    def test_style_guide_covers_all_characters(self):
        text = (MANUSCRIPT / "style-guide.md").read_text(encoding="utf-8")
        for name in CHARACTER_NAMES:
            with self.subTest(character=name):
                self.assertIn(name.capitalize(), text)

    def test_style_guide_states_core_conventions(self):
        text = (MANUSCRIPT / "style-guide.md").read_text(encoding="utf-8")
        for term in ("past tense", "close third", "1,900", "show"):
            with self.subTest(term=term):
                self.assertIn(term, text.lower())


class TestTextEncoding(unittest.TestCase):
    """Regression test: README.md was once silently UTF-16 and unreadable
    as plain text. Make sure no tracked text file regresses to that."""

    SKIP_DIRS = {".git", "node_modules"}
    TEXT_SUFFIXES = {".md", ".txt", ".py"}

    def test_all_tracked_text_files_are_valid_utf8(self):
        bad = []
        for path in ROOT.rglob("*"):
            if not path.is_file():
                continue
            if any(part in self.SKIP_DIRS for part in path.parts):
                continue
            if path.suffix not in self.TEXT_SUFFIXES:
                continue
            try:
                path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                bad.append(str(path.relative_to(ROOT)))
        self.assertEqual(bad, [], f"non-UTF-8 text files found: {bad}")


if __name__ == "__main__":
    unittest.main()
