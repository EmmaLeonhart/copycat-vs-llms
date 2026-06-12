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
