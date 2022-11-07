'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2022/11/4 14:40

给你一个由若干 0 和 1 组成的数组 nums 以及整数 k。如果所有 1 都至少相隔 k 个元素，则返回 True ；否则，返回 False 。

拼接成字符串按1分割，判断每组0的个数（分割子串的长度）如果小于k，则返回False
'''


class Solution:
    def kLengthApart(self, nums, k):
        print(''.join([str(i) for i in nums]).split('1'))
        for item in ''.join([str(i) for i in nums]).split('1')[1:-1]:
            if len(item) < k:
                return False
        return True


if __name__ == '__main__':
    # nums = [1,0,0,0,1,0,0,1]
    # nums = [1,0,0,0,1,0,0,1,0]
    nums = [1,1,1,0]
    k = 2
    s = Solution()
    print(s.kLengthApart(nums, k))