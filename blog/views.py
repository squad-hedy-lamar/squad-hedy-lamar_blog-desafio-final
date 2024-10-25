from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from blog.models import Post


def home(request):
    # Lista todos os posts
    # posts = Post.objects.all()
    posts = Post.objects.all().order_by("-created_at")
    return render(
        request, "blog/list.html", {"posts": posts}
    )  # Enviar os posts para o template


def details(request, id):
    # Tenta buscar o post pelo ID, ou retorna 404 se não existir
    post = get_object_or_404(Post, id=id)
    return render(
        request, "blog/details.html", {"post": post}
    )  # Enviar o post específico para o template
