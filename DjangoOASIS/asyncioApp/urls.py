'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2022/6/10 16:01 
'''

from django.urls import path
from . import views


urlpatterns = [
    path("asyncio_request", views.asyncio_request, name="asyncio_request"),
]