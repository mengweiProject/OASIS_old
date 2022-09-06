'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2022/7/20 9:57 
'''

# def func1():
    # enumerate()函数：返回enumerate对象，可以将可迭代对象组成一个索引序列，（索引， 元素值），可以直接获取索引和元素
    # l = list(range(10))
    # for idx, item in enumerate(l):
    #     print(f'第{idx}个元素是{item}')
    # s = 'asdfasdfasdfasdf'
    # for idx, item in enumerate(s):
    #     print(f'第{idx}个元素是{item}')

    # s = 'asdf'
    # l = [i for i in range(4)]
    # # zip_op = zip(l, s, s)
    # # print(list(zip_op))
    # print(hash(s))

#
#     l1 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
#
#     rule = [0, 1, 9, 3, 6, 5, 2, 7, 9, 8]
#
#     # s = sorted(l1, key=lambda x: rule[x])
#     # print(s)
#     s = sorted(l1, key=lambda x: my_sort_rule(x, rule))
#     print(s)
#
#
# def my_sort_rule(x, rule):
#     print(x, rule[x])
#     return rule[x]


# if __name__ == '__main__':
#     func1()
#     import this

# def hello(name):
#     print(f'hello {name}')
#
#
# def my_print(hello, name):
#     hello(name)
#
# my_print(hello, 'python')

# l = [i for i in range(10)]
#
# print(list(map(lambda x: x ** 2, [i for i in range(10)])))

# def my_print(func):
#     print('装饰器还没开始调用...请等待')
#     def inner(*args):
#         print('装饰器已经触发...')
#         func(*args)
#
#     return inner
#
# @my_print
# def out_name(name):
#     print(name)
#
#
# name = 'python'
# out_name(name)

# class Adder:
#     def __init__(self, n):
#         self.n = n
#
#     def __call__(self, *args, **kwargs):
#         return self.n + args[0]
#
#
# a = Adder(1)
#
# print(a(2))


def func():
    """
    怎么才能获取这段话？
    :return:
    """
    print('end...')


if __name__ == '__main__':
    # print(help(func()))
    # print(dir(func()))
    for inner in dir(func()):
        print(inner)
    print(func.__doc__)
















