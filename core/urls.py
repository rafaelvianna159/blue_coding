from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('short/', include('shortner.urls')),
    path('admin/', admin.site.urls),
]
