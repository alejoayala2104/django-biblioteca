from django.shortcuts import render

# Create your views here.
def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def libros(request):
    return render(request, 'libros/index.html')

def crearLibro(request):
    return render(request, 'libros/crear.html')

def editarLibro(request):
    return render(request, 'libros/editar.html')