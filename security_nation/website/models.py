from django.db import models

# Create your models here.
class userm(models.Model):
    id = models.AutoField(primary_key=True)
    uname = models.CharField(max_length=30 , null=True)
    email = models.CharField(max_length=30 , null=True)
    passw = models.CharField(max_length=30 , null=True)
    
class company(models.Model):
    id = models.AutoField(primary_key=True)
    uname = models.CharField(max_length=30 , null=True)
    cemail = models.CharField(max_length=30 , null=True)
    cpassw = models.CharField(max_length=30 , null=True)
    cname = models.CharField(max_length=30 , null=True)
    ccity = models.CharField(max_length=30 , null=True)
    cstate = models.CharField(max_length=30 , null=True)
    czip = models.CharField(max_length=30 , null=True)
    ccost = models.CharField(max_length=30 , null=True)
    cdis = models.CharField(max_length=300 , null=True)
    cimage = models.ImageField(null=True, blank=True, upload_to="images/")
    