from datetime import date
from django.db import models

# Create your models here.

class Excel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length =75)
    date = models.DateTimeField()
    time =models.TimeField()
    shop = models.CharField(max_length =255)
    maziwa_kubwa = models.IntegerField()
    maziwa_ndogo = models.IntegerField()
    premimum = models.IntegerField()
    daily_hope = models.IntegerField()
    geocoords = models.IntegerField(null=True)

    def __str__(self):
        return self.name