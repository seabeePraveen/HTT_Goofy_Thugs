from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request,'index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request,'User Doesnot exist')
            return redirect('login')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.error(request,'Credentials doesnot matched')
            return redirect('login')
    return render(request,'login.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 == password2:
            if User.objects.filter(email=email).exists():
                messages.error(request,"email already exists!")
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username,email=email,password=password1)
                user.save()
                login(request,user)
                return redirect('home')
        else:
            messages.error(request,"passwords are not matched!")
            return redirect('signup')
    return render(request,'signup.html')