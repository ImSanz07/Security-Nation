from django.urls import path
from . import views
from .views import comp_dash

urlpatterns = [
    path("home",views.home,name="home"),
    path("login",views.signin,name="login"),
    path("signup",views.signup,name="signup"),
    path("org_signup",views.org_signup,name="org_signup"),
    path("comp_reg",views.comp_reg,name="comp_reg"),
    path("comp_dash/",comp_dash,name="comp_dash"),
    path('logout/', views.logout_view, name='logout')
]