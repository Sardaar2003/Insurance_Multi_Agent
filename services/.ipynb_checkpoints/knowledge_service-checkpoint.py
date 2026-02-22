def knowledge_service(state):
    state["domain"] = "general"

    state["context"] = {"data": "Knowledge Retrieved"}
    state["logs"].append("📄 Knowledge Retrieved")

    return state