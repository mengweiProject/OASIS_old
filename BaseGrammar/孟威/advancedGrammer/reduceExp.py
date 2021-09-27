'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2021/7/15 15:25 
'''

from functools import reduce


def func(l):
    # reduce用法
    # 第一个值和第二个值当参数传给function，再把function的返回值和第三个值当参数传给function，然后只返回一个结果
    # return reduce(lambda x, y: x + y, l)
    return reduce(add, l)

def add(x, y):
    return x + y


if __name__ == '__main__':
    l = list(range(20))
    print(func(l))