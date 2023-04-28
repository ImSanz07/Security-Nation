from django.contrib import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import userm

# Create your views here.
def home(request):
    return render(request, "website/home.html")

def login(request):
    
    if request.method == 'POST':
        usernamel = request.POST['username1']
        passwordl = request.POST['password1']

        if userm.objects.filter(uname=usernamel, passw=passwordl).exists():
            fname = usernamel
            return render(request, "website/userdash.html", {'fname': fname})
            
        else:
            messages.error(request, "Bad Credentials")
            
    
    return render(request, "website/login.html")    
    
  
def signup(request):
    if request.method == 'POST':
        user = userm()
        user.uname = request.POST['username1']
        user.email = request.POST['email1']
        user.passw = request.POST['password1']
        user.save()
        return render(request, "website/login.html")
    
    return render(request, "website/signup.html")
    