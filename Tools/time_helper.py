'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2021/8/8 16:08 
'''

from datetime import datetime
from threading import Thread


def myAsync(func):
    def wrapper(*args, **kwargs):
        t = Thread(target=func, args=args, kwargs=kwargs)
        t.start()
    return wrapper


def time_consume(func):
    def run(*args, **kwargs):
        s_date = datetime.now()
        func(*args, **kwargs)
        e_date = datetime.now()
        consume_time = e_date - s_date
        print(f'========= {func.__name__} run time is {consume_time}')
    return run