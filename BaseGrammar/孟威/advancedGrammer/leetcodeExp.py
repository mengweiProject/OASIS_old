'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2022/4/20 9:54

def climbStairs(self, n: int) -> int:
    dp = [0] * (n + 1)
    dp[0] = dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[-1]


'''

import timeit
import pysnooper


# def maxSubArray(nums):
#     for i in range(1, len(nums)):
#         nums[i] = nums[i] + max(nums[i - 1], 0)
#         print(nums)
#     return max(nums)
#
# nums = [-2,1,-3,4,-1,2,1,-5,4]
# print(nums)
# print(maxSubArray(nums))


@pysnooper.snoop()
def countElements(nums):
    print(min(nums))
    print(max(nums))
    print(min(nums) < num < max(nums) for num in nums)
    for num in nums:
        print(min(nums) < num < max(nums))
    print(sum(i > 10 for i in range(20)))
    return sum(min(nums) < num < max(nums) for num in nums)

def calc_s():
    n = 0
    for i in range(1000000):
        n += i


nums = [11,7,2,15]
countElements(nums)
# print(timeit.timeit('calc_s()', 'from __main__ import calc_s', number=2))

