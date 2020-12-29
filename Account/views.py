from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate

def login(request):
    return render(request,'index.html')
'''

# Create your views here.
def login_as_student(request):
    user = authenticate(username='Email', password='Password')
    if user is not None:
        return render(request, 'homepage.html')
    else:
        return redirect('index')


def login_as_teacher(request):
    user = authenticate(username='Email', password='Password')
    if user is not None:
        return render(request, 'homepage.html')
    else:
        return redirect('index')


def register_as_student(request):
    return render(request,'index.html')


def register_as_teacher(request):
    return render(request,'index.html')

'''