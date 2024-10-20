from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('post/<int:id>/', views.details, name='post-detail'),
]