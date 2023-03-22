'''
@Project ：OASIS
@Author  ：孟威
@Date    ：2022/12/2 10:06
'''

import pandas as pd
import numpy as np

score_data_df = pd.DataFrame({"student":["01", "01", "01", "01", "01", "01", "01", "02", "02", "02", "02", "02", "02", "02"],
                         "teacher":["A","D","B","B","C","F","C","A","D","A","B","B","C","F"],
                         "course":["031","031","041","041","051","051","051","031","031","031","051","051","061","061"],
                         "homework":[100,100,98,97,100,99,98,98,92,90,92,96,97,100],
                         "final_score":[90,95,88,81,86,92,95,77,61,65,59,69,80,82]})
# print(score_data_df)

# print(pd.pivot_table(score_data_df, index='student'))
# print(score_data_df[
#           score_data_df['teacher'].isin(['A', 'B', 'D']) & ~(score_data_df['student'].str.contains('2'))
#           ]
#       )
#
# print(score_data_df[
#           (
#               (score_data_df['teacher'] == 'A') | (score_data_df['teacher'] == 'B') | (score_data_df['teacher'] == 'D')
#           ) & ~(score_data_df['student'].str.contains('2'))
#           ]
#       )
# score_data_df = score_data_df.reindex([i for i in range(len(score_data_df) + 3)])
# print(score_data_df)

# s = pd.Series([i for i in range(10)], index=[i for i in range(10, 20)])
# print(s)
# s = s.reindex([i for i in range(30)], method='ffill')
# print(s)

df1 = pd.DataFrame(
    {"student":["01", "01", "01", "01", "01", "01", "01", "02", "02", "02", "02", "02", "02", "02"],
     "teacher":["A","D","B","B","C","F","C","A","D","A","B","B","C","Z"]}
                   )

df2 = pd.DataFrame({
    'A': [1, 2, 3],
    'B': ['a', 'a', 'b']
})
print(df2)
print(df2[df2['B'].duplicated(keep=False)])




# print(df1)
# print(df1[df1['teacher'].duplicated(keep=False)])

# df2 = pd.DataFrame(
#     {
#     "student":["01", "01", "01", "01", "01", "01", "01", "02", "02", "02", "02", "02", "02", "02"],
#      "teacher":["A","D","B","B","C","F","C","A","D","A","B","B","C","F"]
# }
# )
# print(df1)
# # df1['student'] = df2['teacher']
# df1[['student', 'teacher']] = df2[['teacher', 'teacher']]
#
# print(df1)
