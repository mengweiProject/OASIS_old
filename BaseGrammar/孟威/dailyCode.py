'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2021/9/16 10:47 
'''


import pandas as pd


def reindexing_only_valid_exception():
    """
    index.map 报错 reindexing only valid with
    :return:
    """
    df1 = pd.DataFrame(index=[0, 1])
    s1 = pd.Series(data=[11, 22, 33], index=[2, 3, 3])
    # print(s1.index.drop_duplicates(keep='first').tolist())
    # print(s1[s1.index.drop_duplicates(keep='first').tolist()])
    # # s1 = s1[[s1.index.drop_duplicates().tolist()]]
    # print(s1.reindex(s1.index.drop_duplicates(keep='first').tolist()))
    # print(df1)
    print(pd.Series(s1.to_dict()))
    print('-' * 20)
    print(s1)
    # df1['s1'] = df1.index.map(s1)
    # print(f'df3: {df1}')


def exp_slice():
    l = [i for i in range(1, 100)]
    print(l[ :20])


if __name__ == '__main__':
    exp_slice()