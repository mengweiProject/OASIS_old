'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2022/2/10 16:00 
'''
from django.urls import path

from . import views

urlpatterns = [
    path('set_cookie', views.set_cookie),
    path('get_cookie', views.get_cookie),
    path('set_session', views.set_session),
    path('get_session', views.get_session),

]
