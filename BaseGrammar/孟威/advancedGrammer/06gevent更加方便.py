'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2022/7/14 10:07 
'''


import gevent
from gevent import monkey
from time import sleep

monkey.patch_all()  # 将time.sleep()改成gevent.sleep()


def work1(n):
    for i in range(n):
        print('---work1---', gevent.getcurrent(), i)
        gevent.sleep(0.5)

def work2(n):
    for i in range(n):
        print('---work2---', gevent.getcurrent(), i)
        gevent.sleep(0.5)

def work3(n):
    for i in range(n):
        print('---work3---', gevent.getcurrent(), i)
        gevent.sleep(0.5)


# if __name__ == '__main__':
#     g1 = gevent.spawn(work1, 5)
#     g2 = gevent.spawn(work2, 5)
#     g3 = gevent.spawn(work3, 5)
#
#     g1.join()
#     g2.join()
#     g3.join()

if __name__ == '__main__':
    # 协程的创建，方式2
    gevent.joinall([
        gevent.spawn(work1, 5),
        gevent.spawn(work2, 5),
        gevent.spawn(work3, 5),
    ])