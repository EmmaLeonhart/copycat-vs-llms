# Topic-finding loop — candidate research questions (OLD & neglected AI)

**Seed area:** a neglected AI area that is **at least ~10 years old** — a
paradigm with pre-deep-learning roots that the DL/LLM wave sidelined, but that
has a crisp, single-GPU/CPU-tractable question to ask *now*. (Round 2 replaced:
the earlier "modern neglected" slate is dropped in favour of *aged* ones.)
**Status: CHOSEN — #3 (Copycat-style fluid analogy as an LLM-failure probe).**
The user selected it from the shortlist (after redirecting the criterion toward
≥10-year-old paradigms). The locked question now lives in `README.md`,
`CLAUDE.md`, and `docs/index.html`; the literature review (queue step 4) narrows
onto it. #1 (ILP sample efficiency) and #2 (reservoir computing) are kept as
alternative old-paradigm directions.

## Scoring rubric (1–5 each; higher is better) + founding year

- **Age** — how established/old the paradigm is (the new seed criterion; ≥10 yrs)
- **Neg** — how sidelined it is *today*
- **Trac** — tractability on small compute (often CPU-only, hours)
- **Int** — intrinsic interest of a clean modern result
- **Worth** — value of a positive *or* negative result

## Candidate slate

| # | Paradigm (founded) → modern question | Age | Neg | Trac | Int | Worth | Σ |
|---|--------------------------------------|-----|-----|------|-----|-------|---|
| 1 | **Inductive Logic Programming** (Muggleton 1991) → On small *relational* tasks, does modern ILP (e.g. Popper) learn correct rules from **orders of magnitude fewer examples** than a neural net — and where exactly does each break (noise, scale)? A sample-efficiency frontier. | 5 | 4 | 5 | 4 | 5 | **23** |
| 2 | **Reservoir Computing / Echo State Networks** (Jaeger 2001; Maass 2002) → On which sequence tasks does an *untrained* random reservoir still rival a trained RNN at matched params, and what governs the boundary (memory capacity vs. nonlinearity)? | 5 | 4 | 5 | 4 | 4 | **22** |
| 3 | **Analogy via Structure-Mapping / Copycat** (Gentner 1983; Hofstadter & Mitchell 1990s) → Build a tiny Copycat-style solver for letter-string analogies and use it as a *probe* for the analogy cases modern LLMs still botch — old idea as a reasoning benchmark. | 5 | 5 | 4 | 5 | 4 | **23** |
| 4 | **Self-Organizing Maps** (Kohonen 1982) → As a cheap, deterministic alternative to UMAP/t-SNE, does a SOM give **more stable / more faithful** low-dim structure on small data across seeds? A fair modern bake-off. | 5 | 5 | 5 | 3 | 3 | **21** |
| 5 | **Adaptive Resonance Theory** (Grossberg/Carpenter 1987) → ART was an early answer to catastrophic forgetting. Does an ART-style learner resist forgetting better than a same-size MLP on a small task-stream, decades before "continual learning" was a field? | 5 | 5 | 4 | 4 | 4 | **22** |
| 6 | **Genetic Programming** (Koza 1992) → On compute-matched budgets, is classic GP still competitive with LLM-guided program synthesis for small symbolic-regression / program tasks — and on which problem shapes does each win? | 5 | 4 | 4 | 4 | 4 | **21** |
| 7 | **Hyperdimensional Computing / VSA** (Plate, Kanerva 1990s–2000s) → For small classification, how close does a *training-free* HDC classifier get to a tuned MLP, and what is the accuracy-per-joule tradeoff? (Adjacent to maintainer's own VSA work — flagged.) | 5 | 4 | 5 | 3 | 4 | **21** |

## Shortlist (top 3 by Σ)

1. **#3 — Copycat-style analogy as an LLM-failure probe** (1983/1990s). Tied for
   top. Maximum neglect + interest: a beautiful old idea (Hofstadter's Copycat)
   repurposed as a sharp modern probe of where today's LLMs still fail at fluid
   analogy. Tractable (the micro-domain is tiny), and a result is very quotable.
2. **#1 — ILP sample-efficiency frontier** (1991). Tied for top. Most tractable
   (CPU-only), crisp falsifiable claim ("ILP needs ~Nx fewer examples until point
   P, then collapses"), and rides the explainable-AI revival of symbolic methods.
3. **#2 — Reservoir computing: memory vs. nonlinearity** (2001). Clean,
   theory-grounded, single-GPU; "when is training the recurrence even worth it?"
   is an under-asked question with a satisfying boundary to map.

**Recommendation:** **#3 (Copycat analogy probe)** for the most *interesting*
old-idea-meets-modern-failure story, or **#1 (ILP sample efficiency)** for the
most *tractable, defensible* study. Both are ≥30 years old and genuinely
sidelined.

> _Next: user confirms one (or redirects), then it's written into
> README / CLAUDE.md / docs as the locked question; literature review follows._
