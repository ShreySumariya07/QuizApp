from datetime import *
from django.contrib.auth.models import *
from Account.models import *
from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib import messages
from Quiz.models import Quiz_Details


def login(request):
    return render(request, 'index.html')


def logout_confirm(request):
    return render(request, "homepage1.html")


def login_confirm(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = auth.authenticate(username=email, password=password)
        if user is not None:
            if user.is_teacher == 1:
                auth.login(request, user)
                tid = User.objects.only("id").get(email=email)
                return render(request, "teacher_navbar_dashboard1.html", {"tea_id": tid.id})
            elif user.is_student == 1:
                auth.login(request, user)
                sid = User.objects.only("id").get(email = email)
                quiz = Quiz_Details.objects.all()[:3]
                user_quiz = {
                    "quizes": quiz,
                    "s_id": sid.id
                }
                return render(request, "student_dash1.html", user_quiz)
        else:
            messages.info(request, 'Invalid Credentials !')
            return redirect('login')
    else:
        return render(request, 'index.html')


def register_confirm(request):
    if request.method == "POST":
        first_name = request.POST.get("fname")
        last_name = request.POST.get("lname")
        pass1 = request.POST.get("pass1")
        pass2 = request.POST.get("pass2")
        email = request.POST.get("email")
        phone_no = request.POST.get("phone")
        teacher_student = request.POST.get("radio")
        if teacher_student == "student":
            b_day = request.POST.get("b_day")
            x = datetime.strptime(b_day, '%Y-%m-%d').date()
            grade = request.POST.get("grade")
            today = date.today()
            age = today.year - x.year-((today.month, today.day) < (x.month, x.day))
            if pass1 == pass2:
                if User.objects.filter(email=email).exists():
                    messages.info(request, "Email Taken")
                    return render(request, "index.html")
                else:
                    user = User.objects.create_user(username=email, first_name=first_name, last_name=last_name, email=email, password=pass1, is_student=True, phone_no=phone_no)
                    student1 = Student.objects.create(user=user, b_day=b_day, age=age, grade=grade)
                    user.save()
                    student1.save()
                    return redirect("login")
            else:
                messages.info(request, "Password didn't match")
                return render(request, "index.html")

        else:
            subject = request.POST.get("subject")
            qualification = request.POST.get("grade")
            if pass1 == pass2:
                if User.objects.filter(email=email).exists():
                    messages.info(request, "Email Taken")
                    return render(request, "index.html")
                else:
                    user = User.objects.create_user(username=email, first_name=first_name, last_name=last_name, email=email, password=pass1, is_teacher=True, phone_no=phone_no)
                    teacher1 = Teacher.objects.create(user=user, subject=subject, qualification=qualification)
                    user.save()
                    teacher1.save()
                    return redirect("login")
            else:
                messages.info(request, "Password didn't match")
                return render(request, "index.html")
    else:
        return render(request, "index.html")