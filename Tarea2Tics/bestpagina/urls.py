from django.urls import path
from .views import *

urlpatterns = [
    path('', productos, name='productos'),
    path('agregar/',agregar,name='agregar'),
    path('signup/',signup,name='signup'),
    path('contact/',contact,name='contact'),
    path('enviado/',enviado,name='enviado'),
path('ficha/',ficha,name='ficha'),
]