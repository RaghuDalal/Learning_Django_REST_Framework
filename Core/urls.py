from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employees/', include('DRF.urls')),
    path('students/', include('serializers.urls')),
    path('cbv/', include('CbvSerializers.urls')),
    path('ns/', include('nestedSerializers.urls')),
]
