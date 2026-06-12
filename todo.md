# todo.md — long-horizon research plan

**Abstract destinations** (not concrete steps). Pulled here → decomposed into
`queue.md` → executed. See `CLAUDE.md` § "Queue and longer-horizon work".

**Research question:** Can a small classic *Copycat*-style fluid-analogy
architecture solve letter-string analogies that current LLMs systematically get
wrong — and where does each break?

---

## H1 — A controlled letter-string analogy benchmark
Curate/generate items in classes: standard; permuted-alphabet; novel-symbol;
predecessor / second-successor; length-generalization; ambiguous (multiple
defensible answers). Record human-consensus answers (from prior work + light
annotation). This benchmark is itself a contribution.

## H2 — Stand up a Copycat solver (recipe-first)
Adopt an existing Python Copycat port (Saldyt & Brogan / co.py.cat), get it
running on the benchmark, and expose its **answer distribution + temperature** per
item (not just a single answer — the distribution is the point).

## H3 — Run current LLMs on identical items
Zero-shot with fixed prompts, *and* code-augmented (per the PNAS Nexus 2025
result, for fairness). Same items, same scoring as Copycat.

## H4 — The failure-boundary map
Per variant class: human-agreement-weighted accuracy for Copycat vs. LLMs; the
win/lose boundary; a qualitative account of each side's failure mode (LLMs on
permuted alphabets; Copycat where world-knowledge/semantics matter).

## H5 — The deliverable: "old model vs. new model" analogy report
Publish the benchmark, the head-to-head, and the boundary map as a diagnostic of
the abstraction gap the LLM-analogy debate keeps circling. Themed `docs/` site +
`FINDINGS.md` + PDF. Release the benchmark + Copycat harness.

## Stretch
- Add Metacat (self-watching) for a confidence signal.
- Extend beyond letter-strings toward Bongard / a tiny ARC slice (Mitchell's
  bridge) — does the boundary generalize across idealized domains?
- A hybrid: LLM proposes, Copycat-style Slipnet verifies structural consistency.
