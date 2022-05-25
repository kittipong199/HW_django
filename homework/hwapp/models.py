

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    usertype = models.CharField(max_length=100,default='member')# ตั้งค่าเริ่มต้นให้เป็น member
    mobile = models.CharField(max_length=15,null=True,blank=True)
    verified = models.BooleanField(default=False)
    verify_token = models.CharField(max_length=100,default='no token')# เอาไว้เก็บ token 

    def _str_(Self):
        return Self.user.username

