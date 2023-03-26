from django.db import models
from django.contrib.auth.models import User

class userdetails(models.Model):
    mobile = models.CharField(max_length=10,null=False,blank=False)
    address = models.TextField()
    subscription = models.SmallIntegerField(default=0)
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    pincode = models.CharField(max_length=6,null=False,blank=False,default=0)

    def __str__(self):
        return str(self.user.username)
    
# monthly weekly start date, end date

class owner_details(models.Model):
    username = models.CharField(max_length=20,null=False,blank=False)
    email = models.EmailField(null=False,blank=False)
    password = models.CharField(max_length=50,null=False,blank=False)

    def __str__(self):
        return str(self.username)