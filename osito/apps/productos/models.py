from django.db import models
from apps.clientes.models import Cliente
# Create your models here.
class Producto(models.Model):
    descripcion = models.CharField(max_length=40)
    precio = models.IntegerField()
    numero_exit = models.IntegerField()
    cliente = models.ManyToManyField(Cliente, through='Compras')
    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

class Compras(models.Model):
    Cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name="Cliente")
    Producto = models.ForeignKey(Producto, on_delete=models.CASCADE, verbose_name="Producto")
    fecha_compra = models.DateField()