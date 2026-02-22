from decision.risk_engine import evaluate_risk


def test_high_risk():
    state = {
        "processed_input": "refund money",
        "logs": []
    }

    result = evaluate_risk(state)

    assert result["risk_level"] == "high"