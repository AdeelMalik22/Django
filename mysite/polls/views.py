from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# def function(request):
#     return HttpResponse("HI there")

# def add_new(request):
#     return HttpResponse("HEY HOW'S DOING")

# Create your views here.
