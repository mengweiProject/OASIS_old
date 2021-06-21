'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2021/4/15 9:42 
'''


from multiprocessing import Pool
import numpy as np
from time import sleep
from random import random, randint
import math

def myPrint(n):
    print(randint(0, 3))
    sleep(randint(0, 3))
    return n


if __name__ == '__main__':
    # p = Pool(2)
    # idList = [i for i in range(100)]
    # # print(idList)
    # for slice in range(33):
    #     ret = p.map(myPrint, idList[slice * 3: (slice + 1) * 3])
    #     print(ret)
    # print(" ".split(","))
    print("" is None)
    print(math.inf is float("inf"))
    print(np.inf)