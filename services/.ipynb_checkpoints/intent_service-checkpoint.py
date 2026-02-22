def classify_intent(state):
    text = state["processed_input"].lower()

    if "policy" in text:
        intent = "policy"
    elif "claim" in text:
        intent = "claims"
    elif "customer" in text:
        intent = "customer"
    else:
        intent = "general"

    state["intent"] = intent
    state["logs"].append(f"✅ Intent Classified → {intent}")
    return state