'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2022/10/26 10:12 
'''

# class Solution:
#     def solve(self, s, k):
#         def lcs(a, b):
#             m, n = len(a), len(b)
#             table = [[0] * (n + 1) for _ in range(m + 1)]
#             for i in range(1, m + 1):
#                 for j in range(1, n + 1):
#                     if a[i - 1] == b[j - 1]:
#                         table[i][j] = 1 + table[i - 1][j - 1]
#                     else:
#                         table[i][j] = max(table[i][j - 1], table[i - 1][j])
#             return table[m][n]
#
#         return len(s) - lcs(s, s[::-1]) <= k
#
#
# def solve(s):
#     k = 2
#     def lcs(a, b):
#         m, n = len(a), len(b)
#         table = [[0] * (n + 1) for _ in range(m + 1)]
#         for i in range(1, m + 1):
#             for j in range(1, n + 1):
#                 print(a[i - 1], b[j - 1])
#                 if a[i - 1] == b[j - 1]:
#                     table[i][j] = 1 + table[i - 1][j - 1]
#                 else:
#                     table[i][j] = max(table[i][j - 1], table[i - 1][j])
#         return table[m][n]
#
#     return len(s) - lcs(s, s[::-1]) <= k


def StringChallenge(s: str):
    # 空字符串处理
    if not s:
        return 'not possible'

    # 输入原本就是回文
    if s == s[::-1]:
        return s

    # 获取所有不同字符列表
    s_li = list(s)

    for i,n in enumerate(s_li):
        s1 = s_li.copy()
        s1.pop(i)

        # 回文检测机制
        if s1 == s1[::-1]:
            return f'{n}'

        for j,m in enumerate(s1):
            s2 = s1.copy()
            s2.pop(j)
            if s2 == s2[::-1]:
                return f'{n}{m}'
    return 'not possible'

# ob = Solution()
s = "mmop"
# k = 4
# # print(ob.solve(s, k))
print(StringChallenge(s))


def ArrayChallenge(strArr):
    appr_time_dict = {}
    for item in strArr:
        item = eval(item)
        if item[1] in appr_time_dict.keys():
            appr_time_dict[item[1]] = appr_time_dict[item[1]] + 1
        else:
            appr_time_dict[item[1]] = 1

    for i in appr_time_dict.values():
        if i > 2:
            return False
    return True
  # code goes here
  #   return strArr

# keep this function call here
# l = ["(1,2)", "(2,4)", "(5,7)", "(7,2)", "(9,5)"]
# print(ArrayChallenge(l))