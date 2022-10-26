'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2022/10/24 8:17 
'''

import threading

lock = threading.Lock()


p_number = 0


def add_number1(times):
    global p_number
    for i in range(times):
        with lock:
            p_number += 1
    print(f'func1中：{p_number}')


def add_number2(times):
    global p_number
    for i in range(times):
        with lock:
            p_number += 1
    print(f'func2中：{p_number}')


if __name__ == '__main__':
    # add_number1()
    times = 1000000
    t1 = threading.Thread(target=add_number1, args=(times, ))
    t2 = threading.Thread(target=add_number2, args=(times, ))

    t1.start()
    t2.start()
    print(p_number)