from django.contrib import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from .models import userm,company,User,BookingRequest,Requests
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout,authenticate,login
from django.db.models import Q
from django.template.response import TemplateResponse
import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt




# Create your views here.
def home(request):
    return render(request, "website/home.html")
def aboutus(request):
    return render(request,"website/aboutus.html")
def req_accept(request):
    return render(request,"website/req_accept.html")


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
                return redirect('userdash')
            elif company.objects.filter(user=user1).exists():
                fname = username
                if check_if_data_exists(user1):
                    return redirect('comp_dash')
                    # return render(request, "website/comp_dash.html", {'fname': fname})
                else:
                    # return redirect('comp_reg')
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
        new_booking_request=BookingRequest.objects.create(company=new_company_profile)
        new_booking_request.save()
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

def comp_dash(request):
    company_obj = company.objects.get(user=request.user)
    request_of_bookings = BookingRequest.objects.get(company=company_obj)
    request_list_final=request_of_bookings.request_list.all()
    

    return render(request, 'website/comp_dash.html', {'company_obj': company_obj,'request_key':request_list_final})

def userdash(request):
    companies=company.objects.all()
    return render(request,'website/userdash.html',{'companies':companies})

def logout_view(request):
    logout(request)
    return render(request,"website/home.html")


def search(request):
    query = request.GET.get('q')
    results = company.objects.filter(Q(cname__icontains=query))
    print(results)
    return render(request, 'website/userdash.html', {'companies': results})

def booking(request,company_id):
    username = userm.objects.get(user=request.user)
    comp_name = company.objects.get(id=company_id)
    user_request = Requests.objects.create(user=username,company_name=comp_name.cname,cost=comp_name.ccost)

    current_booking_request = BookingRequest.objects.get(company=company_id)
    current_booking_request.request_list.add(user_request)
    return render(request,"website/book_done.html")
@csrf_exempt
def accepting_request(request,request_id):
    request_object=Requests.objects.get(request_id=request_id)
    request_object.is_accepted=True
    request_object.save()
    return render(request,'website/req_accept.html')

def rejecting_request(request,request_id):
    request_object=Requests.objects.get(request_id=request_id)
    request_object.delete()
    return render(request,'website/comp_dash.html')
@csrf_exempt
def book_done(request):
     if request.method=='POST':
        print("lala")
        return render(request,'website/book_done.html')

# authorize razorpay client with API Keys.
razorpay_client = razorpay.Client(auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))

@csrf_exempt
def userpastorders(request,cost):
    current_user=userm.objects.get(user=request.user)
    current_user_request=Requests.objects.filter(user=current_user)
    
    if cost!=0 :
        currency = 'INR'
        amount = cost*100
        print(amount)

        # Create a Razorpay Order
        razorpay_order = razorpay_client.order.create(dict(amount=amount,currency=currency,payment_capture='0'))

        # order id of newly created order.
        razorpay_order_id = razorpay_order['id']
        callback_url = 'book_done'

        # we need to pass these details to frontend.
        context = {}
        context['razorpay_order_id'] = razorpay_order_id
        context['razorpay_merchant_key'] = settings.RAZOR_KEY_ID
        context['razorpay_amount'] = amount
        context['currency'] = currency
        context['callback_url'] = callback_url
        context['current_user_key'] = current_user_request
        return render(request,'website/userpastorders.html',context=context)
    else:
        return render(request,'website/userpastorders.html',{'current_user_key':current_user_request})
#RAZORPAY STUFF


# we need to csrf_exempt this url as
# POST request will be made by Razorpay
# and it won't have the csrf token.



         