from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import request
from django.http import HttpResponse
from .tasks import notify_customer
import json

# return render(request, 'NotificationTest/lobby.html')

@api_view(['get','post'])
def test(request):
   
    print("testing ===================>>>>>>>>> ")
    result = notify_customer.delay()
    # print(result.get())
    return HttpResponse(json.dumps({"message": "Hello, world!"}))
    
