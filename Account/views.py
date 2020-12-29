import datetime
from django.contrib.auth.models import *
from Account.models import *
from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate


def login(request):
    return render(request,'index.html')

def login_confirm(request):
    user = authenticate(username='Email', password='Password')
    if user is not None:
        return render(request, 'index1.html')
    else:
        return render(request,"index.html")

def register_confirm(request):
    if request.method == "POST":
        first_name = request.POST.get("fname")
        last_name = request.POST.get("lname")
        pass1 = request.POST.get("pass1")
        pass2 = request.POST.get("pass2")
        email = request.POST.get("email")
        phone_no = request.POST.get("phone")
        teacher_student = request.POST.get("radio")
        if(teacher_student == "student"):
            b_day = request.POST.get("b_day")
            grade = request.POST.get("grade")
            age = int((datetime.datetime.now() - b_day).days / 365.25 )
            if pass1 == pass2:
                if User.objects.filter(email=email).exists():
                    messages.info(request,"Email Taken")
                    return render(request, "index.html")
                else:
                    user = User.objects.create(first_name = first_name,last_name=last_name,email=email,password=pass1,is_student=True,phone_no=phone_no)
                    student1 = Student.objects.create(user = user,b_day = b_day,age=age,grade = grade)
                    user.save()
                    student1.save()
                    return redirect("login")
            else:
                messages.info(request,"Password didn't match")
                return render(request, "index.html")

        else:
            subject = request.POST.get("subject")
            qualification = request.POST.get("grade")
            if pass1 == pass2:
                if User.objects.filter(email=email).exists():
                    messages.info(request,"Email Taken")
                    return render(request, "index.html")
                else:
                    user = User.objects.create_user(first_name = first_name,last_name=last_name,email=email,password=pass1,is_teacher=True,phone_no=phone_no)
                    user.save()
                    teacher1 = Teacher.objects.create_user(user = user,subject = subject,qualification =qualification)
                    teacher1.save()
                    return redirect("login")
            else:
                messages.info(request,"Password didn't match")
                return render(request, "index.html")
    else:
        return render(request,"index.html")

def regsiter(request):
    if request.method == "POST":
        teacher_student = request.POST.get("radio")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        pass1 = request.POST.get("pass1")
        pass2 = request.POST.get("pass2")
        phone = request.POST.get("phone")
        print(first_name)
        user = User.objects.create_user(email=email,last_name=last_name,first_name=first_name,password=pass1,phone_no=phone,is_student=True)
        user.save()
        return render(request,"homepage.html")
    else:
        return render("test.html")
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