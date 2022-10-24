from django.shortcuts import render,redirect
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Excel
from resources import ExcelResource
from tablib import Dataset
from.serializer import ExcelSerializer
import io, csv
from .forms import *
import datetime
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
import os
from django.conf import settings
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            email = form.cleaned_data['email']
    else:    
        form = RegisterForm()
    return render(request, 'register.html',{'form':form}) 
# def login_user(request):
#     form = AuthenticationForm()
#     context = {'form':form}
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request,user)
#             return redirect('/')
#         else:
#             return render(request,'registration/login.html',context)  
#     else:
#         return render(request, 'registration/login.html',context)  

# def logout_user(request):
#     logout(request)
#     return redirect('login')        
def excel_upload(request):
    if request.method == 'POST':
        excel_resource = ExcelResource()
        dataset = Dataset()
        new_excel = request.FILES['myfile']
        if not new_excel.name.endswith('.xlsx'):
            messages.error(request,'this is not a .xlsx file')
            return render(request,'index.html')
        imported_data = dataset.load(new_excel.read(),format='xlsx')
        for data in imported_data:
            value = Excel(
                data[0],
                data[1],
                data[2],
                data[3],
                data[4],
                data[5],
                data[6],
                data[7],
                data[8],
                data[9]
            )
            value.save()
    return render(request, 'index.html')
        

# @permission_required('admin.can_add_log_enable/disable')
# def excel_upload(request):
#     template = 'index.html'

#     prompt ={
#         'order':'order of CSV should be id, name, date, time, shop,maziwa_kubwa,maziwa_ndogo,premimum,daily_hope,geocoords'
#     }
#     if request.method =="GET":
#         return render(request,template,prompt)

#     csv_file =request.FILES['file']

#     if not csv_file.name.endswith('.csv'):
#         messages.error(request,'this is not a .csv file')

#     data_set = csv_file.read().decode('utf-8')
#     io_string= io.StringIO(data_set)
#     next(io_string)
#     for column in csv.reader(io_string,delimiter = ',',quotechar='"'):
#         _, created = Excel.objects.update_or_create(
#             id = column[0],
#             name =column[1],
#             date = column[2],
#             time =column[3],
#             shop = column[4],
#             maziwa_kubwa = column[5],
#             maziwa_ndogo = column[6],
#             premimum = column[7],
#             daily_hope =column[8],
#             geocoords = column[9]

#         )
#         context= {}
#     return render(request,template,context)