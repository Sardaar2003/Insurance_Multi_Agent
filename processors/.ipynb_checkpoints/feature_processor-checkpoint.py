def process_features(state):
    text = state.get("processed_input", "")

    state["context"] = state.get("context", {})
    state["context"]["features"] = {
        "length": len(text),
        "keywords": text.split()[:5]
    }

    state["logs"].append("⚙️ Feature Processing Completed")
    return state