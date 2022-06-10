'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2022/4/25 9:48 
'''

import numpy as np
import pandas as pd

# from SanicExp import exp001
from time import sleep

def a(s_d):
    s_d['a'] = 1


if __name__ == '__main__':
    s_d = {'a': 2}
    a(s_d)
    print(s_d)
    # print('这是exp002')
    # while True:
    #     exp001.l_001 += 2
    #     print(exp001.l_001)
    #     sleep(3)
    # df = pd.DataFrame(np.random.random((3, 5)))
    # print(df)