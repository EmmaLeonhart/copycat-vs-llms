"""H2 — Copycat harness: run the vendored Copycat port on a benchmark item.

Classic Copycat (the FARGitecture) is hardwired to the 26-letter alphabet a–z:
its Slipnet encodes successor/predecessor over those letters. To run it on the
benchmark's *counterfactual* alphabets (permuted letters, Greek, digits) we
**position-map** the item's alphabet onto the first N letters of a–z, run
Copycat, then map answers back.

This is deliberate and is the methodological point: it hands Copycat the *ordered
-list relation* (successor/predecessor) without any alphabet-specific memorization
— exactly the structure the LLM-analogy debate says models must have. So a fair
question becomes "given the relation, does each system apply it?" — and Copycat,
being relation-native, is predicted to be alphabet-agnostic where LLMs are not.

The vendored port (``src/vendor/copycat``, github.com/jalanb/co.py.cat) is pure
Python. ``run(initial, modified, target, iterations)`` returns a distribution:
``{answer: {count, avgtemp, avgtime}}``.
"""

from __future__ import annotations

import logging
import string
import sys
from dataclasses import dataclass
from pathlib import Path

from .benchmark import AnalogyItem

_VENDOR = Path(__file__).resolve().parents[1] / "vendor" / "copycat"
if str(_VENDOR) not in sys.path:
    sys.path.insert(0, str(_VENDOR))

_LATIN = string.ascii_lowercase  # 'abc...z'


@dataclass(frozen=True)
class CopycatResult:
    item_id: str
    top_answer: str | None              # most frequent answer (mapped back), or None
    distribution: dict                  # {answer_in_item_alphabet: {count, avgtemp, avgtime}}
    iterations: int

    def is_correct(self, answers: tuple[str, ...]) -> bool:
        return self.top_answer is not None and self.top_answer in answers


class AlphabetTooLargeError(ValueError):
    """Copycat's Slipnet only spans 26 letters; alphabets longer than that can't map."""


def _maps(alphabet: str) -> tuple[dict, dict]:
    """Return (item→latin, latin→item) position-preserving symbol maps."""
    if len(alphabet) > 26:
        raise AlphabetTooLargeError(f"alphabet of length {len(alphabet)} > 26")
    to_latin = {sym: _LATIN[i] for i, sym in enumerate(alphabet)}
    from_latin = {_LATIN[i]: sym for i, sym in enumerate(alphabet)}
    return to_latin, from_latin


def _translate(s: str, mapping: dict) -> str:
    return "".join(mapping[ch] for ch in s)


def solve(item: AnalogyItem, iterations: int = 10) -> CopycatResult:
    """Run Copycat on *item* and return the answer distribution (in the item's
    own alphabet). Raises ``AlphabetTooLargeError`` for >26-symbol alphabets."""
    # Quiet the port's per-trial logging.
    logging.getLogger().setLevel(logging.WARNING)
    from copycat.copycat import run  # noqa: E402  (import after sys.path insert)

    to_latin, from_latin = _maps(item.alphabet)
    a = _translate(item.a, to_latin)
    b = _translate(item.b, to_latin)
    c = _translate(item.c, to_latin)

    raw = run(a, b, c, iterations)  # {latin_answer|None: {count, avgtemp, avgtime}}

    dist: dict = {}
    for ans, stats in raw.items():
        key = _translate(ans, from_latin) if ans else None
        dist[key] = {
            "count": stats["count"],
            "avgtemp": round(stats.get("avgtemp", 0.0), 2),
            "avgtime": round(stats.get("avgtime", 0.0), 1),
        }
    top = max(dist, key=lambda k: dist[k]["count"]) if dist else None
    return CopycatResult(item_id=item.id, top_answer=top, distribution=dist, iterations=iterations)
