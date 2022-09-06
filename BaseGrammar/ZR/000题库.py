
import time
from datetime import datetime


# l = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
# print(max(l))
# l.remove(max(l))
# print(l)


s = 'shkdahkdmdhkajhdkja'
# print('m' in s)
#
# print('有' if 'm' in s else '没有')
#
# n = 300
# t = 250
# print('小于等于' if n <= t else '大于')
# c = '小于等于' if n <= t else '大于'
# print(c)


#判断是否为回文字符串

def judge_pd_str(s1):
    """
    判断是否为回文字符串
    :param s1: 字符串
    :return:
    """
    if s1 == s1[::-1]:
        print(True)
    else:
        print(False)


def feibo(n):
    '''
    斐波那契
    :param n:
    :return: 斐波那契数列
    '''
    a = 0
    b = 1
    l = [a, b]
    for i in range(n - 2):
        a, b = b, a + b
        l.append(b)
        # print(a, b)
    return l


def random_three():
    '''
    四个数随机组成一个3位数，三位数之间均不重复，能组成多少个，各是多少
    :return:
    '''
    l = [0, 1, 2, 3]
    count = 0
    for a in l:
        for b in l:
            for c in l:
                if a!= 0 and a != b and a != c and b != c:
                    count += 1
                    # print(a, b, c)
                    print(int(f'{a}{b}{c}'))     #第一种方法
                    # print(''.join([str(a), str(b), str(c)]))   #第二种方法
    return count


def judge_time():
    '''
    输入某年某月某日，判断这一天是这一年的第几天？
    :return:
    '''
    s = '2022-08-06'
    s1 =time.strptime(s, '%Y-%m-%d')
    print(s1)
    print(s1.tm_yday)


def paixu(a, b, c):
    '''
    输入三个整数x,y,z，请把这三个数由小到大输出
    :param a:
    :param b:
    :param c:
    :return:
    '''
    l = [a, b, c]
    print(sorted(l))


def datetime_1():
    '''
    输出当前时间：2022-07-18 17:24:32.477967
    :return:
    '''
    s = time.gmtime()
    print(s)
    print(time.strftime('%Y-%m-%d %H:%M:%S', s))
    # 输出当前时间（带小数点）
    print(datetime.now())




if __name__ == '__main__':
    # s = 'abcddcba'
    # judge_pd_str(s)
    # print(feibo(7))
    # d = {'a': 1, 'b': 2}
    # # del d['a']
    # d.pop('a')
    # print(d)
    # print(random_three())
    # judge_time()
    # paixu(84, 56, 222222)
    pass
    datetime_1()
