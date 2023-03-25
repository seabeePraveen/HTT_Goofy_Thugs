from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from . models import userdetails
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import Settings
# Create your views here.


def index(request):
    return render(request,'index.html')

def loginpage(request):
    if request.user.is_authenticated:
        return redirect('home')
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
            return redirect('home')
        else:
            messages.error(request,'Credentials doesnot matched')
            return redirect('login')
    return render(request,'login.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password1')
        password2 = request.POST.get('password2')
        mobile = request.POST.get('mobile')
        address = request.POST.get('address')
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,"Email id already exists")
                return redirect('signup')
            else:
                user = User.objects.create_user(username = username, email = email, password=password)
                user.save()
                login(request,user)
                detailing = userdetails.objects.create(user=user,mobile=mobile,address=address)
                detailing.save()
                return redirect('loginpage')
        else:
            messages.error(request,"passwords are not matched!")
            return redirect('signup')
    return render(request,'signup.html')

@login_required(login_url='loginpage')
def home(request):
    return render(request,'home.html')

def logoutpage(request):
    logout(request)
    return redirect('index')

def forgot(request):
    email = request.POST.get('email')
    send_mail(
        'Contact Form',
        'otp',
        'settings.EMAIL_HOST_USER',
        '[reciever email]',
        fail_silently=False
    )
    return render(request,'index.html')
