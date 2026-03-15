from agent.prompt_template import BASE_PROMPT
from agent.parser import parse_action
from tools.tool_registry import TOOLS

class MiniAgent:
    def __init__(self, llm):
        self.llm = llm

    def run(self, question):
        prompt = BASE_PROMPT + "\nUser Question:" + question

        for step in range(5):
            print("\n====== LLM Thinking =====")
            response = self.llm(prompt)
            print(response)

            action, action_input = parse_action(response)
            if action == "finish":
                return action_input
            
            if action in TOOLS:
                tool_func = TOOLS[action]

                if action_input == "" or action == "time":
                    result = tool_func()
                else:
                    result = tool_func(action_input)
                observation = f"\nObservation:{result}\n"
                prompt += response + observation
            
            else:
                return "Unkown tool"