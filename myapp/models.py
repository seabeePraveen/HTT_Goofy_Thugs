from django.db import models
from django.contrib.auth.models import User

class userdetails(models.Model):
    mobile = models.IntegerField(max_length=10)
    address = models.TextField()
    subscription = models.SmallIntegerField(default=0)
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)


    def __str__(self):
        return str(self.user.username)