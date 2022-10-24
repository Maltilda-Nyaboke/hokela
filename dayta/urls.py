from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('',views.excel_upload, name='excel_upload'),
    path('register/',views.register,name ='register'),
    # path('login/',views.login,name ='login'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)