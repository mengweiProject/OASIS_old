'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2021/4/1 17:20 
'''


import pandas as pd
import numpy as np


# if __name__ == '__main__':
#     # funX = lambda x: x ** 2
#     # print(funX(2))
#     # print(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
#     df = pd.DataFrame([{"col1": 11, "col2": 22, "col3": 33},
#                        {"col1": 44, "col2": 55, "col3": 66},
#                        {"col1": 77, "col2": 88, "col3": 99}], index=list("abc"))
#     print(df)
#     df["col1"] = df.apply(lambda x: x * 100, axis=1)
#     print(df)
#     df["col2"] = df.apply(lambda x: x * 100, axis=0)
#     print(df)

def applyExp1():
    df = pd.DataFrame([{"a": 1, "b": 2, "c": 3}])
    print(df)
    df["len"] = df["a"].apply(lambda x: x ** 2)
    print(df)


if __name__ == '__main__':
    applyExp1()