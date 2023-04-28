from django.contrib import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, "website/home.html")

def login(request):
    return render(request, "website/login.html")

def signup(request):
    return render(request, "website/signup.html")