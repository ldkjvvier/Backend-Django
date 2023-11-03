from django.shortcuts import render

# Create your views here.

def home (request):
    return render(request, 'index.html') #index.html es la pagina principal
def tecnologia (request):
    return render(request, 'tecnologia.html')
def juguetes (request):
    return render(request, 'juguetes.html')
def ropa (request):
    return render(request, 'ropa.html')
def proyectos (request):
    return render(request, 'proyectos.html')
