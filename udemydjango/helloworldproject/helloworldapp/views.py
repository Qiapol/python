from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def hellofunction(request):
    return HttpResponse('hello')