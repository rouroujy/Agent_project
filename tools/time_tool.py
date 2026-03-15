'''
time_tool.py

提供当前时间的工具
'''

from datetime import datetime

def get_time() -> str:
    '''
    返回当前时间
    '''
    now = datetime.now()

    return now.strftime("%Y-%m-%d %H:%M:%S")