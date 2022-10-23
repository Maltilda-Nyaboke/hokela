from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.excel_upload, name='excel_upload'),
]