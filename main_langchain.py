'''
main_langchain.py
'''
from agent.langchain_agent import build_agent

agent = build_agent()

while True:
    question = input("User:")

    result = agent.invoke(
        {"messages":[{"role":"user","content":question}]},
        config={"verbose": True}
    )

    print(result["messages"][-1].content)