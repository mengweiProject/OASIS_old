'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2022/7/12 8:34 
'''

import copy


if __name__ == '__main__':
    l1 = [1, 2, 3]
    # l2 = l1 # 通过赋值，两个列表指向的是内存空间中的同一块空间
    # print(l1)
    # print(l2)
    # l1[0] = 111
    # print(l2)

    # l3 = l1.copy()  # 浅拷贝，是在内存中重新开辟一块空间出来，复制一个新的列表（可变类型同理）
    # l1[1] = 222
    # print(l1)
    # print(l3)

    # 但是，浅拷贝只能复制最外面一层，什么叫最外面一层？就是列表嵌套列表
    # 我们对列表进行浅拷贝，只复制的列表的最外一层
    # l4 = [1, 2, 3, [4, 5]]
    # l5 = l4.copy()
    # l4[0] = 111111
    # print(l4)
    # print(l5)
    #
    # l4[3][0] = 999
    # print(l4)
    # print(l5)

    # 深拷贝，开辟一块新的内存空间，复制列表的每一层
    l6 = [1, 2, 3, [4, 5]]
    l7 = copy.deepcopy(l6)
    l6[0] = 111
    print(l6)
    print(l7)

    l6[3][0] = 444
    print(l6)
    print(l7)
