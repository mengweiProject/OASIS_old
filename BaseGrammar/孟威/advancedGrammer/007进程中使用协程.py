'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2022/11/3 13:19 
'''

import multiprocessing
import gevent
import os


def calc_work1():
    for _ in range(10):
        gevent.sleep(1)
        print(f'end...{os.getpid()}, {os.getppid()}')


def calc_work2():
    for _ in range(20):
        gevent.sleep(0.5)
        print(f'end...{os.getpid()}, {os.getppid()}')

def calc_main(_):
    t1 = gevent.spawn(calc_work1)
    t2 = gevent.spawn(calc_work2)
    gevent.joinall([t1, t2])


if __name__ == '__main__':
    pool = multiprocessing.Pool(3)
    # pool.map(calc_main, iterable=range(10))
    pool.map_async(calc_main, iterable=range(10))
    pool.close()
    pool.join()
    print('main end...')
