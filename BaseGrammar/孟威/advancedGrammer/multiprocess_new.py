

from concurrent.futures import ProcessPoolExecutor, as_completed, wait, ALL_COMPLETED, FIRST_COMPLETED
from multiprocessing import cpu_count, Manager
from time import sleep
from datetime import datetime
import os

from Tools.time_helper import time_consume


# worker_n = cpu_count() // 3 * 2
worker_n = 2


def worder_1(n):
    sleep(n)
    print(f'worker {n} finish time is {datetime.now()}, subpid is {os.getpid()}')
    return n


def get_tasks():
    tasks = [i * 2 for i in [3, 1, 2]] * 2
    print(tasks)
    return tasks


@time_consume
def run1():
    # map
    tasks = get_tasks()
    with ProcessPoolExecutor(max_workers=worker_n) as pool:
        # 开启多任务执行任务列表中的任务
        results = pool.map(worder_1, tasks)
        # 获取任务返回结果
        for res in results:
            print(f'res is {res}')
    print(f'main process end... pid is {os.getpid()}')


@time_consume
def run2():
    tasks = get_tasks()
    with ProcessPoolExecutor(max_workers=worker_n) as pool:
        results = [pool.submit(worder_1, task) for task in tasks]
        # print(results)
    # wait：阻塞函数，让主进程等待指定部分子任务执行结束，再向下执行
    wait(results, return_when=FIRST_COMPLETED)
    print('========== continue main process')
    # pool.shutdown(wait=False)               # 没看懂
    # sleep(3)
    # as_completed：一个迭代器，按照子任务执行结束的顺序返回
    for res in as_completed(results):
        print(res.result())





if __name__ == '__main__':
    queue = Manager().Queue()
    run2()