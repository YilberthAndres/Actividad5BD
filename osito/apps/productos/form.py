from django import forms
from django.forms import fields
from apps.productos.models import Producto
from django.forms import fields
class ProductoForm(forms.ModelForm): 
    class Meta:   
        model = Producto
        fields = [
            'descripcion',
            'precio',
            'numero_exit',
            'cliente',
            'fecha'
        ]
        labels = {
            'descripcion': 'Ingrese la descripcion',
            'precio': 'Ingrese el precio',
            'numero_exit': 'Ingrese el numero de existencia',
            'cliente': 'Seleccione el Cliente',
            'fecha': 'Digite la fecha'
        }

        widgets = {
            'descripcion': forms.TextInput(attrs={'class': 'form-controls'}),
            'precio': forms.TextInput(attrs={'class': 'form-controls'}),
            'numero_exit': forms.TextInput(attrs={'class': 'form-controls'}),
            'cliente': forms.Select(attrs={'class': 'form-controls'}),
            'fecha': forms.TextInput(attrs={'class': 'form-controls'}),

        }