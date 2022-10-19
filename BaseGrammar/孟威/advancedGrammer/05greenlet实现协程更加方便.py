'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2022/7/14 9:54 
'''

import greenlet
import time

from django.utils.encoding import escape_uri_path


# def work1():
#     for i in range(5):
#         print("work1...")
#         time.sleep(0.2)
#         g2.switch()
#
#
# def work2():
#     for i in range(5):
#         print("work2...")
#         time.sleep(0.2)
#         g1.switch()
#
#
# if __name__ == '__main__':
#     g1 = greenlet.greenlet(work1)
#     g2 = greenlet.greenlet(work2)
#
#     g1.switch()

def func1():
    while True:
        print('func1...')
        # 切换到gr2
        gr2.switch()
        time.sleep(1)


def func2():
    while True:
        print('func2___')
        # 切换到gr1
        gr1.switch()
        time.sleep(1)


gr1 = greenlet.greenlet(func1)
gr2 = greenlet.greenlet(func2)

gr1.switch()
