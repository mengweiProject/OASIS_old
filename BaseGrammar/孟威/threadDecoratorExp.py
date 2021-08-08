'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2021/7/5 16:28 
'''


import random
import threading
import time


def background_thread(func):
    def callf(*args, **kwargs):
        # args=(*args,)正常 kwargs=kwargs 未验证
        t = threading.Thread(target=func, args=(*args,), kwargs=kwargs)
        t.start()
        # t.join()  # 不等待子线程结束
        return  # 不需要子线程函数执行结果

    return callf


@background_thread
def demo_thr(sleep, name):
    print('Hi, ', name)
    time.sleep(sleep)
    print('end demo_thr')
    return 'demo_thr 执行完成'


if __name__ == '__main__':
    # demo_thr(5, 'Caspar')
    # demo_thr(5, 'Caspar')
    # demo_thr(5, 'Caspar')
    # demo_thr(5, 'Caspar')
    for i in range(65001):
        print(hex(i))




# def run_async(func):
#     def wrapper(*args, **kwargs):
#         thr = threading.Thread(target = func, args = args, kwargs = kwargs)
#         thr.start()
#         thr.setName("func-{}".format(func.__name__))
#         # thr.join()
#         print("线程id={},\n线程名称={},\n正在执行的线程列表:{},\n正在执行的线程数量={},\n当前激活线程={}".format(
#             thr.ident,thr.getName(),threading.enumerate(),threading.active_count(),thr.isAlive)
#         )
#     return wrapper
#
#
#
# @run_async
# def test(param):
#     while True:
#         time.sleep(3)
#         t = random.randint(1,param)
#         print("/test:" + str(t))
#
#
# @run_async
# def test2(param):
#     while True:
#         time.sleep(2)
#         t = random.randint(1,param)
#         print("/test2:" + str(t))
#
#
#
# # test(10)
# test2(1000)