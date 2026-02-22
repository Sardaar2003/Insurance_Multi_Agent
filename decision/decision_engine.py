def make_decision(state):
    """
    Final decision node.
    Must NEVER remove existing response.
    """

    state["logs"].append("Decision engine executed")

    # ⭐ DO NOT overwrite existing response
    if not state.get("final_response"):
        state["final_response"] = (
            state.get("agent_output")
            or "Information not available."
        )

    return state