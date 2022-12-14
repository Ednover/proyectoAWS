from django.urls import path
from . import views

urlpatterns = [
    path('alumnos', views.queryStudents),
    path('alumnos/', views.queryStudents),
    path('alumnos/<int:id>', views.queryStudent),
    path('alumnos/<int:id>/fotoPerfilUrl', views.queryImgStudent),
    path('alumnos/<int:id>/fotoPerfilUrl/', views.queryImgStudent),

    path('profesores', views.queryTeachers),
    path('profesores/', views.queryTeachers),
    path('profesores/<int:id>', views.queryTeacher),
]