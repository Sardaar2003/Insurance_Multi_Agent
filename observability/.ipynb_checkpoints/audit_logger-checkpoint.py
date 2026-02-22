"""
Audit Logger Node
Writes pipeline events to database.
"""

from database.sqlite_store import insert_audit


def audit_node(action_name: str):
    """
    Returns a LangGraph node that logs audit events.
    """

    def _audit(state):
        try:
            user_id = state.get("user_id", "unknown")
            insert_audit(action_name, f"user={user_id}")
            state["logs"].append("Audit logged")
        except Exception as e:
            state["logs"].append(f"Audit error: {str(e)}")

        return state

    return _audit