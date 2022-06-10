'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2022/4/22 14:45 
'''

# from sanic import Sanic
# from sanic.response import json
#
#
# app = Sanic(__name__)
#

from time import sleep

print('这是exp001。import的操作会使得被import的文件中的代码全部执行（编译）一遍（__main__除外）')

l_001 = [1, 3, 4]

while True:
    l_001[2] += 1
    print(f'exp001：{l_001}')
    sleep(1)