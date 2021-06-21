


import pandas as pd



if __name__ == '__main__':
    # d_list = [{"a": 1, "b": 2, "c": 3}, {"a": 1, "b": 2, "c": 3}, {"a": 1, "b": 2, "c": 3}]
    # df = pd.DataFrame(d_list, index=['2019-12-01', '2019-12-02', '2019-12-03'])
    # print(df)
    # print(df.to_json())
    # print(df.to_dict())

    s = pd.Series(data=[1, 2, 3, 4, 5], index=['2019-12-01', '2019-12-02', '2019-12-03', '2019-12-04', '2019-12-05'])
    print(s)
    s = s[s.index >= '2019-12-06']
    s = s[s.index <= '2019-12-04']
    print(s)