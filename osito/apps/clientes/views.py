from django.shortcuts import redirect, render
from apps.clientes.models import Cliente
from apps.clientes.form import ClienteForm
# Create your views here.

def index(request):
    cliente = Cliente.objects.all().order_by('-id')
    context = {'clientes': cliente}
    return render(request, 'clientes/listar.html', context)

def home(request):

    return render(request, 'base/base.html')


def clientCreate(request):

    if(request.method == 'POST'):
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect('clientes:index')
    else:
        form = ClienteForm()
        return render(request, 'clientes/formCliente.html', {'form': form})

def clientEdit(request, id_client):

    client = Cliente.objects.get(pk=id_client)

    if request.method == 'GET':
        form = ClienteForm(instance=client)
    else:
        form = ClienteForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
        return redirect('clientes:index')
    
    return render(request, 'clientes/formCliente.html', {'form': form})


def clientDelete(request, id_client):

    client = Cliente.objects.get(pk=id_client)

    if request.method == 'POST':
        client.delete()
        return redirect('clientes:index')
    return render(request, 'clientes/clienteEliminar.html', {'clientes': client})

