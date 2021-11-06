from django.contrib import admin

from apps.proveedores.models import Proveedore 

# Register your models here.





class ProveedoreAdmin(admin.ModelAdmin):
      
      list_display = ('nombre', 'apellido', 'direccion', 'provincia', 'telefono')
      ordering = ('nombre', 'apellido', 'direccion', 'provincia', 'telefono')
      search_fields = ('nombre', 'apellido', 'direccion', 'provincia', 'telefono')




admin.site.register(Proveedore, ProveedoreAdmin )
