from django.urls import path
from . import views

urlpatterns = [
    path("home",views.home,name="home"),
    path("login",views.login,name="login"),
    path("signup",views.signup,name="signup"),
    path("org_signup",views.org_signup,name="org_signup")
]