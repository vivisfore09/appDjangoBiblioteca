from django.db import models

# Create your models here.
class Libro(models.Model):
    Isbn=models.CharField(max_length=25,primary_key=True)
    titulo=models.CharField(max_length=50, unique=True)
    editorial=models.CharField(max_length=50)
    autor=models.CharField(max_length=25)
    no_page=models.IntegerField()
    
    def __str__(self) -> str:
        return self.titulo


class Estudiante(models.Model):
    documento=models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()
    telefono=models.CharField(max_length=50)
   
    def __str__(self) -> str: #Agregar al Modelo
        return self.nombre

class Prestamo(models.Model):
    id=models.AutoField(primary_key=True)
    estudiante=models.ForeignKey(Estudiante,  on_delete=models.CASCADE)
    libro=models.ForeignKey(Libro, on_delete=models.CASCADE)
    fecha=models.DateField(auto_now=True)


class Devolucion(models.Model):
    id=models.AutoField(primary_key=True)
    prestamo=models.OneToOneField(Prestamo,  on_delete=models.CASCADE)
    fecha=models.DateField(auto_now=True)
    
    def __str__(self) -> str:
        return self.id+" - "+self.fecha

class Usuario(models.Model):
    email=models.EmailField()
    clave=models.CharField(max_length=30)
    rol=models.CharField(max_length=30)
    estudiante=models.OneToOneField(Estudiante,  on_delete=models.CASCADE)