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



def maxSubArray(nums):
    for i in range(1, len(nums)):
        nums[i] = nums[i] + max(nums[i - 1], 0)
        print(nums)
    return max(nums)

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(nums)
print(maxSubArray(nums))
