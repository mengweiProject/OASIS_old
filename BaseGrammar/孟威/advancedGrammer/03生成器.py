'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2022/7/14 9:41 
生成器，是一类特殊的迭代器。但是生成器不需要再像之前的类一样，写__iter__()和__next__()方法。
使用非常方便，可以直接使用next函数和for循环取值
'''


def fib_generator(n):
    """
    斐波那契数列的生成器版本
    :param n:
    :return:
    """
    a = 0
    b = 1
    current_index = 0
    while current_index < n:
        a, b = b, a + b
        current_index += 1
        yield b



if __name__ == '__main__':
    # l = (i for i in range(10))
    # print(l)
    # print(type(l))
    # for item in l:
    #     print(item)
    fib = fib_generator(100)
    # print(next(fib))
    # print(next(fib))
    # print(next(fib))
    # print(next(fib))

    for i in fib:
        print(i)
