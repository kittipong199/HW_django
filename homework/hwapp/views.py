from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required


# from typing_extensions import Required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from homework.settings import DATABASES
from .models import *


#image
from django.core.files.storage import FileSystemStorage


# Paginator
from django.core.paginator import Paginator

# Create your views here.
def Home(request):
    return render(request, 'sent/home.html')
    


def Contects(request):
    return render(request, 'sent/contect.html')


def Login(request):
    return render(request, 'sent/login.html')


def Register(request):
    return render(request, 'sent/register.html')