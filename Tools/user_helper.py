'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2022/2/16 8:51 
'''
from django.http import HttpResponse


def login_verification(func):
    def inner(request, *args, **kwargs):
        print(request.session)
        if 'username' not in request.session:
            c_username = request.COOKIES.get('username')
            print(c_username)
            if not c_username:
                return HttpResponse('login please...')
            else:
                request.session['username'] = c_username
        return func(request, *args, **kwargs)
    return inner