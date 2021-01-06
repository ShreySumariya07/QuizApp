from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import date
from Quiz.models import *
from Account.models import *
from django.contrib import messages
# Create your views here.


def course_details(request):
    return HttpResponse("Quiz Hello")


def topic_details(request):
    return HttpResponse("Quiz Hello")


def quiz_details(request):
    return render(request, "quiz_index.html")


def submit_quiz_details(request):
    if request.method == 'POST':
        quiz_name = request.POST.get('name')
        topic_name = request.POST.get('topic')
        questions = request.POST.get('no_of_ques')
        marks = request.POST.get('marks_per_ques')
        tname = request.POST.get('email')
        total_marks = int(questions) * int(marks)
        teacher_id = User.objects.only("id").get(email=tname)
        update_on = date.today()
        # topic_id = Topic.objects.only("Topic_id").get(Topic_name = topic_name)
        if Topic.objects.filter(Topic_name=topic_name).exists():
            topic_id = Topic.objects.only("Topic_id").get(Topic_name=topic_name)
            new_quiz = Quiz_Details.objects.create(quiz_name=quiz_name, quiz_topic=topic_id, no_of_questions=questions,
                                                   Mark_per_question=marks, total_marks=total_marks,
                                                   teacher_id=teacher_id, update_on=update_on)
            new_quiz.save()
            quiz = Quiz_Details.objects.filter(teacher_id=teacher_id)
            user_quiz = {"quizes": quiz}
            return render(request, "display_index.html", user_quiz)
        else:
            messages.info(request, "Invalid Topic")
            return redirect('quiz_details')
    else:
        messages.info(request, "Invalid Input method")
        return redirect('quiz_details')
"""
def display_quiz(request):
    if request.session.has_key("tid"):
        ses = request.session["tid"]
        quiz = Quiz_Details.objects.filter(teacher_id = ses)
        user_quiz = {
            "quizes":quiz
        }
        return render(request,"display_index.html",user_quiz)
    # else:
    #     return render(request,"teacher_navbar_dashboard.html")
"""


def to_add_question(request, no_of_Q):
    return render(request, "add_question.html")


def check_my_answer(request):
    return HttpResponse("Quiz Hello")


def final_score(request):
    return HttpResponse("Quiz Hello")