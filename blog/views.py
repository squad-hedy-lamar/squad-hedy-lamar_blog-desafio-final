from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Post

def home(request):
    post = Post.objects.all()
    return render(request, "blog/list.html")

def details(request, id):
    post  = get_object_or_404(Post, id=id)
    return render(request, "blog/details.html", {'post': post})

