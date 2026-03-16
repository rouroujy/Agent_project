'''
dictionary_tool.py

模拟一个词典查询工具

'''

from langchain_core.tools import tool

@tool
def dictionary(word: str) -> str:
    """Look up word meaning."""
    d = {
        "agent":"一个可以决定行为和使用工具的AI系统",
        "llm":"大语言模型",
        "rag":"检索增强生成",
        "AI":"Artificial Intelligence人工智能"
    }
    return d.get(word, "Not found")

# dictionary_data = {
    # "agent":"一个可以决定行为和使用工具的AI系统",
    # "llm":"大语言模型",
    # "rag":"检索增强生成"
# }

# def dictionary(word:str) -> str:
#     '''
#     查询单词含义
#     '''
#     word = word.lower()

#     if word in dictionary_data:
#         return dictionary_data[word]
#     else:
#         return "word not found"