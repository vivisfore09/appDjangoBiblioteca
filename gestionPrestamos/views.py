#from django.shortcuts import render #Trabajar con Plantillas
import json
from django.views import View
# Create your views here.
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from gestionPrestamos.models import Estudiante, Libro, Prestamo, Devolucion

class LibroView(View):
    
    #Saltar Restriccion CSRF
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs) :
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, isbn=""): #Listar Todos
        
        if len(isbn)>0:
            libros=list(Libro.objects.filter(Isbn=isbn).values())
            if len(libros)>0:
                datos={'Lista':libros, 'Mensaje':'Resultado de la Busqueda.'}
            else:
                datos={'Error':'No se Encontraron Libros.'}
            return JsonResponse(datos)
        else:
            Libros=list(Libro.objects.values())
            if len(Libros)>0:
                datos={"Lista":Libros}
                return JsonResponse(datos)
            else:
                datos={"Error":"No se encontraron datos"}
                return JsonResponse(datos)
    
       
    def post(self, request):
        dat=json.loads(request.body)
        lib=Libro(Isbn=dat["Isbn"],titulo=dat["titulo"],editorial=dat["editorial"],autor=dat["autor"],no_page=dat["no_page"])
        lib.save()
        mensaje={"Mensaje":"Libro Registrado Exitosamente"}
        return JsonResponse(mensaje)
       
    
    def put(self, request): #Actualizar Uno
        data=json.loads(request.body)
        datos=list(Libro.objects.filter(Isbn=data["Isbn"]).values())
        if len(datos)>0:
            libro=Libro.objects.get(Isbn=data["Isbn"])
            libro.titulo=data["titulo"]
            libro.editorial=data["editorial"]
            libro.autor=data["autor"]
            libro.no_page=data["no_page"]
            libro.save()
            mensaje={'message':"Libro Actualizado exitosamente"}
        else:
            mensaje={'Error':'No se encontro Libro a actualizar.'}
            
        return JsonResponse(mensaje)
    
    
    def delete(self, request,isbn):
        datos=list(Libro.objects.filter(Isbn=isbn).values())
        if len(datos)>0:
            Libro.objects.filter(Isbn=isbn).delete()
            datos={"Mensaje": "Registro eliminado Exitosamente."}
        else:
            datos={"Error": "El Libro no existe."}
        
        return JsonResponse(datos)
    
    
class PrestamoView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs) :
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request):
        
        Pres=list(Prestamo.objects.values())
        if len(Pres)>0:
            datos={"Datos":Pres}
            return JsonResponse(datos)
        else:
            datos={"Mensaje":"No se encontraron datos"}
        
        return JsonResponse(datos)
    
    def post(self, request):
        data=json.loads(request.body)
        try:
            lib=Libro.objects.get(Isbn=data["libro"])
            est=Estudiante.objects.get(documento=data["estudiante"])
            pres=Prestamo.objects.create(libro=lib,estudiante=est)
            pres.save()
            mensaje={"mensage":"Success"}
        except Libro.DoesNotExist:
            mensaje={"mensage":"El Libro no Existe"}
        except Estudiante.DoesNotExist:
            mensaje={"mensage":"El estudiante no existe"}
            
              
        return JsonResponse(mensaje)
    
class DevolucionView(View):
        
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs) :
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request):
        
        Dev=list(Devolucion.objects.values())
        if len(Dev)>0:
            datos={"Datos":Dev}
            return JsonResponse(datos)
        else:
            datos={"Mensaje":"No se encontraron datos"}
        
        return JsonResponse(datos)
    
    def post(self, request):
        data=json.loads(request.body)
        try:
            pres=Prestamo.objects.get(id=data["prestamo"])
            Dev=Devolucion.objects.create(prestamo=pres)
            Dev.save()
            mensaje={"mensage":"Success"}
        except Prestamo.DoesNotExist:
            mensaje={"mensage":"El Prestamo no existe."}
        except:
            mensaje={"mensage":"Ya existe una devolucion para el prestamo"}
        
        return JsonResponse(mensaje)