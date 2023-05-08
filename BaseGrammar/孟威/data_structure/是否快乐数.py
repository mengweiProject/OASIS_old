'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2022/11/11 8:44 
'''

class Solution:
    his_list = []
    def isHappy(self, n: int) -> bool:
        print(n)
        if n == 1:
            return True
        num = sum([int(i) ** 2 for i in list(str(n))])
        if num == 1:
            return True
        if num in Solution.his_list:
            return False
        Solution.his_list.append(num)
        print(num, Solution.his_list)
        return self.isHappy(num)


if __name__ == '__main__':
    n = 7
    s = Solution()
    print(s.isHappy(n))