from django.db.models.signals import post_save
from django.dispatch import receiver
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm,PasswordChangeForm,AuthenticationForm
from django.contrib.auth import update_session_auth_hash,authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.decorators import login_required
from .forms import CadastroForm, ProfileForm
from blog.models import Post
from unidecode import unidecode
from django.db.models import Q
from django_comments.models import Comment
from .models import Profile
from django.contrib import messages

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
    post = get_object_or_404(Post, id=id)
    comments = Comment.objects.filter(object_pk=post.pk, content_type__model='post')
    return render(request, "blog/details.html", {'post': post, 'comments': comments})

def cadastrar(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            form.save()
            Profile.objects.get_or_create(user=request.user) # cria o perfil 
            return redirect('profile')
        if form.errors.get('username'):
            messages.error(request, form.errors.get('username')[0]) # username is a tuple
        if form.errors.get('email'):    
            messages.error(request, form.errors.get('email')[0]) # email is a tuple 
        if form.errors.get('user already exists'):
            messages.error(request, form.errors.get('user already exists')[0])
            return redirect('login')
    else:
        form = CadastroForm()
    return render(request, 'users/cadastrar.html', {'form': form})

@login_required
def delete_user(request):
    user = request.user
    if request.method == 'POST':
        user.delete()
        messages.success(request, 'Conta deletada com sucesso.')
        return redirect('login')
    return render(request, 'users/delete_user.html')

@login_required
def profile(request):
    profile = get_object_or_404(Profile, user=request.user)
    return render(request, 'users/profile.html', {'profile': profile})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request,username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/profile/')
            else:
                form.add_error(None, 'Usuário ou senha inválidos. Tente novamente.')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

@login_required
def create_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')
    else:
        form = ProfileForm()
    return render(request, 'users/profile.html', {'form': form})

@login_required
def edit_profile(request):
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'users/edit_profile.html', {'form': form})

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

def password_reset(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            form.save(
                request=request,
                use_https=request.is_secure(),
                email_template_name='registration/password_reset_email.html'
            )
            return redirect('password_reset_done')
    else:
        form = PasswordResetForm()
    return render(request, 'users/password_reset.html', {'form': form})

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Atualiza a sessão do usuário para evitar logout
            messages.success(request, 'Sua senha foi alterada com sucesso!')
            return redirect('profile')
        else:
            messages.error(request, 'Por favor, corrija os erros abaixo.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'users/change_password.html', {'form': form})
