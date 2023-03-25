from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.models import User,auth
from . models import userdetails
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from project.settings import RAZORPAY_API_KEY,RAZORPAY_API_SECRET_KEY
from random import randint
from django.conf import settings
import razorpay,stripe
from django.views.decorators.csrf import csrf_exempt
client = razorpay.Client(auth=(RAZORPAY_API_KEY,RAZORPAY_API_SECRET_KEY))
# Create your views here.
stripe.api_key = settings.STRIPE_SECRET_KEY

def index(request):
    return render(request,'index.html')

def loginpage(request):
    if request.user.is_authenticated:
        return redirect('index')
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
            return redirect('index')
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

@login_required(login_url='loginpage')
def subscribe(request):
    if request.method == 'POST':
        if type == '1' or type == 1:
            amount = 2000
        else:
            amount = 7000
        order_currency = 'INR'
        context = {
            'amount':amount
        }
        return render(request,'confirmpay.html',context)
    #     payment_order = client.order.create(
    #         {'amount':amount,'currency':order_currency,'payment_capture':'1'})
    #     payment_order_id = randint(0,99999)
    #     context = {
    #         'amount':amount,'api_key':RAZORPAY_API_KEY,
    #         'order_id':payment_order_id,
    #         'type':type
    #     }
    #     return render(request,'confirmpay.html',context)

from django.views.generic.base import TemplateView
@login_required(login_url='loginpage')
class confirmpay(TemplateView):
    template_name = 'confirmpage.html'

    def get_content_data(self,**kwargs):
        context = super().get_content_data(**kwargs)
        context['key']=settings.STRIPE_PUBLISHABLE_KEY
        return context

@login_required(login_url='loginpage')
def success(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        charge = stripe.Charge.create(amount=amount,currency='usd',description='Django charge',source = request.POST['stripeToken'])
        return render(request,'success.html')
