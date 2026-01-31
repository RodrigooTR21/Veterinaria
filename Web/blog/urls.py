from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name="Blog"),
    path('categorias/<categorias_id>/', views.categoria, name="categorias"),
]