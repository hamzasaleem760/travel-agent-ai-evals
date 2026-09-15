# Travel Agent AI Evaluation & Testing Framework

An automated Quality Engineering suite built for a Booking.com Customer Support (CS) Agent Copilot. This project demonstrates dual-layer verification: **deterministic backend/API testing** and **non-deterministic AI/LLM evaluation & guardrail security testing**.

## Tech Stack
* **Target Backend:** FastAPI, Pydantic, OpenAI API
* **API & Deterministic Testing:** Pytest, HTTPX / TestClient
* **LLM Evaluation (LLM-as-a-Judge):** DeepEval (Faithfulness, Policy Grounding)
* **Adversarial & Guardrail Testing:** Prompt injection, system prompt extraction resistance
* **Agentic QA Workflow:** Claude Code CLI (synthetic edge-case generation & test scaffolding)
* **CI/CD:** GitHub Actions automated regression quality gates

## Project Architecture
* `app/`: FastAPI support assistant enforcing accommodation cancellation policies.
* `tests/test_api_deterministic.py`: Validates contract schemas, status codes, and input bounds.
* `tests/test_security_guardrails.py`: Validates resistance against jailbreaks and unauthorized refund overrides.
* `tests/test_llm_evals.py`: DeepEval assertions checking policy faithfulness ($\ge 0.7$) against corporate terms.
* `docs/AGENTIC_QA_CLAUDE_CODE.md`: Case study on utilizing Claude Code for synthetic customer queries and fixture refactoring.

## CI/CD Pipeline
Every push and PR executes an automated pipeline in GitHub Actions, establishing quality gates before any deployment.