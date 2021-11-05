from django.contrib import admin
from apps.clientes.models import Cliente

# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    list_display  = ('nombre','apellidos','direccion','telefono')
    ordering      = ('nombre','apellidos')
    search_fields = ('nombre','apellidos')


admin.site.register(Cliente, ClienteAdmin)