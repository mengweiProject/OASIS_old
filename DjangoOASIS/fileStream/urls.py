'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2022/7/7 14:15
django接口返回文件流测试
'''

from django.urls import path
from . import views


urlpatterns = [
    path(r'get_user_info', views.get_user_info),
    path(r'get_user_info_excel', views.get_user_info_excel),
]