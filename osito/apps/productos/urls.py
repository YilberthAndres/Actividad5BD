from django.urls import path, include
from apps.productos.views import index, productoCreate, productoEdit, productoEliminar
app_name = "productos"
urlpatterns = [
    path('', index, name='index'),
    path('nuevo/', productoCreate, name='productoCreate'),
    path('actualizar/<int:id_producto>/', productoEdit, name='productoEdit'),
    path('eliminar/<int:id_producto>/', productoEliminar, name='productoEliminar'),

]