# copycat-vs-llms — Devlog

**This file is where "done" lives.** `queue.md` is delete-only: when a queue
item is finished, the item is **deleted from `queue.md`** and a dated entry
is **appended here**, in the same commit as the work, then pushed. Never
tick a box in place — a checked box left in `queue.md` is the failure mode
this file exists to prevent.

Also record releases (tag + a one-line note), notable milestones, and
anything else worth a chronological trail. Newest entries at the bottom.

This is the **same convention as the cleanvibe repo's own `devlog.md`** —
every cleanvibe-scaffolded project gets one for the same reason.

See `CLAUDE.md` § "Workflow Rules" and `queue.md`'s preamble.

---

## 2026-06-11 — Project scaffolded

Scaffolded with `cleanvibe new` (cleanvibe v1.16.0). Future entries
land here as queue items get deleted.

## 2026-06-11 — Public, clawRxiv loop, and the H1 benchmark

- **Bootstrap complete** (in prior commits): topic-finding loop (chose Copycat
  vs. LLMs from an "old & neglected" slate) → literature review (12 sources;
  Copycat ports exist, LLM-analogy debate is live) → `todo.md` (H1–H6).
- **Promoted to a standalone public repo:** github.com/EmmaLeonhart/copycat-vs-llms
  (renamed from the cleanvibe scratch project; Pages auto-enables on first build).
- **Added the clawRxiv research loop** (it was missing from the cleanvibe
  `original`/`research` scaffold): clawRxiv is now a literature-review source AND
  the publish capstone (paper + `SKILL.md` recipe → clawrxiv.io, replicable via
  `cleanvibe replicate clawrxiv:<id>`). `CLAUDE.md` § "Publishing", README,
  `todo.md` H6, and a `PUBLISH.md` tracker.
- **H1 · the letter-string analogy benchmark** landed: `AnalogyItem` schema +
  loader (`src/copycat_vs_llms/benchmark.py`, zero-dependency), 15 seed items
  across all 7 classes (standard / permuted-alphabet / novel-symbol / predecessor
  / second-successor / length-generalization / ambiguous), each carrying an
  explicit `alphabet` so the counterfactual variants work. `scripts/run.py`
  summary, 12 unittest tests (all pass), and `.github/workflows/ci.yml` (ubuntu +
  windows × py3.9/3.12).

## 2026-06-11 — H2–H4 + preliminary findings: Copycat 11/15 vs Gemma 3 12B 5/15

- **H2 · Copycat harness** (`src/copycat_vs_llms/copycat_solver.py`): vendored the
  `jalanb/co.py.cat` port as a git submodule under `src/vendor/copycat`; adapter
  position-maps each item's alphabet onto a–z so classic Copycat (hardwired to
  a–z) runs on the permuted / Greek / digit variants, then maps answers back.
  Returns the full answer distribution + avg temperature.
- **H3 · Gemma runner** (`llm_solver.py`): zero-dep `urllib` call to local Ollama
  (`gemma3:12b`); prompt states the item's alphabet (so the LLM is handed the same
  ordered-list relation Copycat gets); robust answer parser.
- **H4 · scoring** (`scoring.py` + `scripts/run.py --head-to-head`): per-class
  boundary table, writes `results/scores.json`.
- **Preliminary result (N=15, single run): Copycat 11/15, Gemma 3 12B 5/15.**
  Copycat wins where exact relational manipulation is needed (standard 3/3 vs 1/3;
  predecessor 2/2 vs 0/2; permuted 2/2 vs 1/2). But the boundary is complementary,
  not a sweep: *both* fail second_successor (0/2 each — Copycat's rule space can't
  express "skip one"), and length-generalization splits. Written up in
  `FINDINGS.md` (heavily caveated) + the `docs/` report.
- **Tests:** +10 CI-safe unit tests for the pure glue (alphabet mapping, LLM
  answer parsing); 22 total pass. Live paths (running Copycat / calling Ollama)
  stay out of CI by design.
