from django.urls import path
from .views import LibroView, PrestamoView, DevolucionView
from gestionPrestamos.viewsFrontend import *

urlpatterns=[
  path('Libros/', LibroView.as_view(), name='Listar'),  
  path('Libros/<str:isbn>', LibroView.as_view(), name='Buscar'),
  path('Prestamos/', PrestamoView.as_view(), name='ListarPres'),  
  path('Devolucion/', DevolucionView.as_view(), name='ListarDev'),
  path('', principal, name='index'),
  path('registrarLibro/', formLibro, name='formulario'),
  path('listaLibros/', listaLibros, name='ListaLib'),
  path('consultaLibro/', consultaLibro, name='ListaLib'),
  path('guardarLibros/', guardarLibro, name='guardaLib'),
  path('cargarForm/<str:isbn>',cargarForm, name="cargarFormulario"),
  path('actualizarLibro/', actualizarLibro, name='actualizar'),
  path('eliminarLibro/<str:isbn>', eliminarLibro, name='eliminar')
]