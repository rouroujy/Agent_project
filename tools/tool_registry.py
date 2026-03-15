from langchain.tools import Tool

from tools.calculator_tool import calculator
from tools.dictionary_tool import dictionary
from tools.time_tool import get_time

tools = [
    Tool(
        name = "calculator",
        func = calculator,
        description = "使用数学计算"
    ),

    Tool(
        name = "dictionary",
        func = dictionary,
        description = "查找单词定义"
    ),

    Tool(
        name = "time",
        func = get_time,
        description = "获取当前时间"
    )
]