

from functools import reduce



# l1 = [i for i in range(100)]
# print(l1)




#过滤
# l2 = list(filter(lambda x: x % 2 != 0, l1))
# print(l2)
### [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]




# s = 'gliyfd;ihkfuigtioy;uoiygu yigh;uitg ugf;uoytg; ough;ougbughj;kh;kjlh  h jgb hbv jb jh jkh jh jkb jkb kjgb kjb kjhgb '
# s1 = list(filter(lambda x: x != ' ', s))
# s2 = ''.join(s1)
# print(s2)
### gliyfd;ihkfuigtioy;uoiyguyigh;uitgugf;uoytg;ough;ougbughj;kh;kjlhhjgbhbvjbjhjkhjhjkbjkbkjgbkjbkjhgb

# map 计算
# l3 = [i for i in range(100)]
# print(list(map(lambda x: x ** 2, l3)))
### [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900, 961, 1024, 1089, 1156, 1225, 1296, 1369, 1444, 1521, 1600, 1681, 1764, 1849, 1936, 2025, 2116, 2209, 2304, 2401, 2500, 2601, 2704, 2809, 2916, 3025, 3136, 3249, 3364, 3481, 3600, 3721, 3844, 3969, 4096, 4225, 4356, 4489, 4624, 4761, 4900, 5041, 5184, 5329, 5476, 5625, 5776, 5929, 6084, 6241, 6400, 6561, 6724, 6889, 7056, 7225, 7396, 7569, 7744, 7921, 8100, 8281, 8464, 8649, 8836, 9025, 9216, 9409, 9604, 9801]
#
# l4 = [1, 2, 3, 4, 5]
# print(list(map(lambda x: x % 2 != 0, l4)))
### [True, False, True, False, True]

# reduce 累计
# l5 = [1, 2, 3, 4, 5]
# print(reduce(lambda x, y: x * y, l5))
# ### 120



def filter_oneone():
    l = [i for i in range(100)]
    print(l)
    ll = []
    for i in l:
        if i % 2 != 0:
            ll.append(i)
    return ll

if __name__ == '__main__':
    print(filter_oneone())



