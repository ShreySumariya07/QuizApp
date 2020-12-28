from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate


# Create your views here.
def login_as_student(request):
    user = authenticate(username='entered_email', password='entered_password')
    if user is not None:
        return HttpResponse("Welcome")
    else:
        return HttpResponse("Try again")


def login_as_teacher(request):
    user = authenticate(username='entered_email', password = 'entered_password')
    if user is not None:
        return HttpResponse("Welcome")
    else:
        return HttpResponse("Try again")


def register_as_student(request):
    return HttpResponse("Hello")


def register_as_teacher(request):
    return HttpResponse("Hello")

