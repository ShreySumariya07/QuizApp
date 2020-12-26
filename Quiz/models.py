from django.db import models
from Account.models import Teacher,Student

'''
class Courses(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_name = models.CharField(null=False)
    updated_on = models.DateField(auto_now=True)
    #REQUIRED_FIELDS = ['course_id', 'course_name', 'updated_on']
    #USERNAME_FIELD = 'course_id'
'''


class Courses(models.Model):
    course_id = models.AutoField(primary_key=True, blank=False)
    course_name = models.CharField(null=False, blank=False)
    updated_on = models.DateField(auto_now=True, blank=False)


class Topic(models.Model):
    Topic_id = models.AutoField(primary_key = True)
    Topic_name = models.CharField(max_length=100)
    updated_on = models.DateField(auto_now=True)


class Quiz_Details(models.Model):
    quiz_id = models.AutoField(primary_key = True)
    quiz_name = models.CharField(max_length=100)
    #quiz_course = models.ForeignKey(Courses,on_delete=models.CASCADE)
    quiz_topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    no_of_questions = models.IntegerField(null=False)
    Mark_per_question = models.IntegerField(null=False)
    total_marks = models.IntegerField()
    teacher_id = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    update_on = models.DateField(auto_now=True)


class add_question(models.Model):
    quiz__id = models.ForeignKey(Quiz_Details,on_delete=models.CASCADE)
    question_id = models.AutoField(primary_key = True)
    question = models.TextField(max_length=300)
    Choice_1 = models.CharField(max_length=100)
    Choice_2 = models.CharField(max_length=100)
    Choice_3 = models.CharField(max_length=100)
    Choice_4 = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)


class check_answers(models.Model):
    qu_id = models.ForeignKey(Quiz_Details,on_delete=models.CASCADE)
    ques_id = models.ForeignKey(add_question,on_delete=models.CASCADE)
    st_id = models.ForeignKey(Student,on_delete=models.CASCADE)
    selected_answer = models.CharField(max_length=100)
    correct_answer = models.ForeignKey(add_question,to_field="question_id",db_column="correct_answer",on_delete=models.CASCADE)
    check_result = models.BooleanField(default=False)


class Result(models.Model):
    q_id = models.ForeignKey(Quiz_Details,on_delete=models.CASCADE)
    s_id = models.ForeignKey(Student,on_delete=models.CASCADE)
    score = models.IntegerField()
    total_m = models.ForeignKey(Quiz_Details,to_field="total_marks",db_column="total_m",on_delete=models.CASCADE)
    status = models.CharField(max_length=100)
