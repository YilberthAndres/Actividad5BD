from django.contrib import admin
from apps.productos.models import Producto, Compras


class MembershipInLine(admin.TabularInline):
    '''TabularInline Inline View for '''

    model = Compras
    extra = 1

class ProductoAdmin(admin.ModelAdmin):
    inlines = (MembershipInLine, )



admin.site.register(Producto, ProductoAdmin)