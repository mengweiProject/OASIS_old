'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2022/10/24 9:36 
'''

import multiprocessing
from time import sleep


def sub_process():
    # while True:
    for i in range(3):
        sleep(1)
        print('sub_processing...')
#
#
# if __name__ == '__main__':
#     p = multiprocessing.Process(target=sub_process)
#     p.start()   # 调用start()方法的时候才会真正创建进程！！！
#
#     while True:
#         sleep(0.1)
#         print('main processing...')

# class SubPorcessing(multiprocessing.Process):
#     def __init__(self):
#         super().__init__()
#
#     def run(self) -> None:
#         # while True:
#         sleep(1)
#         print('子任务执行...')
#
#
# # if __name__ == '__main__':
#
# sp = SubPorcessing()
# sp.start()
#
# while True:
#     sleep(2)
#     print(f'main...')



if __name__ == '__main__':
    p = multiprocessing.Process(target=sub_process)
    p.start()

    p.join()
    print('end...')
