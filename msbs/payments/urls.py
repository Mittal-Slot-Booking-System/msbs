from django.urls import path
from .views import pay,callback

urlpatterns = [
    path('pay/', pay, name='pay'),
    path('callback/', callback, name='callback'),
]

