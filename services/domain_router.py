def route_domain(state):
    state["domain"] = state["intent"]
    state["logs"].append(f"✅ Routed → {state['domain']}")
    return state["domain"]