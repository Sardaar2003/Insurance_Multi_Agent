from langchain_openai import ChatOpenAI
from config.settings import MODEL

from agents.a2a_bus import send_message, get_messages


# ============================================================
# LLM INITIALIZATION
# ============================================================

llm = ChatOpenAI(model=MODEL)


# ============================================================
# POLICY AGENT
# ============================================================

def run_policy_agent(state):
    """
    Enterprise Policy Agent

    Responsibilities:
    - handle insurance policy queries
    - collaborate with other agents
    - send/receive A2A messages
    - reason using context
    """

    query = state.get("processed_input", "")
    context = state.get("context", {})

    state["logs"].append("🤖 Policy Agent Started")

    try:
        # ====================================================
        # RECEIVE MESSAGES FROM OTHER AGENTS
        # ====================================================

        incoming_msgs = get_messages("policy_agent")

        if incoming_msgs:
            state["logs"].append("📩 Policy Agent received A2A messages")

        collaboration_context = "\n".join(incoming_msgs)

        # ====================================================
        # AGENT REASONING PROMPT
        # ====================================================

        prompt = f"""
        You are an enterprise insurance policy specialist.

        Context:
        {context}

        Messages from other agents:
        {collaboration_context}

        User Query:
        {query}

        Instructions:
        - answer policy related questions
        - if claim related work required mention CLAIM_REQUIRED
        - if customer info required mention CUSTOMER_REQUIRED
        - be concise and professional
        """

        response = llm.invoke(prompt)
        output = response.content

        state["agent_output"] = output
        state["logs"].append("🤖 Policy Agent Completed")

        # ====================================================
        # AGENT COLLABORATION SIGNALS
        # ====================================================

        # delegate to claims agent
        if "CLAIM_REQUIRED" in output:
            send_message("policy_agent", "claims_agent", query)
            state["logs"].append("🔁 Policy → Claims delegation message sent")

        # delegate to customer agent
        if "CUSTOMER_REQUIRED" in output:
            send_message("policy_agent", "customer_agent", query)
            state["logs"].append("🔁 Policy → Customer delegation message sent")

        return state

    except Exception as e:
        state["agent_output"] = "Policy service unavailable"
        state["logs"].append(f"❌ Policy Agent Error: {str(e)}")
        return state