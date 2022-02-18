'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2022/2/7 14:38

给你一个 m * n 的矩阵，矩阵中的数字 各不相同 。请你按 任意 顺序返回矩阵中的所有幸运数。

幸运数是指矩阵中满足同时下列两个条件的元素：

在同一行的所有元素中最小
在同一列的所有元素中最大
 

示例 1：

输入：matrix = [[3,7,8],[9,11,13],[15,16,17]]
输出：[15]
解释：15 是唯一的幸运数，因为它是其所在行中的最小值，也是所在列中的最大值。
示例 2：

输入：matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
输出：[12]
解释：12 是唯一的幸运数，因为它是其所在行中的最小值，也是所在列中的最大值。
'''

import random
import numpy as np

np.random.seed(1)
random.seed(1)


def calc_lucky_N(matrix):
    for row in matrix:
        print(row)

    print()
    for column in np.transpose(matrix):
        print(column)





if __name__ == '__main__':
    # rows = [random.randint(0, 10) for _ in range(10)]
    rows = 3
    columns = 6
    matrix = [[random.randint(0, 10) for _ in range(columns)] for _ in range(rows)]
    # print(matrix)
    # for row in matrix:
    #     print(row)
    # matrix = np.random.randint(1, 10, (3, 3))
    # print(matrix)
    # print(matrix[0][1])
    calc_lucky_N(matrix)