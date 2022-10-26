'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2022/10/20 16:12
multiprocessing.Manger().Queue()
'''

import multiprocessing
from time import sleep
import os


def calc_some_data():
    sleep(1)
    print(f'calc函数执行...，当前进程id为：{os.getpid()}，当前进程的父进程id为：{os.getppid()}')


def calc_data_with_args(a=1):
    sleep(1)
    print(f'calc函数执行...结果为：{a}')
    return a


def calc_data_with_many_args(a, b):
    sleep(1)
    print(f'calc函数执行...，计算{a} + {b}，结果为：{a + b}')
    return a + b


if __name__ == '__main__':
    # cpu核心数
    cpu_number = multiprocessing.cpu_count()
    print(cpu_number)
    pool = multiprocessing.Pool(cpu_number // 2)

    # apply和apply_async函数用法
    # for i in range(3):
        # 顺序执行，实际上还是开启了多个进程
        # 12
        # calc函数执行...，当前进程id为：12376，当前进程的父进程id为：4964
        # calc函数执行...，当前进程id为：18604，当前进程的父进程id为：4964
        # calc函数执行...，当前进程id为：26396，当前进程的父进程id为：4964
        # everything is OK...
        # pool.apply(calc_some_data)

        # 异步执行，自动为每个任务分配一个进程去执行
        # 12
        # calc函数执行...，当前进程id为：16648，当前进程的父进程id为：26112
        # calc函数执行...，当前进程id为：28284，当前进程的父进程id为：26112
        # calc函数执行...，当前进程id为：15592，当前进程的父进程id为：26112
        # everything is OK...
        # pool.apply_async(func=calc_some_data)


    # map和map_async函数用法，只支持单个参数
    # map，阻塞当前主进程。
    # 并发，为每个进程分配一个任务，当所有任务结束后，继续回到主进程来执行
    # 12
    # calc函数执行...结果为：0
    # calc函数执行...结果为：1
    # calc函数执行...结果为：2
    # calc函数执行...结果为：3
    # calc函数执行...结果为：4
    # calc函数执行...结果为：5
    # calc函数执行...结果为：6
    # calc函数执行...结果为：7
    # calc函数执行...结果为：8
    # calc函数执行...结果为：9
    # all sub process done...
    # everything is OK...
    # r = pool.map(calc_data_with_args, iterable=range(10))
    # print(r, type(r))
    # print('all sub process done...')

    # 并发，不阻塞主进程
    # 12
    # sub process still running...
    # calc函数执行...结果为：0
    # calc函数执行...结果为：1
    # calc函数执行...结果为：2
    # calc函数执行...结果为：3
    # calc函数执行...结果为：4
    # calc函数执行...结果为：5
    # calc函数执行...结果为：6
    # calc函数执行...结果为：7
    # calc函数执行...结果为：8
    # calc函数执行...结果为：9
    # everything is OK...
    # pool.map_async(calc_data_with_args, iterable=range(10))
    # print('sub process still running...')

    # starmap和starmap_async用法，支持多个参数
    # pool.starmap()，阻塞主进程
    # 12
    # calc函数执行...，计算0 + 0，结果为：0
    # calc函数执行...，计算1 + 1，结果为：2
    # calc函数执行...，计算2 + 2，结果为：4
    # calc函数执行...，计算3 + 3，结果为：6
    # calc函数执行...，计算4 + 4，结果为：8
    # calc函数执行...，计算5 + 5，结果为：10
    # calc函数执行...，计算6 + 6，结果为：12
    # calc函数执行...，计算7 + 7，结果为：14
    # calc函数执行...，计算8 + 8，结果为：16
    # calc函数执行...，计算9 + 9，结果为：18
    # all sub process done...
    # everything is OK...
    args = [(i, i) for i in range(10)]
    pool.starmap(calc_data_with_many_args, iterable=args)
    print('all sub process done...')

    # pool.starmap_async()，不阻塞主进程
    # 12
    # sub process running...
    # calc函数执行...，计算0 + 0，结果为：0
    # calc函数执行...，计算1 + 1，结果为：2
    # calc函数执行...，计算2 + 2，结果为：4
    # calc函数执行...，计算4 + 4，结果为：8
    # calc函数执行...，计算3 + 3，结果为：6
    # calc函数执行...，计算5 + 5，结果为：10
    # calc函数执行...，计算6 + 6，结果为：12
    # calc函数执行...，计算7 + 7，结果为：14
    # calc函数执行...，计算8 + 8，结果为：16
    # calc函数执行...，计算9 + 9，结果为：18
    # everything is OK...
    # 可以在子进程结束后，获取结果
    #     print(type(rs))
    #     print(rs.get())
    #     for r in rs.get():
    #         print(r)
    # args = [(i, i) for i in range(10)]
    # rs = pool.starmap_async(calc_data_with_many_args, iterable=args)
    # print('sub process running...')

    # imap（有序）和imap_unordered（无序）用法，
    # map/map_async返回的结果是列表，返回列表list，通过get()方法获取结果，效率更高
    # imap/imap_unordered更像是生成器，返回iterable，通过next()函数获取结果，占用内存小
    # 12
    # calc函数执行...结果为：0
    # 0
    # calc函数执行...结果为：1
    # 1
    # calc函数执行...结果为：2
    # 2
    # calc函数执行...结果为：3
    # 3
    # calc函数执行...结果为：4
    # 4
    # calc函数执行...结果为：5
    # 5
    # calc函数执行...结果为：6
    # 6
    # calc函数执行...结果为：7
    # 7
    # calc函数执行...结果为：8
    # 8
    # calc函数执行...结果为：9
    # 9
    # everything is OK...
    # rs = pool.imap(calc_data_with_args, iterable=range(10))
    # for i in range(10):
    #     print(rs.next())

    # 12
    # calc函数执行...结果为：0
    # 0
    # calc函数执行...结果为：1
    # 1
    # calc函数执行...结果为：2
    # 2
    # calc函数执行...结果为：3
    # 3
    # calc函数执行...结果为：4
    # 4
    # calc函数执行...结果为：5
    # 5
    # calc函数执行...结果为：6
    # 6
    # calc函数执行...结果为：7
    # 7
    # calc函数执行...结果为：8
    # 8
    # calc函数执行...结果为：9
    # 9
    # everything is OK...
    # rs = pool.imap_unordered(calc_data_with_args, iterable=range(10))
    # for i in range(10):
    #     print(rs.next())


    pool.close()
    pool.join()

    print('everything is OK...')