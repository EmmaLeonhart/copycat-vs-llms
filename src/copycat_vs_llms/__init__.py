"""copycat-vs-llms — a head-to-head between Hofstadter & Mitchell's Copycat
fluid-analogy model and modern LLMs on letter-string analogies.

The package is split so the cheap, deterministic parts (the benchmark) have no
dependencies and can be tested in CI without API keys or third-party code.
"""

__version__ = "0.1.0"
