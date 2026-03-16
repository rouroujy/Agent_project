'''
time_tool.py

提供当前时间的工具
'''

from langchain_core.tools import tool
import datetime

@tool
def time() -> str:
    """Get current time."""
    return str(datetime.datetime.now())

# from datetime import datetime

# def time() -> str:
#     '''
#     返回当前时间
#     '''
#     now = datetime.now()

#     return now.strftime("%Y-%m-%d %H:%M:%S")