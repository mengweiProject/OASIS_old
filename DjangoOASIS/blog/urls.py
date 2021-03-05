from django.urls import path
from . import views


urlpatterns = [
    path("index", views.index, name="index"),
    path("service", views.serviceList, name="serviceList"),
    path("testJson", views.testJson, name="testJson")
]