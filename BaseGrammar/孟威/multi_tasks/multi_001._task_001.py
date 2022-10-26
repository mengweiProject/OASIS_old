'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2022/10/17 9:31 
'''

import threading
from time import sleep


def default_func(a, b, c=3, name='xiaohuang'):
    for i in range(5):
        print(f'default_func_{i}_{a}_{b}')
        sleep(1)



# def sing():
#     for _ in range(3):
#         print('是谁在唱歌，呦吼..')
#         sleep(1)
#
#
# def dance():
#     for _ in range(3):
#         print('跳舞...')
#         sleep(1)
#
#
# if __name__ == '__main__':
#     # sing()
#     # dance()
#     t1 = threading.Thread(target=sing)
#     t2 = threading.Thread(target=dance)
#     t1.start()
#     t2.start()

# def say_helle():
#     sleep(1)
#     print('helllo everyone')
#     return 'helllo'
#
# if __name__ == '__main__':
#     for i in range(3):
#         t = threading.Thread(target=say_helle, name=f't_{i}')
#         t.start()
#         print(t.name)


# print(threading.enumerate())
# t = threading.Thread(target=default_func, args=(11, 22), name=default_func.__str__())
# t.start()
# print(threading.enumerate())

# print(threading.enumerate())
# # t = threading.Thread(target=default_func, args=(11, 22), kwargs={'c': 33, 'name': 'xiaolv'}, name=default_func.__str__())
# # t.start()
# # print(threading.enumerate())


class ThreadMan(threading.Thread):
    def run(self) -> None:
        print('这是我自己定义的run方法，当调用start方法的时候，会执行这里的run方法')


if __name__ == '__main__':
    t = ThreadMan()
    t.start()