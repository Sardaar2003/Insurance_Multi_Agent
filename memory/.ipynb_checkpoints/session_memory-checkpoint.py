def load_session(state):
    if not state.get("domain"):
        state["logs"].append("⚠️ Domain missing before memory")

    state["logs"].append("🧠 Session Memory Updated")
    return state