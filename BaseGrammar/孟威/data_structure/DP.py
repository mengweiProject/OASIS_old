'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2022/7/4 10:53
DP，动态规划
'''


def db_make_change(coinValueList, change, minCoins):
    """
    找零问题，动态规划解法
    :return:
    """
    for cents in range(1, change + 1):
        coinCount = cents
        for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents - j] + 1 < coinCount:
                coinCount = minCoins[cents - j] + 1