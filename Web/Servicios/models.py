from django.db import models

# Create your models here.

class Servicios(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='servicios')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    # La clase Meta debe estar indentada DENTRO de Servicios
    class Meta:
        verbose_name = 'servicios'
        verbose_name_plural = 'servicios'

    # El método __str__ debe estar indentado DENTRO de Servicios
    # (También corregí el nombre del método de _str_ a __str__)
    def __str__(self): 
        return self.titulo