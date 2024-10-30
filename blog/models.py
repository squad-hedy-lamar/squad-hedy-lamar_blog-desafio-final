from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.conf import settings
from django.forms import ModelForm

class CustomUser(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        related_name="customuser_groups",  # Define um related_name personalizado
        blank=True,
        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
        verbose_name="groups",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="customuser_permissions",  # Define um related_name personalizado
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )

# Create your models here.
class Post(models.Model):
    image = models.ImageField(
        upload_to="post_images/", blank=True, null=True
    )  # Novo campo de imagem
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

class Comment(models.Model):
  post = models.ForeignKey(Post, on_delete=models.CASCADE)
  content = models.TextField()
  author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='likes', blank=True)
  def __str__(self):
    return f'{self.author} - {self.content}'

class Profile(models.Model):
  user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  bio = models.TextField()
  profile_pic = models.ImageField(upload_to="profile_pics/", null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  def __str__(self):
    return self.user.username

  
class Cadastrar(models.Model):
  username = models.CharField(max_length=100)
  email = models.EmailField()
  password1 = models.CharField(max_length=100)
  password2 = models.CharField(max_length=100)

class PasswordReset(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  token = models.CharField(max_length=100)
  created_at = models.DateTimeField(auto_now_add=True)

