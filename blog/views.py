from django.http import HttpResponse
from django.shortcuts import render
from .models import Post
from unidecode import unidecode
from django.db.models import Q

def home(request):
    query = request.GET.get('q')
    if query:
        query = unidecode(query)
        query_parts = query.split()
        q_objects = Q()
        
        for part in query_parts:
            q_objects |= (Q(title__icontains=part) | Q(content__icontains=part))
        
        posts = Post.objects.filter(q_objects)
    else: 
        posts = Post.objects.all()
        
    return render(request, "blog/list.html", {'posts': posts, 'query': query})

def details(request, id):

    #lista todos os posts
    return render(request, "blog/details.html")