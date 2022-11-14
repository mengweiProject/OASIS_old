'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2021/7/15 15:21 
'''

from datetime import datetime
from time import sleep

from tools import calcTimeCost, calcTimeCostParams

# @calcTimeCost
# def test():
#     sleep(3)
#
#
# @calcTimeCostParams
# def testParam(n, m):
#     sleep(n)
#
#
# if __name__ == '__main__':
#     # test()
#     testParam(3, 3)

# from functools import reduce
#
# class Solution:
#     def singleNumber(self, nums):
#         return reduce(lambda x, y: x ^ y, nums)
#
# if __name__ == '__main__':
#     l = [i for i in range(101)]
#     for i in l:
#         print(i ^ (i + 1))
#     print(reduce(lambda x, y: x ^ y, l))


# print(list(str(123)))

class Person:
    name = 'Human'
    def run(self):
        print(Person.name)