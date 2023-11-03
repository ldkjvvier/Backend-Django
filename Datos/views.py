from django.shortcuts import render
from django.db.models import Sum, Max
from .models import Producto, Proyecto
from pagina.views import home, proyectos
from . import forms
from .forms import FormProyecto
# Create your views here.

def Productos (request):
    productos = Producto.objects.all().order_by('nombre')
    stock_total = Producto.objects.aggregate(Sum('stock'))
    mayor_precio = Producto.objects.aggregate(Max('precio'))
    data = {'producto' : productos,
            'stock_total' : stock_total['stock__sum'],
            'mayor_precio' : mayor_precio['precio__max']
            }
    return render(request, 'productos.html', data)

def UserRegistrationForm(request):
    form = forms.UserRegistrationForm()

    if request.method == 'POST':
        form = forms.UserRegistrationForm(request.POST)
        if form.is_valid():
            print("Form es valido")
            print("Nombre: ", form.cleaned_data['nombre'])
            print("Email: ", form.cleaned_data['email'])
            print("Fono: ", form.cleaned_data['fono'])
    
    data = {"form" : form}
    return render(request, 'userRegistration.html', data)

def listadoProyecto(request):
    proyectos = Proyecto.objects.all()
    data = {'proyectos' : proyectos}
    return render(request, 'proyectos.html', data)

def agregarProyecto(request):
    form = FormProyecto()
    if request.method == 'POST':
        form = FormProyecto(request.POST)
        print(form)
        if form.is_valid():
            form.save()
        return home(request)
    data = {'form' : form}
    return render(request, 'agregarProyecto.html', data)

def actualizarProyecto(request, id):
    proyecto = Proyecto.objects.get(id=id)
    form = FormProyecto(instance=proyecto)
    if request.method == 'POST':
        form = FormProyecto(request.POST, instance=proyecto)
        if form.is_valid():
            form.save()
        return home(request)
    data = {'form' : form}
    return render(request, 'agregarProyecto.html', data)

def eliminarProyecto(request, id):
    proyecto = Proyecto.objects.get(id=id)
    proyecto.delete()
    return home(request)