import csv

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def blog_download(request):
    res = HttpResponse(content_type='text/csv')
    res['Content-Disposition'] = 'attachment;filename="blog_info.csv"'
    data = ['name', 'content', 'author', 'publish_date']
    writer = csv.writer(res)
    for i in range(10):
        writer.writerow([data])
    return res