'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2023/2/23 8:41 
'''

from queue import Queue as q_Q
from multiprocessing import Queue as m_Q, Pool, Process, Manager
from time import sleep


q_queue = m_Q()

for i in range(1000):
    q_queue.put(i)

def program_a():
    while True:
        if not q_queue.empty():
            print(q_queue)
            print(q_queue.get())
        sleep(1)


def program_b():
    while True:
        if not q_queue.empty():
            print(q_queue)
            print(q_queue.get())
        sleep(1)


def calc_c(a=1):
    for i in range(10):
        print(q_queue)
        print(q_queue.empty())
        print(q_queue.get())
        sleep(1)


if __name__ == '__main__':

    # p1 = Process(target=calc_c, args=())

    p1 = Process(target=program_a, args=())
    p2 = Process(target=program_b, args=())
    p1.start()
    p2.start()

    p1.join()
    p2.join()
    # for i in range(100):
    #     print(q_queue.get())




