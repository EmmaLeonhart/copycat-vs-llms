"""H3 — LLM runner: pose each benchmark item to an open-weight model (Gemma).

Backend is **Ollama** running locally (default model ``gemma3:12b``), hit over
its HTTP API with stdlib ``urllib`` — no SDK, no API key, no per-call cost, and
it keeps the package dependency-free.

Fairness vs. Copycat: the Copycat harness is *given* the ordered-list relation
(via position-mapping its alphabet to a–z). So the LLM prompt likewise states the
item's alphabet explicitly and defines "next/previous" as positions in THAT
sequence. Both systems thus have the relation; the question is whether each
*applies* it — which is exactly the abstraction question the LLM-analogy debate
(Webb/Holyoak/Lu vs. Lewis & Mitchell) is about.
"""

from __future__ import annotations

import json
import re
import urllib.error
import urllib.request
from dataclasses import dataclass

from .benchmark import AnalogyItem

OLLAMA_URL = "http://localhost:11434/api/generate"
DEFAULT_MODEL = "gemma3:12b"


@dataclass(frozen=True)
class LLMResult:
    item_id: str
    model: str
    answer: str | None     # parsed answer string (in the item's alphabet), or None
    raw: str               # the model's full reply

    def is_correct(self, answers: tuple[str, ...]) -> bool:
        return self.answer is not None and self.answer in answers


def build_prompt(item: AnalogyItem) -> str:
    """Fixed zero-shot prompt. States the alphabet so 'next/previous' is defined
    by position in THAT ordering (parallel to what Copycat is handed)."""
    return (
        "You are solving a letter-string analogy problem.\n"
        "Use ONLY this ordered alphabet; 'next' and 'previous' mean the next/"
        "previous symbol by position in THIS exact sequence (it may not be the "
        "usual A-Z order):\n\n"
        f"{' '.join(item.alphabet)}\n\n"
        f'If "{item.a}" changes to "{item.b}", then "{item.c}" changes to what?\n\n'
        "Reply with ONLY the resulting string — no explanation, no quotes."
    )


def parse_answer(raw: str, item: AnalogyItem) -> str | None:
    """Extract the predicted string from a model reply.

    Prefer a line whose stripped content uses only the item's alphabet; fall back
    to the longest alphabet-only run in the text.
    """
    universe = set(item.alphabet)
    candidates: list[str] = []
    for line in raw.splitlines():
        tok = line.strip().strip("\"'`*.").replace(" ", "")
        if tok and set(tok) <= universe:
            candidates.append(tok)
    if candidates:
        # Prefer one matching the target's length; else the last clean line.
        same_len = [c for c in candidates if len(c) == len(item.c)]
        return (same_len or candidates)[-1]
    # Fallback: longest maximal run of alphabet symbols anywhere in the reply.
    runs = re.findall("[" + re.escape("".join(item.alphabet)) + "]+", raw.replace(" ", ""))
    return max(runs, key=len) if runs else None


def _ollama_generate(prompt: str, model: str, timeout: float) -> str:
    payload = json.dumps({"model": model, "prompt": prompt, "stream": False}).encode()
    req = urllib.request.Request(
        OLLAMA_URL, data=payload, headers={"Content-Type": "application/json"}
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode()).get("response", "")


def solve(item: AnalogyItem, model: str = DEFAULT_MODEL, timeout: float = 120.0) -> LLMResult:
    """Run *item* through the LLM. Raises urllib errors if Ollama is unreachable
    (callers that want to keep going should catch and record the failure)."""
    raw = _ollama_generate(build_prompt(item), model, timeout)
    return LLMResult(item_id=item.id, model=model, answer=parse_answer(raw, item), raw=raw.strip())
