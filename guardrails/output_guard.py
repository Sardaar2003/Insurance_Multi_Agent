def apply_guardrails(state):
    state["logs"].append("Guardrails applied")

    # only block unsafe content
    if "hack" in (state.get("final_response") or "").lower():
        state["final_response"] = "Request blocked."

    return state