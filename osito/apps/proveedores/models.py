from django.db import models



# Create your models here.
class Proveedore(models.Model):
    nombre = models.CharField(max_length=100)
    apellido= models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    provincia = models.CharField(max_length=100)
    telefono = models.CharField(max_length=12)
    
    
 
    def __str__(self):
        return self.nombre 


