from django.urls import path, include
from apps.clientes.views import index
app_name = "ventas";

urlpatterns = [
    path('', index)
]