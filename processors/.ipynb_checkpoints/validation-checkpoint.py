def validate_input(state):
    text = state["user_input"]
    if not text:
        raise ValueError("Empty input")
    state["logs"].append("✅ Input Validated")
    return state