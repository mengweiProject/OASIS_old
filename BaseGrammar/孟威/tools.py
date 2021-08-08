'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2021/7/15 15:06 
'''


from datetime import datetime, date
from time import sleep


def calcTimeCost(paramFunc):
    def timeCost():
        sDate = datetime.now()
        paramFunc()
        fDate = datetime.now()
        print(fDate - sDate)
    return timeCost


def calcTimeCostParams(paramFunc):
    def timeCost(n, m):
        sDate = datetime.now()
        paramFunc(n, m)
        fDate = datetime.now()
        print(fDate - sDate)
    return timeCost


