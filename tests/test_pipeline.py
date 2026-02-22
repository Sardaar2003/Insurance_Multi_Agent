from graphs.main_graph import build_graph


def test_pipeline_runs():
    graph = build_graph()

    state = {
        "user_input": "check my policy",
        "authenticated": False,
        "processed_input": None,
        "intent": None,
        "domain": None,
        "context": {},
        "agent_output": None,
        "risk_level": None,
        "final_response": None,
        "logs": []
    }

    result = graph.invoke(state)

    assert "final_response" in result