'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2021/4/28 9:44 
'''

from copy import deepcopy


if __name__ == '__main__':
    # l = [1, 2, 3]
    # l1 = l
    # l[0] = 111
    # print(l)
    # print(l1)
    # l2 = l.copy()
    # l[1] = 222
    # print(l)
    # print(l1)
    # print(l2)
    l1 = [1, 2, 3]
    l2 = l1.copy()
    print(l1)
    print(l2)
    l1[0] = 111
    print(l1)
    print(l2)