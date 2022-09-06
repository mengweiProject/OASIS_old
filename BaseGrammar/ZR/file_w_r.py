
'''
时间：2022/7/17
作者：小威威
功能：文件读/写
'''

with open(file=r'asdf.txt', mode='r') as f:

    # 多行读取，一次读取文件所有的内容，返回一个列表，列表的每个元素，是文件的一行
    # print(f.readlines())
    # for line in f.readlines():
    #     print(line)
    print(f.readlines())
    print(f.readlines())
    # 按行读取，每次读取一行。且下一次调用，会读取到下一行内容，不会重复（后续可参考生成器）
    # print(f.readline())
    # print(f.readline())
    # print(f.readline())
    # print(f.readline())
    # print(f.readline())
    # print(f.readline())
    # print(f.readline())


# with open(file=r'asdf.txt', mode='a') as f:

    # f.write('这是我追加的第三行\n')
    # f.write('这是我追加的第四行\n')

