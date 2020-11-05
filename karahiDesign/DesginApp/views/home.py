from django.views import View
from django.shortcuts import render , redirect
from django.http import HttpResponse


def home(request):
    return  render(request, "index.html")

def contact(request):
    return  render(request, "contact.html")
