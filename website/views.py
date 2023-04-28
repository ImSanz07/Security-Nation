from django.contrib import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import userm,company,User
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout,authenticate,login


# Create your views here.
def home(request):
    return render(request, "website/home.html")

def signin(request):
    if request.method=='POST':
        #attempt user to sign in
        username=request.POST['username1']
        password=request.POST['password1']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            user1=request.user
            if userm.objects.filter(user=user1).exists():
                fname = username
                return render(request, "website/userdash.html", {'fname': fname})
            elif company.objects.filter(user=user1).exists():
                fname = username
                if check_if_data_exists(user1):

                    return render(request, "website/comp_dash.html", {'fname': fname})
                else:
                    return render(request, "website/comp_reg.html", {'fname': fname})               
        else:
            messages.info(request,'enter a valid username and password')
            return redirect('login')
    else:
        return render(request,'website/login.html')

def check_if_data_exists(user1):
    
    try:
        company_obj = company.objects.get(user=user1)
        if (company_obj.cemail and company_obj.cname and company_obj.ccontact and company_obj.cgstin and company_obj.ccity and company_obj.cstate and company_obj.czip and company_obj.ccost and company_obj.cdis):
            return True
    except company.DoesNotExist:
        pass
    return False

def signup(request):
    if request.method == 'POST':
        username= request.POST['username1']
        email = request.POST['email1']
        password = request.POST['password1']
        user=User.objects.create_user(username=username,email=email,password=password)
        user.save()
        #creating a profile model
        user_model=User.objects.get(username=username)
        new_profile=userm.objects.create(user=user_model,id=user_model.id,email=email)
        new_profile.save()
        return render(request, "website/login.html")
    
    return render(request, "website/signup.html")

def org_signup(request):
    if request.method == 'POST':
        user = company()
        username = request.POST['username1']
        email = request.POST['email1']
        password = request.POST['password1']
        user=User.objects.create_user(username=username,email=email,password=password)
        user.save()
        user_model=User.objects.get(username=username)
        new_company_profile=company.objects.create(user=user_model,id=user_model.id,cemail=email)
        new_company_profile.save()
        return render(request, "website/login.html")

    return render(request, "website/org_signup.html")


def comp_reg(request):
    current_user=company.objects.get(user=request.user)
    if request.method == 'POST':
        current_user.cname=request.POST['name1']
        current_user.ccontact=request.POST['contact1']
        current_user.cgstin=request.POST['gstin1']
        current_user.ccity=request.POST['city1']
        current_user.cstate=request.POST['state1']
        current_user.czip=request.POST['pincode1']
        current_user.ccost=request.POST['cost']
        current_user.cdis=request.POST['description1']
        current_user.save()
        return render(request, "website/comp_dash.html")

    return render(request, "website/comp_reg.html")


def logout_view(request):
    logout(request)
    return render(request,"website/home.html")

def comp_dash(request):
    company_obj = company.objects.get(user=request.user)
    context = {'company_obj': company_obj}
    return render(request, 'comp_dash.html', context)