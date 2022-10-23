from datetime import date
from django.db import models

# Create your models here.

class excel(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField()
    time =models.TimeField()
    name = models.CharField(max_length =75)
    shop = models.CharField(max_length =255)
    maziwa_kubwa = models.IntegerField()
    maziwa_ndogo = models.IntegerField()
    premimum = models.IntegerField()
    daily_hope = models.IntegerField()
    geocoords = models.IntegerField(null=True)