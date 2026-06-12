"""Tests for the pure parts of the solvers (H2/H3) — no Ollama, no Copycat run.

The live integration paths (running Copycat, calling the LLM) are exercised by
``scripts/run.py --head-to-head`` locally; CI only checks the deterministic glue:
alphabet position-mapping and LLM answer parsing.
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from copycat_vs_llms.benchmark import AnalogyItem  # noqa: E402
from copycat_vs_llms.copycat_solver import (  # noqa: E402
    AlphabetTooLargeError,
    _maps,
    _translate,
)
from copycat_vs_llms.llm_solver import build_prompt, parse_answer  # noqa: E402


class TestAlphabetMapping(unittest.TestCase):
    def test_standard_alphabet_is_identity(self):
        to_latin, from_latin = _maps("abcdefghijklmnopqrstuvwxyz")
        self.assertEqual(_translate("ijk", to_latin), "ijk")
        self.assertEqual(_translate("ijk", from_latin), "ijk")

    def test_permuted_maps_by_position_and_roundtrips(self):
        alpha = "qwertyuiopasdfghjklzxcvbnm"
        to_latin, from_latin = _maps(alpha)
        # 'q' is position 0 -> 'a'; 'w' -> 'b'; 'e' -> 'c'.
        self.assertEqual(_translate("qwe", to_latin), "abc")
        self.assertEqual(_translate(_translate("tyu", to_latin), from_latin), "tyu")

    def test_novel_symbol_alphabet(self):
        to_latin, _ = _maps("0123456789")
        self.assertEqual(_translate("567", to_latin), "fgh")  # 5->f,6->g,7->h

    def test_alphabet_over_26_rejected(self):
        with self.assertRaises(AlphabetTooLargeError):
            _maps("a" * 27)


class TestLLMParsing(unittest.TestCase):
    def _item(self, c="ijk", alphabet="abcdefghijklmnopqrstuvwxyz"):
        return AnalogyItem(id="t", klass="standard", a="abc", b="abd", c=c,
                           answers=("ijl",), alphabet=alphabet)

    def test_prompt_contains_alphabet_and_strings(self):
        p = build_prompt(self._item())
        self.assertIn("a b c", p)            # alphabet is space-joined
        self.assertIn("abc", p)
        self.assertIn("ijk", p)

    def test_parses_bare_answer(self):
        self.assertEqual(parse_answer("ijl", self._item()), "ijl")

    def test_strips_quotes_and_chatter(self):
        raw = 'The answer is:\n"ijl"'
        self.assertEqual(parse_answer(raw, self._item()), "ijl")

    def test_prefers_target_length_candidate(self):
        # A reply with an explanation line plus the answer; pick the len-3 one.
        raw = "abc becomes abd so\nijl"
        self.assertEqual(parse_answer(raw, self._item()), "ijl")

    def test_respects_item_alphabet(self):
        # Greek item: only Greek symbols are valid; latin chatter is ignored.
        it = AnalogyItem(id="g", klass="novel_symbol", a="αβγ", b="αβδ", c="ηθι",
                         answers=("ηθκ",), alphabet="αβγδεζηθικλμνξοπρστυφχψω")
        self.assertEqual(parse_answer("I think it is ηθκ", it), "ηθκ")

    def test_no_valid_answer_returns_none(self):
        self.assertIsNone(parse_answer("12345", self._item()))


if __name__ == "__main__":
    unittest.main()
