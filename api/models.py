from django.db import models

# Create your models here.
class Alumno(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    matricula = models.CharField(max_length=20)
    promedio = models.FloatField()
    fotoPerfilUrl = models.TextField(null=True, blank=True)

class Profesor(models.Model):
    numeroEmpleado = models.IntegerField()
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    horasClase = models.IntegerField()