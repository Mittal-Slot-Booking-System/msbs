from django.urls import path

from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [ 
    path('medical_form', views.medical_certificate, name='upload_cerificate'),  
]  