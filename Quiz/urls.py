from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'Quiz'

urlpatterns = [
    path("course/", views.course_details, name="course_details"),
    path("topic/", views.topic_details, name="topic_details"),
    path("quiz_details/", views.quiz_details, name="quiz_details"),
    path("to_add_question/<int:qu_id>/", views.to_add_question, name="to_add_question"),
    #url(r'^to_add_question/(?P<no_of_Q>[0-9]+)$', views.to_add_question, name="to_add_question"),
    path("check_answers/", views.check_my_answer, name="check_my_answer"),
    path("result/", views.final_score, name="final_score"),
    path("submit_quiz_details/",views.submit_quiz_details, name="submit_quiz_details"),
    # path("display_quiz/",views.display_quiz,name="display_quiz")
]
