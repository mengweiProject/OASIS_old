from django.shortcuts import render
from time import sleep
from django.http import HttpResponse
from datetime import datetime

from Tools import time_helper

# Create your views here.


@time_helper.myAsync
def consuming_operating():
    """
    模拟耗时操作
    :return:
    """
    sleep(5)
    print(f'耗时操作结束：{datetime.now()}')
    return


# 接口示例：http://127.0.0.1:8000/asyncioApp/asyncio_request
def asyncio_request(request):
    consuming_operating()
    return HttpResponse(f'return success，后台计算仍在继续：{datetime.now()}')
