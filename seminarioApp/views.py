from django.shortcuts import render, redirect
from seminarioApp.models import Seminarios
from seminarioApp.forms import IngresoForm

# Create your views here.


def index(request):
    return render(request, 'index.html')


def consultarSeminarios(request):
    listaSeminarios = Seminarios.objects.all()
    data = {'seminarios': listaSeminarios}
    return render(request, 'consultar.html', data)


def agregarSeminario(request):
    form = IngresoForm()
    if request.method == 'POST':
        form = IngresoForm(request.POST)
        if form.is_valid():
            modeloSeminario = Seminarios()
            modeloSeminario.nombre = form.cleaned_data['nombre']
            modeloSeminario.telefono = form.cleaned_data['telefono']
            modeloSeminario.fecha = form.cleaned_data['fecha']
            modeloSeminario.organizacion = form.cleaned_data['organizacion']
            modeloSeminario.email = form.cleaned_data['email']
            modeloSeminario.profesion = form.cleaned_data['profesion']
            modeloSeminario.observaciones = form.cleaned_data['observaciones']
            modeloSeminario.save()
            return redirect('/')
    data = {'form': form}
    return render(request, 'formSeminario.html', data)


def modificarSeminario(request, id):
    seminario = Seminarios.objects.get(id=id)
    form = IngresoForm(instance=seminario)

    if request.method == 'POST':
        form = IngresoForm(request.POST, instance=seminario)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form': form}
    return render(request, 'formSeminario.html', data)


def eliminarSeminario(request, id):
    seminario = Seminarios.objects.get(id=id)
    seminario.delete()
    return redirect('/consultar/')
