'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2021/3/30 15:56 
'''

from celeryTasks import app
import random


@app.task
def calc_common():
    print("计算指标数据等等...")
    return random.randint(0, 10)


if __name__ == '__main__':
    print(calc_common())