
"""
表格处理
"""

import xlwt


ex = xlwt.Workbook(encoding='utf-8')    # 创建excel操作对象，相当于新建一个工作簿，但是还没有保存

sheet1 = ex.add_sheet('希特1')        # 创建

for i in range(1, 10):
    for j in range(1, i+1):
        sheet1.write(i-1, j-1, f'{j} * {i} = {i * j}')


sheet2 = ex.add_sheet('希特2')        # 创建

for i in range(10):
    for j in range(10):
        sheet2.write(i, j, i * j)

sheet3 = ex.add_sheet('希特3')        # 创建

for i in range(1, 6, 2):
    for j in range(1, 6):
        sheet3.write(i // 2, j-1, '*' * i)
        # print(i // 2, j-1, '*' * i)

sheet4 = ex.add_sheet('希特4')  # 创建 抛物线

for i in range(15):
    sheet4.write(i, (i - 2) ** 2 + 3 , '*')

ex.save(r'C:\Users\13395\Desktop\projectDir\tempFiles\九九乘法表.xlsx')




# 格式
# 样式