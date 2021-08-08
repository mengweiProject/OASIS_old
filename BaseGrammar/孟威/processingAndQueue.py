'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2021/7/15 9:42 
'''

from multiprocessing import pool
import queue
from time import sleep


# def generator(n, q):
#     sleep(n)
#     q.put(n)
#     print(n)

def jud(n):
    return n <= 10


if __name__ == '__main__':
    # t = pool.Pool(3)
    # q = queue.Queue()
    # task_list = [i for i in range(10)]
    # for task in task_list:
    #     t.map(generator, (task, q))
    # s = map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])
    # print(s)
    # for i in filter(jud, [1, 2, 333, 44]):
    #     print(i)
    # # print(jud(1))

    # 函数应用和映射
    import numpy as np
    import pandas as pd

    df = pd.DataFrame(np.random.randn(4, 3), columns=list('bde'), index=['utah', 'ohio', 'texas', 'oregon'])
    print(df)
    #将函数应用到由各列或行形成的一维数组上。DataFrame的apply方法可以实现此功能
    f=lambda x:x.max()-x.min()
    #默认情况下会以列为单位，分别对列应用函数
    t1=df.apply(f)
    print(t1)
    # axis=1时，表示按行应用
    t2=df.apply(f,axis=1)
    print(t2)