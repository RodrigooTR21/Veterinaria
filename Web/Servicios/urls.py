from django.urls import path
from . import views # Correcto, ya que views.py está en el mismo directorio.

# Importaciones de configuración y archivos estáticos/media
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # Ruta principal que llama a la función servicios (en minúsculas)
    path('', views.servicios, name="Servicios"),
]


# 🚨 CORRECCIÓN: SOLO añadir las rutas de MEDIA si DEBUG es True 🚨
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)