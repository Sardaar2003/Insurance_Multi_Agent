from rag.vector_store import search


def retrieve_context(query):
    docs = search(query)

    if not docs:
        return None

    return "\n\n".join(docs)