from django.contrib import admin
from blog.models import Post

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (  # Campos a serem exibidos na lista
        "title",
        "author",
        "created_at",
        "updated_at",
    )
    search_fields = ("title", "content")  # Campos para o campo de busca
    list_filter = ("created_at", "author")  # Filtros laterais
