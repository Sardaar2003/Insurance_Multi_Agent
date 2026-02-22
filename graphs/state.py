from typing import TypedDict, Optional, List

class AgentState(TypedDict):
    user_input: str
    authenticated: bool
    processed_input: Optional[str]
    intent: Optional[str]
    domain: Optional[str]
    context: Optional[dict]
    agent_output: Optional[str]
    risk_level: Optional[str]
    final_response: Optional[str]
    logs: List[str]