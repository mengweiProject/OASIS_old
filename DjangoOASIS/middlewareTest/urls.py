'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2022/2/22 10:19 
'''

from django.urls import path
from . import views


urlpatterns = [
   path('test_middleware', views.test_middleware),

]