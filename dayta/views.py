from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Excel
from.serializer import ExcelSerializer
import io, csv
import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage


# Create your views here.

# Create your views here.
def excel_upload(request):
    data = Excel.objects.all()
    if request.method=='POST':
        return render()
    data_set = csv_file.read().decode('UTF-8')

    context ={}
    return render(request,'context')


def welcome(request):
    return render(request,'index.html')
