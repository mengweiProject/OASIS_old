'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2022/7/14 10:07 
'''


import gevent
from time import sleep


def work(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        gevent.sleep(0.5)


if __name__ == '__main__':
    g1 = gevent.spawn(work, 5)
    g2 = gevent.spawn(work, 5)
    g3 = gevent.spawn(work, 5)

    g1.join()
    g2.join()
    g3.join()
