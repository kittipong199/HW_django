from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required
from typing import Text
import uuid

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
    allproduct = Product.objects.all()

    product_per_page = 3
    paginator = Paginator(allproduct, product_per_page)
    page = request.GET.get('page') # locahost 
    allproduct = paginator.get_page(page)
    print("coun: " ,len(allproduct))
    context = {'allproduct':allproduct}

    #แยกแถวละ 3 คอลัม
    allrow = []
    row = []

    for i,p in enumerate(allproduct):
        if i % 3 ==0:
            if i != 0:
                allrow.append(row)
            row = []
            row.append(p)
        else:
            row.append(p)
    allrow.append(row)
    context['allrow'] = allrow
    return render(request, 'sent/home.html',context)
    


def Contects(request):

    context = {} # คือส่งที่จะแนบไป

    if request.method == 'POST':
        data = request.POST.copy()
        title = data.get('title')
        email = data.get('email')
        detail = data.get('detail')
        print(title)
        print(email)
        print(detail)
        print("---------------------")

        if title == ''and  email == '':
            context['message'] = 'กรุณากรอกข้อมูล หัวข้อและ อีเมล เพราะเราไม่สามารถส่งคำตอบให้คุณได้'
            return render(request, 'company/contact.html',context)
        #เมื่อได้ข้อมูลแล้ว จะทำการบันทึกข้อมูล
        newrecord = ContectList()
        newrecord.title=title
        newrecord.email=email
        newrecord.detail=detail
        newrecord.save()
        context['message'] = 'เราได้รับข้อความของคุณแล้ว'
    return render(request, 'sent/contect.html',context)


def Login(request):

    context = {}  # สิ่งที่จะแนบไป if request.method == 'POST':
    
    if request.method == 'POST':
        data = request.POST.copy()
        username = data.get('username')
        password = data.get('password')

        try: 
            user = authenticate(username = username, password=password)
            login(request,user)
            return redirect('home-page')
        except:
            context['message'] = 'username or password ไม่ถูกต้อง'
    return render(request, 'sent/login.html',context)


def Register(request):

    context = {}
    if request.method == "POST":
        data = request.POST.copy()
        yourname = data.get('yourname')
        emails = data.get('email')
        mobile = data.get('mobile')
        password1 = data.get('password1')
        password2 = data.get('password2')

        try:
            check = User.objects.get(username=emails)
            context['yourname'] = yourname  # เก็บค่า เดิม ไว้ จะได้ไม่ต้องกรอกใหม่ 
            return render(request, 'sent/home.html',context)
        except:
            if password1 != password2:
                context['warning'] = ' กรุณากรอก password ให้ตรงกัน'
                return render(request, 'sent/register.html',context)

            newuser = User()
            newuser.username = emails
            newuser.email = emails
            newuser.first_name = yourname
            newuser.set_password(password1)
            newuser.save()

            u = uuid.uuid1()
            token = str(u) #random uuid


            newprofile = Profile()
            newprofile.user = User.objects.get(username=emails)
            newprofile.mobile = mobile
            newprofile.verify_token = token
            newprofile.save()

    return render(request, 'sent/register.html', context)

# Addproduct
def Addproduct(request):
    
    if request.method == 'POST':
        data = request.POST.copy()
        title = data.get('title')
        description = data.get('description')
        cost = data.get('price')
        quantity = data.get('quantity')
        
        print(title)
        print(description)
        print(cost)
        print(quantity)
        

        print('file',request.FILES)#  คำสั่งปริ้นไฟล์ ว่ามีไฟล์หรือไหม

        new = Product()
        new.title = title
        new.description = description
        new.cost = float(cost)
        new.quantity = quantity
        

        if 'picture' in request.FILES:
            file_image = request.FILES['picture']
            file_image_name = file_image.name.replace(' ','')
            fs = FileSystemStorage(location='media/product')
            filename = fs.save(file_image_name, file_image)
            upload_file_url = fs.url(filename)
            print('Picture url:', upload_file_url)
            new.picture = '/product' + upload_file_url[6:]

        if 'specfile' in request.FILES:
            file_image = request.FILES['specfile']
            file_image_name = file_image.name.replace(' ','')
            fs = FileSystemStorage(location='media/specfile')
            filename = fs.save(file_image_name, file_image)
            upload_file_url = fs.url(filename)
            print('Specfile url:', upload_file_url)
            new.specfile = '/specfile' + upload_file_url[6:]

        new.save()

    return render(request, 'sent/addproduct.html')