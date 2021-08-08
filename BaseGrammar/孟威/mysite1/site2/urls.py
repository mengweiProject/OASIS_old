'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2021/7/20 10:21 
'''
from django.urls import path
from . import views


urlpatterns = [
    path("page2/", views.page2),
    path("page3/<int:page>", views.page3),
]