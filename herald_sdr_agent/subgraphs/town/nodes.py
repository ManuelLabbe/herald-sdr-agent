from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.messages import AIMessage

from typing import Literal
from langchain.messages import SystemMessage
from langgraph.graph import END
from langgraph.prebuilt import ToolNode

from herald_sdr_agent.subgraphs.town.tools import tools
from herald_sdr_agent.subgraphs.town.state import AgentState
from herald_sdr_agent.subgraphs.reviewer.graph import worker_graph

model = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")
model_with_tools = model.bind_tools(tools)

def only_text(msg) -> str:
    return "".join(b["text"] for b in msg.content_blocks if b["type"] == "text")

def call_model(state: AgentState):
    response = model_with_tools.invoke(
        [SystemMessage(content="Eres un asistente útil y servicial."), *state["messages"]]
    )
    return {"messages": [response], "llm_calls": state.get("llm_calls", 0) + 1}

def call_reviewer(state: AgentState):
    last = state["messages"][-1]
    draft = only_text(last)
    print(last.text)
    response = worker_graph.invoke({"draft": state["messages"][-1].content})
    print(response["review"])
    return {"messages": [AIMessage(content=response["review"], id=last.id)]}

tool_node = ToolNode(tools)



def should_continue(state: AgentState) -> Literal["tools", "reviewer"]:
    if state["messages"][-1].tool_calls:
        return "tools"
    return "reviewer"
                               