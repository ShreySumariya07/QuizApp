from . import views
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path("login_as_student/",views.login_as_student,name="student_login"),
    path("login_as_teacher/",views.login_as_teacher,name="teacher_login"),
    path("register_as_student/",views.register_as_student,name="student_register"),
    path("register_as_tecaher/",views.register_as_teacher,name="teacher_register")
]


