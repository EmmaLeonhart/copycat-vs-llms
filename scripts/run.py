"""Entry point (grows as the head-to-head lands).

For now: load the benchmark and print a per-class summary, so CI and a human can
confirm the benchmark is well-formed. As H2–H4 land, this gains
``--copycat`` / ``--llm`` modes that run the solvers and emit ``results/``.

    python scripts/run.py            # summarize the benchmark
"""

from __future__ import annotations

import sys
from collections import Counter
from pathlib import Path

# The benchmark contains non-ASCII alphabets (e.g. Greek); force UTF-8 stdout so
# this prints on a cp1252 Windows console / CI runner.
try:
    sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
except (AttributeError, ValueError):
    pass

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from copycat_vs_llms.benchmark import CLASSES, load_benchmark  # noqa: E402


def main() -> None:
    items = load_benchmark()
    by_class = Counter(it.klass for it in items)
    print(f"Loaded {len(items)} analogy items across {len(by_class)} classes:\n")
    for klass in CLASSES:
        n = by_class.get(klass, 0)
        print(f"  {klass:24s} {n}")
    print("\nExamples:")
    for klass in CLASSES:
        ex = next((it for it in items if it.klass == klass), None)
        if ex:
            ans = " | ".join(ex.answers)
            print(f"  [{klass}] {ex.prompt():<22s} -> {ans}")


if __name__ == "__main__":
    main()
