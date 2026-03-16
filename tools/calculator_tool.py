'''
calculator_tool.py

这个文件实现一个简单的计算器工具。
Agent可以调用它进行数学计算。

'''

from langchain_core.tools import tool

@tool
def calculator(expression: str) -> str:
    """Useful for math calculations."""
    return str(eval(expression))

# mini agent 手写流程使用
# def calculator(expression: str) -> str:
#     '''
#     计算数学表达式

#     参数：
#         expression: 字符串形式的数学表达式
#         例如："12*235"
     
#     返回：
#         计算结果字符串
#     '''
    
#     try:
#         #eval是Python内置函数
#         #可以直接计算数学表达式
#         result = eval(expression)
#         return str(result)
    
#     except Exception as e:
#         return f"calculation error:{str(e)}"