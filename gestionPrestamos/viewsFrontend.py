import json
from urllib import response
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
import requests

def principal(request):
    return render(request, 'index.html')

def formLibro(request):
    return render(request, 'formLibro.html')

def listaLibros(request):
    response=requests.get('http://localhost:8000/prestamos/Libros/')
    libros=response.json()
    print(libros)
    return render(request, "Libros.html",libros)

def consultaLibro(request):
    #template_name="Libro.html"
    dato=request.POST["isbn"]
    response=requests.get('http://localhost:8000/prestamos/Libros/'+dato)
    libros=response.json()
    print(libros)
    return render(request, "Libros.html",libros)

def guardarLibro(request):
    #template_name="formLibro.html"
    datos=    {
      "Isbn": request.POST["isbn"],
      "titulo": request.POST["titulo"],
      "editorial": request.POST["editorial"],
      "autor": request.POST["autor"],
      "no_page": request.POST["page"]
    }
    requests.post('http://localhost:8000/prestamos/Libros/',data=json.dumps(datos))
    return redirect('../listaLibros/')

def cargarForm(request,isbn):
    response=requests.get('http://localhost:8000/prestamos/Libros/'+isbn)
    libros=response.json()
    print(libros)
    return render(request, "formActualizar.html",libros)
    

def actualizarLibro(request):
    datos=    {
      "Isbn": request.POST["isbn"],
      "titulo": request.POST["titulo"],
      "editorial": request.POST["editorial"],
      "autor": request.POST["autor"],
      "no_page": request.POST["page"]
    }
    response=requests.put('http://localhost:8000/prestamos/Libros/',data=json.dumps(datos))
    message=response.json()
    print(message)
    return redirect('../listaLibros/')

def eliminarLibro(request,isbn):
    response=requests.delete('http://localhost:8000/prestamos/Libros/'+isbn)
    libros=response.json()
    print(libros)
    return redirect('../listaLibros/')