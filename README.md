# original-neglected-2

> An **original-research project** scaffolded with
> [cleanvibe](https://github.com/Immanuelle/cleanvibe) `original`.

**Focus area:** Fluid analogy-making (Hofstadter & Mitchell's *Copycat*, 1980s–90s) — an old, sidelined paradigm.
**Research question:** Can a small classic *Copycat*-style fluid-analogy architecture solve letter-string analogy problems that current LLMs systematically get wrong — and where does each break? We build a tiny analogy benchmark, run a Copycat-style solver against current LLMs, and map each one's failure boundary.

## About

This is an original-research project with an **uncertain topic**. It is
`cleanvibe research` plus an up-front **topic-finding loop**: it explores the
focus area, generates and scores candidate research questions, and converges on
one *before* the literature review narrows in — then runs experiments / builds
something to answer it and publishes the findings as a themed GitHub Pages
report + a transportable PDF.

The distinctive first move is **topic finding** (see `topics/`); the second is a
**literature review** (agentic RAG) on the chosen question (see `literature/`).

## How it's organized

- `topics/` — the topic-finding loop (candidates + scoring + `TOPICS.md`), first.
- `literature/` — the literature review on the chosen question (sources + `REVIEW.md`).
- `data_lake/` — datasets and supplied material.
- `src/` — the research code; `scripts/run.py` — the run entry point.
- `results/` — run outputs (gitignored). `FINDINGS.md` — the write-up.
- `docs/` — the published GitHub Pages report site (themed) + built PDF.
- `queue.md` / `todo.md` / `devlog.md` — the cleanvibe work loop.

## Getting started

```
cd original-neglected-2
claude
```

Then work `queue.md` top to bottom. The bootstrap sequence runs the
topic-finding loop to choose the question, runs the literature review on it,
plans the experiments, takes the repo public, and keeps the report current as
results land.

## Published report

Once the repo is public with Pages set to **Source: GitHub Actions**,
`.github/workflows/pages.yml` deploys `docs/` (the report site) and builds
`docs/report.pdf`. Site-shape inspiration: http://latent-space.emmaleonhart.com/
