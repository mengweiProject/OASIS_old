from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.

def page2(request):
    return JsonResponse({"msg": "OK", "code": 0, "data": "this is my page2"})


def page3(request, page):
    return HttpResponse("this is my page{}".format(page))