'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2021/3/24 17:29 
'''


from multiprocessing import Pool
from time import sleep


def run(n):
    sleep(2)
    # print(n)
    return n ** 2


if __name__ == '__main__':
    idList = [i for i in range(100)]
    p = Pool(10)

    for i in range(100):
        paramList = [x for x in range(i * 10, i * 10 + 10)]
        # print(paramList)
        result = p.map(run, paramList)
        print(result)
        print("==============")
        if i > 6:
            break




    # p2 = Pool(6)
    # p2.map(run, idList)