from django.urls import path
from .views import *

urlpatterns = [
    path('', Home, name="home-page"),
    path('contect/', Contects, name="contect-page"),
    
    path('register/', Register, name="register-page"),
]
