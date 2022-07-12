'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2022/7/5 13:39
计算股票最大收益
假设给定一个数组，每一个索引位置的元素代表当天的股票价格，求能够获得的股票的最大收益是多少
[1, 3, 5, 4, 2]
最大收益是在第三天买入，第五天卖出，收益为3
'''



def calc_stock_max_profit(arr):
    n  = len(arr)
    dp = [0 for _ in range(n)]
    max_profit = 0
    i = 1
    min_price = arr[0]
    while i < n:
        min_price = min(min_price, arr[i])
        dp[i] = max(arr[i] - min_price, dp[i - 1])
        i += 1
    return max(dp)


if __name__ == '__main__':
    # arr = [7,1,5,3,6,4]
    arr = [7,6,4,3,1]
    print(calc_stock_max_profit(arr))