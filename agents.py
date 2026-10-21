from dotenv import load_dotenv
load_dotenv()

import os
from langchain_anthropic import ChatAnthropic
from typing import Literal
from langchian.tools import Tool


# Apuntar al endpoint de MiniMax
model = ChatAnthropic(
    model="MiniMax-M2.7",
    base_url="https://api.minimax.io/anthropic",
    max_tokens=-1,
    api_key=os.environ["MINIMAX_API_KEY"],
)

#   Agente industrial
#   Primero replicacón simple de gastown trabajo menores para luego avanzar a interacción con entornos de empresas
#   Grado padre = EL MAYOR: Guarda en su estado el objetivo, lista de tareas y resultados



