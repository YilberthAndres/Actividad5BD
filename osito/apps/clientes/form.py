from apps.clientes.models import Cliente
from django import forms

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente

        fields = [
            'nombre',
            'apellidos',
            'direccion',
            'telefono'
        ]

        labels = {
            'nombre':    'Nombre',
            'apellidos': 'Apellidos',
            'direccion': 'Direccion',
            'telefono':  'telefono'
        }

        widgets = {
            'nombre':    forms.TextInput(attrs={'class': 'form-control'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono':  forms.TextInput(attrs={'class': 'form-control'})
        }