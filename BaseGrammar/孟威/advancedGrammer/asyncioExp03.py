'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2022/6/10 15:57 
'''


from threading import Thread


def myAsync(func):
    def wrapper(*args, **kwargs):
        t = Thread(target=func, args=args, kwargs=kwargs)
        t.start()
    return wrapper