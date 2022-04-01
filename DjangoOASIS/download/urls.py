'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2022/2/23 14:57 
'''
from django.urls import path
from . import views

urlpatterns = [
    path('blog_download', views.blog_download),
]