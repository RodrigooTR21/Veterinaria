from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "WebApp/home.html")

def tienda(request):
    return render(request, "WebApp/tienda.html")

def galeria(request):
    return render(request, "WebApp/galeria.html")

