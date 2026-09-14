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


class TestChapterFiles(unittest.TestCase):
    def test_chapter_01_exists(self):
        self.assertTrue((MANUSCRIPT / "chapters" / "chapter-01.md").exists())


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
