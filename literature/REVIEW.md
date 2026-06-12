# Literature review — Copycat fluid analogy as a probe of modern LLMs

**Research question.** Can a small, classic *Copycat*-style fluid-analogy
architecture, on the letter-string micro-domain, solve analogy problems that
current LLMs systematically get wrong — and where does each break? Build a tiny
letter-string analogy benchmark (incl. hard/counterfactual cases), run a
re-implemented Copycat-style solver against current LLMs, and map each one's
failure boundary.

This sits at the intersection of a **30-year-old, sidelined architecture** and a
**live 2023–2026 debate** about whether LLMs do genuine analogy. The review maps
both sides and the specific, un-run experiment that connects them.

---

## 1. The old paradigm: Copycat and the FARGitecture

Hofstadter & Mitchell's **Copycat** (developed 1988; definitive write-up in
*Fluid Concepts and Creative Analogies*, 1995) models analogy-making as **abstract
perception**: concepts in a **Slipnet** (a semantic network whose link-lengths
flex with context) are activated by a situation in the **Workspace** (working
memory), while many small agents (**codelets**) on the **Coderack** run in
parallel — a **parallel terraced scan** — probabilistically building and breaking
structure until an answer crystallizes. Its test domain is **letter-string
analogies** ("abc:abd :: ijk:?"). The whole family — Copycat, **Metacat**
(Marshall; adds self-watching), Tabletop, Seqsee, Musicat — is the **FARGitecture**.
This is the sidelined classic: deeply influential conceptually, almost never run
as a *baseline* in modern ML papers.

**Crucially for a solo project, working reimplementations exist** — recipe-first:
- **jalanb/co.py.cat** — a Python 3 port (from Boland's Java port).
- **Saldyt & Brogan 2018, "Reimplementation and Reinterpretation of the Copycat
  Project"** (arXiv:1811.04747) — a maintained Python 3 reimplementation.
- **eraoul/Fluid-Concepts-and-Creative-Analogies** — companion code.
So the symbolic side is **cheap to stand up**; the work is benchmark design +
the head-to-head, not re-deriving Copycat.

## 2. Mitchell's bridge to modern AI

Mitchell's **"Abstraction and Analogy-Making in Artificial Intelligence"**
(arXiv:2102.10717) explicitly connects Copycat-style idealized domains
(letter-strings, Bongard problems, the **Abstraction and Reasoning Corpus / ARC**)
to deep learning and program synthesis, and argues abstraction is the open
frontier. This is the intellectual frame: our study is one concrete instance of
"old analogy model vs. modern method" that she calls for.

## 3. The live LLM-analogy debate (the modern side)

A genuine, unresolved 2023–2026 controversy:

- **Pro-emergence:** Webb, Holyoak & Lu (2023) reported strong zero-shot LLM
  performance on letter-string/digit-matrix/story analogies, "rivaling humans."
  Extended by **"Evidence from counterfactual tasks supports emergent analogical
  reasoning in LLMs"** (PNAS Nexus 2025) — LLMs generalize to counterfactual
  variants *when allowed to write and execute code*.
- **Brittleness camp:** **"Response: Emergent analogical reasoning in LLMs"**
  (arXiv:2308.16118) and **Lewis & Mitchell, "Evaluating the Robustness of
  Analogical Reasoning in LLMs"** (arXiv:2411.14215) show GPT performance
  **declines sharply** on simple letter-string *variants* (permuted / novel
  alphabets, predecessor / second-successor rules) where humans stay near-ceiling.
- **Developmental angle:** **"Can LLMs generalize analogy solving like children
  can?"** (arXiv:2411.02348) — children transfer to unfamiliar domains; LLMs do
  not.

**Consensus take-away:** apparent LLM analogical fluency is **fragile under
controlled perturbation**, especially on *non-standard alphabets* and rules that
require an explicit ordered-list notion of "next/previous." Genuine abstraction —
deep structure vs. surface cue — "remains elusive."

## 4. The gap this project addresses

The debate is conducted **almost entirely on the LLM side**: papers perturb the
*tasks* and measure *LLMs*, but the **symbolic Copycat model is cited historically,
not run as a live competitor**. Conversely, Copycat papers predate modern LLMs.
**No work puts the actual Copycat architecture and current LLMs on a single,
controlled letter-string benchmark — including the counterfactual/permuted-alphabet
variants that break LLMs — and maps where *each* fails.** Copycat should, by
construction, be alphabet-agnostic about "successor/predecessor" (it operates on
Slipnet relations, not memorized letter sequences), so the prediction is sharp:
**Copycat should hold up exactly on the variants where LLMs collapse, and may fail
where LLMs lean on world knowledge / fuzzy semantics.**

**What this project adds:**
1. **One shared letter-string benchmark**, including the standard set *and* the
   counterfactual variants (permuted alphabet, novel symbols, predecessor /
   second-successor, longer strings) from Lewis & Mitchell.
2. **A genuine head-to-head**: a reimplemented Copycat (recipe-first, off existing
   Python ports) vs. current LLMs, scored identically.
3. **A failure-boundary map**: for each variant class, who wins and *why* —
   turning a 30-year-old architecture into a diagnostic instrument for the
   abstraction gap the LLM-analogy debate keeps circling.

## 5. Method implications (feeding into `todo.md`)

1. **Benchmark.** Curate/generate letter-string items in classes: standard;
   permuted-alphabet; novel-symbol; predecessor / second-successor; length-
   generalization; ambiguous (multiple defensible answers — Copycat gives a
   *distribution*, a feature, not a bug).
2. **Copycat side.** Stand up a Python Copycat port; record its answer
   *distribution* + "temperature"/confidence per item.
3. **LLM side.** Run current LLMs zero-shot (and with code, per the PNAS Nexus
   result) on the identical items, fixed prompts.
4. **Scoring + boundary.** Human-agreement-weighted accuracy per class; report the
   win/lose boundary and a qualitative account of each side's failure mode.

---

### Sources

- Hofstadter & Mitchell 1995 — *The Copycat Project: A Model of Mental Fluidity and Analogy-Making* (in *Fluid Concepts and Creative Analogies*) — orig. 1988
- *Copycat (software)* — Wikipedia (architecture: Slipnet / Workspace / Coderack / codelets)
- Saldyt & Brogan 2018 — *Reimplementation and Reinterpretation of the Copycat Project* — arXiv:1811.04747
- jalanb — *co.py.cat* (Python 3 port) — github.com/jalanb/co.py.cat
- Marshall — *Metacat: A Self-Watching Cognitive Architecture for Analogy-Making*
- Mitchell 2021 — *Abstraction and Analogy-Making in Artificial Intelligence* — arXiv:2102.10717
- Webb, Holyoak & Lu 2023 — *Emergent analogical reasoning in large language models* (Nature Human Behaviour)
- *Response: Emergent analogical reasoning in LLMs* — arXiv:2308.16118
- Lewis & Mitchell 2024 — *Evaluating the Robustness of Analogical Reasoning in LLMs* — arXiv:2411.14215
- *Can LLMs generalize analogy solving like children can?* — arXiv:2411.02348
- Webb et al. 2025 — *Evidence from counterfactual tasks supports emergent analogical reasoning in LLMs* — PNAS Nexus
- Mitchell — *Can GPT-3 Make Analogies?* — Medium

_Full per-source notes in `sources.md`._
