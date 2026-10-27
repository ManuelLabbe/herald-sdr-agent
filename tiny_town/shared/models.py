from langchain_google_genai import ChatGoogleGenerativeAI

# Modelo principal (agente y corrección)
main_model = ChatGoogleGenerativeAI(model="gemini-3.7-flash", temperature=0)

# Modelo para evaluar: por ahora el mismo, cámbialo a uno más liviano si quieres ahorrar
light_model = ChatGoogleGenerativeAI(model="gemini-3.7-flash", temperature=0)