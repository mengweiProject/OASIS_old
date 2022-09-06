# '''
# @Project ：OASIS
# @Author  ：孟威
# @Date    ：2022/7/26 11:07
# '''
#
#
# import array
# import pandas as pd
#
#
#
#
# if __name__ == '__main__':
#     # arr = array.array('f')
#     # print(arr)
#     # df = pd.DataFrame([{'a': 1, 'b': 2},
#     #                    {'a': 1, 'b': 2},
#     #                    {'a': 1, 'b': 2}])
#     # print(df)
#     # print(df.mul(df.b, 1))
#     # l1 = [1, 3, 5, 7, 9, 7, 5, 3, 2, 4]
#     # # rule_l = [0, 1, 10, 3, 4, 5, 6, 7, 8, 9]
#     # # print(sorted(l, key=lambda x: rule_l[x]))
#     # # print(sorted(range(-5, 6), key=lambda x: x * x))
#     # l2 = [1, 3, 5, 7, 9, 7, 5, 3, 2, 4]
#     # # print(l1 is l2)
#     # #
#     # # s1 = 1
#     # # s2 = 1
#     # # print(s1 is s2)
#     # print(id(l1))
#     # print(id(l2))
#     # l3 = l1
#     # print(id(l3))
#     # print(l1)
#     # print(l3)
#     # l1[0] = 111
#     # print(l1)
#     # print(l3)
#     l1 = [1, 2, 3, [44, 55]]
#     l2 = l1
#     print(l1)
#     print(l2)
#     l1[3][0] = 666
#     print(l1)
#     print(l2)
#     # 可变类型的参数传递是引用传递
#


def change_a_number(x):
    # 不可变类型的参数传递是值传递
    x = x ** 2


def change_a_list(l):
    # 可变类型的参数传递是引用传递
    l[0] = 123


if __name__ == '__main__':
    n = 111
    change_a_number(n)
    print(n)

    l = [1, 2, 3]
    change_a_list(l)
    print(l)