from django.shortcuts import render
from django.http import HttpResponse
import json


# Create your views here.


def index(request):
    return HttpResponse("欢迎来到绿洲科技！")


def serviceList(request):
    return HttpResponse("服务列表：...")


def testJson(request):
    infoJson = {"name": "威震天", "age": "999", "wars": ["大战擎天柱", "手撕大黄蜂", "脚踢救护车"]}
    return HttpResponse(json.dumps(infoJson))