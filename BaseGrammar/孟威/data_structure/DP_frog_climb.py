'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2022/7/5 13:24
青蛙跳台阶，动态规划解法
'''


def frog_climb_steps(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return frog_climb_steps(n - 1) + frog_climb_steps(n - 2)


if __name__ == '__main__':
    print(frog_climb_steps(4))