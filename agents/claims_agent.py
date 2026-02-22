from langchain_openai import ChatOpenAI
from config.settings import MODEL

llm = ChatOpenAI(model=MODEL, temperature=0)

def run_claims_agent(state):

    prompt = f"""
        You are an expert insurance claims assistant.
        
        ROLE:
        - Help users understand claim processes.
        - Evaluate claim eligibility based on policy context.
        - Explain claim steps, documents, and outcomes.
        
        INSTRUCTIONS:
        - Use ONLY the provided context.
        - Do not make assumptions.
        - If information is missing, say "Information not available".
        - Be clear, concise, and professional.
        - Provide structured explanations.
        
        CONTEXT:
        {state['context']}
        
        USER QUERY:
        {state['processed_input']}
        
        RESPONSE:
        """

    response = llm.invoke(prompt)

    state["agent_output"] = response.content
    state["logs"].append("🤖 Claims Agent Executed")

    return state