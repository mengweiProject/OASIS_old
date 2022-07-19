'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2022/7/14 9:22 
'''


import time
from collections import Iterable


# 实现一个可迭代对象
class MyIterable:
    def __init__(self):
        self.my_list = list()
        # 记录当前按索引取数的下标
        self.current_index = 0


    def append_item(self, item):
        self.my_list.append(item)


    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index < len(self.my_list):
            self.current_index += 1
            return self.my_list[self.current_index - 1]
        else:
            print('元素取完了，你还想干嘛？')
            raise StopIteration


if __name__ == '__main__':
    it = MyIterable()
    it.append_item(1)
    it.append_item(2)
    it.append_item(3)
    res = isinstance(it, Iterable)
    print(res)
    print(type(it))

    for item in it:
        print(item)
