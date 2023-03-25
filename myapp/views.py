from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.models import User,auth
from . models import userdetails
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import Settings
from random import randint
from django.conf import settings
import stripe
from django.urls import reverse

stripe.api_key
stripe.api_key = "sk_test_51MpXZ8SJajCx9dubySNTtw5trymGETmPK47MbNGokGog6LfsGO0mWASC2NMr0xWIUE4aSoW6zQodbLNIRuQaY4gk009ph1d8vd"
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
            return redirect('loginpage')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'Credentials doesnot matched')
            return redirect('loginpage')
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
    otp = randint(0000,9999)
    send_mail(
        'Contact Form',
        'Your OTP to reset password for Simple Salad '+str(otp),
        'settings.EMAIL_HOST_USER',
        [email],
        fail_silently=False
    )
    return render(request,'index.html')

def menu(request):
    return render(request,'menu.html')

def subscribe(request):
    if request.method == 'POST':
        if type == '1':
            amount = 2000
        elif type == '2':
            amount = 7000
        
def charges(request):
    if request.method == 'POST':
        if type == '1':
            amount = 2000
        elif type == '2':
            amount = 7000
        return redirect(reverse('success',args=[amount]))
    return render(request,'charges.html')

def successmsg(request):
    pass
