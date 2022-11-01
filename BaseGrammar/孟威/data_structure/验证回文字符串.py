'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2022/10/31 16:16 
'''

class Solution:
    def validPalindrome(self, s):
        s_len = len(s)
        # print(s)
        l_index = 0
        r_index = s_len - 1
        # print(s[l_index])
        # print(s[r_index])
        while l_index < r_index:
            if s[l_index] == s[r_index]:
                l_index += 1
                r_index -= 1
            else:
                break
        # print(l_index, r_index)
        # print(s[:l_index], s[l_index+1:])
        # print(s[:l_index] + s[l_index+1:] == s[l_index+1:][::-1] + s[:l_index][::-1])
        # print(s[:r_index] + s[r_index+1:], s[r_index+1:][::-1] + s[:r_index][::-1])
        # print(s[:r_index], s[r_index+1:])
        return s[:l_index] + s[l_index+1:] == s[l_index+1:][::-1] + s[:l_index][::-1] or \
               s[:r_index] + s[r_index + 1:] == s[r_index+1:][::-1] + s[:r_index][::-1]




if __name__ == '__main__':
    s = 'aba'
    solution = Solution()
    print(solution.validPalindrome(s))