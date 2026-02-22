from langchain_openai import ChatOpenAI
from config.settings import MODEL

llm = ChatOpenAI(model=MODEL, temperature=0)

def run_customer_agent(state):

    prompt = f"""
        You are a professional insurance customer support assistant.
        
        ROLE:
        - Help customers with general insurance questions.
        - Provide policy guidance and service information.
        - Explain processes clearly and politely.
        
        INSTRUCTIONS:
        - Use ONLY the provided context.
        - Do not make assumptions.
        - If information is missing, say "Information not available".
        - Be polite, empathetic, and professional.
        - Keep answers simple and easy to understand.
        
        CONTEXT:
        {state['context']}
        
        USER QUERY:
        {state['processed_input']}
        
        RESPONSE:
        """

    response = llm.invoke(prompt)

    state["agent_output"] = response.content
    state["logs"].append("🤖 Customer Agent Executed")

    return state