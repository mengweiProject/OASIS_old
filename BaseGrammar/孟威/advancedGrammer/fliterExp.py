'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2021/7/15 15:26 
'''


def func(sequence):
    # filter返回值类型是一个filter对象
    # filter方法作用：filter(function, sequence)：对sequence中的item依次执行function(item)
    # 将执行结果为True的item组成一个filter对象
    # return list(filter(lambda x: x % 2 == 0, sequence))
    return list(filter(is2, sequence))

def is2(n):
    return True if n % 2 == 0 else False


if __name__ == '__main__':
    seq = list(range(100))
    print(func(seq))