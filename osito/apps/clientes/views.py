from django.shortcuts import redirect, render
from apps.clientes.models import Cliente
# Create your views here.

def index(request):
    cliente = Cliente.objects.all().order_by('-id')
    context = {'clientes': cliente}
    return render(request, 'clientes/listar.html', context)

def home(request):

    return render(request, 'base/base.html')


def clientCreate(request):

    if(request.method == 'POST'):
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect()
