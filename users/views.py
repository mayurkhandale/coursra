from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Users(request):
    return HttpResponse('<h1>Hi this  is the Users Template</h1>')