def execute_tool(state):
    tool = state.get("selected_tool")

    if tool == "db_lookup":
        result = "Database result"
    else:
        result = "No tool used"

    state["context"]["tool_result"] = result
    state["logs"].append("🧪 Tool Executed in Sandbox")
    return state