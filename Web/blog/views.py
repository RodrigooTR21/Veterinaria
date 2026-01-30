from django.shortcuts import render
from blog.models import Post, categorias

# Create your views here.

def blog(request):
    posts = Post.objects.all()
    categorias_qs = categorias.objects.all()
    return render(request, "blog/blog.html", {"posts": posts, "categorias": categorias_qs})

def categoria(request, categorias_id):
    categoria = categorias.objects.get(id=categorias_id)
    posts= Post.objects.filter(categorias=categoria)
    categorias_qs = categorias.objects.all()
    return render(request, "blog/categorias.html", {"categoria": categoria, "posts": posts, "categorias": categorias_qs})
