from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('login',views.loginpage,name='loginpage'),
    path('signup',views.signup,name='signup'),
    path('home',views.home,name='home'),
    path('logoutpage',views.logoutpage,name='logoutpage')
]