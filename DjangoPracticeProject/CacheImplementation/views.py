from django.shortcuts import render
from .tasks import notify_customer
from rest_framework import request
# Create your views here.

def say_hello(request):
    print("say_hello")
    notify_customer.delay('This Is Message')

    return render(request,'CacheImplementation/mssg.html',{'test':'Main task is running background'})