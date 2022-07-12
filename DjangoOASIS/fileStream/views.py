from django.shortcuts import render
import csv
from django.http import HttpResponse
from io import BytesIO
# Create your views here.
import xlrd
import xlwt



def get_user_info(request):
    """
    获取用户信息，以csv形式返回
    :param request:
    :return:
    """
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="user_info.csv"'

    writer = csv.writer(response)
    writer.writerow(['111', '222', '333'])
    writer.writerow(['aa', 'cc', 'bb'])

    return response


def get_user_info_excel(request):

    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment;filename=user_info.xls'

    wb = xlwt.Workbook(encoding='utf-8')

    sheet1 = wb.add_sheet('sheet-001')
    # sheet1.write(0, 0, 'A')
    # sheet1.write(0, 1, 'B')
    # sheet1.write(0, 2, 'C')
    sheet1.write(11, 11, [33, 44, 55])
    sheet1.write(12, 12, 'cc')
    output = BytesIO()
    wb.save(output)
    response.write(output.getvalue())
    return response