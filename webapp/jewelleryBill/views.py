from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html',{'name':'krishna'})

def add(request):
    
    a=request.GET["a"]
    b=request.GET["b"]
    res =a+b+2
    return render(request,'result.html',{'result':res})

def addform(request):
    return render(request, 'add.html',{})


     
    
    
    
    