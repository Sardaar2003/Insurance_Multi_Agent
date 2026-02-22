def evaluate_risk(state):
    state["logs"].append("Risk evaluation")

    # do not touch response
    state["risk_level"] = "low"

    return state