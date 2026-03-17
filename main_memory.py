# main_memory.py

from agent.langchain_agent import build_agent

agent = build_agent()
messages = []

while True:
    question = input("User:")

    if question == "exit":
        break

    messages.append(
        {
            "role":"user",
            "content":question
        }
    )

    result = agent.invoke(
        {
            "messages":messages
        }
    )

    reply = result["messages"][-1]

    print("Assistant:",reply.content)

    messages.append(reply)