from rest_framework import serializers
from api.models import Alumno, Profesor

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = '__all__'

class TeacherSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profesor
        fields = '__all__'