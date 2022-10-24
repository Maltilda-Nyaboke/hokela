from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Excel

# Register your models here.
admin.site.register(Excel)

@admin.register(Excel)
class ExcelAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'date', 'time', 'shop','maziwa_kubwa','maziwa_ndogo','premimum','daily_hope','geocoords')