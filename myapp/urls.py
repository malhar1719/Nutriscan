# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.scan_image, name='scan_image'),
]
