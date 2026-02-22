def claims_service(state):
    state["domain"] = "claims"

    state["context"] = {"data": "Claims Data Loaded"}
    state["logs"].append("📄 Claims Service Loaded")

    return state