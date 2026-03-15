from agent.mini_agent import MiniAgent
from llm.dashscope_llm import call_llm

agent = MiniAgent(call_llm)

question = "现在几点+5"

result = agent.run(question)

print("\nFinal Answer:",result)