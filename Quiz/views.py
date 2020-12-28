from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def course_details(request):
    return HttpResponse("Quiz Hello")


def topic_details(request):
    return HttpResponse("Quiz Hello")


def quiz_details(request):
    return HttpResponse("Quiz Hello")


def to_add_question(request):
    return HttpResponse("Quiz Hello")


def check_my_answer(request):
    return HttpResponse("Quiz Hello")


def final_score(request):
    return HttpResponse("Quiz Hello")