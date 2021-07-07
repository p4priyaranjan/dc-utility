from home.views import version
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index,name='home'),
    path("index",views.index,name='home'),
    path("version",views.version,name='version'),
    path("loginuser",views.loginuser,name='login'),
    path("logoutuser",views.logoutuser,name='logout'),

]