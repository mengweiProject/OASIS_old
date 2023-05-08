'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2022/10/31 17:17 
'''

class Solution:
    def divideArray(self, nums):
        record_dict = {k: 0 for k in nums}
        for num in nums:
            record_dict[num] += 1
        for v in record_dict.values():
            if v % 2 == 1:
                return False
        return True


if __name__ == '__main__':
    nums = [3,2,3,2,2,2]
    s = Solution()
    print(s.divideArray(nums))