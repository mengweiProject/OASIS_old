'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2021/8/8 15:39 
'''

from threading import Thread
from time import sleep
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

from Tools.time_helper import time_consume


@time_consume
def my_sleep(n=3):
    sleep(2)
    print('sub thread end...')
    return 'end...'



if __name__ == '__main__':
    s_date = datetime.now()
    # t = Thread(target=my_sleep)
    # t.start()
    # print('main thread end...')

    # 线程池的用法1
    # tasks = [x for x in range(3)]
    # results = []
    # with ThreadPoolExecutor() as pool:
    #     for task in tasks:
    #         result = pool.submit(my_sleep, task)
    #         results.append(result)
    #
    #     for res in results:
    #         print(res.result())
    #
    # f_date = datetime.now()
    # consume_time = f_date - s_date
    # print(f'process consumes time: {consume_time}')

    # 线程池的用法2
    tasks = [x for x in range(10)]
    # 通过max_workers
    with ThreadPoolExecutor(max_workers=2) as pool:
        results = pool.map(my_sleep, tasks)
        # print(results)

        # for res in results:
        #     print(res)

    f_date = datetime.now()
    consume_time = f_date - s_date
    print(f'process consumes time: {consume_time}')