# graph/too_node.py

from tools.tool_registry import TOOLS
from langchain_core.messages import ToolMessage

def tool_node(state):
    messages = state["messages"]

    last_messages = messages[-1]

    #判断是否有tool
    if not hasattr(last_messages, "tool_calls") or not last_messages.tool_calls:
        return state

    tool_call = last_messages.tool_calls[0]

    tool_name = tool_call["name"]
    tool_args = tool_call.get("args", {})
    tool_call_id = tool_call["id"]

    #执行工具
    tool_func = TOOLS.get(tool_name)

    if tool_func is None:
        result = f"工具 {tool_name} 没找到"
    else:
        result = tool_func.invoke(tool_args)

    # 用 ToolMessage（关键）
    messages.append(
        ToolMessage(
            content=str(result),
            tool_call_id=tool_call_id
        )
    )

    return {"messages":messages}