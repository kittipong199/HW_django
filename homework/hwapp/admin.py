from django.contrib import admin

from .models import *
# Register your models here.
# เป็นการทำให้แอดมินสามารถเห็นฐานข้อมูล เวลาสร้าง models ใหม่ ให้มา register ในนี้ด้วยทุกครั้ง
admin.site.register(Profile)
