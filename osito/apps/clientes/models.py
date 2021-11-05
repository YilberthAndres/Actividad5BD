from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre    = models.CharField(max_length=100, verbose_name="Nombre")
    apellidos = models.CharField(max_length=100, verbose_name="Apellido")
    direccion = models.CharField(max_length=100, verbose_name="Direccion")
    telefono  = models.CharField(max_length=100, verbose_name="Telefono")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Cliente"
        verbose_name = "Clientes"