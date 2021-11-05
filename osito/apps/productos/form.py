from django import forms
from django.forms import fields
from apps.productos.models import Producto

class ProductoForm(forms.ModelForm): 
    class Meta:   
        model = Producto
        fields = [
            'descripcion',
            'precio',
            'numero_exit'
        ]
        labels = {
            'descripcion': 'Ingrese la descripcion',
            'precio': 'Ingrese el precio',
            'numero_exit': 'Ingrese el numero de existencia'
        }

        widgets = {
            'descripcion': forms.TextInput(attrs={'class': 'form-controls'}),
            'precio': forms.TextInput(attrs={'class': 'form-controls'}),
            'numero_exit': forms.TextInput(attrs={'class': 'form-controls'})
            # tipo de relacion entre cliente y tipo cliente  de uno a muchos
            # 'tipoCliente': forms.Select(attrs={'class': 'form-controls'})

        }