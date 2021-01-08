from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'Quiz'

urlpatterns = [
    path("course/", views.course_details, name="course_details"),
    path("topic/", views.topic_details, name="topic_details"),
    path("quiz_details/", views.quiz_details, name="quiz_details"),
    path('quiz_added/<int:teacher_id>/', views.quiz_added, name="quiz_added"),
    path("to_add_question/<int:qu_id>/", views.to_add_question, name="to_add_question"),
    path("save_question/", views.save_question,name="save_question"),
    path("check_answer/<int:question_id>/", views.check_answer, name="check_answer"),
    path("result/", views.final_score, name="final_score"),
    path("submit_quiz_details/", views.submit_quiz_details, name="submit_quiz_details"),
    path("show_quiz/<int:s_id>", views.student_quiz, name="student_quiz"),
    path("results_page/<int:s_id>/", views.results_page, name="results_page"),
    path("play_quiz/<int:quiz_id>/", views.play_quiz, name="play_quiz"),
    # path("display_quiz/",views.display_quiz,name="display_quiz")
]
