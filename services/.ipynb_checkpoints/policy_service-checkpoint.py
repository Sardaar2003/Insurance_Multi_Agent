def policy_service(state):
    state["domain"] = "policy"   # ⭐ ADD THIS

    state["context"] = {"data": "Policy Data Loaded"}
    state["logs"].append("📄 Policy Service Loaded")

    return state