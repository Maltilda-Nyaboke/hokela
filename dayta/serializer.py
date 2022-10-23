from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Excel

class ExcelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Excel
        fields = ('id', 'name', 'date', 'time', 'shop','maziwa_kubwa','maziwa_ndogo','premimum','daily_hope','geocoords')