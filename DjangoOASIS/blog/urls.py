from django.urls import path
from . import views


urlpatterns = [
    path("index", views.index, name="index"),
    path("service", views.serviceList, name="serviceList"),
    path("testJson", views.testJson, name="testJson"),
    path("set_cookies_t", views.set_cookies_t, name="set_cookies_t"),
    path("get_cookies_t", views.get_cookies_t, name="get_cookies_t"),

    path('add_blog', views.add_blog),
    path('show_blog', views.show_blog),
    path('show_current_time_cache', views.show_current_time_cache),
    path('exp_local_cache', views.exp_local_cache),
]