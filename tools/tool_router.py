"""
Tool Router (Enterprise Pattern)

- tool_router_node → executes and returns state
- tool_route_decision → decides next node
"""


# ============================================================
# NODE (must return state)
# ============================================================

def tool_router_node(state):
    state["logs"].append("🔧 Tool Router Executed")
    return state


# ============================================================
# ROUTING DECISION (returns route key)
# ============================================================

def tool_route_decision(state):
    query = (state.get("processed_input") or state.get("user_input") or "").lower()

    # route profile queries to DB
    if "profile" in query:
        return "db"

    # default route
    return "db"