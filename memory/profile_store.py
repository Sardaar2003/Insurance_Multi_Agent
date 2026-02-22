PROFILE_DB = {}

def load_profile(state):
    user_id = "default_user"

    profile = PROFILE_DB.get(user_id, {"name": "Guest"})
    state["context"] = state.get("context", {})
    state["context"]["profile"] = profile

    state["logs"].append("👤 Customer Profile Loaded")
    return state