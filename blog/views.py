from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #lista todos os posts
    return render(request, "blog/list.html")

def details(request, id):

    #lista todos os posts
    return render(request, "blog/details.html")