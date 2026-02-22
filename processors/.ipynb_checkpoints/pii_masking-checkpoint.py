import re

def mask_pii(state):
    text = state["user_input"]
    text = re.sub(r"\d{10}", "[PHONE]", text)
    state["processed_input"] = text
    state["logs"].append("✅ PII Masked")
    return state