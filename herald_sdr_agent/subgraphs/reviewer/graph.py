from langgraph.graph import StateGraph, START, END

from tiny_town.subgraphs.reviewer.state import WorkerState
from tiny_town.subgraphs.reviewer.nodes import evaluate, fix_draft, route_review

builder = StateGraph(WorkerState)
builder.add_node("evaluate", evaluate)
builder.add_node("fix_draft", fix_draft)

builder.add_edge(START, "evaluate")
builder.add_conditional_edges("evaluate", route_review, ["fix_draft", END])
builder.add_edge("fix_draft", END)

worker_graph = builder.compile()