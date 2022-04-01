'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2022/2/22 10:04 
'''
from django.utils.deprecation import MiddlewareMixin


class PrintMiddleWare(MiddlewareMixin):

    def process_request(self, request):
        print('111 before request...')

    def process_view(self, request, view_func, view_args, view_kwargs):
        print('222 before view...')

    def process_exception(self, request, exception):
        print('exception process...')

    def process_response(self, request, response):
        print('444 before response')
        return response
