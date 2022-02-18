'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2022/2/15 9:50 
'''
from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login),
    path('get_user_info', views.get_user_info),
    path('log_out', views.log_out),

]