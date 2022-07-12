'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2022/6/27 14:13
递归实现汉诺塔
'''

import numpy as np


def recursion(n, A, B, C):
    """

    :param n:
    :param A: source
    :param B: middle
    :param C: target
    :return:
    """
    if n == 1:
        print(f'move: {A} --> {C}')
        return
    recursion(n - 1, A, C, B)
    recursion(1, A, B, C)
    recursion(n - 1, B, A, C)


if __name__ == '__main__':
    # recursion(3, 'A', 'B', 'C')
    d = {'a': 1, 'b': np.nan}
    d = {k: v if v == v and v is not None else None for k, v in d.items()}
    print(d)