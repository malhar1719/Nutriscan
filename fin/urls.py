# fin/urls.py
from django.contrib import admin
from django.urls import path, include
from myapp import views  # Import views from your app

urlpatterns = [
    path('', views.scan_image, name='scan_image'),  # Map root URL to scan_image view
    path('myapp/', include('myapp.urls')),
    path('admin/', admin.site.urls),
]
