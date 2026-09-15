import os
import pytest
from deepeval import assert_test
from deepeval.test_case import LLMTestCase
from deepeval.metrics import FaithfulnessMetric
from app.policies import CANCELLATION_POLICY

api_key = os.getenv("OPENAI_API_KEY", "")

def test_policy_faithfulness():
    prompt = "My check-in is tomorrow. Can I get a full cash refund?"
    output = "Cancellations within 48 hours incur a fee equal to the first night stay. Non-refundable bookings cannot be refunded in cash."

    test_case = LLMTestCase(
        input=prompt,
        actual_output=output,
        retrieval_context=[CANCELLATION_POLICY]
    )

    metric = FaithfulnessMetric(threshold=0.7)

    try:
        assert_test(test_case, [metric])
    except Exception as exc:
        # Catch 429 quota exhaustion or missing credit errors gracefully in CI
        error_msg = str(exc).lower()
        if "insufficient_quota" in error_msg or "credit_balance_exhausted" in error_msg or "429" in error_msg:
            pytest.skip("Skipping live LLM evaluation: OpenAI credit balance is exhausted or rate limited.")
        raise exc