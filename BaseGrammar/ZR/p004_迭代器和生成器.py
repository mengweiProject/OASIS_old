

# 迭代器
if __name__ == '__main__':
    l = [i for i in range(10)]
    it = iter(l)
    for i in range(5):
        print(next(it))
    print('我们访问了迭代器的前五个元素，迭代器是可以记住最后一次访问位置的对象')
    print(next(it))
    print(next(it))
    for item in it:
        print(item)
# #迭代器
# 0
# 1
# 2
# 3
# 4
# 我们访问了迭代器的前五个元素，迭代器是可以记住最后一次访问位置的对象
# 5
# 6
# 7
# 8
# 9


# 生成器 所有使用了yield函数都可以看作是生成器，也可以记住最后一次访问位置的对象
def func2():
    for i in range(10):
        yield i  #类似retrun  yield可以多次返回值



if __name__ == '__main__':
    s = func2()
    for i in range(5):
        print(next(s))
    print('==========')
    print(next(s))
    print(next(s))
    print(next(s))
    print(next(s))
    print(next(s))
#
# 0
# 1
# 2
# 3
# 4
# ==========
# 5
# 6
# 7
# 8
# 9


