from . import views
from django.urls import path

app_name = 'Account'
urlpatterns = [
    path("", views.login, name="login"),
    path("login_confirm", views.login_confirm, name="login_confirm"),
    path("register_confirm", views.register_confirm, name="register_confirm"),
    path("logout_confirm",views.logout_confirm, name="logout_confirm")
]

'''
    #from django.contrib import admin
    #path("login_as_student/",views.login_as_student,name="student_login"),
    #path("login_as_teacher/",views.login_as_teacher,name="teacher_login"),
    #path("register_as_student/",views.register_as_student,name="student_register"),
    #path("register_as_tecaher/",views.register_as_teacher,name="teacher_register")
'''


