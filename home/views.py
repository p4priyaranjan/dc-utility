from django.contrib.auth import models
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
from home.models import TotalEntry
from datetime import datetime

# Create your views here.

def index(request):
    if request.user.is_anonymous:
        return redirect('/loginuser')

    tot_entry=TotalEntry.objects.all()
    context={
        'total_entry':tot_entry,
        'time':datetime.now()
    }
    return render(request,'index.htm',context)

def loginuser(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pwd=request.POST.get('passwd')
        user=authenticate(username=username,password=pwd)
        print(user)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            return render(request,'login.htm')
    else:
        return render(request,'login.htm')

def logoutuser(request):
    logout(request)
    return render(request,'login.htm')
