'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2022/7/14 9:50 
'''

from time import sleep


def func1():
    while 1:
        print('func1...')
        yield
        sleep(0.5)


def func2():
    while 1:
        print('func2___')
        yield
        sleep(0.5)


if __name__ == '__main__':
    # 在单线程中，就已经实现了 多任务
    w1 = func1()
    w2 = func2()
    while 1:
        next(w1)
        next(w2)