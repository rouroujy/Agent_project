def parse_action(response: str):
    if "Final Answer:" in response:
        answer = response.split("Final Answer:")[1].strip()
        return ("finish",answer)
    
    lines = response.split("\n")
    action = None
    tool_input = ""

    for line in lines:
        if line.startswith("Action:") and action is None:
            action = line.replace("Action:","").strip().lower()
        
        if line.startswith("Input:"):
            tool_input = line.replace("Input:","").strip()

            break
    
    if action:
        return (action,tool_input)
    
    return (None, None)

    # if "Action:" in response and "Input:" in response:
    #     tool = response.split("Action:")[1].strip("\n")[0].strip()
    #     tool = tool.lower()
    #     tool_input = response.split("Input:")[1].strip()

    #     return (tool, tool_input)
    
