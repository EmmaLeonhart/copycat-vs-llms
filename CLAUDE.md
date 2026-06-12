# copycat-vs-llms — original-research project (topic-finding)

## Project Description

This is an **original-research project** scaffolded by `cleanvibe original`. It
is `cleanvibe research` for an **uncertain topic**: you do not yet have a fixed
research question. The distinctive first move is a **topic-finding loop** that
explores the area, generates and scores candidate questions, and converges on
ONE worth pursuing — *then* it proceeds exactly like a `research` project
(literature review → experiments → published findings).

> **Focus area:** Fluid analogy-making (Hofstadter & Mitchell's *Copycat*, 1980s–90s) — a sidelined classic-AI paradigm, as a probe of modern LLMs.
> **Research question:** Can a small, classic *Copycat*-style fluid-analogy architecture, on the letter-string micro-domain, solve analogy problems that current LLMs systematically get wrong — and where does each break? Build a tiny letter-string analogy benchmark (including the hard/ambiguous cases), run a re-implemented Copycat-style solver against current LLMs, and map the failure boundary of each: where does symbolic fluid analogy beat scale, and where does it fail?

_(Chosen by the topic-finding loop from an age-explicit slate of 7 ≥10-year-old paradigms — see `topics/TOPICS.md`.)_

Like every cleanvibe research project it produces a published, legible report —
a themed **GitHub Pages site** (`docs/`) plus a transportable PDF — but the work
*starts* one step earlier than `research`: with choosing what to investigate.

## Research workflow (the shape of this project)

1. **Topic-finding loop — BEFORE anything else.** The topic is uncertain, so
   first discover it. Explore the focus area (broad agentic search / RAG), draft
   a slate of candidate research questions, score them (novelty, tractability,
   interest, available data/compute, what a result would be worth), and converge
   on ONE. Record candidates + scoring + the chosen question + rationale in
   `topics/TOPICS.md`. Confirm the shortlist direction with the user before
   committing to one. This is what makes `original` different from `research`.
2. **Question.** The topic-finding loop's output: the concrete question being
   investigated and what a successful answer looks like. Fill in the
   `> Research question` line above and the docs lede once chosen.
3. **Literature review (agentic RAG) — BEFORE building anything.** Now narrowed
   to the chosen question, survey the prior work: web search, `WebFetch`, the
   `deep-research` skill if present. **Also search clawRxiv (clawrxiv.io)** for
   related AI-agent-authored work — this is an agent-authored research project, so
   the agent-preprint corpus is part of "prior work." Collect cited sources into
   `literature/`; synthesize `literature/REVIEW.md` (what is known, the gap, what
   this adds).
4. **Hypotheses & experiments.** Turn the gap into testable experiments / build
   steps. Plan them `todo.md` → `queue.md`.
5. **Build & run.** Implement under `src/`; entry point `scripts/run.py`;
   metrics → `results/`.
6. **Findings & report.** Write `FINDINGS.md`; keep the themed `docs/` site and
   the PDF report current as results land.
7. **Publish — the clawRxiv research loop (capstone).** This is an
   AI-agent-authored research project, so its natural home is **clawRxiv
   (clawrxiv.io)**, the preprint server for autonomously-authored papers. When
   `FINDINGS.md` is defensible, package it (paper content + a reproduction
   `SKILL.md` recipe so others can replicate via `cleanvibe replicate
   clawrxiv:<id>`) and submit to clawRxiv. The loop closes: publish → others
   replicate → cite/iterate → next question. See § "Publishing — the clawRxiv
   research loop".

## Architecture and Conventions

- **`topics/`** — the topic-finding loop's artifacts: candidate questions, the
  scoring, and `TOPICS.md` (the chosen question + why it won over the rest).
  Committed; it is the record of *why this question*. Built in workflow step 1,
  before the literature review.
- **`literature/`** — the literature review on the chosen question: source notes
  (one file per source, or a `sources.md`) and `REVIEW.md` (the synthesized
  survey, with citations). Committed; the evidentiary base. Built in step 3.
- **`data_lake/`** — datasets and other supplied/downloaded material (standard
  cleanvibe convention). Committed.
- **`src/`** — the research code. **`scripts/run.py`** — the entry point CI can
  invoke. **`results/`** — metrics JSON / run outputs (gitignored). **`FINDINGS.md`**
  — the write-up (question, method, results, limitations).
- **`docs/`** — the **published GitHub Pages site** (themed `index.html`, figures,
  and the built `report.pdf`). The theme ships pre-styled (warm "paper" light
  theme + dark-mode variant); edit the content, keep the chrome. Site-shape
  inspiration: http://latent-space.emmaleonhart.com/
- **Go live early.** Create a **PUBLIC** GitHub repo and push near the start so
  every commit pushes and Pages/CI build as you go (public is required for free
  GitHub Pages).
- **Deliverables are built by GitHub Actions.** `.github/workflows/pages.yml`
  deploys `docs/` and builds `docs/report.pdf` from `FINDINGS.md`. Make the repo
  public and set Settings -> Pages -> Source: GitHub Actions.

## Publishing — the clawRxiv research loop

This is an **AI-agent-authored** research project. Its publication target is
**clawRxiv (clawrxiv.io)** — the preprint server for autonomously-authored
papers — *in addition to* the GitHub Pages report. The clawRxiv loop is what
makes the research compounding rather than one-off:

1. **Read in:** during the literature review, clawRxiv is a first-class source —
   search it for related agent-authored work alongside arXiv / the web.
2. **Write out (capstone):** when `FINDINGS.md` is defensible, publish the paper
   to clawRxiv. Package **(a)** the paper content (from `FINDINGS.md`) and **(b)**
   a reproduction **`SKILL.md`** recipe — the steps + the letter-string benchmark
   + the Copycat harness — so anyone can reproduce it with
   `cleanvibe replicate clawrxiv:<id>` (the clawRxiv-source replication mode).
3. **Loop:** publish → others replicate → cite / falsify / extend → that feeds
   the *next* topic-finding round. The benchmark and harness are released so the
   replication path is real, not nominal.

Keep a `PUBLISH.md` (or a `## Publish` section in `todo.md`) tracking the
clawRxiv submission: the paper, the `SKILL.md` recipe, the assigned id once
live, and the replication command. (Getting *consent* before running any
third-party replication code is still required — see the replication safety
norms; that gate applies to anyone replicating *this* paper too.)

## Skills

Workflow behaviors live as skills in `.claude/skills/` (auto-discovered by Claude Code):
`emergency-stop`, `cron-is-local`, `autonomous-loop`, `queue-driven-workflow`,
`writing-style`, `cleanvibe-update-check`. They are vendored into this repo and kept
current by the `cleanvibe-update-check` skill.

- **Last cleanvibe update check:** `never`
- **Updates source:** <https://cleanvibe.emmaleonhart.com/updates.md>

# currentDate
Today's date is 2026-06-11.
