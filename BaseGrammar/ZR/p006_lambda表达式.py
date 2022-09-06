

l = lambda x: x ** 2
print(l(2))      ### 4

#排序
# l1 = [1, 3, 5, 7, 9, 8, 6, 4, 2]
#
# rule_l = [0, 1, 3, 4, 5, 6, 7, 8, 9, 2]
#
# # l2 = sorted(l1, reverse=False)
# # print(l2)
#
# print([rule_l[i] for i in l1])
#
# l3 = sorted(l1, key=lambda x: rule_l[x])
# print(l3)


nums = [2, 3, 0, 1, 5, 4]
nums1 = sorted(nums, key=lambda x: x*-1)
print(nums1)
### [5, 4, 3, 2, 1, 0]
