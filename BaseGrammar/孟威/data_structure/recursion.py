'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2022/6/13 16:26 
'''


def add(n):
    if n > 0:
        return n + add(n - 1)
    else:
        return n


def add_list(arr):
    if len(arr) > 1:
        return arr[0] + add_list(arr[1: ])
    return arr[0]



if __name__ == '__main__':
    # print(add(100))
    print(add_list([1, 2, 3]))