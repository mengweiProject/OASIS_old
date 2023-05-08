'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2022/11/4 13:25

给定一个字符串，编写一个函数判定其是否为某个回文串的排列之一。

回文串是指正反两个方向都一样的单词或短语。排列是指字母的重新排列。

回文串不一定是字典当中的单词。



示例1：

输入："tactcoa"
输出：true（排列有"tacocat"、"atcocta"，等等）

'''


class Solution:
    def canPermutePalindrome(self, s: str):
        appear_time_dict = {k: 0 for k in s}
        for item in s:
            appear_time_dict[item] += 1
        jishu_times = 0
        for value in appear_time_dict.values():
            if value % 2 == 1:
                jishu_times += 1
                if jishu_times > 1:
                    return False
        return True


if __name__ == '__main__':
    l = 'tactcoa'
    s = Solution()
    print(s.canPermutePalindrome(l))