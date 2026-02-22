"""
Authentication Service
"""

from database.sqlite_store import get_conn


# ============================================================
# LOGIN (Streamlit UI)
# ============================================================

def login_user(username, password):

    conn = get_conn()

    row = conn.execute(
        "SELECT role FROM users WHERE username=? AND password=?",
        (username, password)
    ).fetchone()

    conn.close()

    if row:
        return row[0]

    return None


# ============================================================
# LANGGRAPH NODE
# ============================================================

def authenticate(state):
    """
    Only validate user exists.
    DO NOT block pipeline.
    """

    user_id = state.get("user_id")
    role = state.get("role")

    state["logs"].append(f"Auth check: user={user_id}, role={role}")

    # mark authentication status
    if user_id and role:
        state["authenticated"] = True
    else:
        state["authenticated"] = False

    # NEVER set final_response here
    return state