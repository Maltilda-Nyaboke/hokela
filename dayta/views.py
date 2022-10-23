from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Excel
from.serializer import ExcelSerializer


# Create your views here.

# Create your views here.
def welcome(request):
    return render(request,'index.html')
