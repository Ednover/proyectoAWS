from rest_framework import serializers

class Student(serializers.Serializer):
    id = serializers.IntegerField()
    nombres = serializers.CharField()
    apellidos = serializers.CharField()
    matricula = serializers.CharField()
    promedio = serializers.FloatField()

class Teacher(serializers.Serializer):
    id = serializers.IntegerField()
    numeroEmpleado = serializers.IntegerField()
    nombres = serializers.CharField()
    apellidos = serializers.CharField()
    horasClase = serializers.IntegerField()