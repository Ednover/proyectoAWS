from django.urls import path
from . import views

urlpatterns = [
    path('alumnos', views.queryStudents),
    path('alumnos/', views.queryStudents),
    path('alumnos/<int:id>', views.queryStudent),

     path('profesores', views.queryTeachers),
    path('profesores/', views.queryTeachers),
    path('profesores/<int:id>', views.queryTeacher),
]