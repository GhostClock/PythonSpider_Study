# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("Rango says Hello world!!!!<br> <a href='/rango/about'>About</a>")
    context_dict = {'boldmessage': 'I am bold font from the context'}
    return render(request, 'rango/index.html', context_dict)

def about(request):
    # return HttpResponse("Rango says here is the about page !!!!<br> <a href='/rango/'>Index</a>")

    data = {'data': u"[这是一个关于页面]"}
    return render(request, 'rango/about.html', data) #用render返回模板
