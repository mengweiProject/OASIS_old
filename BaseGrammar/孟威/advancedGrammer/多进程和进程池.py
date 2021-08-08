'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2021/8/8 16:48 
'''

from multiprocessing import Process
from time import sleep
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

from Tools.time_helper import time_consume


# @time_consume   # https://blog.csdn.net/kuyu05/article/details/104267106
def my_sleep(n=3):
    sleep(2)
    print('sub process end...')
    return 'end...'



if __name__ == '__main__':
    s_date = datetime.now()
    # p = Process(target=my_sleep, args=())
    # p.start()
    # print('main process end...')

    tasks = [i for i in range(10)]
    results = []
    with ProcessPoolExecutor(max_workers=3) as pool:
        for task in tasks:
            result = pool.submit(my_sleep, task)
            results.append(result)

        for res in results:
            print(res.result())
    f_date = datetime.now()
    print('main process end...', f_date - s_date)
