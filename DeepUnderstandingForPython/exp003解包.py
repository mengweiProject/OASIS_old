'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2022/7/25 9:29 
'''


import pandas as pd



def func1(a, b, c):
    print(f'{a, b, c}')


def func2(a=1, b=2, c=3):
    print(a)
    print(b)
    print(c)



if __name__ == '__main__':
    # a, b, c = 1, 2, 3
    # l = [a, b, c]
    # func1(*l)
    # d = {'a': 1, 'b': 2, 'c': 3}
    # func2(**d)
    df1 = pd.DataFrame()
    df2 = pd.DataFrame(data=[1, 2, 3], columns=['a'])
    print(df2)
    df1 = df1.append(df2)
    print(df1)