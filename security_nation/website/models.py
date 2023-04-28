from django.db import models

# Create your models here.
class userm(models.Model):
    id = models.AutoField(primary_key=True)
    uname = models.CharField(max_length=30 , null=True)
    email = models.CharField(max_length=30 , null=True)
    passw = models.CharField(max_length=30 , null=True)

    