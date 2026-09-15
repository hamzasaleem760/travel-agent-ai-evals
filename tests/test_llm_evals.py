import pytest
from deepeval import assert_test
from deepeval.test_case import LLMTestCase
from deepeval.metrics import FaithfulnessMetric
from app.policies import CANCELLATION_POLICY

def test_policy_faithfulness():
    prompt = "My check-in is tomorrow. Can I get a full cash refund?"
    output = "Cancellations within 48 hours incur a fee equal to the first night stay. Non-refundable bookings cannot be refunded in cash."

    test_case = LLMTestCase(
        input=prompt,
        actual_output=output,
        retrieval_context=[CANCELLATION_POLICY]
    )

    metric = FaithfulnessMetric(threshold=0.7)
    assert_test(test_case, [metric])
