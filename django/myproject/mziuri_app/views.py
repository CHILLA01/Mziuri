from django.shortcuts import render
from django.http import HttpResponse

def my_name(request):
    return HttpResponse("GIORGI TCHILAIA")

