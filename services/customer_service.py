def customer_service(state):
    state["domain"] = "customer"

    state["context"] = {"data": "Customer Profile Loaded"}
    state["logs"].append("📄 Customer Service Loaded")

    return state