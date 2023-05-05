from django.urls import path
from . import views


urlpatterns = [
    path("home",views.home,name="home"),
    path("login",views.signin,name="login"),
    path("aboutus",views.aboutus,name="aboutus"),

    path("signup",views.signup,name="signup"),
    path("org_signup",views.org_signup,name="org_signup"),
    path("comp_reg",views.comp_reg,name="comp_reg"),
    path("comp_dash",views.comp_dash,name="comp_dash"),
    path('userdash',views.userdash,name='userdash'),
    path('userpastorders/<int:cost>',views.userpastorders,name='userpastorders'),
    path('payment_user/<int:cost>',views.userpastorders,name='payment_user'),
    path('search/', views.search, name='search'),
    path('booking/<int:company_id>', views.booking, name='booking'),
    path('accepting_request/<int:request_id>',views.accepting_request,name='accepting_request'),
    path('rejecting_request/<int:request_id>',views.rejecting_request,name='rejecting_request'),
    path('book_done', views.book_done, name='book_done'),
    path('req_accept', views.req_accept, name='req_accept'),
    path('logout/', views.logout_view, name='logout')   
]