from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Most Welcome !!!!!!")

def first_app(request):
    dic = {'greats' : 'Hello Mahmoud !!!!!!!'}
    return render(request,'first_app/index.html',dic)