from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("course/", views.course_details, name="course_details"),
    path("topic/", views.topic_details, name="topic_details"),
    path("Quiz_Details/", views.quiz_details, name="quiz_details"),
    path("add_question/", views.to_add_question, name="to_add_question"),
    path("check_answers/", views.check_my_answer, name="check_my_answer"),
    path("result/", views.final_score, name="final_score"),
]
