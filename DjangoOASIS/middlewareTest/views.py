from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def test_middleware(request):
    print('\033[31m 333 test_middleware...]')
    return HttpResponse('test_middleware...')

