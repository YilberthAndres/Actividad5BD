from django.urls import path, include
from apps.clientes.views import index, clientCreate,clientEdit,clientDelete

app_name = "clientes";

urlpatterns = [
    path('', index,  name='index'),
    path('nuevo/', clientCreate, name='clienteCreate'),
    path('actualizar/<int:id_client>/', clientEdit, name='clientEdit'),
    path('eliminar/<int:id_client>/', clientDelete, name='clientDelete'),
]