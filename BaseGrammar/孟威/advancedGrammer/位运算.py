'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2022/10/27 9:59 
'''

# n = 16
# print(n)
# print(bin(n))   # 十进制转二进制
# print(oct(n))   # 十进制转八进制
# print(hex(n))   # 十进制转十六进制
#
# # 16
# # 0b10000
# # 0o20
# # 0x10
#
# print(int('10000', 2))  # 二进制转十进制
# print(int('0o20', 8))   # 八进制转十进制
# print(int('0x10', 16))  # 十六进制转十进制
#
# # 除十进制外，其他进制之间相互转换，需要使用十进制中转
# # 八进制转十六进制，应该先由八进制转成十进制，再从十进制转十六进制
# print(hex(int('0o20', 8)))



# a = 11
# print(bin(a))
# print(a << 3)
# print(bin(a << 3))

# print(21 & 6)
# print(bin(21))
# print(bin(6))
# print(bin(21 & 6))

# &：按位与运算符，参与运算的两个值，如果两个相应位都为1，则该位的结果为1，否则为0；
# print(bin(21))
# print(bin(6))
# print(bin(21 & 6))



# |：按位或运算符，只要对应的二个二进位有一个为1时，结果位就为1；
# print(bin(21))
# print(bin(6))
# print(bin(21 | 6))



# ^：按位异或运算符，当两对应的二进位相异时，结果为1；
# print(bin(21))
# print(bin(6))
# print(bin(21 ^ 6))



# ~：按位取反运算符，对数据的每个二进制位取反，即把1变为0，把0变为1；
# print(bin(21))
# print(~21)
# print(bin(~21))

# >>：右移动运算符，把 >> 左边的运算数的各二进位全部右移若干位，>> 右边的数指定移动的位数；
# print(bin(21))
# print(21 >> 3)
# print(bin(21 >> 3))


# <<：左移动运算符，运算数的各二进位全部左移若干位，由 << 右边的数指定移动的位数，高位丢弃，低位补0。
# print(bin(21))
# print(21 << 3)
# print(bin(21 << 3))

# for idx, item in enumerate(list(range(10))):
#     print(idx, item)

