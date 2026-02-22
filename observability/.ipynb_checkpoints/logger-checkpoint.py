def log_step(state, message):
    state["logs"].append(message)
    return state