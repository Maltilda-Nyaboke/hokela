from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Excel
from.serializer import ExcelSerializer
import io, csv
import datetime
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage


# Create your views here.

# Create your views here.
# def excel_upload(request):
#     data = Excel.objects.all()
#     if request.method=='POST':
#         return render()
#     data_set = csv.read().decode('UTF-8')

#     context ={}
#     return render(request,'context')


@permission_required('admin.can_add_log_enable/disable')
def excel_upload(request):
    template = 'index.html'

    prompt ={
        'order':'order of CSV should be id, name, date, time, shop,maziwa_kubwa,maziwa_ndogo,premimum,daily_hope,geocoords'
    }
    if request.method =="GET":
        return render(request,template,prompt)

    csv_file =request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request,'this is not a .csv file')

    data_set = csv_file.read().decode('utf-8')
    io_string= io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string,delimiter = ',',quotechar='"'):
        _, created = Excel.objects.update_or_create(
            id = column[0],
            name =column[1],
            date = column[2],
            time =column[3],
            shop = column[4],
            maziwa_kubwa = column[5],
            maziwa_ndogo = column[6],
            premimum = column[7],
            daily_hope =column[8],
            geocoords = column[9]

        )
        context= {}
    return render(request,template,context)