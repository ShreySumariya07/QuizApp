from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import date
# Create your views here.


def course_details(request):
    return HttpResponse("Quiz Hello")


def topic_details(request):
    return HttpResponse("Quiz Hello")


def quiz_details(request):
    return render(request, "quiz_info.html")


def submit_details(request):
    quiz_name = request.POST.get('name')
    topic_name = request.POST.get('topic')
    no_of_questions = request.POST.get('no_of_ques')
    Mark_per_question = request.POST.get('marks_per_ques')
    total_marks = no_of_questions * Mark_per_question
    tname = request.POST.get('author')
    user = User.object.filter(email=tname, is_teacher=1)
    teacher_id = user.id
    topicId = Topic.object.filter(Topic_name=topic_name)
    Topic_id = topicId.id
    update_on = date.today()
    new_quiz = Quiz_Details.object.create(quiz_name=quiz_name, quiz_topic=Topic_id, )

def to_add_question(request):
    return HttpResponse("Quiz Hello")


def check_my_answer(request):
    return HttpResponse("Quiz Hello")


def final_score(request):
    return HttpResponse("Quiz Hello")