"""
agent/langchain_agent.py

使用langchain来封装agent
"""

from langchain.agents import create_agent

from tools.calculator_tool import calculator
from tools.dictionary_tool import dictionary
from tools.time_tool import time

from llm.qwen_llm import get_llm

def build_agent():
    llm = get_llm()

    tools = [
        calculator,
        dictionary,
        time
    ]
    
    agent = create_agent(
        model=llm,
        tools=tools,
        system_prompt="You are a helpful AI assistant.",
        debug=True
    )

    return agent
