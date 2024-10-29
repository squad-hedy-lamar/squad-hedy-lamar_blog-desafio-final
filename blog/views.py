from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post
from unidecode import unidecode
from django.db.models import Q
from django_comments.models import Comment

# from .forms import PostForm


def home(request):
    query = request.GET.get("q")
    if query:
        query = unidecode(query)
        query_parts = query.split()
        q_objects = Q()

        for part in query_parts:
            q_objects |= Q(title__icontains=part) | Q(content__icontains=part)

        posts = Post.objects.filter(q_objects)
    else:
        posts = Post.objects.all().order_by("-created_at")

    return render(request, "blog/list.html", {"posts": posts, "query": query})


def details(request, id):
    # Tenta buscar o post pelo ID, ou retorna 404 se não existir
    post = get_object_or_404(Post, id=id)
    comments = Comment.objects.filter(
        object_pk=post.pk, content_type__model="post"
    )  # Filtrar pelos comentários do post
    return render(request, "blog/details.html", {"post": post, "comments": comments})


def criar_post(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        image = request.FILES.get("image")  # Captura a imagem enviada

        post = Post(title=title, content=content, image=image, author=request.user)
        post.save()
        return redirect("blog-home")

    return render(request, "blog/create_post.html")


# def criar_post(request):
#     if request.method == "POST":
#         form = PostForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect(
#                 "blog-home"
#             )
#     else:
#         form = PostForm()
#     return render(request, "blog/create_post.html", {"form": form})
