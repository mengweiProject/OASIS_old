
from time import sleep
from datetime import datetime

def calc_run_time(func):
    print('calc_run_time函数')
    def inner(*args, **kwargs):
        start_time = datetime.now()
        func(*args, **kwargs)
        finish_time = datetime.now()
        print(f'该函数的运行时间是:{finish_time - start_time}')
    return inner


#函数的嵌套
def print1():
    print('print1正在执行')
    def print_inner():
        print('print_inner正在执行')
    # print_inner()


#闭包  1.一定要有函数的嵌套2.外部函数的返回值是内部函数3.内部函数调用外部函数的参数/变量
def print2(func):
    # print('print111111111正在执行')
    def print_inner(*args, **kwargs):
        print('print_inner正在执行')
        func()
    return print_inner


#装饰器
# @print2
def print3():
    print('print3正在执行')



def check_name(func):
    print('check_name函数')
    def inner(*args, **kwargs):
        user_name = args[0]
        pwd = args[1]
        print(user_name)
        print(pwd)
        if len(user_name) > 6:
            func(user_name, pwd)
        else:
            print('用户名不合法')
    return inner


# @check_name
# @calc_run_time
def register(user_name, pwd):
    print('开始注册')
    print('写入数据库')
    print('注册成功')


def check_purchase(func):
    print('check_purchase函数')
    def inner(*args, **kwargs):
        sleep(1)
        balance = args[0]
        price = args[1]
        if balance >= price:
            func(balance, price)
        else:
            print('余额不足，请充值')
    return inner



@calc_run_time
@check_purchase
def buy(balance, price):
    curr_balance = balance - price
    sleep(3)
    print(curr_balance)


# @calc_run_time
def my_sleep(n):
    print('开始sleep')
    sleep(n)
    print('结束sleep')

#
if __name__ == '__main__':
    # print3()
    register('asdfdhaksjhd', 123456)
    # buy(1000, 100)
    # pass
    # start_time = datetime.now()
    # print(start_time)
    # sleep(3)
    # finish_time = datetime.now()
    # print(finish_time)
    # print(f'该函数的运行时间是:{finish_time - start_time}')
    # my_sleep(4)