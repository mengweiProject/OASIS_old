from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse


def set_cookie(request):
    res = HttpResponse('set cookie...')
    res.set_cookie('name', value='xiaohuang', max_age=100)
    return res


def get_cookie(request):
    cookie = request.COOKIES.get('name')
    return HttpResponse(f'cookie is {cookie}')


def set_session(request):
    request.session['name'] = 'xiaolv'
    return HttpResponse('set session is OK')


def get_session(request):
    session = request.session['name']
    return HttpResponse(f'session is {session}')
