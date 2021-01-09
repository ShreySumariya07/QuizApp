from itertools import chain

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
        request.session["email_save"] = tname
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


def quiz_added(request, teacher_id):
    quiz = Quiz_Details.objects.filter(teacher_id=teacher_id)
    user_quiz={
        "quizes":quiz
    }
    return render(request, 'display_index.html', user_quiz)


def to_add_question(request, qu_id):
    q_obj = Quiz_Details.objects.only("no_of_questions").get(quiz_id=qu_id)
    q_no = q_obj.no_of_questions
    request.session['quiz_id12'] = qu_id
    request.session['ques_no'] = q_no
    count = Quiz_Details.objects.only("questions_entered").get(quiz_id=qu_id)
    if count.questions_entered <= q_no:
        return render(request, "add_question.html")
    else:
        return HttpResponse("All questions already entered")


def save_question(request):
    email_save_id = None
    qu_no = None
    quiz_id12 = None

    if "quiz_id12" in request.session:
        quiz_id12 = request.session["quiz_id12"]

    quiz_id1 = Quiz_Details.objects.only("quiz_id").get(quiz_id=quiz_id12)

    if "ques_no" in request.session:
        qu_no = request.session["ques_no"]

    count = Quiz_Details.objects.only("questions_entered").get(quiz_id=quiz_id12)

    if "email_save" in request.session:
        email_save_id = request.session["email_save"]
    tea_id = User.objects.only("id").get(email = email_save_id)



    if count.questions_entered < qu_no:
        count.questions_entered += 1
        count.save()
        if request.method == "POST":
            question = request.POST.get("question")
            Choice_1 = request.POST.get("choice_1")
            Choice_2 = request.POST.get("choice_2")
            Choice_3 = request.POST.get("choice_3")
            Choice_4 = request.POST.get("choice_4")
            answer = request.POST.get("answer")
            quiz = add_question.objects.create(quiz_id1=quiz_id1, question=question, Choice_1=Choice_1, Choice_2=Choice_2, Choice_3=Choice_3, Choice_4=Choice_4, answer=answer)
            quiz.save()
            print("Total questions : ", qu_no)
            print("Entered questions : ", count.questions_entered)
            return render(request, "add_question.html")
        else:
            messages.info(request, "invalid method")
            return render(request, "teacher_navbar_dashboard.html",{"tea_id": tea_id.id})
    else:
        messages.info(request,"Thanks for adding the questions")
        return render(request, "teacher_navbar_dashboard.html",{"tea_id": tea_id.id})


def final_score(request):
    return HttpResponse("Quiz Hello")


def student_quiz(request,s_id):
    stud_id = s_id
    request.session["student_id"] = stud_id
    quiz = Quiz_Details.objects.all()
    user_quiz = {"quizes":quiz}
    return render(request, "play_quiz.html",user_quiz)


def play_quiz(request,quiz_id):
    quiz_questions = add_question.objects.filter(quiz_id1 = quiz_id)
    no_quest = quiz_questions.count()
    marks_per_questionss = Quiz_Details.objects.get(quiz_id = quiz_id)
    marks_per_question = marks_per_questionss.Mark_per_question
    request.session["mark_per_question"] = marks_per_question
    request.session["quiz_id"] = quiz_id
    request.session["no_quest"] = no_quest

    user_questions = {"user_questions":quiz_questions}
    return render(request, "plain.html",user_questions)

score = 0
i=1


def check_answer(request,question_id):
    global score,i
    if "quiz_id" in request.session:
        quiz_id1 = request.session["quiz_id"]
    if "no_quest" in request.session:
        no_question = request.session["no_quest"]
    if "mark_per_question" in request.session:
        mark_per_question = request.session["mark_per_question"]
    if "student_id" in request.session:
        stud_id = request.session["student_id"]
    quiz_id = Quiz_Details.objects.only("quiz_id").get(quiz_id = quiz_id1)
    quizzz_name = Quiz_Details.objects.only("quiz_name").get(quiz_id = quiz_id1)
    questi_id = add_question.objects.only("question_id").get(question_id = question_id)
    stu_id = User.objects.only("id").get(id = stud_id)
    quiz_questions = add_question.objects.filter(quiz_id1=quiz_id1)[i:no_question]
    user_questions = {"user_questions":quiz_questions}
    if request.method == "POST":
        selected_answer = request.POST.get("radio")
        quest = add_question.objects.only("answer").get(question_id = question_id)

        que = quest.answer

        if selected_answer == que:
            check_result = True
            score = score + mark_per_question
        else:
            check_result = False
        quiz_check = check_answers.objects.create(qu_id = quiz_id , ques_id = questi_id, st_id=stu_id,selected_answer = selected_answer, correct_answer = quest, check_result = check_result)
        quiz_check.save()
        total_mark = no_question * mark_per_question
        if i == no_question:
            percentage = (score * 100)/total_mark
            if percentage >= 35:
                status = "Pass"
            else:
                status = "Fail"
            result = Result.objects.create(q_id = quiz_id, s_id = stu_id, score = score, status = status,total_marks = total_mark,q_name=quizzz_name)
            result.save()
            messages.info(request,"thanks for playing the quiz")
            return redirect("Quiz:results_page", s_id=stud_id)
        else:
            i = i + 1
            return render(request,"plain.html",user_questions)
    else:
        messages.info(request,"invalid method of sending the responses")
        return redirect("student_quiz", stud_id)


def show_result(request,res_id):
    total_result = Result.objects.get(id=res_id)
    question_result = check_answers.objects.filter(qu_id = total_result.q_id,st_id = total_result.s_id)
    return render(request,"plain2.html",{"res":total_result,"question":question_result})


def results_page(request, s_id):
    # stud_id = None
    # if "student_id" in request.session:
    #     stud_id = request.session["student_id"]
    #     print(stud_id)
    stud_id = s_id
    print(s_id)
    stu_id = User.objects.only("id").get(id=stud_id)
    stude_id = stu_id.id

    all_result = Result.objects.filter(s_id = stude_id)

    # quiz_results_details = Quiz_Details.objects.filter(quiz_id__in = all_result.values_list("q_id",flat=True)).select_related("q_id_quiz_name")
    # print(quiz_results_details).
    # result_query = chain(all_result,quiz_results_details)
    return render(request, "result.html", {"all_res":all_result})
    # return render(request, "result.html",{"all_res":all_result,"quiz_res":quiz_results_details})
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