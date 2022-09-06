'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2022/7/25 8:13 
'''


def str_add1(func):
    print('装饰器1被调用')
    def inner(*args, **kwargs):
        return f'aaa{func(*args, **kwargs)}bbb'
    return inner


def str_add2(func):
    print('装饰器2被调用')
    def inner(*args, **kwargs):
        return f'ddd{func(*args, **kwargs)}ddd'
    return inner

@str_add1
@str_add2
def func(s):
    return s * 5


if __name__ == '__main__':
    s = '1'
    print(func(s))