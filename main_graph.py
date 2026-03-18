'''
main_graph.py
'''
from graph.simple_graph import build_graph

app = build_graph()

state = {"messages":[]}

def clean_text(text: str) -> str:
    return text.encode("utf-8", "ignore").decode("utf-8")

while True:
    question = input("User:")

    question = clean_text(question)

    if question == "exit":
        break

    state["messages"].append(
        {
            "role":"user",
            "content":question
        }
    )

    state = app.invoke(state)

    print("Assistant:",state["messages"][-1]["content"])