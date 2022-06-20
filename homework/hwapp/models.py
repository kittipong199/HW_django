

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    usertype = models.CharField(max_length=100,default='member')# ตั้งค่าเริ่มต้นให้เป็น member
    mobile = models.CharField(max_length=15,null=True,blank=True)
    verified = models.BooleanField(default=False)
    verify_token = models.CharField(max_length=100,default='no token')# เอาไว้เก็บ token 

    def __str__(self):
        return self.user.username

class ContectList(models.Model):# ถ้าอยากให้ มีfurrndtion นี้ ในห้า adminให้ไปเพิ่ม furndtion ที่ หา้ admin.py ด้วย
    title = models.CharField(max_length=200) # max_length=200 คือกำหนดค่าตัวอักษรได้มากสุด กี่ตัวอักษร
    email = models.CharField(max_length=200)
    detail = models.TextField(null=True, blank=True)# null=True, blank=True คือไม่ต้องใส่ค่าก็ได้
    complete = models.BooleanField(default=False)#

    def __str__(self):
        return self.title  # คือการแสดงรายละเอียดในหลังบ้าน


class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    cost = models.DecimalField(max_digits=10,decimal_places=2,null=True , blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    
    #file
    picture = models.ImageField(upload_to='product',null=True,blank=True)
    specfile = models.FileField(upload_to='specfile',null=True,blank=True)
    
    
    def __str__(self):
        return self.title