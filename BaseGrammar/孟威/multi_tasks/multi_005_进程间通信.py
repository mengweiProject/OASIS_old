'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2022/10/20 17:10 
'''


import multiprocessing
from time import sleep


def produce_baozi(queue):
    baozi_n = 1
    while True:
        sleep(2)
        print('生产包子')
        queue.put(f'包子：{baozi_n}')
        baozi_n += 1


def consume_baozi(queue):
    while True:
        if queue.qsize() > 0:
            print(queue.qsize())
            print(f'出售：{queue.get()}')


if __name__ == '__main__':
    queue = multiprocessing.Manager().Queue()
    p1 = multiprocessing.Process(target=produce_baozi, args=(queue, ))
    p2 = multiprocessing.Process(target=consume_baozi, args=(queue, ))

    p1.start()
    p2.start()
    p1.join()
    p2.join()
    p1.close()
    p2.close()