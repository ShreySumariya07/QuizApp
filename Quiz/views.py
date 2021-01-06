from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import date
from Quiz.models import *
from Account.models import *
from django.contrib import messages


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
        topic_id = Topic.objects.only("Topic_id").get(Topic_name = topic_name)
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


def quiz_added(request, teacher_id):
    quiz = Quiz_Details.objects.filter(teacher_id=teacher_id)
    user_quiz = {"quizes": quiz}
    return render(request, 'display_index.html', user_quiz)


def to_add_question(request, qu_id):
    q_obj = Quiz_Details.objects.only("no_of_questions").get(quiz_id=qu_id)
    q_no = q_obj.no_of_questions
    request.session['quiz_id12'] = qu_id
    request.session['ques_no'] = q_no
    return render(request, "add_question.html")


count = 1


def save_question(request):
    global count
    qu_no = None
    quiz_id12 = None

    if "quiz_id12" in request.session:
        quiz_id12 = request.session["quiz_id12"]
        print(quiz_id12)
    quiz_id1 = Quiz_Details.objects.only("quiz_id").get(quiz_id = quiz_id12)

    if "ques_no" in request.session:
        qu_no = request.session["ques_no"]
        print(qu_no)

    if request.method == "POST":
        question = request.POST.get("question")
        Choice_1 = request.POST.get("choice_1")
        Choice_2 = request.POST.get("choice_2")
        Choice_3 = request.POST.get("choice_3")
        Choice_4 = request.POST.get("choice_4")
        answer = request.POST.get("answer")
        quiz = add_question.objects.create(quiz_id1=quiz_id1, question=question, Choice_1=Choice_1, Choice_2=Choice_2, Choice_3=Choice_3, Choice_4=Choice_4, answer=answer)
        quiz.save()
        if count <= qu_no:
            count = count + 1
            return render(request, "add_question.html")
        else:
            return HttpResponse("done")
    else:
        messages.info(request, "invalid method")
        return render(request, "teacher_navbar_dashboard.html")


def check_my_answer(request):
    return HttpResponse("Quiz Hello")


def final_score(request):
    return HttpResponse("Quiz Hello")


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