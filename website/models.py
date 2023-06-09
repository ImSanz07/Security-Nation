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
    ccost=models.IntegerField(null=True)
    cdis = models.CharField(max_length=300 , null=True)
    cimage = models.ImageField(null=True, blank=True, upload_to="images/")
    comp=models.BooleanField(default= True,null=True)
    

class BookingRequest(models.Model):
    company = models.ForeignKey(company, on_delete=models.CASCADE)
    request_list = models.ManyToManyField('Requests',blank=True,related_name='request')
    

class Requests(models.Model):
    user = models.ForeignKey(userm,on_delete=models.CASCADE,null=True)
    company_name=models.CharField(max_length=300 , null=True)
    request_id = models.AutoField(primary_key=True)
    is_accepted = models.BooleanField(default=False)
    payment_completed = models.BooleanField(default=False)
    cost=models.IntegerField(null=True)
