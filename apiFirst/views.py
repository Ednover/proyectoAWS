from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework import status
from django.shortcuts import redirect

import boto3
from botocore.config import Config

from api.models import Alumno, Profesor
from .serializers import StudentSerializers, TeacherSerializers

my_config = Config(
    region_name = 'us-east-1',
    signature_version = 'v4',
    retries = {
        'max_attempts': 10,
        'mode': 'standard'
    },
)

s3_client = boto3.client(
    's3', 
    config=my_config, 
    aws_access_key_id='ASIA4U7QOCMZX4STJ3A4', 
    aws_secret_access_key='TVkTmZxNu7CwNsY4CeFgqRkrvbkHhAHJrfJqzggB',
    aws_session_token='FwoGZXIvYXdzEK///////////wEaDLri6Ld4vzwX33g4hCLPASSVQnk7BRBrv4u1VCVLRZfHrj0Hx8NFYE/NjLYYBepNtDoPm4+aAzbGzHFZwYWEjJRQuA6EMljiHRv9OU9LJlU9eyxvCMESv00/yjAZ3SqEvxEMzBpPlBO4cv0I0+I0BpEWeJ6tFtZVlr96HCYiNgRzCbEl1x4hj91XWu8Zrcy0BdKzjAdNk9BlS7wtzgJ/+ACmx5NZBd8NdKAeD8J5anqBxMLG+CzhwSQ3JxR2EzhWayEHKxBXHwSyDgSbzZXnYKYRagrmj9TkCP/Yd/78jiit7OOcBjItSIFbguOsBxQgPgmdYR6dH0cRDELPal3az5HZHdUdr2Eo+IkIIwnxb2PGGTho')

@api_view(['GET', 'POST'])
def queryStudents(request):
    if request.method == 'GET':
        students = Alumno.objects.all()
        serializer = StudentSerializers(students, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = StudentSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse({'message': 'Los datos del alumno no son correctos'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','DELETE', 'PUT'])
def queryStudent(request, id):
    try:
        student = Alumno.objects.get(id=id)
    except Alumno.DoesNotExist:
        return JsonResponse({'message': 'El alumno no existe'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = StudentSerializers(student)
        return Response(serializer.data)
    if request.method == 'DELETE':
        serializer = StudentSerializers(student)
        student.delete()
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = StudentSerializers(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'message': 'Los datos del alumno no son correctos'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def queryTeachers(request):
    if request.method == 'GET':
        teachers = Profesor.objects.all()
        serializer = TeacherSerializers(teachers, many = True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = TeacherSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse({'message': 'Los datos del profesor no son correctos'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','DELETE', 'PUT'])
def queryTeacher(request, id):
    try:
        teacher = Profesor.objects.get(id=id)
    except Profesor.DoesNotExist:
        return JsonResponse({'message': 'El profesor no existe'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = TeacherSerializers(teacher)
        return Response(serializer.data)
    if request.method == 'DELETE':
        serializer = TeacherSerializers(teacher)
        teacher.delete()
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = TeacherSerializers(teacher, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return JsonResponse({'message': 'Los datos del profesor no son correctos'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT'])
def queryImgStudent(request, id):
    try:
        student = Alumno.objects.get(id=id)
    except Alumno.DoesNotExist:
        return JsonResponse({'message': 'El alumno no existe'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = StudentSerializers(student)
        url = serializer.data['fotoPerfilUrl']
        file = request.data['foto']
        response = s3_client.upload_file(file, 'proyectoaws-bucket', id+'.jpg',
                    ExtraArgs={'ACL': 'public-read'})
        if(url != None):
            
            response = redirect(url)
            return response
        else:
            return Response({'message': 'El alumno no tiene foto de perfil'})
    if request.method == 'PUT':
        serializer = StudentSerializers(student, data = request.data)
        file = request.data['foto']
        print(file)
        response = s3_client.upload_file(file, 'proyectoaws-bucket', id+'.jpg',
                    ExtraArgs={'ACL': 'public-read'})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return JsonResponse({'message': 'Los datos del alumno no son correctos'}, status=status.HTTP_400_BAD_REQUEST)