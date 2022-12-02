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

# class Person:
#     name = 'Human'
#     def run(self):
#         print(Person.name)


if __name__ == '__main__':
    # a = 111
    # b = a
    # print(id(a))
    # print(id(b))
    # print(a is b)
    # s1 = 'asdgjkajiogwerioogeabj'
    # s2 = s1
    # print(id(s1))
    # print(id(s2))
    # print(s1 is s2)
    # l1 = [1, 2, 3, 6, 7, [9, 0]]
    # l2 = l1
    # print(id(l1))
    # print(id(l2))
    # print(l1 is l2)

    l1 = [1, 2, 3, 4, [5, 6]]
    l2 = l1.copy()
    print(id(l1))
    print(id(l2))
    print(id(l1[4]))
    print(id(l2[4]))
    print(l1 is l2)

    import copy
    l3 = [1, 2, 3, 4, [5, 6]]
    l4 = copy.deepcopy(l3)
    print(id(l3))
    print(id(l4))



















