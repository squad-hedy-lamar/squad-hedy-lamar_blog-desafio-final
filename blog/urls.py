from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="blog-home"),
    path("post/<int:id>/", views.details, name="post-detail"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="users/login.html"),
        name="login",
    ),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    # path("comments/", include("django_comments.urls")),
    path("criar_post/", views.criar_post, name="criar_post"),
]
