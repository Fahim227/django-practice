from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import request
from django.http import HttpResponse
import json
@api_view(['get','post'])
def test(request):
    # return HttpResponse(json.dumps({"message": "Hello, world!"}))


    return render(request, 'NotificationTest/lobby.html')
