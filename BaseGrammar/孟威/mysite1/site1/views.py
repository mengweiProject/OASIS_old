from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

# Create your views here.


def calcNum(request):
    x = int(request.GET.get('x'))
    y = int(request.GET.get('y'))
    # return lambda x, y: x + y
    # return JsonResponse({'ret': 123})
    return HttpResponse(x + y)


def calcNumsWords(request):
    targetWords = str(request.GET.get("targetWords"))
    print(targetWords)
    return JsonResponse({"times": targetWords.split(" ").count("you")})


def page1(request):
    return HttpResponse("this is my pate1")