from django.contrib import admin
from .models import userm,company,BookingRequest,Requests


# Register your models here.

admin.site.register(userm)
admin.site.register(company)
admin.site.register(BookingRequest)
admin.site.register(Requests)


