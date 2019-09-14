from django.urls import path
from .views import *

urlpatterns = [
    path('', blank, name='blank'),
    path('checkout/',checkout,name='checkout'),
    path('signup/',signup,name='signup'),
    path('contact/',contact,name='contact'),
    path('enviado/',enviado,name='enviado'),
]