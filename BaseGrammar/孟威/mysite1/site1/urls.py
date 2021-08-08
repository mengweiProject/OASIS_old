'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2021/7/14 9:19 
'''


from django.conf.urls import url
from django.urls import path, re_path
from . import views


urlpatterns = [
    url(r'^calcNum/$', views.calcNum),
    # re_path(r'^calcNum/$', views.calcNum),
    url(r"^calcNumsWords/$", views.calcNumsWords),
    path('page1', views.page1),
]