'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2021/7/15 15:21 
'''

from datetime import datetime
from time import sleep

from tools import calcTimeCost, calcTimeCostParams

@calcTimeCost
def test():
    sleep(3)


@calcTimeCostParams
def testParam(n, m):
    sleep(n)


if __name__ == '__main__':
    # test()
    testParam(3, 3)