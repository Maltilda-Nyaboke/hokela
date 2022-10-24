import datetime
from django.db import models

# Create your models here.
# datetime.time
# d = datetime.time (10:33:45)
class Excel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length =75)
    date = models.DateField()
    time =models.TimeField()
    shop = models.CharField(max_length =255)
    maziwa_kubwa = models.IntegerField()
    maziwa_ndogo = models.IntegerField()
    premimum = models.IntegerField()
    daily_hope = models.IntegerField()
    geocoords = models.BigIntegerField(null=True)

    
    @property
    def sales_agents(self):
        return Excel.objects.all().aggregate(filter=('name'))
        

    @classmethod
    def search_by_name(cls, search_term):
        sale = cls.objects.filter(name__icontains=search_term)
        return sale          

    def __str__(self):
        return self.name
