from django import forms
from django.forms import fields, widgets
from apps.proveedores.models import Proveedore

class ProveedorForm(forms.ModelForm):
    class Meta: 
        model = Proveedore

        fields = [
          'nombre',
          'apellido',
          'direccion',
          'provincia',
          'telefono',
          'producto',
          'cantidad'

        ]

        labels= {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'direccion': 'Direccion',
            'provincia': 'Provincia',
            'telefono': 'Telefono',
            'producto': 'Seleccione producto',
            'cantidad': 'Cantidad'
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'provincia': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'producto': forms.Select(attrs={'class': 'form-control'}),
            'cantidad': forms.TextInput(attrs={'class': 'form-control'}),
        }