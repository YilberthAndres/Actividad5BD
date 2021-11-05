from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from apps.productos.models import Producto
from apps.productos.form import ProductoForm
# Create your views here.

def home(request):   

    return render(request, 'base/base.html')

def index(request):   
    producto = Producto.objects.all().order_by('-id')
    context = {'productos': producto}
    return render(request, 'productos/index.html', context)
    # return render(request, 'clientes/index.html')

def productoCreate(request): 
    if(request.method == 'POST'): 
        form = ProductoForm(request.POST)
        if form.is_valid(): 
            form.save()

        return redirect('productos:index')
    else:  
        form = ProductoForm()
        return render(request, 'productos/formProducto.html', {'form': form})

def productoEdit(request, id_producto):
    producto = Producto.objects.get(pk=id_producto)
    if request.method == 'GET':
        form = ProductoForm(instance=producto)
    else: 
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
        return redirect('productos:index')
    return render(request, 'productos/formProducto.html', {'form': form})



def productoEliminar(request, id_producto):

    producto = Producto.objects.get(pk=id_producto)

    if request.method == 'POST':
        producto.delete()
        return redirect('productos:index')
    return render(request, 'productos/productoEliminar.html', {'productos': producto})