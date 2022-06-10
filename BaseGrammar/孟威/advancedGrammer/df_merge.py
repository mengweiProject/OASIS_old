'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2022/4/19 10:37 
'''

import pandas as pd

df1 = pd.DataFrame({'id': [1, 2, 4],
                    'A': ['a1', 'a2', 'a4'],
                    'B': ['b1', 'b2', 'b4'],
                    'D': ['d1', 'd2', 'd4']})

df2 = pd.DataFrame({'id': [1, 3],
                    'C': ['c1', 'c3']})

print(df1)
print(df2)

print(pd.merge(df1, df2, how='inner', on='id'))