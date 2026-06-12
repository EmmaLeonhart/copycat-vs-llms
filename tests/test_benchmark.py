"""Tests for the letter-string analogy benchmark (H1). Stdlib unittest, no deps."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from copycat_vs_llms.benchmark import (  # noqa: E402
    CLASSES,
    AnalogyItem,
    load_benchmark,
)


class TestAnalogyItem(unittest.TestCase):
    def test_valid_item_roundtrips(self):
        it = AnalogyItem(
            id="x", klass="standard", a="abc", b="abd", c="ijk", answers=("ijl",)
        )
        self.assertEqual(it.prompt(), "abc : abd :: ijk : ?")
        self.assertEqual(AnalogyItem.from_json(it.to_json()), it)

    def test_unknown_class_rejected(self):
        with self.assertRaises(ValueError):
            AnalogyItem(id="x", klass="nope", a="a", b="b", c="c", answers=("d",))

    def test_symbol_outside_alphabet_rejected(self):
        # '1' is not in the default a-z alphabet.
        with self.assertRaises(ValueError):
            AnalogyItem(id="x", klass="standard", a="a1c", b="abd", c="ijk", answers=("ijl",))

    def test_answer_outside_alphabet_rejected(self):
        with self.assertRaises(ValueError):
            AnalogyItem(id="x", klass="standard", a="abc", b="abd", c="ijk", answers=("ij9",))

    def test_duplicate_alphabet_rejected(self):
        with self.assertRaises(ValueError):
            AnalogyItem(
                id="x", klass="standard", a="a", b="a", c="a", answers=("a",),
                alphabet="aabc",
            )

    def test_empty_answers_rejected(self):
        with self.assertRaises(ValueError):
            AnalogyItem(id="x", klass="standard", a="abc", b="abd", c="ijk", answers=())


class TestBenchmarkCorpus(unittest.TestCase):
    def setUp(self):
        self.items = load_benchmark()

    def test_loads_and_is_nonempty(self):
        self.assertGreater(len(self.items), 0)

    def test_ids_unique(self):
        ids = [it.id for it in self.items]
        self.assertEqual(len(ids), len(set(ids)))

    def test_every_class_represented(self):
        present = {it.klass for it in self.items}
        for klass in CLASSES:
            self.assertIn(klass, present, f"no benchmark items for class {klass!r}")

    def test_ambiguous_items_have_multiple_answers(self):
        amb = [it for it in self.items if it.klass == "ambiguous"]
        self.assertTrue(amb)
        for it in amb:
            self.assertGreater(len(it.answers), 1, f"{it.id} marked ambiguous but has one answer")

    def test_nonambiguous_items_have_one_answer(self):
        for it in self.items:
            if it.klass != "ambiguous":
                self.assertEqual(len(it.answers), 1, f"{it.id} should have a single consensus answer")

    def test_all_items_validate(self):
        # Re-construct each item to re-run __post_init__ validation.
        for it in self.items:
            AnalogyItem.from_json(it.to_json())


if __name__ == "__main__":
    unittest.main()
