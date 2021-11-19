from django.contrib import admin
from apps.productos.models import Producto


class ProductoAdmin(admin.ModelAdmin):
    list_display  = ('descripcion','precio','numero_exit')
    ordering      = ('descripcion','precio')
    search_fields = ('descripcion','precio')


admin.site.register(Producto, ProductoAdmin)