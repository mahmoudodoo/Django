from django.shortcuts import render
from django.template import context

# Create your views here.

def index(request):
    context = {'greet' : 'Hello World Welcome To Index'}
    return render(request,'basic_app/index.html',context)

def other(request):
    return render(request,'basic_app/other.html')

def relative(request):
    return render(request,'basic_app/relative_url_templates.html')