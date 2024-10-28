from django.db import models
from django.contrib.auth.models import User
from.models import User

# Create your models here.
class Post(models.Model):
    image = models.ImageField(
        upload_to="post_images/", blank=True, null=True
    )  # Novo campo de imagem
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
  post = models.ForeignKey(Post, on_delete=models.CASCADE)
  content = models.TextField()
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  bio = models.TextField()
  profile_pic = models.ImageField(null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

class Cadastrar(models.Model):
  username = models.CharField(max_length=100)
  email = models.EmailField()
  password1 = models.CharField(max_length=100)
  password2 = models.CharField(max_length=100)

def create_profiles_for_existing_users():
    for user in User.objects.all():
        Profile.objects.get_or_create(user=user)
class PasswordReset(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  token = models.CharField(max_length=100)
  created_at = models.DateTimeField(auto_now_add=True)

