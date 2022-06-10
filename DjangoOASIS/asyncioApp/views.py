from django.shortcuts import render
from time import sleep
from django.http import HttpResponse

from Tools import time_helper

# Create your views here.


@time_helper.myAsync
def consuming_operating():
    """
    模拟耗时操作
    :return:
    """
    sleep(5)
    return


# 接口示例：http://127.0.0.1:8000/asyncioApp/asyncio_request
def asyncio_request(request):
    consuming_operating()
    return HttpResponse('return success，后台计算仍在继续')
