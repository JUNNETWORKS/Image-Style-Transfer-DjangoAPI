from django.shortcuts import render

# Create your views here.
from django.http.response import HttpResponse

def api(request):
  return HttpResponse('This is a response for request from iOS app and Web app.')

def line(request):
    return HttpResponse('This is a response for request from LINE Messaging API.')