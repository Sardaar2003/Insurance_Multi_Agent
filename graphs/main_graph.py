"""
Minimal Enterprise Graph
Auth → Tool Router → Executor → Decision
"""

from langgraph.graph import StateGraph, END
from graphs.state import AgentState

from services.auth_service import authenticate
from tools.tool_router import tool_router_node, tool_route_decision
from agents.executor_agent import run_executor_agent


# ============================================================
# FINAL RESPONSE
# ============================================================

def final_node(state):
    """
    Ensure response exists.
    """

    if not state.get("final_response"):
        state["final_response"] = "Information not available."

    return state


# ============================================================
# BUILD GRAPH
# ============================================================

def build_graph():

    graph = StateGraph(AgentState)

    # nodes
    graph.add_node("auth", authenticate)
    graph.add_node("tool_router", tool_router_node)
    graph.add_node("executor", run_executor_agent)
    graph.add_node("final", final_node)

    # entry
    graph.set_entry_point("auth")

    # flow
    graph.add_edge("auth", "tool_router")

    graph.add_conditional_edges(
        "tool_router",
        tool_route_decision,
        {"db": "executor"}
    )

    graph.add_edge("executor", "final")
    graph.add_edge("final", END)

    return graph.compile()