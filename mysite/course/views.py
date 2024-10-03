from django.shortcuts import render
from django.http import HttpResponse

def new_pro(request):
    return HttpResponse("HI i am an other app")

def index(request):
    return render(request,'course/index.html',{'nm':True})

def wajdan(request):
    return render(request,'course/wajdan.html')
