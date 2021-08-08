'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2021/8/8 16:08 
'''

from datetime import datetime


def time_consume(func):
    def run(*args, **kwargs):
        s_date = datetime.now()
        func(*args, **kwargs)
        e_date = datetime.now()
        consume_time = e_date - s_date
        print(f'thread run time is {consume_time}')
    return run