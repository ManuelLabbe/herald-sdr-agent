from langgraph.graph import StateGraph, START, END
from typing_extensions import TypedDict

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.messages import SystemMessage, HumanMessage

# Sección del state.py
class WorkerState(TypedDict):
    draft: str
    review: str

# Sección del nodes.py
model = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")

def only_text(msg) -> str:
    return "".join(b["text"] for b in msg.content_blocks if b["type"] == "text")

def review_draft(state: WorkerState):
    response = model.invoke([
        SystemMessage(
            "Revisa la respuesta que te entregue el usuario. Corrige Errores"
            "o imprecicionses y devuelve solo la versión final, sin comentarios."),
        HumanMessage(state["draft"]),
    ])
    return {"review": only_text(response)}


# esto debería ser un un graph.py dentro de subdir para ensambara y compilar el grafo
builder = StateGraph(WorkerState)
builder.add_node("review_draft", review_draft)
builder.add_edge(START, "review_draft")
builder.add_edge("review_draft", END)
worker_graph = builder.compile()