from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export.admin import ExportActionMixin
from .models import Excel

# Register your models here.
admin.site.register(Excel)

@admin.register(Excel)
class ExcelAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'date', 'time', 'shop','maziwa_kubwa','maziwa_ndogo','premimum','daily_hope','geocoords')
    actions = [*ExportActionMixin.export_admin_action]

# class SiteEntityAdmin(ExportActionMixin):
#     readonly_fields=('created_at', 'updated_at', 'created_by', 'updated_by', 'identifier')

