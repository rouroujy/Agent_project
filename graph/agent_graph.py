# graph/agent_graph.py

from langgraph.graph import StateGraph, END
from llm.qwen_llm import get_llm
from graph.tool_node import tool_node
from tools.tool_registry import TOOLS
from langchain_core.messages import AIMessage

llm = get_llm()


def clean_text(text: str) -> str:
    if not isinstance(text, str):
        text = str(text)
    return text.encode("utf-8", "ignore").decode("utf-8")

#LLM节点
def llm_node(state):
    messages = state["messages"]

    response = llm.bind_tools(list(TOOLS.values())).invoke(messages)
    # 清洗输出
    safe_content = clean_text(response.content)

    messages.append(
        AIMessage(content=safe_content, tool_calls=response.tool_calls)
    )

    return {"messages":messages}

# 判断是否走工具
def should_use_tool(state):
    last_message = state["messages"][-1]

    if hasattr(last_message, "tool_calls") and last_message.tool_calls:
        return "tool"
    
    return "end"

def build_graph():
    graph = StateGraph(dict)

    graph.add_node("llm", llm_node)
    graph.add_node("tool",tool_node)

    graph.set_entry_point("llm")

    graph.add_conditional_edges(
        "llm",
        should_use_tool,
        {
            "tool":"tool",
            "end":END
        }
    )

    #工具执行完，再返回LLM
    graph.add_edge("tool","llm")

    return graph.compile()