'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2021/4/6 14:22
多进程装饰器示例
'''

from time import sleep
from multiprocessing import Process, Pool
from random import randint


def myPrint(port_id, end_date):
    # sleep(3)
    sleep(randint(1, 3))
    print(port_id, end_date)


def run():
    for i in range(100):
        p = Process(target=myPrint, args=(i, "2019-12-31"))
        p.start()


def run1():
    pool = Pool(10)
    for i in range(100):
        pool.apply_async(myPrint, (i, "2019-12-31"))
    pool.close()
    pool.join()


if __name__ == '__main__':
    run1()