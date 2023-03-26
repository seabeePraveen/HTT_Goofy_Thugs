from django.contrib import admin

from .models import userdetails,owner_details
# Register your models here.

admin.site.register(userdetails)
admin.site.register(owner_details)