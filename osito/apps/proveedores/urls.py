from django.urls import path, include
from apps.proveedores.views import index, proveedorCrear, proveedorEditar, proveedorEliminar


app_name = "proveedores"
urlpatterns = [
    path('',index, name= 'index'),
    path('nuevo/', proveedorCrear, name= 'proveedorCrear'),
    path('actualizar/<int:id_proveedor>/', proveedorEditar, name= 'proveedorEditar'),
     path('eliminar/<int:id_proveedor>/', proveedorEliminar, name= 'proveedorEliminar'),


]
