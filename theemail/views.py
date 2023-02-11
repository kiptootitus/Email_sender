from django.shortcuts import render
from django.http import HttpResponse

def members(request):
    return HttpResponse("Welcome to My Email sender website!")