from django.db import models

class alumnos(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    matricula = models.CharField(max_length=20)
    promedio = models.FloatField()
    fotoPerfilUrl = models.TextField()

class profesores(models.Model):
    numeroEmpleado = models.IntegerField()
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    horasClase = models.IntegerField()