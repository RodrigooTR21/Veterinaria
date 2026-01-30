from django.conf import settings
from django.shortcuts import redirect, render
from django.core.mail import EmailMessage

from .forms import FormularioContacto


# Create your views here.


def contacto(request):
    formulario_contacto = FormularioContacto

    if request.method == 'POST':
        form = FormularioContacto(data=request.POST)
        if form.is_valid():
            nombre = request.POST.get('nombre')
            email = request.POST.get('email')
            contenido = request.POST.get('contenido')
            asunto =  "Mensaje enviado desde Contacto"
            cuerpo = "El usuario con nombre {} y con la direccion {} escribe lo siguiente:\n\n {}".format(
                    nombre,
                    email,
                    contenido
                )
            email_mensaje = EmailMessage(
                asunto,
                cuerpo,
                settings.DEFAULT_FROM_EMAIL,
                ['tapiar349@gmail.com'],
                reply_to=[email]
            )
            try:
                email_mensaje.send()
                return redirect('/contacto/?valido')
            except Exception as e:
                print("Error al enviar el correo: ", e)
                return redirect('/contacto/?novalido')
        else:
            return render (request, "contacto/contacto.html", {'formulario': form})
            
            
    return render(request, "contacto/contacto.html", {'formulario': formulario_contacto})