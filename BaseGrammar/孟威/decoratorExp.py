'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2021/3/31 11:03 
'''


def decorator(func):
    def run(username, pwd):
        print("验证...")
        return func(username, pwd)
        # return 123
    return run


@decorator
def login(username, pwd):
    print("login...", username, pwd)
    return 1

if __name__ == '__main__':
    print(login(212312, 23452345))