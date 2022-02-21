from django.core.cache import cache
from django.shortcuts import render
from django.http import HttpResponse
import json
from time import sleep
from datetime import datetime


# Create your views here.
from django.views.decorators.cache import cache_page

from Tools.user_helper import login_verification
from DAO.blog_helper import add_blog_dao
from DAO import blog_helper


def index(request):
    return HttpResponse("欢迎来到绿洲科技！")


def serviceList(request):
    return HttpResponse("服务列表：...")


def testJson(request):
    infoJson = {"name": "威震天", "age": "999", "wars": ["大战擎天柱", "手撕大黄蜂", "脚踢救护车"]}
    return HttpResponse(json.dumps(infoJson))


def set_cookies_t(request):
    res = HttpResponse('success')
    res.set_cookie('my_cookie', value='xiaohuang', max_age=100)
    return res


def get_cookies_t(request):
    cookie = request.COOKIES.get('my_cookie', None)
    print(cookie)
    return HttpResponse('success get cookies')


@login_verification
def add_blog(request):
    title = request.GET.get('title')
    author = request.GET.get('author')
    content = request.GET.get('content')
    ret = add_blog_dao(title, author, content)
    return HttpResponse(f'insert result is {"success" if ret == 0 else "failure"}')


@cache_page(30)
@login_verification
def show_blog(request):
    print(request.GET)
    # df = blog_helper.show_blog_by_keys(title=request.GET.get(), author=request.GET.get('author'))
    df = blog_helper.show_blog_by_keys()
    print(df)
    return HttpResponse(df.to_json())


@cache_page(10)
def show_current_time_cache(request):
    t = datetime.now()
    return HttpResponse(t)


def exp_local_cache(request):
    cache.set('myname', 'mengweiaksdjfa;lsdjfa;lkdjf;lakds', 20)
    print(cache)
    # print(help(cache))
    key = cache.get('myname')
    print(key)
    return HttpResponse(key)
    # return HttpResponse('key')