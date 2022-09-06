
from time import sleep
import datetime



#当前日期
print(datetime.datetime.now().year)             # 2022
print(datetime.datetime.now().month)            # 7
print(datetime.datetime.now().day)              # 29

#传入年月日，格式化成date对象      2020-01-01
print(datetime.date(2020, 1, 1))
print(type(datetime.date(2020, 1, 1)))

#传入时分秒，格式化成一个独立于日期的理想化时间  12:40:54
print(datetime.time(12, 40, 54))

# 2022-02-28 00:00:00
print(datetime.datetime(2022, 2, 28))

# datetime.timedelta两个对象的时间间隔    10天之后的日期
d_date = datetime.date(2022, 4, 30)
print(d_date + datetime.timedelta(days=10))

#datetime.datetime.strptime()/strftime() 用法可参考time.strptime()/strftime()
print(datetime.datetime.today())
# print(datetime.datetime.strptime())

#  0:00:03.005255
start_time = datetime.datetime.now()
sleep(3)
finish_time = datetime.datetime.now()
print(finish_time - start_time)


#
# d_date2 = datetime.date(2022, 4, 30)
# print(d_date2 - datetime.datetime.r)

