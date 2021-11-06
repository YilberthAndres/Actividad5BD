from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from apps.proveedores.models import Proveedore
from apps.proveedores.form import ProveedorForm

# Create your views here.
def home (request):
    return render(request, 'base/base.html')

def index (request):

    proveedor = Proveedore.objects.all().order_by('id')
    context = {'proveedores' : proveedor}
    return render(request, 'proveedores/index.html', context)
    # return render(request,'proveedores/index.html')
    # return HttpResponse("you're looking at question")

def proveedorCrear(request):
    if(request.method == 'POST'):
        form = ProveedorForm(request.POST)  
        if form.is_valid():
            form.save()

        return redirect('proveedores:index')    
    else: 
        form = ProveedorForm()  
        return render(request,'proveedores/formProveedor.html', {'form': form})  

def proveedorEditar(request, id_proveedor):

    proveedor = Proveedore.objects.get(pk= id_proveedor)

    if request.method == 'GET':
        
        form = ProveedorForm(instance=proveedor)  
    else:
        form = ProveedorForm(request.POST, instance=proveedor)   
        if form.is_valid():
            form.save()
        return redirect('proveedores:index')    

    return render(request,'proveedores/formProveedor.html', {'form': form})


def proveedorEliminar(request, id_proveedor):

    proveedor = Proveedore.objects.get(pk= id_proveedor)

    if request.method == 'POST':
        
        proveedor.delete()
        return redirect('proveedores:index') 

    return render(request,'proveedores/proveedorEliminar.html', {'proveedores': proveedor})    

           

    


