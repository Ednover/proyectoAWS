from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework import status

from .serializers import Student, Teacher

students = []
teachers = []

@api_view(['GET', 'POST'])
def queryStudents(request):
    if request.method == 'GET':
        studentsArray = Student(students, many = True).data
        return Response(studentsArray)
    if request.method == 'POST':
        serializer = Student(data = request.data)
        if serializer.is_valid():
            students.append(serializer.data)
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse({'message': 'Los datos del alumno no son correctos'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','DELETE', 'PUT'])
def queryStudent(request, id):
    idstudent = id
    studentQuery = None
    for student in students:
        if student['id'] == idstudent:
            studentQuery = student
            currentId = students.index(student)
    if studentQuery is None:
        return JsonResponse({'message': 'El alumno no existe'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        return Response(studentQuery)
    if request.method == 'DELETE':
        students.pop(currentId)
        return Response(studentQuery)
    if request.method == 'PUT':
        serializer = Student(data = request.data)
        if serializer.is_valid():
            students.pop(currentId)
            students.insert(currentId, serializer.data)
            return Response(serializer.data)
        else:
            return JsonResponse({'message': 'Los datos del alumno no son correctos'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def queryTeachers(request):
    if request.method == 'GET':
        teachersArray = Teacher(teachers, many = True).data
        return Response(teachersArray)
    if request.method == 'POST':
        serializer = Teacher(data = request.data)
        if serializer.is_valid():
            teachers.append(serializer.data)
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse({'message': 'Los datos del profesor no son correctos'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','DELETE', 'PUT'])
def queryTeacher(request, id):
    idTeacher = id
    teacherQuery = None
    for teacher in teachers:
        if teacher['id'] == idTeacher:
            teacherQuery = teacher
            currentId = teachers.index(teacher)
    if teacherQuery is None:
        return JsonResponse({'message': 'El profesor no existe'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        return Response(teacherQuery)
    if request.method == 'DELETE':
        teachers.pop(currentId)
        return Response(teacherQuery)
    if request.method == 'PUT':
        serializer = Teacher(data = request.data)
        if serializer.is_valid():
            teachers.pop(currentId)
            teachers.insert(currentId, serializer.data)
            return Response(serializer.data)
        else:
            return JsonResponse({'message': 'Los datos del profesor no son correctos'}, status=status.HTTP_400_BAD_REQUEST)