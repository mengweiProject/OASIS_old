'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2022/11/2 8:38 
'''


class Solution:
    def isStraight(self, nums):
        nums.sort()
        zero_nums = 0
        diff_sum = 0
        nums_temp = nums.copy()
        nums_temp.insert(0, 0)
        print(nums)
        print(nums_temp)
        # print(not (0 and 0))
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_nums += 1
            if not (nums[i] and nums_temp[i]):
                continue
            if nums[i] == nums_temp[i]:
                return False
            diff = nums[i] - nums_temp[i] - 1
            if diff > 0:
                diff_sum += diff
        print(diff_sum, zero_nums)
        return zero_nums >= diff_sum
        # return len(list(filter(lambda x: x == 0, nums))) >= sum(list(filter(lambda x: x > 0, [x - y - 1 for x, y in zip(nums_temp, nums[1:])])))

if __name__ == '__main__':
    # nums = [0,0,2,2,5]
    nums = [4,1,6,0,9]
    s = Solution()
    print(s.isStraight(nums))
    # print(list(range(4)))