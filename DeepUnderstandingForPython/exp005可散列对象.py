'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2022/7/26 10:55 
'''



if __name__ == '__main__':
    d = {(1, 2, 3): {1, 2, 3}}
    print(d)
    print(type(d))
    print(type(d.keys()))
    for key in d.keys():
        print(key)
        print(type(key))