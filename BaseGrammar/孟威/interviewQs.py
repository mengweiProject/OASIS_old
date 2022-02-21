'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2022/2/7 8:58 
'''

from datetime import datetime, date
from time import sleep
import random
import re

from django.core.cache import cache

from time_helper import time_consume


def calc_consume_time(func):
    def calc_inner(*args, **kwargs):
        s_date = datetime.now()
        func(*args, **kwargs)
        f_date = datetime.now()
        # print(f'consume_time is : {f_date - s_date}')
        print(f'\033[31mconsume_time is : {f_date - s_date}')
    return calc_inner


# 1. list.reverse()
def one():
    # 反转，不是排序
    l = [1, 3, 5, 8, 6, 4]
    print(l)
    l.reverse()
    print(l)
    return l


# 2. sum&range
def two():
    # 一行代码实现1--100之和
    print(sum(range(1, 101)))
    return


# 3. 如何在一个函数内部修改全局变量
n = 123
def three():
    n = 456
    def threeInner():
        global n
        n = 888
        print(n)
    threeInner()
    return n


def threeOne():
    global n
    n = 999
    return n


# 4. 列出5个python标准库
def four():
    print('sys文件目录操作管理支持, shutil, os系统操作交互, '
          '数学运算，数据分析，math, random, numpy, pandas, '
          '日期处理，date, datetime, '
          '爬虫，url请求和解析，requests, urllib, beautifulsoup, '
          're正则表达匹配工具, '
          '数据压缩，zlib, '
          '')
    return

# 字典如何删除键和合并两个字典
def five():
    # 创建一个字典
    d1 = {'a': 1, 'b': 2, 'c': 3}
    for k, v in d1.items():
        print(f'k: {k}, v: {v}')
    print(d1)
    # 删除字典的键
    d1.pop('a')
    print(d1)
    # 删除一个不存在的键会引发KeyError异常
    # d1.pop('d')

    # 字典生成式
    d2 = {k: v for k, v in d1.items()}
    print(d2)
    d3 = {i: i for i in range(10)}
    print(d3)
    # 字典的键区分大小写
    d4 = {'a': 123, 'A': 456}
    print(d4)

    # 如何合并两个字典的四种方法：
    # 1. update，直接操作原字典，
    # 2. dict1.items() + dict2.items()，
    # 3. dict3 = dict(dict1, **dict2)，
    # 4. 遍历复制添加
    d1.update(d4)
    print(d1)
    del d1['A']
    print(d1)
    # del d1['d']
    # print(d1)
    return


# 谈下python的GIL
def six():
    print(u'谈下GIL，全局解释器锁：python在执行时，如果同一个进程中有多个线程运行，一个线程在执行的时候会霸占python解释器，'
          u'使得该进程内的其他线程无法执行，等该线程执行结束后其他线程才可以执行。')
    return


# reduce，map，filter
def seven():
    l = list(range(1, 100))
    # 百分比取整
    # filter：将所有元素按照筛选条件过滤，得到新的可迭代对象
    print(list(filter(lambda x: x % 2 == 1, l)))

    print(list(map(lambda x: x * 3, l)))

    from functools import reduce
    print(reduce(lambda x, y: x * y, l, 0))
    return


# fun(*args,**kwargs)中的*args,**kwargs什么意思？
def eight(*args):
    """
    *args参数作用：接收多个参数，以元组的形式保存，传递到函数内部
    :param args:
    :return:
    """
    print(args)
    for arg in args:
        print(arg)

def nine(**kwargs):
    """
    **kwargs：key&words参数，可接收不定长度的关键字参数，以字典的形式统一接收传递到函数内部
    :param kwargs:
    :return:
    """
    print(kwargs)
    for k, v in kwargs.items():
        print(k, v)


# python2和python3中range（）的区别
def ten():
    print(u'python2中range返回列表，python3中range返回迭代器，好处是节约内存')


@calc_consume_time
def eleven():
    # print(f'\033[4;31m这是啥这是啥这是啥')
    for _ in range(3):
        sleep(1)


# python内建数据类型
def twelve():
    """
    列表：有序，可修改
    元组：有序，不可修改
    集合：无序，可修改
    字典：无序，可修改
    字符串：有序，不可修改
    :return:
    """
    return


# 简述面向对象中，__new__和__init__的区别
class Thirteen:
    def __init__(self):
        print('\033[33m__init__被调用')
        # self.name = name
        # print(self.name)

    def __new__(cls, *args, **kwargs):
        print('\033[34m__new__被调用')
        return object.__new__(cls)

    def desc(self):
        print(u'区别：1. new优先于init被调用，2. new是实例创建之前被调用的，作用是用于创建对象然后返回该实例对象，是个静态方法'
              u'，init是实例创建之后被调用的，用于设置对象属性的一些初始值，属于实例方法'
              u'也就是： __new__先被调用，__init__后被调用，__new__的返回值（实例）将传递给__init__方法的第一个参数，然后__init__给这个实例设置一些参数。')

# 列表[1,2,3,4,5],请使用map()函数输出[1,4,9,16,25]，并使用列表推导式提取出大于10的数，最终输出[16,25]
def fourteen():
    l = list(range(1, 6))
    print(l)
    print(list(map(lambda x: x ** 2, l)))
    print([i for i in list(map(lambda x: x ** 2, l)) if i > 10])
    return

# python中生成随机整数、随机小数、0--1之间小数方法
def fifteen():
    print(random.randint(1, 10))
    print(random.randint(1, 10))
    print(random.randint(1, 10))
    # 随机小数
    print(random.random())


# <div class="nam">中国</div> 正则匹配出“中国”
def sixteen():
    target_str = '<div class="nam">中国</div>'
    reg = r'.*?class.*?\>([\s\S]*?)\<'
    s = re.findall(reg, target_str)
    print(s[0])
    return


# assert（）方法，断言成功，则程序继续执行，断言失败，则程序报错
def seventeen():
    a = 0
    for i in range(10):
        a += i
        try:
            assert a >= 30
            print(u'程序结束...')
            print(a)
            return 111
        except:
            continue
    return 222


# 列出十个常用的linux命令
def eighteen():
    print('top, ls, pwd, grep, tailf, chmod, cp, rm, tree, mkdir')
    return


# python2和python3的区别
def nineteen():
    print(u'python2和python3的区别，列举下：'
          u'1. print函数的不同，python2没有括号，python3有括号， '
          u'2. range函数，python2返回列表，python3返回迭代器，节约内存'
          u'3. python2中如果有中文，需要引入coding')



if __name__ == '__main__':
    seventeen()
    # Thirteen()
    # t = Thirteen()
    # print(t.name)
    # eleven()
    # print(five())
    # seven()
    # argL = [1, 'a', {'name': 'xiaohuang'}]
    # eight(argL, 'asdf', u'天地无极')
    # kw = {'a': 1, 'b': 2, 'name': 'xiaolv'}
    # nine(a=1, b=2, name='xiaolv')
    # print('\033[46;33mmasdfjasd;jkfasdkfj')