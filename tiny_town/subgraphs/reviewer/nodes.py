from typing import Literal
from langchain.messages import SystemMessage, HumanMessage
from langgraph.graph import END

from tiny_town.utils.models import main_model, light_model
from tiny_town.utils.messages import only_text
from tiny_town.subgraphs.reviewer.state import WorkerState, Evaluation

evaluator = light_model.with_structured_output(Evaluation)

def evaluate(state: WorkerState):
    result = evaluator.invoke([
        SystemMessages(
            "Eres un revisor. Evalúa si la respuesta del usuario contiene errores,"
            "imprecisiones o información inventada. No evalúes estilo."
        ),
        HumanMessage(state["draft"]),
    ])

    update = {"needs_fix": result.needs_fix, "reason": result.reason}
    if not result.needs_fix:
        update["review"] = state["draft"]
    return update

def fix_draft(state: WorkerState):
    response = main_model.invoke([
        SystemMessages(
            "Corrige la respuesta que te entregue el usuario."
            "Devuelve solo la versión final, sin comentarios."
        ),
        HumanMessage(f"Problema detectado: {state['reason']}\n\nRespuesta:\n{state['draft']}"),
    ])
    return {"review": only_text(response)}

def route_review(state: WorkerState) -> Literal["fix_draft", "__end__"]:
    return "fix_draft" if state["needs_fix"] else END