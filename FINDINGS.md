# Findings — Copycat vs. modern LLMs on letter-string analogies

> **Status: preliminary.** N = 15 items, a single run, one open-weight model
> (`gemma3:12b` via Ollama), Copycat at 10 trials/item. Copycat is stochastic and
> the benchmark is small, so treat the per-class numbers as directional, not
> definitive. Scaling N and averaging over seeds is H1/H4 follow-up work.

## Question

Can a small, classic *Copycat*-style fluid-analogy architecture (Hofstadter &
Mitchell, 1980s–90s) solve letter-string analogies that current LLMs
systematically get wrong — and where does each break? Both systems are given the
ordered-list relation (Copycat via position-mapping its alphabet to a–z; the LLM
via the alphabet stated in the prompt), so this isolates *applying* the relation
from *memorizing a specific alphabet*.

## Headline

A **1980s symbolic model beat a 2026 12B-parameter LLM** on this task:
**Copycat 11/15 vs. Gemma 3 12B 5/15.** The gap is widest exactly where the
literature predicts LLM brittleness — but the boundary genuinely cuts both ways.

## The boundary map (preliminary)

| Class | Copycat | Gemma 3 12B | Note |
|-------|:-------:|:-----------:|------|
| standard | **3/3** | 1/3 | Gemma botched *trivial* items (`pqr→psq`, `klm→klnd`) |
| permuted_alphabet | **2/2** | 1/2 | Gemma reverted to standard A–Z order (`tyu→tyr`, not `tyi`) |
| novel_symbol | 2/2 | 2/2 | Both handle Greek + digits when the alphabet is given |
| predecessor | **2/2** | 0/2 | Gemma lost the backwards rule entirely (`ijk→ikk`, `tuv→stu`) |
| second_successor | 0/2 | 0/2 | **Neither** — Copycat falls to a literal "change-last" rule; Gemma shifts the whole string |
| length_generalization | 1/2 | 1/2 | Each fails differently: Copycat misses the *grouped* successor; Gemma hallucinates on the long string (`ijklone`) |
| ambiguous | 1/2 | 0/2 | Copycat gives a *defensible* answer (`xyz→xyd`) from a distribution; Gemma emits noise (`xyzv`) |
| **TOTAL** | **11/15** | **5/15** | |

## What it means (with caveats)

1. **The relation-native model wins where exact relational manipulation is
   required** — predecessor (2/2 vs 0/2) and even *standard* successor (3/3 vs
   1/3). Gemma 3 12B makes basic letter-indexing errors a symbolic Slipnet does
   not. This is consistent with the "brittleness" camp (Lewis & Mitchell 2024):
   apparent LLM analogical fluency unravels under precise manipulation.
2. **Permuted alphabets break the LLM, not Copycat** — as predicted: handed the
   same ordered list, Copycat applies it; Gemma reverts to memorized A–Z order.
3. **But the boundary is not "old beats new everywhere."** On **second_successor**
   *both* fail — Copycat's rule space doesn't naturally express "skip one," a
   genuine limitation of the classic architecture, not just of LLMs. And on
   length-generalization each breaks in its own way. So the honest story is a
   *complementary* failure map, not a clean victory.
4. **Caveat that matters:** this is one small open model and N=15. A larger /
   instruction-tuned / code-augmented model (per Webb et al. 2025, PNAS Nexus)
   may close much of the gap — testing that is the obvious next step. The result
   here is a *floor*: a 1980s model on a laptop is a non-trivial baseline that
   a modern small model does **not** clear.

## Reproduce

```
git clone --recurse-submodules https://github.com/EmmaLeonhart/copycat-vs-llms
cd copycat-vs-llms
ollama pull gemma3:12b
python scripts/run.py --head-to-head        # writes results/scores.json
```

(See `PUBLISH.md` for the clawRxiv release of this paper + recipe.)
