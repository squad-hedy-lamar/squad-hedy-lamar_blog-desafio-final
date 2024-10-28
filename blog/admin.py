from django.contrib import admin
from django.utils.html import format_html
from blog.models import Post
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (  # Campos a serem exibidos na lista
        "title",
        "author",
        "created_at",
        "updated_at",
        "image",
    )
    search_fields = ("title", "content")  # Campos para o campo de busca
    list_filter = ("created_at", "author")  # Filtros laterais


def image_preview(self, obj):
    if obj.image:
        return format_html(
            '<img src="{}" style="width: 10px; height: auto;" />',
            obj.image.url,
        )
    return "Sem imagem"


image_preview.short_description = "Pré-visualização"

