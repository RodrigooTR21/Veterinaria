from django.contrib import admin
from .models import categorias, Post
# Register your models here.

class categoriaAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')

admin.site.register(categorias, categoriaAdmin)
admin.site.register(Post, PostAdmin)
