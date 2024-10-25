from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from blog.models import Post
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
        posts = Post.objects.all().order_by("-created_at")
        
    return render(request, "blog/list.html", {'posts': posts, 'query': query})

def details(request, id):
    # Tenta buscar o post pelo ID, ou retorna 404 se não existir
    post = get_object_or_404(Post, id=id)
    return render(
        request, "blog/details.html", {"post": post}
    )  # Enviar o post específico para o template
