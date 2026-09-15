# Enhancing QA Practices with Claude Code

This case study documents how Anthropic's agentic CLI tool, **Claude Code**, was integrated into our testing lifecycle to accelerate quality engineering for the Booking.com CS Agent Copilot.

## 1. Automated Test Scaffolding & Boundary Generation
Instead of manually typing contract assertions, Claude Code was prompted directly from the terminal:
> `claude "Inspect app/main.py and create parametrized pytest edge cases covering malformed booking IDs and invalid payloads in tests/test_api_deterministic.py"`

Claude Code parsed the Pydantic schemas, identified unhandled boundary conditions, and authored strict HTTP assertion fixtures.

## 2. Synthetic Customer Query Generation
LLMs require diverse linguistic test cases. Claude Code was instructed:
> `claude "Read app/policies.py and generate 15 realistic customer edge-case messages (flight delays, non-refundable hotel emergencies, aggressive tone) in tests/data/synthetic_cases.json"`

This produced structured datasets without requiring manual copy-pasting or mock data services.

## 3. Root Cause Analysis on Eval Regressions
When a DeepEval faithfulness threshold drops below 0.7:
> `claude "Analyze the failed test report from tests/test_llm_evals.py and identify whether the prompt drifted or the system prompt requires stricter guardrails."`

Claude Code isolated policy ambiguity in `policies.py` and recommended system prompt adjustments to eliminate hallucinated voucher amounts.