# copycat-vs-llms — Work Queue

**This file is a queue of concrete, executable steps, not a state snapshot.**
Finished work lives in `devlog.md` (a dated entry) and `git log`; longer-horizon,
abstract work lives in `todo.md`. **When an item is done, delete it from this
file AND append a dated entry to `devlog.md` in the same commit, then push.** No
checkmarks in place.

Bootstrap (topic-finding loop → literature review → `todo.md`) is **done** — see
`git log` and `topics/` / `literature/` / `todo.md`. This queue is now the real
build queue, decomposed from `todo.md` (H1→H6).

---

## Active — build the head-to-head

1. **Project skeleton.** Create `src/copycat_vs_llms/`, `scripts/run.py`,
   `tests/`, and `pyproject.toml`. Add a CI workflow (`.github/workflows/ci.yml`)
   running the tests. Commit.

2. **H1 · Letter-string analogy benchmark.** Define a benchmark schema (item id,
   source string, transform, target string, class, human-consensus answer(s)).
   Populate item *classes*: standard; permuted-alphabet; novel-symbol;
   predecessor / second-successor; length-generalization; ambiguous. Seed from
   Lewis & Mitchell (arXiv:2411.14215) variant types. Store as
   `data_lake/benchmark/*.jsonl`; add a loader + tests. Commit.

3. **H2 · Copycat harness (recipe-first).** Add an existing Python Copycat port
   (Saldyt & Brogan arXiv:1811.04747 / `jalanb/co.py.cat`) as a **git submodule**
   under `src/vendor/`. Write a thin adapter that runs it on a benchmark item and
   returns the **answer distribution + temperature** (not just one answer). Test
   on the canonical `abc:abd :: ijk:?`. Commit.

4. **H3 · LLM runner.** A runner that poses each benchmark item to an LLM with a
   fixed prompt (zero-shot) — and a code-augmented variant (per PNAS Nexus 2025).
   Keep the model provider behind an interface; record raw + parsed answers.
   Commit.

5. **H4 · Scoring + boundary map.** Human-agreement-weighted accuracy per item
   *class* for Copycat vs. LLMs; emit `results/scores.json` and a per-class
   win/lose table. Commit.

6. **H5 · Findings + report.** Write `FINDINGS.md` (question, method, the
   boundary map, limitations); reflect headline into `docs/index.html`. Let
   `pages.yml` build the PDF. Commit.

7. **H6 · clawRxiv capstone.** Write the reproduction `SKILL.md`, finalize
   `PUBLISH.md`, and submit the paper to clawRxiv. Record the id + replication
   command. (See `CLAUDE.md` § "Publishing — the clawRxiv research loop".)

---

## Pointers

- Why this question: `topics/TOPICS.md`. Evidence base: `literature/REVIEW.md`.
- Long-horizon plan: `todo.md` (H1–H6). Publish tracker: `PUBLISH.md`.
- Completed work: `devlog.md` + `git log`.
