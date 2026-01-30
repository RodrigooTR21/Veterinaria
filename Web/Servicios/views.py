from django.shortcuts import render
# servicios/views.py
from Servicios.models import Servicios as ModeloServicios

# Create your views here.
# La función debe ser en snake_case
def servicios(request): 
    
    # Asigna la consulta a una variable con nombre diferente
    listado_servicios = ModeloServicios.objects.all()

    return render(request, "servicios/servicios.html", {'servicios': listado_servicios})