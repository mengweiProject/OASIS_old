'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2021/3/8 9:03

常量配置
'''

import string


# 程序执行结果，0表示成功，4表示失败
SUCESS = 0
FAILURE = 4
# 已存在
EXISTENCE = 5
# 不存在
NOTEXISTENCE = 6


# 26个大写/小写字母，列表
UPPERCASE = [chr(i) for i in range(65, 91)]
LOWERCASE = [chr(i) for i in range(97, 123)]


if __name__ == '__main__':
    print(string.ascii_lowercase)
    print(string.ascii_uppercase)
    print(ord("A"))
    print(ord("z"))
    print(chr(122))
    print(UPPERCASE)
    print(LOWERCASE)