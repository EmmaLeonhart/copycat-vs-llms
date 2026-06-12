"""Entry point.

    python scripts/run.py                 # summarize the benchmark (no model needed)
    python scripts/run.py --head-to-head  # run Copycat vs. the LLM over the benchmark
        [--model gemma3:12b] [--iterations 10]

``--head-to-head`` writes ``results/scores.json`` (the full report) and prints the
per-class boundary table. It needs a local Ollama serving the model; without it,
the Copycat column still fills and the LLM column records the connection error.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

# The benchmark contains non-ASCII alphabets (e.g. Greek); force UTF-8 stdout so
# this prints on a cp1252 Windows console / CI runner.
try:
    sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
except (AttributeError, ValueError):
    pass

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from copycat_vs_llms.benchmark import CLASSES, load_benchmark  # noqa: E402


def summarize() -> None:
    items = load_benchmark()
    by_class = Counter(it.klass for it in items)
    print(f"Loaded {len(items)} analogy items across {len(by_class)} classes:\n")
    for klass in CLASSES:
        print(f"  {klass:24s} {by_class.get(klass, 0)}")
    print("\nExamples:")
    for klass in CLASSES:
        ex = next((it for it in items if it.klass == klass), None)
        if ex:
            print(f"  [{klass}] {ex.prompt():<22s} -> {' | '.join(ex.answers)}")


def head_to_head(model: str, iterations: int) -> None:
    from copycat_vs_llms.scoring import format_table, run_head_to_head, to_report

    print(f"Running Copycat (x{iterations}) vs. {model} over the benchmark...\n")
    rows = run_head_to_head(model=model, iterations=iterations)
    report = to_report(rows, model)
    out = ROOT / "results"
    out.mkdir(exist_ok=True)
    (out / "scores.json").write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    print(format_table(report))
    errs = [r for r in rows if r.llm_error]
    if errs:
        print(f"\n  ({len(errs)} LLM call(s) errored, e.g. {errs[0].llm_error})")
    print(f"\nWrote {out / 'scores.json'}")


def main() -> None:
    p = argparse.ArgumentParser(description="copycat-vs-llms runner")
    p.add_argument("--head-to-head", action="store_true", help="run Copycat vs. the LLM")
    p.add_argument("--model", default="gemma3:12b", help="Ollama model (default gemma3:12b)")
    p.add_argument("--iterations", type=int, default=10, help="Copycat trials per item")
    args = p.parse_args()
    if args.head_to_head:
        head_to_head(args.model, args.iterations)
    else:
        summarize()


if __name__ == "__main__":
    main()
