from django.shortcuts import render
from dijango.http import HttpResponse


# Create your views here.

def index(requests):
    return HttpResponse("Hello, world. You're at the pools index.")
