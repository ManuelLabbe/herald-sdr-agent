from langchain.messages import AIMessage
from langgraph.graph import StateGraph, START, END
from tiny_town.subgraphs.town.state import AgentState
from tiny_town.subgraphs.town.nodes import call_model, tool_node, should_continue, call_reviewer


workflow = StateGraph(AgentState)
workflow.add_node("agent", call_model)
workflow.add_node("tools", tool_node)
workflow.add_node("reviewer", call_reviewer)

workflow.add_edge(START, "agent")
workflow.add_conditional_edges("agent", should_continue, ["tools", "reviewer"])
workflow.add_edge("tools", "agent")
workflow.add_edge("reviewer", END)

graph = workflow.compile()