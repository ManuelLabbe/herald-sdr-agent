from typing_extensions import TypedDict
from pydantic import BaseModel, Field

class WorkerState(TypedDict):
    draft: str
    review: str 
    needs_fix: bool
    reason: str

class Evaluation(BaseModel):
    needs_fix: bool = Field(
        description="True si la respuesta tiene errores, impresiciones o datos inventados"
        "False si la respuesta es correcta y clara"
    )
    reason: str = Field(description="Explicación breve de la desición")
    