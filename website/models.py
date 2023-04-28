from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class userm(models.Model):  
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=30 , null=True)
    comp=models.BooleanField(default= False,null=True)
    def __str__(self):
        return self.user.username
    
class company(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    id = models.AutoField(primary_key=True)
    cemail = models.CharField(max_length=30 , null=True)
    cname = models.CharField(max_length=30 , null=True)
    ccontact = models.CharField(max_length=30 , null=True)
    cgstin = models.CharField(max_length=30 , null=True)
    ccity = models.CharField(max_length=30 , null=True)
    cstate = models.CharField(max_length=30 , null=True)
    czip = models.CharField(max_length=30 , null=True)
    ccost = models.CharField(max_length=30 , null=True)
    cdis = models.CharField(max_length=300 , null=True)
    cimage = models.ImageField(null=True, blank=True, upload_to="images/")
    comp=models.BooleanField(default= True,null=True)
    