from langgraph.graph import StateGraph
from state.agent_state import AgentState
from langchain_core.messages import AIMessage, HumanMessage

from llm.qwen_llm import get_llm

llm = get_llm()

def clean_text(text: str) -> str:
    if not isinstance(text, str):
        text = str(text)
    return text.encode("utf-8", "ignore").decode("utf-8")

def chatbot_node(state: AgentState):
    messages = state['messages']

    # 转换为LangChain Message
    lc_messages = []

    for m in messages:
        if isinstance(m, dict):
            if m["role"] == "user":
                lc_messages.append(HumanMessage(content = m["content"]))
            elif m["role"] == "assistant":
                lc_messages.append(AIMessage(content = m["content"]))

        else:
            lc_messages.append(m)

    response = llm.invoke(lc_messages)

    # 清洗输出
    safe_content = clean_text(response.content)

    # 转回dict
    messages.append(
        {
            "role":"assistant",
            "content":safe_content
        }
    )

    return {"messages":messages}

def build_graph():
    graph = StateGraph(AgentState)

    graph.add_node("chatbot",chatbot_node)
    
    graph.set_entry_point("chatbot")

    graph.set_finish_point("chatbot")

    app = graph.compile()

    return app