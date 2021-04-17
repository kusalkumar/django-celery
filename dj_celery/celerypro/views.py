from django.shortcuts import render
from django.http import JsonResponse

from celerypro.tasks import *

# Create your views here.

def celerytest(request):
    data ={
            "success": True,
            "message": "let's see"
            }
    sleep_well.delay(100)
    return JsonResponse(data)
