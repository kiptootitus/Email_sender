from django.shortcuts import render
from django.http import HttpResponse

def members(request):
  template = loader.get_template('home.html')
  return HttpResponse(template.render())
