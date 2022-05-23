from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.
def Home(request):
    return render(request, 'sent/home.html')
    


def Contects(request):
    return render(request, 'sent/contect.html')


def Login(request):
    return render(request, 'sent/login.html')


def Register(request):
    return render(request, 'sent/register.html')