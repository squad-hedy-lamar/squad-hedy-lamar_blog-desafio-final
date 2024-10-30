from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import home, cadastrar, profile, create_profile, edit_profile, delete_user, password_reset,change_password, user_login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='blog-home'),
    path('post/<int:id>/', views.details, name='post-detail'),
    path('login/',user_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('comments/', include('django_comments.urls')),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('profile/', views.profile, name='profile'),
    path('create_profile/', views.create_profile, name='create_profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('delete_user/',delete_user, name='delete_user'),
    path('password_reset/', password_reset, name='password_reset'),
    path('change_password/', change_password, name='change_password')
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)