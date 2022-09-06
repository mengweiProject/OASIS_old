


n = 10   #全局变量

def func1():
    global n      # local 存疑
    n = 20        # 局部变量
    # print(n)

func1()
print(n)
