"""The letter-string analogy benchmark (H1).

An *item* poses ``a : b :: c : ?`` and records the human-consensus answer(s).
Each item carries an explicit ``alphabet`` (the ordered list that *defines*
successor / predecessor), so the same machinery covers the standard a–z domain,
permuted alphabets, and novel-symbol alphabets — exactly the counterfactual
variants on which LLMs are known to be brittle (Lewis & Mitchell,
arXiv:2411.14215) but a relation-based model like Copycat should not be.

Zero dependencies: stdlib only, so this loads and validates in CI without any
install. The benchmark lives as JSONL under ``data_lake/benchmark/``.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path

# The item *classes* — the axes along which we map the Copycat-vs-LLM boundary.
CLASSES = (
    "standard",            # canonical a–z successor/predecessor analogies
    "permuted_alphabet",   # a–z letters, but order scrambled (successor redefined)
    "novel_symbol",        # non-letter symbol alphabet
    "predecessor",         # rule runs backwards along the alphabet
    "second_successor",    # rule skips one (needs explicit ordered-list notion)
    "length_generalization",  # longer strings / groups
    "ambiguous",           # multiple defensible answers (Copycat gives a distribution)
)

STANDARD_ALPHABET = "abcdefghijklmnopqrstuvwxyz"


@dataclass(frozen=True)
class AnalogyItem:
    """One letter-string analogy problem: ``a : b :: c : ?``."""

    id: str
    klass: str
    a: str
    b: str
    c: str
    answers: tuple[str, ...]          # human-consensus answer(s); >1 ⇒ genuinely ambiguous
    alphabet: str = STANDARD_ALPHABET  # ordered list defining successor/predecessor
    rule_note: str = ""
    source: str = ""
    extra: dict = field(default_factory=dict)

    def __post_init__(self) -> None:
        if self.klass not in CLASSES:
            raise ValueError(f"{self.id}: unknown class {self.klass!r} (allowed: {CLASSES})")
        if not self.answers:
            raise ValueError(f"{self.id}: at least one consensus answer is required")
        if len(set(self.alphabet)) != len(self.alphabet):
            raise ValueError(f"{self.id}: alphabet has duplicate symbols")
        # Every symbol used in a/b/c/answers must be in the item's alphabet.
        universe = set(self.alphabet)
        for label, s in (("a", self.a), ("b", self.b), ("c", self.c)):
            bad = set(s) - universe
            if bad:
                raise ValueError(f"{self.id}: {label}={s!r} uses symbols {bad} not in alphabet")
        for ans in self.answers:
            bad = set(ans) - universe
            if bad:
                raise ValueError(f"{self.id}: answer {ans!r} uses symbols {bad} not in alphabet")

    def prompt(self) -> str:
        """Human/LLM-facing rendering of the problem."""
        return f"{self.a} : {self.b} :: {self.c} : ?"

    def to_json(self) -> dict:
        d = {
            "id": self.id,
            "klass": self.klass,
            "a": self.a,
            "b": self.b,
            "c": self.c,
            "answers": list(self.answers),
            "alphabet": self.alphabet,
            "rule_note": self.rule_note,
            "source": self.source,
        }
        if self.extra:
            d["extra"] = self.extra
        return d

    @classmethod
    def from_json(cls, d: dict) -> "AnalogyItem":
        return cls(
            id=d["id"],
            klass=d["klass"],
            a=d["a"],
            b=d["b"],
            c=d["c"],
            answers=tuple(d["answers"]),
            alphabet=d.get("alphabet", STANDARD_ALPHABET),
            rule_note=d.get("rule_note", ""),
            source=d.get("source", ""),
            extra=d.get("extra", {}),
        )


def benchmark_dir() -> Path:
    """Repo-root ``data_lake/benchmark/`` (independent of CWD)."""
    return Path(__file__).resolve().parents[2] / "data_lake" / "benchmark"


def load_benchmark(path: Path | None = None) -> list[AnalogyItem]:
    """Load every ``*.jsonl`` item under ``data_lake/benchmark/`` (or *path*).

    Validates each item (via ``AnalogyItem.__post_init__``) and that ids are
    unique across the whole benchmark.
    """
    root = path or benchmark_dir()
    items: list[AnalogyItem] = []
    seen: set[str] = set()
    for jsonl in sorted(root.glob("*.jsonl")):
        for lineno, line in enumerate(jsonl.read_text(encoding="utf-8").splitlines(), 1):
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            try:
                item = AnalogyItem.from_json(json.loads(line))
            except (json.JSONDecodeError, KeyError, ValueError) as e:
                raise ValueError(f"{jsonl.name}:{lineno}: {e}") from e
            if item.id in seen:
                raise ValueError(f"{jsonl.name}:{lineno}: duplicate item id {item.id!r}")
            seen.add(item.id)
            items.append(item)
    return items
