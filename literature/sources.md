# Sources — per-source notes

One entry per source: claim / method / what it contributes / citation.

---

## Hofstadter & Mitchell 1995 — The Copycat Project (orig. 1988)
- **Where:** *Fluid Concepts and Creative Analogies* (1995); FARG, Indiana.
- **Claim/method:** Analogy = abstract perception. Slipnet (flexing concept net)
  + Workspace + Coderack of codelets running a parallel terraced scan; answers
  letter-string analogies (abc:abd :: ijk:?) with a *distribution* + temperature.
- **Contributes:** The architecture under study; the letter-string domain.

## Copycat (software) — Wikipedia
- **Contributes:** Concise architecture reference (Slipnet/Workspace/Coderack/
  codelets; "active symbol" architecture; parallel terraced scan).

## Saldyt & Brogan 2018 — Reimplementation and Reinterpretation of Copycat
- **arXiv:** 1811.04747
- **Contributes:** Maintained Python 3 reimplementation → recipe-first; the
  symbolic side is cheap to stand up rather than re-derive.

## jalanb — co.py.cat (Python 3 port)
- **Where:** github.com/jalanb/co.py.cat
- **Contributes:** A second runnable Python Copycat (from Boland's Java port).

## Marshall — Metacat
- **Claim:** Self-watching extension of Copycat (reflects on its own analogies).
- **Contributes:** Possible richer baseline / "confidence" source.

## Mitchell 2021 — Abstraction and Analogy-Making in AI
- **arXiv:** 2102.10717
- **Contributes:** Connects Copycat-style domains (letter-strings, Bongard, ARC)
  to deep learning + program synthesis; frames the "old model vs modern method"
  comparison this project instantiates.

## Webb, Holyoak & Lu 2023 — Emergent analogical reasoning in LLMs
- **Where:** Nature Human Behaviour.
- **Claim:** Strong zero-shot LLM analogy, "rivaling humans." The pro-emergence
  pole of the debate; the claim our counterfactual variants stress-test.

## Response: Emergent analogical reasoning in LLMs
- **arXiv:** 2308.16118
- **Claim:** Rebuts the above on modified/counterfactual tasks. The brittleness pole.

## Lewis & Mitchell 2024 — Robustness of Analogical Reasoning in LLMs
- **arXiv:** 2411.14215
- **Claim:** GPT performance drops sharply on letter-string *variants* (permuted/
  novel alphabets; predecessor / second-successor) where humans stay near-ceiling.
- **Contributes:** The counterfactual variant set our benchmark adopts; the exact
  regime where Copycat should, by construction, hold up.

## Can LLMs generalize analogy solving like children can?
- **arXiv:** 2411.02348
- **Contributes:** Developmental angle — humans transfer to unfamiliar domains,
  LLMs don't; motivates "far-analogy" items.

## Webb et al. 2025 — Counterfactual tasks support emergent analogical reasoning
- **Where:** PNAS Nexus.
- **Claim:** LLMs generalize to counterfactual variants *with code execution*.
- **Contributes:** Tells us to run LLMs both plain and code-augmented for fairness.

## Mitchell — Can GPT-3 Make Analogies? (Medium)
- **Contributes:** Accessible early statement of the brittleness case; example items.
