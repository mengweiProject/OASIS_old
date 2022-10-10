'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2021/3/25 16:08 
'''


if __name__ == '__main__':
    import pandas as pd

    df = pd.DataFrame([{"a": 1, "b": 2, "c": 3},
                       {"a": 2, "b": 3, "c": 3},
                       {"a": 3, "b": 4, "c": 3},
                       {"a": 4, "b": 5, "c": 3}])
    # print(df)
    # print(df.corr())
    for i in df:
        print(i)
        print(df[i])