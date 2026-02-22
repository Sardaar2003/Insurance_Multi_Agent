"""
General Agent with RAG + LLM Answer Generation
"""

from rag.retriever import retrieve_context
from langchain_openai import ChatOpenAI
from langchain_classic import PromptTemplate
from dotenv import load_dotenv
load_dotenv()
import os
print(os.getenv("OPENAI_API_KEY"))


# initialize LLM
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)


def run_general_agent(state):

    query = state.get("user_input", "")

    state["logs"].append("Knowledge retrieval")

    # ================= RETRIEVE =================
    context = retrieve_context(query)

    if not context:
        state["final_response"] = (
            "No relevant information found in knowledge base."
        )
        return state

    # ================= PROMPT =================
    prompt = PromptTemplate.from_template("""
You are an enterprise insurance assistant.

Use the knowledge below to answer the user's question clearly.

Knowledge:
{context}

Question:
{question}

Give a concise professional answer.
""")

    final_prompt = prompt.format(
        context=context,
        question=query
    )

    # ================= LLM GENERATION =================
    response = llm.invoke(final_prompt)

    state["final_response"] = response.content
    return state