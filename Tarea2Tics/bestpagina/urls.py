from django.urls import path
from .views import *

urlpatterns = [
    path('', blank, name='blank'),
    path('checkout/',checkout,name='checkout')
]