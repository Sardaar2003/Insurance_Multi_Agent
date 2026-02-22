from database.sqlite_store import get_conn
import json


def run_executor_agent(state):

    query = (state.get("user_input") or "").lower()
    user_id = state.get("user_id")
    role = state.get("role")

    state["logs"].append("Executor running")

    if "profile" not in query:
        return state

    if role == "admin":
        state["final_response"] = "Admins cannot access user profile data."
        return state

    conn = get_conn()

    row = conn.execute(
        "SELECT profile FROM user_profiles WHERE user_id=?",
        (user_id,)
    ).fetchone()

    conn.close()

    if row:
        profile = json.loads(row[0])
        state["final_response"] = f"Your Profile:\n{profile}"
    else:
        state["final_response"] = "Profile not found."

    return state