import hashlib

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from DAO import user_info
from Tools import constants
from Tools.user_helper import login_verification


def login(request):
    if request.method == 'POST':
        print('regist...')
        print(request.POST)
        user_name = str(request.POST.get('user_name'))
        pwd = str(request.POST.get('pwd'))
        exist_flag = user_info.check_user_name(user_name)
        if exist_flag == constants.EXISTENCE:
            return HttpResponse('already exist user name, change one, please.')

        m = hashlib.md5()
        # m.update(b'123456')
        m.update(bytes(pwd, encoding='utf-8'))
        print(m.hexdigest())
        user_info.insert_into_user_info(user_name, m.hexdigest())

        # 注册成功之后，一天之内免登录，在settings.py中配置：SESSION_COOKIE_AGE = 60 * 60 * 24
        request.session['username'] = user_name

        return HttpResponse('register success..')
    else:
        user_name = request.GET.get('user_name')
        pwd = request.GET.get('pwd')
        md5_pwd = hashlib.md5()
        # md5_pwd.update(bytes(pwd, encoding='utf-8'))
        md5_pwd.update(pwd.encode())
        # pwd = md5_pwd.hexdigest()

        user_info_df = user_info.look_for_user_df(user_name)
        if user_info_df is not None:
            pwd = user_info_df.iloc[0]['pwd']
            print(pwd, md5_pwd.hexdigest())
            if pwd == md5_pwd.hexdigest():
                resp = HttpResponse('logging in sucess, jump to index.html...')
                resp.set_cookie('username', user_name)
                return resp
            else:
                return HttpResponse('username or pwd wrong...')
        return HttpResponse('register first please...')


@login_verification
def get_user_info(request):
    user_name = request.COOKIES.get('username')
    print(user_name)
    user_info_df = user_info.look_for_user_df(user_name)
    print(user_info_df)
    return HttpResponse(user_info_df.to_records())


@login_verification
def log_out(request):
    res = HttpResponse('log out... ')
    if 'username' in request.session:
        del request.session['username']
    if 'username' in request.COOKIES:
        res.delete_cookie('username')
    return res