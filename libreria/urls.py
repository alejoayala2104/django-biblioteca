from django.urls import path
from . import views

urlpatterns = [
	path('nosotros', views.nosotros, name='nosotros'),
	path('', views.inicio, name='inicio'),
	path('libros', views.libros, name='libros'),
	path('libros/crear', views.crearLibro, name='crear'),
	path('libros/editar', views.editarLibro, name='editar'),
 
]
