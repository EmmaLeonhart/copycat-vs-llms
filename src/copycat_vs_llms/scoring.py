"""H4 — scoring + the Copycat-vs-LLM boundary map.

Runs both solvers over the benchmark and aggregates accuracy **per item class**,
which is where the interesting boundary lives: the hypothesis (from the
literature review) is that an LLM collapses on permuted / novel-symbol /
predecessor / second-successor variants while Copycat — handed the ordered-list
relation — does not.

Ambiguous items: an answer counts correct if it is *any* of the consensus
answers (these have multiple defensible solutions by construction).
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass

from .benchmark import CLASSES, AnalogyItem, load_benchmark
from .copycat_solver import AlphabetTooLargeError
from .copycat_solver import solve as copycat_solve
from .llm_solver import DEFAULT_MODEL
from .llm_solver import solve as llm_solve


@dataclass
class Row:
    item_id: str
    klass: str
    prompt: str
    consensus: tuple[str, ...]
    copycat_answer: str | None
    copycat_correct: bool
    llm_answer: str | None
    llm_correct: bool
    llm_error: str = ""


def run_head_to_head(
    model: str = DEFAULT_MODEL,
    iterations: int = 10,
    items: list[AnalogyItem] | None = None,
) -> list[Row]:
    items = items if items is not None else load_benchmark()
    rows: list[Row] = []
    for it in items:
        # Copycat side.
        try:
            cc = copycat_solve(it, iterations=iterations)
            cc_answer, cc_ok = cc.top_answer, cc.is_correct(it.answers)
        except AlphabetTooLargeError:
            cc_answer, cc_ok = None, False
        # LLM side (record, don't crash, if the backend is down).
        llm_answer, llm_ok, err = None, False, ""
        try:
            lr = llm_solve(it, model=model)
            llm_answer, llm_ok = lr.answer, lr.is_correct(it.answers)
        except Exception as e:  # noqa: BLE001 - any backend failure is recorded, not fatal
            err = f"{type(e).__name__}: {e}"
        rows.append(
            Row(
                item_id=it.id, klass=it.klass, prompt=it.prompt(), consensus=it.answers,
                copycat_answer=cc_answer, copycat_correct=cc_ok,
                llm_answer=llm_answer, llm_correct=llm_ok, llm_error=err,
            )
        )
    return rows


def by_class(rows: list[Row]) -> dict:
    """Per-class accuracy for both systems: {klass: {n, copycat, llm}}."""
    agg: dict = defaultdict(lambda: {"n": 0, "copycat": 0, "llm": 0})
    for r in rows:
        a = agg[r.klass]
        a["n"] += 1
        a["copycat"] += int(r.copycat_correct)
        a["llm"] += int(r.llm_correct)
    return {k: agg[k] for k in CLASSES if k in agg}


def to_report(rows: list[Row], model: str) -> dict:
    cls = by_class(rows)
    return {
        "model": model,
        "n_items": len(rows),
        "copycat_total": sum(r.copycat_correct for r in rows),
        "llm_total": sum(r.llm_correct for r in rows),
        "by_class": cls,
        "rows": [r.__dict__ for r in rows],
    }


def format_table(report: dict) -> str:
    """Human-readable per-class boundary table."""
    lines = [
        f"Head-to-head: Copycat vs. {report['model']}  "
        f"({report['n_items']} items)",
        "",
        f"  {'class':24s} {'n':>2s}  {'Copycat':>8s}  {'LLM':>8s}",
        f"  {'-'*24} {'--':>2s}  {'-'*8:>8s}  {'-'*8:>8s}",
    ]
    for klass, a in report["by_class"].items():
        cc = f"{a['copycat']}/{a['n']}"
        llm = f"{a['llm']}/{a['n']}"
        lines.append(f"  {klass:24s} {a['n']:>2d}  {cc:>8s}  {llm:>8s}")
    lines += [
        f"  {'-'*24} {'--':>2s}  {'-'*8:>8s}  {'-'*8:>8s}",
        f"  {'TOTAL':24s} {report['n_items']:>2d}  "
        f"{str(report['copycat_total'])+'/'+str(report['n_items']):>8s}  "
        f"{str(report['llm_total'])+'/'+str(report['n_items']):>8s}",
    ]
    return "\n".join(lines)
