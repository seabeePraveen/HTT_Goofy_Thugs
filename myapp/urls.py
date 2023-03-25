from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('login',views.loginpage,name='loginpage'),
    path('signup',views.signup,name='signup'),
    path('home',views.home,name='home'),
    path('logoutpage',views.logoutpage,name='logoutpage'),
    path('forgot',views.forgot,name='forgot'),
    path('subscribe',views.subscribe,name='subscribe'),
    path('charges',views.charges,name='charges'),
    path('success/<str:args>/',views.successmsg,name='successmsg')
]