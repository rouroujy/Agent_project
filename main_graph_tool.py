# main_graph_tool.py
from graph.agent_graph import build_graph
from langchain_core.messages import HumanMessage

graph = build_graph()

state = {
    "messages": []
}

def clean_text(text: str) -> str:
    return text.encode("utf-8", "ignore").decode("utf-8")

while True:
    question = input("User:")

    question = clean_text(question)
    
    if question == "exit":
        break

    state["messages"].append(
        HumanMessage(content=question)
    )

    state = graph.invoke(state)

    print ("Assistant:",state["messages"][-1].content)
