from langgraph.graph import MessagesState

class AgentState(MessagesState):
    llm_calls: int