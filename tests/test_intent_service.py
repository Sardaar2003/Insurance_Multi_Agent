from services.intent_service import classify_intent


def test_policy_intent():
    state = {
        "processed_input": "check my policy",
        "logs": []
    }

    result = classify_intent(state)

    assert result["intent"] == "policy"