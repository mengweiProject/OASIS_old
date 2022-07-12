'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2021/3/29 12:00 
'''

def arr_to_str():
    # try:
    l1 = [123]
    print(', '.join([str(i) for i in l1]))
    # except TypeError as e:
    #     print(e)
    l2 = [11, 22, 33]
    print(', '.join([str(i) for i in l2]))

    l3 = [11, 22, '33']
    print(', '.join([str(i) for i in l3]))


if __name__ == '__main__':
    arr_to_str()