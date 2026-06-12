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

## Active — scale the result, then publish

Preliminary head-to-head is done and live (Copycat 11/15 vs. Gemma 3 12B 5/15;
see `FINDINGS.md` + `docs/`). Remaining:

1. **H5b · Scale + robustify.** Grow the benchmark to ≥10 items per class
   (especially the discriminating ones: permuted, predecessor, second-successor).
   Average Copycat over multiple seeds and report per-class accuracy with error
   bars (it is stochastic; N=15 single-run is too thin to publish). Optionally add
   a larger / code-augmented model (per Webb et al. 2025) to test whether the gap
   closes. Update `FINDINGS.md` + `docs/` with the firmed-up numbers.

2. **H6 · clawRxiv capstone.** Write the reproduction `SKILL.md` (steps +
   benchmark + Copycat harness), finalize `PUBLISH.md`, and submit the paper to
   clawRxiv. Record the id + replication command. (See `CLAUDE.md` § "Publishing —
   the clawRxiv research loop".)

---

## Pointers

- Why this question: `topics/TOPICS.md`. Evidence base: `literature/REVIEW.md`.
- Long-horizon plan: `todo.md` (H1–H6). Publish tracker: `PUBLISH.md`.
- Completed work: `devlog.md` + `git log`.
