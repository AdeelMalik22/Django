from django.shortcuts import render
import datetime
from django.http import HttpResponse


def index(request):
    return render(request,'polls/index.html',{'pt':56.444,'py':569.33})

def function(request):
    return HttpResponse("HI there d")

# def add_new(request):
#     return HttpResponse("HEY HOW'S DOING")

# Create your views here.
