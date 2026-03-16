from agent.prompt_template import BASE_PROMPT
from agent.parser import parse_action
from tools.tool_registry import TOOLS

class MiniAgent:
    def __init__(self, llm):
        self.llm = llm

    def run(self, question):
        prompt = BASE_PROMPT + "\nUser Question:" + question

        for step in range(5):
            print("\n====== LLM Thinking =====",step)
            response = self.llm(prompt)
            print("大模型输出：",response)

            action, action_input = parse_action(response)
            print("\n得到action:",action)
            print("\n得到input:",action_input)
            if action == "finish":
                return action_input
            
            if action in TOOLS:
                tool_func = TOOLS[action]
                print("\n使用工具func:",tool_func)

                if action_input == "" or action == "time":
                    result = tool_func()
                else:
                    result = tool_func(action_input)
                observation = f"\nObservation:{result}\n"
                print("观察结果：",observation)
                prompt += response + observation
            
            else:
                return "Unkown tool"