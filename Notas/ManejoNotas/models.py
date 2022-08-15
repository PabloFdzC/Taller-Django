from django.db import models
# Se importa el usuario ya que lo necesitamos para la llave foranea
from Usuarios.models import Usuario 

class Nota(models.Model):
    # Al crear el modelo se le pone automáticamente un id
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nombre = models.CharField(max_length = 20)
    texto = models.TextField()

    def __str__(self):
        return self.nombre