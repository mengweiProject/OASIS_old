'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2021/7/15 15:26 
'''


def func(seq1, seq2, seq3):
    # 返回值：返回一个map对象
    # 入参：map(function, sequence) ：对sequence中的item依次执行function(item)，将执行结果function(item)组成一个map对象
    # 作用：对列表入参依次执行函数。入参为列表，有多少个列表，就应该有多少个入参
    # return list(map(lambda x, y, z: x + y + z, seq1, seq2, seq3))
    return list(map(addSeq, seq1, seq2, seq3))


def addSeq(*args):
    return sum(args)


if __name__ == '__main__':
    seq1, seq2, seq3 = range(10), range(10, 20), range(20, 30)
    print(func(seq1, seq2, seq3))