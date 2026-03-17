# tools/tool_registry.py

from tools.calculator_tool import calculator
from tools.dictionary_tool import dictionary
from tools.time_tool import time
from tools.rag_tool import knowledge_base_search

# =========================
# MiniAgent 使用
# =========================

TOOLS = {
    "calculator": calculator,
    "dictionary": dictionary,
    "time": time,
    "knowledge_base_search": knowledge_base_search
}



# =========================
# LangChain Agent 使用
# =========================

# LANGCHAIN_TOOLS = [

#     Tool(
#         name="calculator",
#         func=calculator,
#         description="进行数学计算，例如 2*3+5"
#     ),

#     Tool(
#         name="dictionary",
#         func=dictionary,
#         description="查询单词含义，例如 agent llm rag"
#     ),

#     Tool(
#         name="time",
#         func=lambda _: time(),
#         description="获取当前时间"
#     )
# ]