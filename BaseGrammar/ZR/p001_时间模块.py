

import time


#获取当前时间  time.localtime()/time.gmtime()
print(time.localtime())     # time.struct_time(tm_year=2022, tm_mon=7, tm_mday=29...
print(time.gmtime())        # time.struct_time(tm_year=2022, tm_mon=7, tm_mday=29...

#sleep阻塞函数，让当前程序沉睡几秒
time.sleep(3)
print('end......')      #沉睡3秒后 print('end......')

#格式化当前时间 日期 >>> 字符串
print(time.strftime('%Y年%m月%d日 %H：%M：%S', time.localtime()))        # 2022年07月29日 19：50：23

#字符串 >>> 日期
s = '2022-07-28'
print(time.strptime(s, '%Y-%m-%d'))         # time.struct_time(tm_year=2022, tm_mon=7, tm_mday=28...

l = '2022年07月28日 20：42：38'
s = time.strptime(l, '%Y年%m月%d日 %H：%M：%S')
print(s)                     # time.struct_time(tm_year=2022, tm_mon=7, tm_mday=28...
print(time.strftime('%d day %m month %Y year %H = %M = %S'))        # 29 day 07 month 2022 year 19 = 50 = 23

#时间戳
a = time.time()
print(a)        # 1659095423.159005
print(time.gmtime(a))       # time.struct_time(tm_year=2022, tm_mon=7, tm_mday=29...

#mktime()，将 结构化时间 转换为 时间戳
l = '2022年07月28日 20：42：38'
s = time.strptime(l, '%Y年%m月%d日 %H：%M：%S')
print(s)        # time.struct_time(tm_year=2022, tm_mon=7, tm_mday=28, tm_hour=20...
print(time.mktime(s))       # 1659012158.0





